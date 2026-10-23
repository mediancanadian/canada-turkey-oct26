"""Fetch Canada-Turkiye monthly trade by HS2 chapter and province, 1988-01 to latest,
from StatCan CIMT cubes via WDS:
  12-10-0147 (exports: domestic exports and re-exports, by province of origin, HS2)
  12-10-0150 (imports, by province of clearance, HS2)
Country member 382 = Turkiye; State member 100 = Not applicable.
Usage: python3 -I 01_fetch_hs2.py OUTDIR
"""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wds import fetch

out = sys.argv[1]
GEOS = [1, 10, 11, 12, 13, 24, 35, 46, 47, 48, 59, 60, 61, 62]
CH = [c for c in range(1, 100) if c != 77]
N = 480  # more than 1988-01..2026-08

def run(pid, ests, fname, partner=382):
    coords = ["%d.%d.100.%d.%d" % (g, partner, e, c) for g in GEOS for e in ests for c in CH]
    data = fetch(pid, coords, N)
    json.dump(data, open(os.path.join(out, fname), "w"))
    print(fname, len(coords), "requested", len(data), "returned")

run(12100147, [1, 2], "hs2_exports_tur.json")
run(12100150, [1], "hs2_imports_tur.json")
# World totals for Canada (country 1000 = All countries), Canada-level only
coords = ["1.1000.100.%d.%d" % (e, c) for e in [1, 2] for c in CH]
json.dump(fetch(12100147, coords, N), open(os.path.join(out, "hs2_exports_world.json"), "w"))
coords = ["1.1000.100.1.%d" % c for c in CH]
json.dump(fetch(12100150, coords, N), open(os.path.join(out, "hs2_imports_world.json"), "w"))
print("done")
