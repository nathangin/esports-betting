"""Turn probabilities and quotes into sized, fee-aware bets.

Prices are what you would actually pay as a taker: YES at the ask, NO at 1 - (YES bid).
Kalshi's taker fee is round_up(0.07 * contracts * price * (1 - price)) dollars per order.
"""

from __future__ import annotations

import math
from dataclasses import asdict, dataclass, field


@dataclass
class Rules:
    min_edge: float = 0.03        # expected profit per contract after fees, dollars
    min_roi: float = 0.08         # expected profit / all-in cost
    kelly: float = 0.25           # fraction of full Kelly
    max_bet_frac: float = 0.02    # of bankroll per market
    max_event_frac: float = 0.04  # of bankroll per event (brackets of one city/day)
    max_run_frac: float = 0.20    # new money committed per run
    min_price: float = 0.05       # skip contracts cheaper than this (fat-tail lottery tickets)
    max_price: float = 0.85       # skip paying more than this
    max_contracts: int = 200
    min_contracts: int = 1
    fee_rate: float = 0.07
    max_spread: float = 0.08      # skip markets whose bid/ask spread is wider than this
    max_gap: float = 0.25         # skip matches where model and market disagree by more than this:
                                  # big disagreements are usually news the model has not seen
    sides: tuple = ("yes", "no")

    def to_dict(self) -> dict:
        d = asdict(self)
        d["sides"] = list(self.sides)
        return d

    @classmethod
    def from_dict(cls, d: dict | None) -> "Rules":
        d = dict(d or {})
        if "sides" in d:
            d["sides"] = tuple(d["sides"])
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


def default_rules() -> Rules:
    """Rules used by the backtest and by the main paper book."""
    return Rules(min_edge=0.03, min_roi=0.05, kelly=0.25, max_bet_frac=0.02, max_event_frac=0.02,
                 max_run_frac=0.25, min_price=0.10, max_price=0.90, max_spread=0.06)


def taker_fee(price: float, contracts: int, rate: float = 0.07) -> float:
    """Total fee in dollars for one order (Kalshi rounds up to the next cent)."""
    raw = rate * contracts * price * (1.0 - price)
    return math.ceil(round(raw * 100, 6)) / 100.0


@dataclass
class Bet:
    ticker: str
    event_ticker: str
    side: str            # "yes" or "no"
    price: float         # dollars per contract paid
    prob: float          # probability this side wins
    contracts: int
    cost: float          # contracts * price
    fee: float
    ev: float            # expected profit per contract after fees
    roi: float           # expected profit / (cost + fee)
    kelly_f: float       # full-Kelly fraction of bankroll
    extra: dict = field(default_factory=dict)

    @property
    def outlay(self) -> float:
        return self.cost + self.fee


def side_quotes(yes_bid: float | None, yes_ask: float | None) -> dict[str, float]:
    q = {}
    if yes_ask is not None and 0 < yes_ask < 1:
        q["yes"] = yes_ask
    if yes_bid is not None and 0 < yes_bid < 1:
        q["no"] = round(1.0 - yes_bid, 4)
    return q


def candidates(rows: list[dict], rules: Rules) -> list[dict]:
    """rows: one per market with ticker, event_ticker, p (prob YES), yes_bid, yes_ask.
    Returns the best side per market that clears the thresholds, best first."""
    out = []
    for r in rows:
        p = r.get("p")
        if p is None or not (0.0 <= p <= 1.0):
            continue
        bid, ask = r.get("yes_bid"), r.get("yes_ask")
        if bid is not None and ask is not None and ask - bid > rules.max_spread:
            continue
        best = None
        for side, price in side_quotes(bid, ask).items():
            if side not in rules.sides or not (rules.min_price <= price <= rules.max_price):
                continue
            q = p if side == "yes" else 1.0 - p
            fee_pc = rules.fee_rate * price * (1 - price)
            ev = q - price - fee_pc
            all_in = price + fee_pc
            roi = ev / all_in
            if ev < rules.min_edge or roi < rules.min_roi:
                continue
            kelly_f = (q - all_in) / (1.0 - all_in)
            if kelly_f <= 0:
                continue
            c = {**r, "side": side, "price": price, "prob": q, "ev": ev, "roi": roi, "kelly_f": kelly_f,
                 "max_size": r.get("ask_size") if side == "yes" else r.get("bid_size")}
            if best is None or c["ev"] * c["kelly_f"] > best["ev"] * best["kelly_f"]:
                best = c
        if best:
            out.append(best)
    out.sort(key=lambda c: c["kelly_f"], reverse=True)
    return out


