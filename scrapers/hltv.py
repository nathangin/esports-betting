"""
HLTV scraper for CS2 match data, player stats, and team info.

HLTV uses Cloudflare — if plain requests returns 403, set USE_PLAYWRIGHT=True
in your .env and install: `playwright install chromium`
"""
import time
import json
import re
import os
from datetime import datetime, timedelta
from typing import Optional
from dataclasses import dataclass, field

import requests
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from loguru import logger

from config import HLTV_BASE, REQUEST_DELAY, REQUEST_TIMEOUT, MAX_RETRIES

USE_PLAYWRIGHT = os.getenv("USE_PLAYWRIGHT", "false").lower() == "true"


# ---------------------------------------------------------------------------
# Data containers
# ---------------------------------------------------------------------------

@dataclass
class ScrapedPlayer:
    hltv_id: int
    name: str
    team_name: Optional[str] = None

@dataclass
class ScrapedTeam:
    hltv_id: int
    name: str
    region: Optional[str] = None

@dataclass
class ScrapedPlayerStats:
    player_hltv_id: int
    player_name: str
    team_name: str
    kills: Optional[int] = None
    deaths: Optional[int] = None
    assists: Optional[int] = None
    hs_count: Optional[int] = None
    hs_pct: Optional[float] = None
    kast: Optional[float] = None
    rating: Optional[float] = None
    adr: Optional[float] = None
    first_kills: Optional[int] = None
    first_deaths: Optional[int] = None

@dataclass
class ScrapedMapResult:
    map_name: str
    map_order: int
    team1_name: str
    team2_name: str
    team1_rounds: int
    team2_rounds: int
    winner_name: str
    team1_ct_first: bool = True
    team1_first_half: Optional[int] = None
    team2_first_half: Optional[int] = None
    team1_second_half: Optional[int] = None
    team2_second_half: Optional[int] = None
    went_to_ot: bool = False
    team1_ot: int = 0
    team2_ot: int = 0
    picked_by: Optional[str] = None
    is_decider: bool = False
    player_stats: list = field(default_factory=list)

@dataclass
class ScrapedMatch:
    hltv_id: int
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
# HTTP client
# ---------------------------------------------------------------------------

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://www.hltv.org/",
}

def _fetch_html_playwright(url: str, timeout_ms: int = 60000) -> str:
    from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        ctx = browser.new_context(
            user_agent=HEADERS["User-Agent"],
            locale="en-US",
            extra_http_headers={"Accept-Language": "en-US,en;q=0.9"},
        )
        page = ctx.new_page()
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
        except PWTimeout:
            # Try networkidle as fallback before giving up
            try:
                page.wait_for_load_state("load", timeout=15000)
            except PWTimeout:
                ctx.close()
                browser.close()
                raise
        try:
            page.wait_for_selector("body", timeout=5000)
        except Exception:
            pass
        time.sleep(1.5)
        html = page.content()
        ctx.close()
        browser.close()
    return html


@retry(
    stop=stop_after_attempt(MAX_RETRIES),
    wait=wait_exponential(multiplier=2, min=3, max=20),
    retry=retry_if_exception_type((requests.HTTPError, requests.ConnectionError, Exception)),
    reraise=False,
)
def fetch_html(url: str, delay: float = REQUEST_DELAY) -> BeautifulSoup:
    time.sleep(delay)
    if USE_PLAYWRIGHT:
        html = _fetch_html_playwright(url)
        return BeautifulSoup(html, "lxml")

    resp = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
    if resp.status_code == 403:
        logger.warning(
            f"403 on {url} — HLTV blocked plain requests. "
            "Set USE_PLAYWRIGHT=true in .env to bypass Cloudflare."
        )
        raise requests.HTTPError(response=resp)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "lxml")


# ---------------------------------------------------------------------------
# Results list scraper (paginated)
# ---------------------------------------------------------------------------

