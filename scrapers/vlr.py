"""
VLR.gg scraper for Valorant match data and player stats.

VLR uses server-side HTML — requests + BeautifulSoup works, no JS needed.
Key stats: ACS (Average Combat Score), KAST, ADR, HS%, First Kills/Deaths, Clutches.
"""
import time
import re
from datetime import datetime, timedelta
from typing import Optional
from dataclasses import dataclass, field

import requests
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from loguru import logger

from config import VLR_BASE, REQUEST_DELAY, REQUEST_TIMEOUT, MAX_RETRIES

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml",
    "Referer": "https://www.vlr.gg/",
}


# ---------------------------------------------------------------------------
# Data containers
# ---------------------------------------------------------------------------

@dataclass
class VlrPlayerStats:
    player_name: str
    team_name: str
    agent: str
    acs: Optional[float] = None
    kills: Optional[int] = None
    deaths: Optional[int] = None
    assists: Optional[int] = None
    kast: Optional[float] = None
    adr: Optional[float] = None
    hs_pct: Optional[float] = None
    first_kills: Optional[int] = None
    first_deaths: Optional[int] = None
    clutches_won: Optional[int] = None

@dataclass
class VlrMapResult:
    map_name: str
    map_order: int
    team1_name: str
    team2_name: str
    team1_rounds: int
    team2_rounds: int
    winner_name: str
    team1_attack_first: bool = True
    team1_first_half: Optional[int] = None
    team2_first_half: Optional[int] = None
    team1_second_half: Optional[int] = None
    team2_second_half: Optional[int] = None
    went_to_ot: bool = False
    team1_ot: int = 0
    team2_ot: int = 0
    picked_by: Optional[str] = None
    player_stats: list = field(default_factory=list)

@dataclass
class VlrMatch:
    vlr_id: int
    team1_name: str
    team2_name: str
    winner_name: Optional[str]
    match_date: datetime
    event_name: str
    tournament_stage: Optional[str]
    best_of: int
    is_lan: bool
    team1_map_score: int
    team2_map_score: int
    maps: list = field(default_factory=list)


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

@retry(
    stop=stop_after_attempt(MAX_RETRIES),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type((requests.HTTPError, requests.ConnectionError)),
)
def fetch_vlr(url: str) -> BeautifulSoup:
    time.sleep(REQUEST_DELAY)
    resp = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "lxml")


# ---------------------------------------------------------------------------
# Results list
# ---------------------------------------------------------------------------

def scrape_vlr_results(page: int = 1, days_back: int = 180) -> list[dict]:
    url = f"{VLR_BASE}/matches/results?page={page}"
    soup = fetch_vlr(url)
    cutoff = datetime.utcnow() - timedelta(days=days_back)
    results = []

    for item in soup.select("a.match-item"):
        try:
            href = item.get("href", "")
            m = re.search(r"/(\d+)/", href)
            if not m:
                continue
            vlr_id = int(m.group(1))

            teams = item.select(".match-item-vs-team-name")
            if len(teams) < 2:
                continue
            team1 = teams[0].get_text(strip=True)
            team2 = teams[1].get_text(strip=True)

            score_els = item.select(".match-item-vs-team-score")
            score1 = int(score_els[0].get_text(strip=True)) if score_els else 0
            score2 = int(score_els[1].get_text(strip=True)) if len(score_els) > 1 else 0

            date_el = item.select_one(".match-item-time")
            # VLR stores date in a parent div
            date_container = item.find_parent("div", class_="wf-card")
            date_header = date_container.find_previous_sibling() if date_container else None
            # Approximate: use current time as fallback
            match_date = datetime.utcnow()
            if date_el:
                date_text = date_el.get_text(strip=True)
                # Try to parse; VLR uses relative dates on the page
                try:
                    match_date = datetime.strptime(date_text, "%Y/%m/%d")
                except ValueError:
                    pass

            event_el = item.select_one(".match-item-event-series")
            event = event_el.get_text(strip=True) if event_el else ""

            if match_date < cutoff:
                continue

            results.append({
                "vlr_id": vlr_id,
                "team1": team1,
                "team2": team2,
                "score1": score1,
                "score2": score2,
                "event": event,
                "date": match_date,
                "url": f"{VLR_BASE}{href}",
            })
        except Exception as e:
            logger.debug(f"Error parsing VLR result: {e}")
            continue

    return results