def size(cands: list[dict], bankroll: float, cash: float, rules: Rules,
         event_used: dict[str, float] | None = None, run_budget: float | None = None) -> list[Bet]:
    """Fractional Kelly with per-market, per-event and per-run caps; never spends more than cash."""
    event_used = dict(event_used or {})
    budget = rules.max_run_frac * bankroll if run_budget is None else run_budget
    bets = []
    for c in cands:
        price = c["price"]
        all_in = price + rules.fee_rate * price * (1 - price)
        stake = min(rules.kelly * c["kelly_f"] * bankroll, rules.max_bet_frac * bankroll)
        ev_room = rules.max_event_frac * bankroll - event_used.get(c["event_ticker"], 0.0)
        stake = min(stake, ev_room, budget, cash)
        n = int(stake // all_in)
        n = min(n, rules.max_contracts)
        if c.get("max_size") is not None and c["max_size"] == c["max_size"]:
            n = min(n, int(c["max_size"]))
        if n < rules.min_contracts:
            continue
        fee = taker_fee(price, n, rules.fee_rate)
        cost = round(n * price, 4)
        q = c["prob"]
        ev = q - price - fee / n
        if ev <= 0:
            continue
        outlay = cost + fee
        bets.append(Bet(ticker=c["ticker"], event_ticker=c["event_ticker"], side=c["side"], price=price,
                        prob=q, contracts=n, cost=cost, fee=fee, ev=ev, roi=ev * n / outlay,
                        kelly_f=c["kelly_f"], extra={k: v for k, v in c.items() if k not in (
                            "ticker", "event_ticker", "side", "price", "prob", "ev", "roi", "kelly_f")}))
        event_used[c["event_ticker"]] = event_used.get(c["event_ticker"], 0.0) + outlay
        budget -= outlay
        cash -= outlay
        if budget <= 0 or cash <= 0:
            break
    return bets


def settle_pnl(side: str, contracts: int, price: float, fee: float, result: str) -> float:
    """Profit in dollars once the market's result is known ('yes'/'no'; anything else refunds)."""
    if result not in ("yes", "no"):
        return 0.0
    won = (result == side)
    return round((contracts * (1.0 - price) if won else -contracts * price) - fee, 4)


def market_prob(bid_a, ask_a, bid_b, ask_b) -> float | None:
    """Market's probability that team A wins, from both team markets (they mirror each other)."""
    views = []
    if bid_a is not None and ask_a is not None:
        views.append((bid_a + ask_a) / 2)
    if bid_b is not None and ask_b is not None:
        views.append(1 - (bid_b + ask_b) / 2)
    return float(sum(views) / len(views)) if views else None


def match_candidates(event: str, p_a: float, a: dict, b: dict, rules: Rules) -> list[dict]:
    """Best fee-aware bet for one two-team match, if any.

    a/b: {"ticker", "yes_bid", "yes_ask", "ask_size", "bid_size"} for the team A / team B markets.
    Backing A can be done by buying YES on A or NO on B; the cheaper route is used.
    """
    rows = [{**a, "event_ticker": event, "p": p_a, "outcome": "A"},
            {**b, "event_ticker": event, "p": 1.0 - p_a, "outcome": "B"}]
    cands = candidates(rows, rules)
    for c in cands:   # which team does this position back?
        c["backs"] = c["outcome"] if c["side"] == "yes" else ("B" if c["outcome"] == "A" else "A")
    best: dict[str, dict] = {}
    for c in cands:
        cur = best.get(c["backs"])
        if cur is None or c["price"] < cur["price"]:
            best[c["backs"]] = c
    out = sorted(best.values(), key=lambda c: c["kelly_f"], reverse=True)
    return out[:1]


def flat_candidates(event: str, backs_a: bool, a: dict, b: dict, rules: Rules) -> list[dict]:
    """Cheapest way to back a chosen team regardless of edge (for the favourite/underdog
    baselines); size with ``flat_rules``."""
    loose = Rules(**{**rules.to_dict(), "sides": tuple(rules.sides), "min_edge": -1.0, "min_roi": -1.0,
                     "max_spread": 1.0})
    cands = match_candidates(event, 0.999 if backs_a else 0.001, a, b, loose)
    for c in cands:
        c["kelly_f"] = 1.0
    return cands


def flat_rules(rules: Rules, frac: float = 0.01) -> Rules:
    return Rules(**{**rules.to_dict(), "sides": tuple(rules.sides), "kelly": frac, "max_bet_frac": frac,
                    "max_event_frac": max(frac, rules.max_event_frac)})
