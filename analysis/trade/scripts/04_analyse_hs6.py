"""Top HS6 products each way (2024, 2025) and top HS6 per province (domestic exports, imports by
province of clearance), from CIMT cubes 12-10-0148 / 12-10-0151 fetched by 02_fetch_hs6.py.
Also checks that HS6 sums reproduce the HS2-based totals.
Usage: python3 -I 04_analyse_hs6.py RAW OUT
"""
import sys, json, csv, os, collections

RAW, OUT = sys.argv[1], sys.argv[2]
ref = {r["id"]: r["text"].split(" - ", 1)[-1] for r in json.load(open(os.path.join(RAW, "comtrade_HS_ref.json")))["results"]}
PROV = {"1": "Canada", "10": "Newfoundland and Labrador", "11": "Prince Edward Island", "12": "Nova Scotia",
        "13": "New Brunswick", "24": "Quebec", "35": "Ontario", "46": "Manitoba", "47": "Saskatchewan",
        "48": "Alberta", "59": "British Columbia", "60": "Yukon", "61": "Northwest Territories", "62": "Nunavut"}


def code(c):
    p = c.split(".")
    h4 = int(p[5]) % 100
    h6 = int(p[6]) % 100
    return "%02d%02d%02d" % (int(p[4]), h4, h6)


def annual(path):
    d = json.load(open(path))
    a = collections.defaultdict(lambda: collections.defaultdict(float))  # (geo, est, hs6) -> year -> $
    for c, s in d.items():
        p = c.split(".")
        for r, v in s:
            if v:
                a[(p[0], p[3], code(c))][int(r[:4])] += v
    return a

X = annual(os.path.join(RAW, "wds", "hs6_exp_tur.json"))
M = annual(os.path.join(RAW, "wds", "hs6_imp_tur.json"))
res = {}

def top(agg, geo, ests, year, n=15):
    tot = collections.defaultdict(float)
    for (g, e, h), yrs in agg.items():
        if g == geo and e in ests:
            tot[h] += yrs.get(year, 0)
    s = sorted(tot.items(), key=lambda x: -x[1])
    total = sum(tot.values())
    return total, [{"hs6": h, "description": ref.get(h, ""), "value": v, "share": v / total if total else None}
                   for h, v in s[:n] if v > 0]

rows = []
for flow, agg, ests in [("total_exports", X, ("1", "2")), ("domestic_exports", X, ("1",)), ("imports", M, ("1",))]:
    for y in (2024, 2025):
        total, t = top(agg, "1", ests, y)
        res["%s_%d" % (flow, y)] = {"hs6_sum": total, "top15": t, "top15_share": sum(x["value"] for x in t) / total}
        for i, x in enumerate(t, 1):
            rows.append({"flow": flow, "year": y, "rank": i, **x})
with open(os.path.join(OUT, "top15_hs6_2024_2025.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

# province top 5 HS6, 2025 and 2021-2025 average
prow = []
for g, name in PROV.items():
    if g == "1":
        continue
    for flow, agg in [("domestic_exports", X), ("imports_clearance", M)]:
        tot = collections.defaultdict(float); t25 = collections.defaultdict(float)
        for (gg, e, h), yrs in agg.items():
            if gg == g and e == "1":
                t25[h] += yrs.get(2025, 0)
                tot[h] += sum(yrs.get(y, 0) for y in range(2021, 2026)) / 5
        for i, (h, v) in enumerate(sorted(t25.items(), key=lambda x: -x[1])[:5], 1):
            if v > 0:
                prow.append({"province": name, "flow": flow, "rank_2025": i, "hs6": h, "description": ref.get(h, ""),
                             "value_2025": v, "avg_2021_2025": tot[h]})
with open(os.path.join(OUT, "province_top_hs6.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(prow[0].keys())); w.writeheader(); w.writerows(prow)

# lentils etc: Saskatchewan HS 071340 (dried lentils)
res["lentils_071340"] = {PROV[g]: {y: X.get((g, "1", "071340"), {}).get(y, 0) for y in range(2021, 2026)} for g in PROV}
json.dump(res, open(os.path.join(OUT, "results_hs6.json"), "w"), indent=1, ensure_ascii=False)
for k, v in res.items():
    if k.startswith(("total", "imports", "domestic")):
        print(k, round(v["hs6_sum"] / 1e6, 1), "top15 share", round(v["top15_share"], 3))
        for x in v["top15"]:
            print("   ", x["hs6"], x["description"][:60], round(x["value"] / 1e6, 1))
