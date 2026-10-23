"""Annual and YTD totals, growth, balance, rank/share, CPI-adjusted growth, provinces (HS2 level).
Inputs (RAW dir): wds/hs2_*.json (CIMT cubes 12-10-0147, 12-10-0150), x171/12100171.csv,
x005/18100005.csv (CPI), boc_FXAUSDCAD.json, comtrade/*.json
Usage: python3 -I 03_analyse_totals.py RAW OUT
"""
import sys, json, csv, collections, glob, os

RAW, OUT = sys.argv[1], sys.argv[2]
LAST = None
PROV = {"1": "Canada", "10": "Newfoundland and Labrador", "11": "Prince Edward Island", "12": "Nova Scotia",
        "13": "New Brunswick", "24": "Quebec", "35": "Ontario", "46": "Manitoba", "47": "Saskatchewan",
        "48": "Alberta", "59": "British Columbia", "60": "Yukon", "61": "Northwest Territories", "62": "Nunavut"}
meta = json.load(open(os.path.join(RAW, "meta_12100147.json")))[0]["object"]
CHN = {str(m["memberId"]): m["memberNameEn"] for d in meta["dimension"] if d["dimensionNameEn"] == "HS2" for m in d["member"]}


def load(f):
    return json.load(open(os.path.join(RAW, "wds", f)))


E, I = load("hs2_exports_tur.json"), load("hs2_imports_tur.json")
EW, IW = load("hs2_exports_world.json"), load("hs2_imports_world.json")

# monthly[(flow, geo, chapter)][YYYY-MM] = dollars ; flow: DE, RE, IM
monthly = collections.defaultdict(dict)
for src, flowmap in [(E, {"1": "DE", "2": "RE"}), (I, {"1": "IM"})]:
    for c, s in src.items():
        g, _, _, e, ch = c.split(".")[:5]
        for r, v in s:
            if v is not None:
                monthly[(flowmap[e], g, ch)][r] = v
months = sorted({r for d in monthly.values() for r in d})
LAST = months[-1]
lm = int(LAST[5:7])
print("latest month", LAST)


def ann(flow, geo="1", ch=None, ytd=False):
    a = collections.defaultdict(float)
    for (f, g, c), d in monthly.items():
        if f != flow or g != geo or (ch and c != ch):
            continue
        for r, v in d.items():
            if ytd and int(r[5:7]) > lm:
                continue
            a[int(r[:4])] += v
    return a

DE, RE, IM = ann("DE"), ann("RE"), ann("IM")
DEy, REy, IMy = ann("DE", ytd=True), ann("RE", ytd=True), ann("IM", ytd=True)

# CPI annual, Canada all-items (18-10-0005)
cpi = {}
for row in csv.DictReader(open(os.path.join(RAW, "x005", "18100005.csv"), encoding="utf-8-sig")):
    if row["GEO"] == "Canada" and row["Products and product groups"] == "All-items" and row["VALUE"]:
        cpi[int(row["REF_DATE"])] = float(row["VALUE"])

rows = []
for y in range(1988, int(LAST[:4]) + 1):
    full = y < int(LAST[:4])
    te = DE[y] + RE[y]
    rows.append({"year": y, "period": "Jan-Dec" if full else "Jan-%s YTD" % ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][lm-1],
                 "domestic_exports": DE[y], "re_exports": RE[y], "total_exports": te, "imports": IM[y],
                 "two_way": te + IM[y], "balance": te - IM[y],
                 "import_to_export_ratio": IM[y] / te if te else None,
                 "cpi_2002_100": cpi.get(y),
                 "two_way_2025_dollars": (te + IM[y]) * cpi[2025] / cpi[y] if y in cpi else None})