def scrape_vlr_all_results(max_pages: int = 10, days_back: int = 180) -> list[dict]:
    all_results = []
    cutoff = datetime.utcnow() - timedelta(days=days_back)
    for page in range(1, max_pages + 1):
        page_results = scrape_vlr_results(page=page, days_back=days_back)
        if not page_results:
            break
        all_results.extend(page_results)
        oldest = min(r["date"] for r in page_results)
        if oldest < cutoff:
            break
    return all_results


# ---------------------------------------------------------------------------
# Match detail
# ---------------------------------------------------------------------------

def scrape_vlr_match(vlr_id: int) -> Optional[VlrMatch]:
    url = f"{VLR_BASE}/{vlr_id}/"
    soup = fetch_vlr(url)

    try:
        # Teams
        team_els = soup.select(".match-header-link-name .wf-title-med")
        if len(team_els) < 2:
            return None
        team1_name = team_els[0].get_text(strip=True)
        team2_name = team_els[1].get_text(strip=True)

        # Score
        score_els = soup.select(".match-header-vs-score .js-spoiler")
        t1_score = t2_score = 0
        if len(score_els) >= 3:
            try:
                t1_score = int(score_els[0].get_text(strip=True))
                t2_score = int(score_els[2].get_text(strip=True))
            except ValueError:
                pass

        winner_name = None
        if t1_score > t2_score:
            winner_name = team1_name
        elif t2_score > t1_score:
            winner_name = team2_name

        # Date
        date_el = soup.select_one(".match-header-date .moment-tz-convert")
        match_date = datetime.utcnow()
        if date_el and date_el.get("data-utc-ts"):
            try:
                match_date = datetime.utcfromtimestamp(int(date_el["data-utc-ts"]))
            except (ValueError, KeyError):
                pass

        # Event
        event_el = soup.select_one(".match-header-super a")
        event_name = event_el.get_text(strip=True) if event_el else ""

        # Stage
        stage_el = soup.select_one(".match-header-event-series")
        tournament_stage = stage_el.get_text(strip=True) if stage_el else None

        # LAN
        is_lan = bool(soup.select_one('[class*="lan"]'))

        # Best of
        best_of = max(t1_score + t2_score, 1)
        if t1_score + t2_score <= 3:
            best_of = 3
        elif t1_score + t2_score <= 5:
            best_of = 5

        maps = _parse_vlr_maps(soup, team1_name, team2_name)

        return VlrMatch(
            vlr_id=vlr_id,
            team1_name=team1_name,
            team2_name=team2_name,
            winner_name=winner_name,
            match_date=match_date,
            event_name=event_name,
            tournament_stage=tournament_stage,
            best_of=best_of,
            is_lan=is_lan,
            team1_map_score=t1_score,
            team2_map_score=t2_score,
            maps=maps,
        )

    except Exception as e:
        logger.error(f"Failed to parse VLR match {vlr_id}: {e}")
        return None


def _parse_vlr_maps(
    soup: BeautifulSoup, team1_name: str, team2_name: str
) -> list[VlrMapResult]:
    maps = []
    map_containers = soup.select(".vm-stats-game")

    for idx, container in enumerate(map_containers):
        try:
            # Map name
            map_name_el = container.select_one(".map span:not(.dot)")
            map_name = map_name_el.get_text(strip=True).lower() if map_name_el else "unknown"
            if map_name in ("tbd", "tba", ""):
                continue

            # Score
            score_els = container.select(".score")
            if len(score_els) < 2:
                continue
            try:
                t1_rounds = int(score_els[0].get_text(strip=True))
                t2_rounds = int(score_els[1].get_text(strip=True))
            except ValueError:
                continue

            winner_name = team1_name if t1_rounds > t2_rounds else team2_name

            # Half scores
            half_els = container.select(".mod-t, .mod-ct")
            t1_first = t2_first = t1_second = t2_second = None

            # Player stats
            player_stats = _parse_vlr_map_player_stats(container, team1_name, team2_name)

            maps.append(VlrMapResult(
                map_name=map_name,
                map_order=idx,
                team1_name=team1_name,
                team2_name=team2_name,
                team1_rounds=t1_rounds,
                team2_rounds=t2_rounds,
                winner_name=winner_name,
                team1_first_half=t1_first,
                team2_first_half=t2_first,
                team1_second_half=t1_second,
                team2_second_half=t2_second,
                went_to_ot=(t1_rounds + t2_rounds) > 25,
                player_stats=player_stats,
            ))

        except Exception as e:
            logger.debug(f"Error parsing VLR map {idx}: {e}")

    return maps


