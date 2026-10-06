from esalpha.sides import match_code, parse_side, side_game, side_kind


def test_side_series_and_codes():
    assert side_kind("KXCS2TOTALMAPS") == "total" and side_kind("KXRLSPREAD") == "spread" and side_kind("KXLOLMAP") == "map"
    assert side_kind("KXCS2MAPWINNER") is None and side_kind("KXCS2GAME") is None and side_kind("KXLOLTOTAL") is None
    assert side_game("KXRLSPREAD") == "rl" and side_game("KXCSGOMAP") == "cs2" and side_game("KXOWTOTALMAPS") == "ow"
    assert match_code("KXCODMAP-26AUG091500OGHTCS-5", "KXCODMAP") == ("26AUG091500OGHTCS", 5)
    assert match_code("KXCODTOTALMAPS-26AUG091500OGHTCS", "KXCODTOTALMAPS") == ("26AUG091500OGHTCS", None)


def test_parse_real_side_markets(fixture):
    raw = fixture("kalshi_cod_side_markets.json")
    maps = [parse_side(m, "KXCODMAP") for m in raw["KXCODMAP"]]
    m5 = next(m for m in maps if m["ticker"] == "KXCODMAP-26AUG091500OGHTCS-5-OG")
    assert m5["kind"] == "map" and m5["map_no"] == 5 and m5["code"] == "26AUG091500OGHTCS"
    assert m5["team"] == "OpTic Gaming" and m5["competitor"] == "f0ccadd8-0367-473e-8e56-8f1e600f14d2"
    assert m5["result"] == "yes" and m5["game"] == "cod"
    tot = [parse_side(m, "KXCODTOTALMAPS") for m in raw["KXCODTOTALMAPS"]]
    over85 = next(m for m in tot if m["ticker"].endswith("-9"))
    assert over85["kind"] == "total" and over85["strike"] == 8.5 and over85["result"] == "no"