with open(os.path.join(OUT, "annual_totals_1988_2026ytd.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

R = {r["year"]: r for r in rows}
res = {"latest_month": LAST}
# YTD comparison
y0, y1 = int(LAST[:4]) - 1, int(LAST[:4])
ytd = {}
for y in (y0, y1):
    te = DEy[y] + REy[y]
    ytd[y] = {"total_exports": te, "domestic_exports": DEy[y], "re_exports": REy[y], "imports": IMy[y],
              "two_way": te + IMy[y], "balance": te - IMy[y]}
ytd["pct_change"] = {k: ytd[y1][k] / ytd[y0][k] - 1 for k in ytd[y1] if k != "balance"}
res["ytd"] = ytd

def cagr(a, b, n):
    return (b / a) ** (1 / n) - 1

g = {}
for n in (5, 10, 15, 20, 25):
    a, b = R[2025 - n], R[2025]
    g["%dy" % n] = {"from": 2025 - n,
                   "two_way_total_pct": b["two_way"] / a["two_way"] - 1,
                   "two_way_cagr": cagr(a["two_way"], b["two_way"], n),
                   "exports_cagr": cagr(a["total_exports"], b["total_exports"], n),
                   "imports_cagr": cagr(a["imports"], b["imports"], n),
                   "two_way_real_cagr": cagr(a["two_way_2025_dollars"], b["two_way_2025_dollars"], n),
                   "cpi_change": cpi[2025] / cpi[2025 - n] - 1}
res["growth_to_2025"] = g
# 2021-2025 vs 2020 (PMO "almost 50% in five years")
res["check_pmo_50pct"] = {"2020_to_2025": R[2025]["two_way"] / R[2020]["two_way"] - 1,
                          "2019_to_2024": R[2024]["two_way"] / R[2019]["two_way"] - 1,
                          "2020_to_2024": R[2024]["two_way"] / R[2020]["two_way"] - 1}

# ---- share and rank, 2025, from table 12-10-0171 (annual, by country) ----
t = collections.defaultdict(dict)
for row in csv.DictReader(open(os.path.join(RAW, "x171", "12100171.csv"), encoding="utf-8-sig")):
    if row["North American Product Classification System (NAPCS)"] != "All sections" or not row["VALUE"]:
        continue
    t[(int(row["REF_DATE"]), row["Trading partner"])][row["Trade"]] = float(row["VALUE"]) * 1000
rank = {}
for y in (2015, 2020, 2024, 2025):
    world = t[(y, "All countries")]
    partners = [(p, d.get("Export", 0), d.get("Import", 0)) for (yy, p), d in t.items() if yy == y and p not in ("All countries", "Canada", "High Seas")]
    # "Canada" as partner = Canadian-origin goods re-imported; excluded from partner ranking
    ranked = {}
    for key, fn in [("two_way", lambda x: x[1] + x[2]), ("exports", lambda x: x[1]), ("imports", lambda x: x[2])]:
        s = sorted(partners, key=fn, reverse=True)
        pos = [i for i, x in enumerate(s) if x[0] == "Türkiye"][0]
        ranked[key] = {"rank": pos + 1, "of": len(s),
                       "neighbours": [(i + 1, x[0], fn(x)) for i, x in enumerate(s) if abs(i - pos) <= 3]}
    tu = t[(y, "Türkiye")]
    rank[y] = {"world_exports": world["Export"], "world_imports": world["Import"],
               "tur_exports": tu["Export"], "tur_imports": tu["Import"],
               "share_two_way": (tu["Export"] + tu["Import"]) / (world["Export"] + world["Import"]),
               "share_exports": tu["Export"] / world["Export"], "share_imports": tu["Import"] / world["Import"],
               "rank": ranked}
res["share_rank"] = rank
# country-level 12-10-0171 vs WDS reconstruction check
res["check_0171_vs_cimt"] = {y: {"0171_export": t[(y, "Türkiye")]["Export"], "cimt_total_exports": R[y]["total_exports"],
                                 "0171_import": t[(y, "Türkiye")]["Import"], "cimt_imports": R[y]["imports"]}
                             for y in range(1999, 2026)}

# ---- HS2 by year (2024, 2025, YTD) ----
hs2 = []
for ch in sorted({c for (_, _, c) in monthly}, key=int):
    de, re_, im = ann("DE", ch=ch), ann("RE", ch=ch), ann("IM", ch=ch)
    hs2.append({"hs2": ch.zfill(2), "description": CHN.get(ch, ""),
                **{"exports_%d" % y: de[y] + re_[y] for y in (2021, 2022, 2023, 2024, 2025)},
                **{"domestic_exports_%d" % y: de[y] for y in (2024, 2025)},
                **{"imports_%d" % y: im[y] for y in (2021, 2022, 2023, 2024, 2025)}})
with open(os.path.join(OUT, "hs2_chapters_2021_2025.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(hs2[0].keys())); w.writeheader(); w.writerows(hs2)

# ---- provinces ----
prov = []
for g, name in PROV.items():
    de, im = ann("DE", geo=g), ann("IM", geo=g)
    prov.append({"geo": name, **{"domestic_exports_%d" % y: de[y] for y in range(2021, 2026)},
                 "domestic_exports_avg_2021_2025": sum(de[y] for y in range(2021, 2026)) / 5,
                 **{"imports_clearance_%d" % y: im[y] for y in range(2021, 2026)},
                 "imports_clearance_avg_2021_2025": sum(im[y] for y in range(2021, 2026)) / 5})
with open(os.path.join(OUT, "provinces_2021_2025.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(prov[0].keys())); w.writeheader(); w.writerows(prov)
# top HS2 per province, 2025 domestic exports
ptop = {}
for g, name in PROV.items():
    if g == "1":
        continue
    lst = []
    for ch in CHN:
        v = ann("DE", geo=g, ch=ch)[2025]
        if v:
            lst.append((ch.zfill(2), CHN[ch][:70], v))
    ptop[name] = sorted(lst, key=lambda x: -x[2])[:3]
res["province_top_hs2_2025"] = ptop

# ---- doubling arithmetic ----
base = R[2025]["two_way"]
fx = {o["d"][:4]: float(o["FXAUSDCAD"]["v"]) for o in json.load(open(os.path.join(RAW, "boc_FXAUSDCAD.json")))["observations"]}
res["fx_2025_usdcad"] = fx["2025"]
dbl = {"base_2025_two_way_cad": base, "base_2025_two_way_usd_at_2025_avg": base / fx["2025"], "targets": {}}
for label, tgt in [("double_2025_cad", 2 * base), ("10B_CAD", 10e9), ("10B_USD_as_CAD_at_2025_fx", 10e9 * fx["2025"])]:
    dbl["targets"][label] = {"target_cad": tgt, "multiple_of_2025": tgt / base,
                             **{"cagr_needed_%dy" % n: (tgt / base) ** (1 / n) - 1 for n in (5, 10)}}
res["doubling"] = dbl

# ---- trade gap over time ----
gap = {y: {"ratio": R[y]["import_to_export_ratio"], "balance": R[y]["balance"]} for y in range(1988, 2026)}
res["gap"] = gap
avg = lambda ys, k: sum(R[y][k] for y in ys) / len(ys)
res["gap_5y_avgs"] = {"%d-%d" % (a, a + 4): {"avg_ratio": sum(R[y]["imports"] for y in range(a, a + 5)) / sum(R[y]["total_exports"] for y in range(a, a + 5)),
                                            "avg_balance": avg(range(a, a + 5), "balance")}
                      for a in (1991, 1996, 2001, 2006, 2011, 2016, 2021)}

# ---- Comtrade mirror ----
mir = {}
for f in glob.glob(os.path.join(RAW, "comtrade", "total_r*.json")):
    for x in json.load(open(f)).get("data", []):
        mir.setdefault(x["period"], {})["%s_%s" % ({124: "CAN", 792: "TUR"}[x["reporterCode"]], x["flowCode"])] = x["primaryValue"]
for y, d in mir.items():
    if y in fx:
        d["fx"] = fx[y]
        d["CAN_X_cimt_usd"] = R[int(y)]["total_exports"] / fx[y]
        d["CAN_M_cimt_usd"] = R[int(y)]["imports"] / fx[y]
res["comtrade_mirror_usd"] = dict(sorted(mir.items()))

json.dump(res, open(os.path.join(OUT, "results_totals.json"), "w"), indent=1, ensure_ascii=False, default=str)
print(json.dumps({k: res[k] for k in ("ytd", "growth_to_2025", "check_pmo_50pct", "doubling")}, indent=1, default=str))