def _parse_vlr_map_player_stats(
    container: BeautifulSoup, team1_name: str, team2_name: str
) -> list[VlrPlayerStats]:
    stats = []
    tables = container.select("table.wf-table-inset")

    for t_idx, table in enumerate(tables):
        team_name = team1_name if t_idx == 0 else team2_name
        for row in table.select("tbody tr"):
            cells = row.select("td")
            if len(cells) < 5:
                continue
            try:
                player_el = row.select_one("td.mod-player a")
                if not player_el:
                    continue
                player_name = player_el.get_text(strip=True)

                agent_el = row.select_one("td.mod-agents img")
                agent = agent_el.get("alt", "") if agent_el else ""

                def _stat(sel, pct=False):
                    el = row.select_one(sel)
                    if not el:
                        return None
                    txt = el.get_text(strip=True).replace("%", "").replace("/", "")
                    try:
                        v = float(txt)
                        return v / 100 if pct else v
                    except ValueError:
                        return None

                # ACS
                acs_el = row.select_one("td.mod-stat:nth-child(3)")
                acs = None
                if acs_el:
                    try:
                        acs = float(acs_el.get_text(strip=True))
                    except ValueError:
                        pass

                kd_el = row.select_one("td.mod-stat:nth-child(4)")
                k = d = a = None
                if kd_el:
                    kda_text = kd_el.get_text("/", strip=True).split("/")
                    try:
                        k = int(kda_text[0]) if len(kda_text) > 0 else None
                        d = int(kda_text[1]) if len(kda_text) > 1 else None
                        a = int(kda_text[2]) if len(kda_text) > 2 else None
                    except (ValueError, IndexError):
                        pass

                kast_el = row.select_one("td.mod-stat:nth-child(5)")
                kast = None
                if kast_el:
                    try:
                        kast = float(kast_el.get_text(strip=True).replace("%", "")) / 100
                    except ValueError:
                        pass

                adr_el = row.select_one("td.mod-stat:nth-child(6)")
                adr = None
                if adr_el:
                    try:
                        adr = float(adr_el.get_text(strip=True))
                    except ValueError:
                        pass

                hs_el = row.select_one("td.mod-stat:nth-child(7)")
                hs_pct = None
                if hs_el:
                    try:
                        hs_pct = float(hs_el.get_text(strip=True).replace("%", "")) / 100
                    except ValueError:
                        pass

                fk_el = row.select_one("td.mod-stat:nth-child(8)")
                fd_el = row.select_one("td.mod-stat:nth-child(9)")
                fk = fd = None
                if fk_el:
                    try:
                        fk = int(fk_el.get_text(strip=True))
                    except ValueError:
                        pass
                if fd_el:
                    try:
                        fd = int(fd_el.get_text(strip=True))
                    except ValueError:
                        pass

                stats.append(VlrPlayerStats(
                    player_name=player_name,
                    team_name=team_name,
                    agent=agent,
                    acs=acs,
                    kills=k,
                    deaths=d,
                    assists=a,
                    kast=kast,
                    adr=adr,
                    hs_pct=hs_pct,
                    first_kills=fk,
                    first_deaths=fd,
                ))
            except Exception as e:
                logger.debug(f"VLR player row parse error: {e}")

    return stats


# ---------------------------------------------------------------------------
# Upcoming
# ---------------------------------------------------------------------------

def scrape_vlr_upcoming() -> list[dict]:
    url = f"{VLR_BASE}/matches"
    soup = fetch_vlr(url)
    upcoming = []

    for item in soup.select("a.match-item"):
        try:
            href = item.get("href", "")
            m = re.search(r"/(\d+)/", href)
            if not m:
                continue
            vlr_id = int(m.group(1))

            # Skip completed matches
            if item.select_one(".match-item-vs-score"):
                continue

            teams = item.select(".match-item-vs-team-name")
            if len(teams) < 2:
                continue

            team1 = teams[0].get_text(strip=True)
            team2 = teams[1].get_text(strip=True)

            date_el = item.select_one(".match-item-time .moment-tz-convert")
            scheduled_at = None
            if date_el and date_el.get("data-utc-ts"):
                try:
                    scheduled_at = datetime.utcfromtimestamp(int(date_el["data-utc-ts"]))
                except (ValueError, KeyError):
                    pass

            event_el = item.select_one(".match-item-event-series")
            event = event_el.get_text(strip=True) if event_el else ""

            upcoming.append({
                "vlr_id": vlr_id,
                "team1": team1,
                "team2": team2,
                "scheduled_at": scheduled_at,
                "event": event,
                "url": f"{VLR_BASE}{href}",
            })
        except Exception as e:
            logger.debug(f"VLR upcoming parse error: {e}")

    return upcoming