def scrape_results_page(offset: int = 0) -> list[dict]:
    """Returns a list of {hltv_id, team1, team2, score, event, date} from /results."""
    url = f"{HLTV_BASE}/results?offset={offset}"
    soup = fetch_html(url)
    results = []

    for item in soup.select(".result-con a.a-reset"):
        try:
            href = item.get("href", "")
            match = re.search(r"/matches/(\d+)/", href)
            if not match:
                continue
            hltv_id = int(match.group(1))

            teams = item.select(".team")
            if len(teams) < 2:
                continue
            team1 = teams[0].get_text(strip=True)
            team2 = teams[1].get_text(strip=True)

            score_el = item.select(".result-score span")
            score1 = int(score_el[0].get_text(strip=True)) if score_el else 0
            score2 = int(score_el[1].get_text(strip=True)) if len(score_el) > 1 else 0

            event_el = item.select_one(".event-name")
            event = event_el.get_text(strip=True) if event_el else ""

            date_el = item.select_one(".time")
            ts = int(date_el.get("data-unix", 0)) // 1000 if date_el else 0
            date = datetime.utcfromtimestamp(ts) if ts else datetime.utcnow()

            # Star rating — HLTV shows 0-3 stars on result cards
            stars_el = item.select_one(".stars")
            star_rating = 0
            if stars_el:
                filled = stars_el.select("i.fa-star")
                star_rating = len(filled)

            results.append({
                "hltv_id": hltv_id,
                "team1": team1,
                "team2": team2,
                "score1": score1,
                "score2": score2,
                "event": event,
                "date": date,
                "url": f"{HLTV_BASE}{href}",
                "star_rating": star_rating,
            })
        except Exception as e:
            logger.debug(f"Error parsing result item: {e}")
            continue

    return results


def scrape_results(max_pages: int = 10, days_back: int = 180) -> list[dict]:
    """Scrape multiple pages of results, stopping when entries are older than days_back."""
    cutoff = datetime.utcnow() - timedelta(days=days_back)
    all_results = []

    for page in range(max_pages):
        offset = page * 100
        logger.info(f"Scraping results page {page + 1} (offset={offset})")
        page_results = scrape_results_page(offset)
        if not page_results:
            break
        all_results.extend(page_results)
        oldest = min(r["date"] for r in page_results)
        if oldest < cutoff:
            break

    return [r for r in all_results if r["date"] >= cutoff]


# ---------------------------------------------------------------------------
# Match detail scraper
# ---------------------------------------------------------------------------

