# Probe 2026-10-03T03:04:39.933251+00:00

- OK  kalshi esports series (0.54s)
- OK  kalshi esports markets (0.96s)
- OK  polymarket /sports (0.23s)
- OK  polymarket esports tags (0.04s)
- OK  polymarket events tag=esports open (0.32s)
- OK  polymarket events tag=esports closed (0.22s)
- OK  polymarket events tag=counter-strike open (0.18s)
- OK  polymarket events tag=counter-strike closed (0.42s)
- OK  polymarket events tag=cs2 open (0.23s)
- OK  polymarket events tag=cs2 closed (0.22s)
- OK  polymarket events tag=league-of-legends open (0.39s)
- OK  polymarket events tag=league-of-legends closed (0.18s)
- OK  polymarket events tag=valorant open (0.33s)
- OK  polymarket events tag=valorant closed (0.2s)
- OK  polymarket events tag=dota-2 open (0.43s)
- OK  polymarket events tag=dota-2 closed (0.18s)
- OK  polymarket price history (closed market) (0.29s)
- OK  polymarket price history (open market) (0.02s)
- OK  polymarket order book (0.25s)
- ERR polymarket closed esports depth (38.68s)
    HttpError: HTTP 422 for https://gamma-api.polymarket.com/events?tag_slug=esports&closed=true&limit=500&offset=2100&order=endDate&ascending=false: {"type":"validation error","error":"offset too large, use /events/keyset for deeper pagination"}

- OK  leaguepedia cargo (0.3s)
- ERR liquipedia api (cs) (47.84s)
    HttpError: HTTP 429 for https://liquipedia.net/counterstrike/api.php?action=query&list=search&srsearch=Major&srlimit=3&format=json: <!DOCTYPE HTML><title>Rate Limited - Liquipedia</title><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><style type=text/css>body{margin:40px auto;max-width:700px;line-height:1.6;font-size:18px;color:#444;padding:0 10px}h1{line-height:1.2}.reason{display:none}</st
- OK  vlr.gg results page (honest UA) (0.18s)
- OK  hltv results page (honest UA) (0.31s)
