"""Fetch Canada-Turkiye monthly trade by HS6, 2021-01..latest, from StatCan CIMT cubes via WDS:
  12-10-0148 (exports, HS6; estimate 1=domestic exports, 2=re-exports)
  12-10-0151 (imports, HS6; estimate 1=imports value)
Coordinate = geo.country.state.estimate.HS2.HS4(last 2 digits, 00->100).HS6(last 2 digits, 00->100)
Candidate HS6 codes come from the UN Comtrade HS reference list (all HS editions); codes not in the
cube return no series. To keep request volume small, a (geo, flow, chapter) combination is only
queried if the HS2 series from 01_fetch_hs2.py shows non-zero Turkiye trade in 2021-2026.
Results are checkpointed per request batch to RAW/wds/hs6_<tag>_tur.json.
Usage: python3 -I 02_fetch_hs6.py RAW
"""
import sys, json, os
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wds import fetch

raw = sys.argv[1]
ref = json.load(open(os.path.join(raw, "comtrade_HS_ref.json")))["results"]
codes = sorted({r["id"] for r in ref if len(r["id"]) == 6 and r["id"].isdigit()})
N = 68  # 2021-01 .. 2026-08


def live_hs2(fname):
    d = json.load(open(os.path.join(raw, "wds", fname)))
    live = set()
    for c, s in d.items():
        g, _, _, e, ch = c.split(".")[:5]
        if any(v for r, v in s if r >= "2021-01"):
            live.add((g, e, int(ch)))
    return live


def coord(geo, est, code):
    c2, c4, c6 = int(code[:2]), int(code[2:4]) or 100, int(code[4:6]) or 100
    return "%d.382.100.%d.%d.%d.%d.0.0.0" % (geo, est, c2, c4, c6)


for pid, hs2file, tag in [(12100148, "hs2_exports_tur.json", "exp"), (12100151, "hs2_imports_tur.json", "imp")]:
    out = os.path.join(raw, "wds", "hs6_%s_tur.json" % tag)
    have = json.load(open(out)) if os.path.exists(out) else {}
    live = live_hs2(hs2file)
    # pass 1: Canada level (geo 1), all candidate codes in live chapters
    cc = [coord(1, int(e), k) for (g, e, ch) in sorted(live) if g == "1" for k in codes if int(k[:2]) == ch]
    if all(c in have for c in cc):
        # pass 2: provinces, only HS6 codes with Canada-level data, only live province chapters
        livecodes = {(c.split(".")[3], c.split(".")[4:7].__str__()) for c, s in have.items() if c.startswith("1.") and any(v for _, v in s)}
        cc = []
        for c, s in have.items():
            if not c.startswith("1.") or not any(v for _, v in s):
                continue
            p = c.split(".")
            for (g, e, ch) in live:
                if g != "1" and e == p[3] and ch == int(p[4]):
                    q = list(p); q[0] = g; cc.append(".".join(q))
    todo = [c for c in cc if c not in have]
    print(tag, "candidates", len(cc), "to fetch", len(todo), flush=True)
    chunks = [todo[i:i + 300] for i in range(0, len(todo), 300)]

    def job(ch):
        return fetch(pid, ch, N, batch=100, pause=0.1)

    with ThreadPoolExecutor(max_workers=4) as ex:
        for i, d in enumerate(ex.map(job, chunks)):
            # store every requested coordinate, empty list if not in cube, so reruns skip it
            have.update(d)
            for c in chunks[i]:
                have.setdefault(c, [])
            if i % 10 == 0 or i == len(chunks) - 1:
                json.dump(have, open(out, "w"))
                print(tag, "chunk", i + 1, "of", len(chunks), flush=True)
    json.dump(have, open(out, "w"))
    print(tag, "done, series with data:", sum(1 for s in have.values() if s), flush=True)