def scrape_match(hltv_id: int, url: Optional[str] = None) -> Optional[ScrapedMatch]:
    """Scrape full match details including per-map player stats."""
    if url is None:
        url = f"{HLTV_BASE}/matches/{hltv_id}/"
    soup = fetch_html(url)

    # Detect 404 page
    h1s = [h.get_text(strip=True) for h in soup.find_all("h1")]
    if "404" in h1s:
        logger.warning(f"Match {hltv_id} returned 404 — skipping")
        return None

    try:
        # Teams
        team_els = soup.select(".teamName")
        if len(team_els) < 2:
            logger.warning(f"Could not find teams for match {hltv_id}")
            return None
        team1_name = team_els[0].get_text(strip=True)
        team2_name = team_els[1].get_text(strip=True)

        # Score — .spoiler elements hold the map scores in team1/team2 order
        t1_map_score = t2_map_score = 0
        spoilers = soup.select(".spoiler")
        if len(spoilers) >= 2:
            try:
                t1_map_score = int(spoilers[0].get_text(strip=True))
                t2_map_score = int(spoilers[1].get_text(strip=True))
            except ValueError:
                pass
        # Fallback: strip team name prefix from gradient containers
        if t1_map_score == 0 and t2_map_score == 0:
            for grad, attr in [(".team1-gradient", "t1"), (".team2-gradient", "t2")]:
                el = soup.select_one(grad)
                if el:
                    txt = re.sub(r"[^\d]", "", el.get_text(strip=True))
                    try:
                        val = int(txt[-1]) if txt else 0
                        if attr == "t1":
                            t1_map_score = val
                        else:
                            t2_map_score = val
                    except (ValueError, IndexError):
                        pass

        # Winner
        winner_name = None
        if t1_map_score > t2_map_score:
            winner_name = team1_name
        elif t2_map_score > t1_map_score:
            winner_name = team2_name

        # Date
        date_el = soup.select_one(".date")
        ts_el = soup.select_one(".time[data-unix]")
        if ts_el:
            ts = int(ts_el["data-unix"]) // 1000
            match_date = datetime.utcfromtimestamp(ts)
        else:
            match_date = datetime.utcnow()

        # Event
        event_el = soup.select_one(".event a")
        event_name = event_el.get_text(strip=True) if event_el else ""

        # Best of — look in the map-type or padding text
        best_of = 3
        for sel in [".padding .preformatted-text", ".match-header-vs-note", "[class*='bestof']", "[class*='bo-']"]:
            el = soup.select_one(sel)
            if el:
                bo_m = re.search(r"[Bb]est of\s*(\d)|BO(\d)", el.get_text())
                if bo_m:
                    best_of = int(bo_m.group(1) or bo_m.group(2))
                    break
        # Fallback: infer from number of maps
        n_maps = len(soup.select(".mapholder"))
        if best_of == 3 and n_maps >= 4:
            best_of = 5

        # LAN check — look for LAN text in event/match context
        page_text = soup.get_text()
        is_lan = bool(re.search(r"\bLAN\b", page_text))

        # Stage
        stage_el = soup.select_one(".match-header-event-series, .padding .preformatted-text")
        tournament_stage = stage_el.get_text(strip=True) if stage_el else None

        # Maps
        maps = _parse_maps(soup, team1_name, team2_name, hltv_id)

        return ScrapedMatch(
            hltv_id=hltv_id,
            team1_name=team1_name,
            team2_name=team2_name,
            winner_name=winner_name,
            match_date=match_date,
            event_name=event_name,
            tournament_stage=tournament_stage,
            best_of=best_of,
            is_lan=is_lan,
            team1_map_score=t1_map_score,
            team2_map_score=t2_map_score,
            maps=maps,
        )

    except Exception as e:
        logger.error(f"Failed to parse match {hltv_id}: {e}")
        return None


def _parse_maps(
    soup: BeautifulSoup,
    team1_name: str,
    team2_name: str,
    match_id: int,
) -> list[ScrapedMapResult]:
    maps = []
    map_holders = soup.select(".mapholder")
    # One .matchstats div for the whole match; .stats-content children are per-map (same order as .mapholder)
    match_stats_el = soup.select_one(".matchstats")
    stats_content_divs = match_stats_el.select(".stats-content") if match_stats_el else []

    for idx, holder in enumerate(map_holders):
        # stats_content_divs[0] is always the match-total overview; per-map stats start at index 1.
        # So mapholder[idx] corresponds to stats_content_divs[idx + 1].
        stats_idx = idx + 1
        stats_content = stats_content_divs[stats_idx] if stats_idx < len(stats_content_divs) else None
        try:
            map_name_el = holder.select_one(".mapname")
            if not map_name_el:
                continue
            map_name = map_name_el.get_text(strip=True).lower()
            if map_name in ("default", "tba"):
                continue

            results = holder.select(".results-left, .results-right")
            if len(results) < 2:
                continue

            # Round scores
            t1_rounds = t2_rounds = 0
            score_els = holder.select(".results-team-score")
            if len(score_els) >= 2:
                try:
                    t1_rounds = int(score_els[0].get_text(strip=True))
                    t2_rounds = int(score_els[1].get_text(strip=True))
                except ValueError:
                    pass

            winner_name = team1_name if t1_rounds > t2_rounds else team2_name

            # Half-time scores — HLTV format: "(7:5;4:8)" or "(7:5;5:7)(8:10)" for OT
            t1_first = t2_first = t1_second = t2_second = None
            half_el = holder.select_one(".results-center-half-score")
            if half_el:
                half_text = half_el.get_text(strip=True)
                # Extract all parenthesised groups: ["7:5;4:8"] or ["7:5;5:7", "8:10"]
                groups = re.findall(r"\(([^)]+)\)", half_text)
                if groups:
                    parts = groups[0].split(";")
                    if len(parts) >= 2:
                        try:
                            h1 = parts[0].split(":")
                            h2 = parts[1].split(":")
                            t1_first  = int(h1[0]); t2_first  = int(h1[1])
                            t1_second = int(h2[0]); t2_second = int(h2[1])
                        except (ValueError, IndexError):
                            pass

            # CT/T first half side from scoreboard table
            team1_ct_first = True  # default; refine from stats table if possible

            # Overtime
            went_to_ot = (t1_rounds + t2_rounds) > 30 if t1_rounds and t2_rounds else False
            t1_ot = t2_ot = 0
            if went_to_ot and t1_first is not None and t1_second is not None:
                t1_ot = t1_rounds - t1_first - t1_second
                t2_ot = t2_rounds - t2_first - t2_second

            # Picked by / decider
            picked_el = holder.select_one(".results-center-header-picked")
            picked_by = None
            is_decider = False
            if picked_el:
                picked_text = picked_el.get_text(strip=True).lower()
                if "picked" in picked_text:
                    picked_by = team1_name if team1_name.lower() in picked_text else team2_name
                elif "decider" in picked_text or "left over" in picked_text:
                    is_decider = True

            # tables[0]=team1 full, tables[3]=team2 full inside the per-map stats-content
            player_stats = _parse_map_player_stats(stats_content, team1_name, team2_name)

            maps.append(ScrapedMapResult(
                map_name=map_name,
                map_order=idx,
                team1_name=team1_name,
                team2_name=team2_name,
                team1_rounds=t1_rounds,
                team2_rounds=t2_rounds,
                winner_name=winner_name,
                team1_ct_first=team1_ct_first,
                team1_first_half=t1_first,
                team2_first_half=t2_first,
                team1_second_half=t1_second,
                team2_second_half=t2_second,
                went_to_ot=went_to_ot,
                team1_ot=t1_ot,
                team2_ot=t2_ot,
                picked_by=picked_by,
                is_decider=is_decider,
                player_stats=player_stats,
            ))

        except Exception as e:
            logger.debug(f"Error parsing map {idx} of match {match_id}: {e}")
            continue

    return maps


def _parse_map_player_stats(
    stats_content: Optional[BeautifulSoup],
    team1_name: str,
    team2_name: str,
) -> list[ScrapedPlayerStats]:
    """
    Parse player stats from a per-map .stats-content div (HLTV 2024+ format).

    Table layout inside each .stats-content:
      [0] team1 full-match stats
      [1] team1 CT-side stats
      [2] team1 T-side stats
      [3] team2 full-match stats
      [4] team2 CT-side stats
      [5] team2 T-side stats

    K-D is "54-44" combined in .kd.traditional-data — no HS% column in main table.
    """
    if stats_content is None:
        return []

    stats = []
    all_tables = stats_content.select("table.table")

    # Grab full-match table for each team: index 0 = team1, index 3 = team2
    for t_idx, table_index in enumerate([0, 3]):
        if table_index >= len(all_tables):
            continue
        table = all_tables[table_index]
        team_name = team1_name if t_idx == 0 else team2_name

        for row in table.select("tbody tr"):
            player_el = row.select_one("td.players a")
            if not player_el:
                continue

            href = player_el.get("href", "")
            # Skip team-name header rows — they link to /team/ not /player/
            if "/player/" not in href:
                continue

            try:
                pid_match = re.search(r"/player/(\d+)/([^/]+)", href)
                player_id  = int(pid_match.group(1)) if pid_match else 0
                # IGN is the last URL segment (most reliable, avoids name+tag concatenation)
                player_ign = pid_match.group(2) if pid_match else player_el.get_text(strip=True)

                kills = deaths = None
                kd_el = row.select_one("td.kd.traditional-data")
                if kd_el:
                    kd_text = kd_el.get_text(strip=True)
                    kd_parts = kd_text.split("-")
                    if len(kd_parts) == 2:
                        try:
                            kills  = int(kd_parts[0])
                            deaths = int(kd_parts[1])
                        except ValueError:
                            pass

                adr = None
                adr_el = row.select_one("td.adr.traditional-data")
                if adr_el:
                    try:
                        adr = float(adr_el.get_text(strip=True))
                    except ValueError:
                        pass

                kast = None
                kast_el = row.select_one("td.kast.traditional-data")
                if kast_el:
                    try:
                        kast = float(kast_el.get_text(strip=True).replace("%", "")) / 100
                    except ValueError:
                        pass

                rating = None
                rating_el = row.select_one("td.rating")
                if rating_el:
                    try:
                        rating = float(rating_el.get_text(strip=True))
                    except ValueError:
                        pass

                stats.append(ScrapedPlayerStats(
                    player_hltv_id=player_id,
                    player_name=player_ign,
                    team_name=team_name,
                    kills=kills,
                    deaths=deaths,
                    kast=kast,
                    rating=rating,
                    adr=adr,
                ))
            except Exception as e:
                logger.debug(f"Error parsing player row: {e}")
                continue

    return stats


# ---------------------------------------------------------------------------
# Upcoming matches
# ---------------------------------------------------------------------------

def scrape_upcoming_matches() -> list[dict]:
    """Returns upcoming scheduled matches from /matches."""
    url = f"{HLTV_BASE}/matches"
    soup = fetch_html(url)
    upcoming = []

    for item in soup.select(".upcoming-match"):
        try:
            href = item.select_one("a.match").get("href", "") if item.select_one("a.match") else ""
            m = re.search(r"/matches/(\d+)/", href)
            if not m:
                continue
            hltv_id = int(m.group(1))

            teams = item.select(".team-name")
            if len(teams) < 2:
                continue
            team1 = teams[0].get_text(strip=True)
            team2 = teams[1].get_text(strip=True)

            ts_el = item.select_one(".time[data-unix]")
            ts = int(ts_el["data-unix"]) // 1000 if ts_el else 0
            scheduled_at = datetime.utcfromtimestamp(ts) if ts else None

            event_el = item.select_one(".event-name")
            event = event_el.get_text(strip=True) if event_el else ""

            bo_el = item.select_one(".map-text")
            best_of = 3
            if bo_el:
                bo_m = re.search(r"(\d)", bo_el.get_text())
                if bo_m:
                    best_of = int(bo_m.group(1))

            upcoming.append({
                "hltv_id": hltv_id,
                "team1": team1,
                "team2": team2,
                "scheduled_at": scheduled_at,
                "event": event,
                "best_of": best_of,
                "url": f"{HLTV_BASE}{href}",
            })
        except Exception as e:
            logger.debug(f"Error parsing upcoming match: {e}")
            continue

    return upcoming


# ---------------------------------------------------------------------------
# Team page (for region / roster)
# ---------------------------------------------------------------------------

def scrape_team(hltv_id: int) -> Optional[dict]:
    url = f"{HLTV_BASE}/team/{hltv_id}/"
    soup = fetch_html(url)
    try:
        name_el = soup.select_one(".profile-team-name")
        name = name_el.get_text(strip=True) if name_el else ""

        region_el = soup.select_one(".team-country")
        region = region_el.get_text(strip=True) if region_el else None

        players = []
        for p_el in soup.select(".roster-player-info-container a"):
            p_href = p_el.get("href", "")
            p_m = re.search(r"/player/(\d+)/", p_href)
            if p_m:
                players.append({
                    "hltv_id": int(p_m.group(1)),
                    "name": p_el.select_one(".text-ellipsis").get_text(strip=True)
                    if p_el.select_one(".text-ellipsis") else p_el.get_text(strip=True),
                })

        return {"hltv_id": hltv_id, "name": name, "region": region, "players": players}
    except Exception as e:
        logger.error(f"Failed to scrape team {hltv_id}: {e}")
        return None
