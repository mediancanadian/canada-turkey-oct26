#!/usr/bin/env python3
"""Compute every number used on the slides and the site from the analysis files. Writes values.json.

Run from anywhere: python3 slides/values.py"""
import csv, json, math, os, re

W = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "analysis")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "values.json")
v = {}

# --- Canada's exports by partner, 2025 (StatCan 12-10-0171)
t = {}
for r in csv.DictReader(open(f"{W}/trade/out/x171_all_sections_extract.csv", encoding="utf-8-sig")):
    if r["REF_DATE"] == "2025" and r["North American Product Classification System (NAPCS)"] == "All sections":
        t[(r["Trading partner"], r["Trade"])] = float(r["VALUE"]) * 1000
ex_all, ex_us = t[("All countries", "Export")], t[("United States", "Export")]
ser = {}
for r in csv.DictReader(open(f"{W}/trade/out/x171_all_sections_extract.csv", encoding="utf-8-sig")):
    if r["North American Product Classification System (NAPCS)"] == "All sections" and r["Trade"] == "Export" and r["Trading partner"] in ("All countries", "United States"):
        ser.setdefault(int(r["REF_DATE"]), {})[r["Trading partner"]] = float(r["VALUE"])
v["us_share_years"] = sorted(ser)
v["us_share_series"] = [ser[y]["United States"] / ser[y]["All countries"] * 100 for y in v["us_share_years"]]
v["us_share_peak"] = max(v["us_share_series"])
v["us_share_peak_year"] = v["us_share_years"][v["us_share_series"].index(v["us_share_peak"])]
v["us_share_2025_is_lowest"] = v["us_share_series"][-1] == min(v["us_share_series"])
v["exports_all_2025"] = ex_all
v["exports_us_2025"] = ex_us
v["exports_rest_2025"] = ex_all - ex_us
v["us_share_pct"] = ex_us / ex_all * 100

# --- Canada-Türkiye annual totals (trade thread)
ann = {}
for r in csv.DictReader(open(f"{W}/trade/out/annual_totals_1988_2026ytd.csv")):
    if r["period"] == "Jan-Dec":
        ann[int(r["year"])] = {k: float(r[k]) for k in ("total_exports", "imports", "two_way", "import_to_export_ratio")}
a25 = ann[2025]
v["tr_exports_2025"], v["tr_imports_2025"], v["tr_two_way_2025"] = a25["total_exports"], a25["imports"], a25["two_way"]
v["ratio_2025"] = a25["import_to_export_ratio"]
v["ratio_highest_since"] = max(y for y in ann if y < 2025 and ann[y]["import_to_export_ratio"] >= a25["import_to_export_ratio"]) if any(
    ann[y]["import_to_export_ratio"] >= a25["import_to_export_ratio"] for y in ann if y < 2025) else min(ann)
v["series_years"] = [y for y in sorted(ann) if y >= 1988]
v["series_exports_b"] = [ann[y]["total_exports"] / 1e9 for y in v["series_years"]]
v["series_imports_b"] = [ann[y]["imports"] / 1e9 for y in v["series_years"]]
v["days_of_us_sales"] = a25["two_way"] / (ex_us / 365)
v["share_of_canada_trade_pct"] = a25["two_way"] / (ex_all + t[("All countries", "Import")]) * 100

g = json.load(open(f"{W}/trade/out/results_totals.json"))["growth_to_2025"]["5y"]
v["two_way_growth_5y_pct"] = g["two_way_total_pct"] * 100
v["two_way_cagr_5y_pct"] = g["two_way_cagr"] * 100
v["doubling_cagr_5y_pct"] = (2 ** (1 / 5) - 1) * 100
v["doubling_vs_past_ratio"] = v["doubling_cagr_5y_pct"] / v["two_way_cagr_5y_pct"]

# --- duties (tariffs thread)
exp = list(csv.DictReader(open(f"{W}/tariffs/outputs/ca_exports_to_TR_2025_est_tr_duty.csv")))
imp = list(csv.DictReader(open(f"{W}/tariffs/outputs/ca_imports_from_TR_2025_est_mfn_duty.csv")))


def grp_rate(rows, codecol, prefixes, valcol, dutycol):
    sel = [r for r in rows if any(r[codecol].startswith(p) for p in prefixes)]
    val = sum(float(r[valcol]) for r in sel)
    duty = sum(float(r[dutycol] or 0) for r in sel)
    return dict(value=val, duty=duty, rate=duty / val * 100 if val else 0)


lent = [r for r in exp if r["hs8"].startswith("071340") and "seed" not in r["desc"].lower() and float(r["total_pct"]) > 0]
v["lentil_duty_pct"] = max(float(r["total_pct"]) for r in lent)
v["receipt_to_tr"] = {
    "Lentils": grp_rate(exp, "hs8", ["071340"], "value_cad", "est_duty_cad"),
    "Aircraft": grp_rate(exp, "hs8", ["8802"], "value_cad", "est_duty_cad"),
    "Steel scrap": grp_rate(exp, "hs8", ["7204"], "value_cad", "est_duty_cad"),
    "Optical instruments": grp_rate(exp, "hs8", ["9013"], "value_cad", "est_duty_cad"),
    "Chickpeas": grp_rate(exp, "hs8", ["071320"], "value_cad", "est_duty_cad"),
}
v["receipt_to_ca"] = {
    "Medicines": grp_rate(imp, "hs10", ["3004", "3002"], "value_cad", "est_duty_cad"),
    "Fishing ship": grp_rate(imp, "hs10", ["8902"], "value_cad", "est_duty_cad"),
    "Turbine parts": grp_rate(imp, "hs10", ["8411"], "value_cad", "est_duty_cad"),
    "Carpets": grp_rate(imp, "hs10", ["57"], "value_cad", "est_duty_cad"),
    "Clothing": grp_rate(imp, "hs10", ["61", "62"], "value_cad", "est_duty_cad"),
}
iv = sum(float(r["value_cad"]) for r in imp)
v["tr_goods_duty_free_pct"] = sum(float(r["value_cad"]) for r in imp if r["mfn_rate"].strip().lower() == "free") / iv * 100

# --- provinces (domestic exports by province of origin, 2025)
prov = {r["geo"]: float(r["domestic_exports_2025"]) for r in csv.DictReader(open(f"{W}/trade/out/provinces_2021_2025.csv"))}
dom = prov.pop("Canada")
top = {}
for r in csv.DictReader(open(f"{W}/trade/out/province_top_hs6.csv")):
    if r["flow"] == "domestic_exports" and r["rank_2025"] == "1":
        top[r["province"]] = r["hs6"]
PRODUCT = {"071340": "lentils", "880240": "aircraft", "901380": "optical instruments", "841121": "aircraft engines",
           "720429": "steel scrap", "870390": "vehicles"}
v["provinces"] = sorted([dict(name=p, value=x, top=PRODUCT.get(top.get(p), "")) for p, x in prov.items()],
                        key=lambda d: -d["value"])
v["top3_share_pct"] = sum(d["value"] for d in v["provinces"][:3]) / dom * 100
v["domestic_exports_2025"] = dom

# --- energy
eb = open(f"{W}/energy/outputs/tr_energy_balance_2024.txt").read()
v["tr_energy_import_pct"] = float(re.search(r"net imports / supply = ([\d.]+)%", eb).group(1))
md = open(f"{W}/energy/results.md").read()
gas = {}
for name, vol in re.findall(r"^\| (Russia|Azerbaijan|United States \(LNG\)|Iran|Algeria \(LNG\)|Nigeria \(LNG\)|Others \(LNG mostly\)) \| ([\d,]+) \|", md, re.M):
    gas[name] = float(vol.replace(",", "")) / 1000
v["tr_gas_imports_bcm"] = gas
v["tr_gas_total_bcm"] = sum(gas.values())
cer = open(f"{W}/energy/outputs/cer_lng_summary.txt").read()
v["ca_lng_2025_bcm"] = float(re.search(r"== 2025 all: .*?= ([\d.]+) bcm", cer).group(1))
v["ca_lng_vs_tr_gas_pct"] = v["ca_lng_2025_bcm"] / v["tr_gas_total_bcm"] * 100

# --- defence
mil = {int(r["year"]): float(r["turkiye_value_cad"]) for r in csv.DictReader(open(f"{W}/defence/outputs/exports_turkiye_2010_2025.csv"))}
v["military_years"] = sorted(mil)
v["military_m"] = [mil[y] / 1e6 for y in v["military_years"]]

# --- facts with sources
for k, d in json.load(open(os.path.join(os.path.dirname(OUT), "facts.json"))).items():
    if not k.startswith("_"):
        v[k] = d["value"]

json.dump(v, open(OUT, "w"), indent=1, ensure_ascii=False)
for k in ("us_share_pct", "days_of_us_sales", "ratio_2025", "ratio_highest_since", "lentil_duty_pct", "tr_goods_duty_free_pct",
          "top3_share_pct", "tr_energy_import_pct", "tr_gas_total_bcm", "ca_lng_2025_bcm", "ca_lng_vs_tr_gas_pct",
          "two_way_growth_5y_pct", "two_way_cagr_5y_pct", "doubling_cagr_5y_pct", "doubling_vs_past_ratio", "share_of_canada_trade_pct"):
    print(k, round(v[k], 2) if isinstance(v[k], float) else v[k])
print("provinces", [(d["name"], round(d["value"] / 1e6, 1), d["top"]) for d in v["provinces"]])
print("receipt_to_tr", {k: (round(d["value"] / 1e6, 1), round(d["rate"], 1)) for k, d in v["receipt_to_tr"].items()})
print("receipt_to_ca", {k: (round(d["value"] / 1e6, 1), round(d["rate"], 1)) for k, d in v["receipt_to_ca"].items()})
print("gas", v["tr_gas_imports_bcm"])

# ===== round 2: specifics =====
v = json.load(open(OUT))
# receipt of goods each way, 2025 (HS6 top items), plus everything else so lines add to totals
top = list(csv.DictReader(open(f"{W}/trade/out/top15_hs6_2024_2025.csv")))
def items(flow, groups):
    rows = [r for r in top if r["flow"] == flow and r["year"] == "2025"]
    out = {}
    for name, codes in groups:
        out[name] = sum(float(r["value"]) for r in rows if any(r["hs6"].startswith(c) for c in codes))
    return out
v["goods_to_tr"] = items("total_exports", [("Lentils", ["071340"]), ("Aircraft", ["880240", "880230"]), ("Steel scrap", ["7204"]),
                                           ("Optical instruments", ["901380"]), ("Aircraft engines", ["8411"])])
v["goods_to_tr"]["Everything else"] = v["tr_exports_2025"] - sum(v["goods_to_tr"].values())
v["goods_to_ca"] = items("imports", [("Medicines", ["3004", "3002"]), ("Fishing ship", ["8902"]), ("Turbine parts", ["8411"]),
                                     ("Carpets", ["57"]), ("Steel", ["72", "73"])])
v["goods_to_ca"]["Everything else"] = v["tr_imports_2025"] - sum(v["goods_to_ca"].values())

# receipts of goods by everyday group (HS chapters), lines rounded to $M and adding to the total
h2 = {r["hs2"]: r for r in csv.DictReader(open(f"{W}/trade/out/hs2_chapters_2021_2025.csv"))}
def receipt(col, groups, total):
    out = {n: round(sum(float(h2[c][col]) for c in cs) / 1e6) for n, cs in groups}
    out["Everything else"] = round(total / 1e6) - sum(out.values())
    return out
v["receipt_goods_to_tr"] = receipt("exports_2025", [("Lentils, chickpeas, vegetables", ["07"]), ("Machinery and engines", ["84"]),
    ("Aircraft and parts", ["88"]), ("Optical instruments", ["90"]), ("Cars and parts", ["87"])], v["tr_exports_2025"])
v["receipt_goods_to_ca"] = receipt("imports_2025", [("Machinery and appliances", ["84"]), ("Steel and steel goods", ["72", "73"]),
    ("Fruit, nuts and food", ["08", "20"]), ("Medicines", ["30"]), ("Clothing", ["61", "62"])], v["tr_imports_2025"])

# last year Canada sold more than it bought
v["last_surplus_year"] = max(y for y in ann if ann[y]["total_exports"] > ann[y]["imports"])

# estimated duty by product, 2025 trade at 2026 rates
def duty(rows, codecol, prefixes):
    return sum(float(r["est_duty_cad"] or 0) for r in rows if any(r[codecol].startswith(p) for p in prefixes))
v["duty_in_tr"] = {"Lentils": duty(exp, "hs8", ["071340"]), "Chickpeas": duty(exp, "hs8", ["071320"]), "Cars": duty(exp, "hs8", ["8703"])}
v["duty_in_tr_durum"] = duty(exp, "hs8", ["1001"])
v["duty_in_tr_total"] = duty(exp, "hs8", [""])
v["duty_in_tr"]["Everything else"] = v["duty_in_tr_total"] - v["duty_in_tr_durum"] - sum(v["duty_in_tr"].values())
v["duty_in_ca"] = {"Clothing": duty(imp, "hs10", ["61", "62"]), "Carpets": duty(imp, "hs10", ["57"]), "Car parts": duty(imp, "hs10", ["87"])}
v["duty_in_ca_total"] = duty(imp, "hs10", [""])
v["duty_in_ca"]["Everything else"] = v["duty_in_ca_total"] - sum(v["duty_in_ca"].values())

# Saskatchewan lentils to Türkiye, from the trade thread's province HS6 results
m = re.search(r"Saskatchewan's lentil exports to Türkiye were C\$([\d.]+)M \(2021\), C\$([\d.]+)M \(2022\), C\$([\d.]+)M \(2023\), C\$([\d.]+)M \(2024\), C\$([\d.]+)M \(2025\)",
              open(f"{W}/trade/results.md").read())
v["sk_lentils_m"] = dict(zip([2021, 2022, 2023, 2024, 2025], [float(x) for x in m.groups()]))

# people
cen = {r["geography"]: r for r in csv.DictReader(open(f"{W}/people/outputs/census_turkish_by_geo.csv"))}
v["turkish_origin_canada"] = float(cen["Canada"]["eth_total"])
v["turkish_origin_cities"] = [(k.split(" (CMA)")[0], float(r["eth_total"])) for k, r in cen.items() if "(CMA)" in k][:6]
bd = json.load(open(f"{W}/people/outputs/turkiye_border_canada.json"))["annual_arrivals_canadian_nationals"]
v["ca_arrivals_years"] = sorted(int(y) for y in bd)
v["ca_arrivals"] = [bd[str(y)] for y in v["ca_arrivals_years"]]
v["ca_arrivals_2025_is_max"] = bd["2025"] == max(bd.values())
tv = json.load(open(f"{W}/people/outputs/travel_results.json"))
v["tr_visitors_to_ca_2025"] = [x for x in tv.values() if isinstance(x, dict) and x.get("annual", {}).get("2025") and x["annual"]["2025"] < 1e6][0]["annual"]["2025"]

# energy bill
fu = open(f"{W}/energy/results-followup.md").read()
v["tr_energy_bill_usd"] = float(re.search(r"\*\*USD ([\d,]+)\*\*", fu).group(1).replace(",", ""))

json.dump(v, open(OUT, "w"), indent=1, ensure_ascii=False)
for k in ("last_surplus_year", "duty_in_tr", "duty_in_tr_durum", "duty_in_tr_total", "duty_in_ca", "duty_in_ca_total", "sk_lentils_m",
          "turkish_origin_canada", "turkish_origin_cities", "ca_arrivals_2025_is_max", "tr_visitors_to_ca_2025", "tr_energy_bill_usd", "receipt_goods_to_tr", "receipt_goods_to_ca"):
    print(k, v[k])

# ===== round 3: opportunity, deficit, duty rates, provinces, travel, energy plans, defence =====
v = json.load(open(OUT))
mk = f"{W}/market/outputs"
wi = {r["hs2"]: float(r["usd"]) for r in csv.DictReader(open(f"{mk}/tur_imports_2025_hs2_world.csv"))}
ci = {r["hs2"]: float(r["usd"]) for r in csv.DictReader(open(f"{mk}/tur_imports_2025_hs2_canada.csv"))}
v["tr_imports_world_usd"] = sum(wi.values())
v["tr_imports_from_ca_usd"] = sum(ci.values())
v["ca_share_of_tr_imports_pct"] = v["tr_imports_from_ca_usd"] / v["tr_imports_world_usd"] * 100
cats = [("Energy", ["27"]), ("Machinery", ["84"]), ("Gold and jewellery", ["71"]), ("Aircraft", ["88"]), ("Lentils and other vegetables", ["07"])]
v["tr_buys"] = [dict(name=n, world=sum(wi.get(c, 0) for c in cs), canada=sum(ci.get(c, 0) for c in cs)) for n, cs in cats]
mf = open(f"{W}/market/results-followup.md").read()
v["tr_population"] = float(re.search(r"Population end-2025 \| ([\d,]+)", mf).group(1).replace(",", ""))
v["tr_median_age"] = float(re.search(r"Median age \| ([\d.]+)", mf).group(1))

# trade deficit
v["deficit_2025"] = a25["imports"] - a25["total_exports"]
yt = json.load(open(f"{W}/trade/out/results_totals.json"))["ytd"]
v["deficit_ytd_2025"] = -yt["2025"]["balance"]
v["deficit_ytd_2026"] = -yt["2026"]["balance"]
v["ytd_exports_change_pct"] = yt["pct_change"]["total_exports"] * 100
v["ytd_imports_change_pct"] = yt["pct_change"]["imports"] * 100
v["deficit_series"] = {y: ann[y]["imports"] - ann[y]["total_exports"] for y in range(2014, 2026)}

# duty rates, dollars and share of trade that pays duty (Canadian goods exclude durum wheat)
nd = [r for r in exp if not r["hs8"].startswith("1001")]
base_ca = sum(float(r["value_cad"]) for r in nd)
v["duty_ca_goods"] = dict(base=base_ca, duty=sum(float(r["est_duty_cad"] or 0) for r in nd),
                          free_pct=sum(float(r["value_cad"]) for r in nd if float(r["total_pct"] or 0) == 0) / base_ca * 100)
v["duty_ca_goods"]["rate"] = v["duty_ca_goods"]["duty"] / base_ca * 100
base_tr = sum(float(r["value_cad"]) for r in imp)
v["duty_tr_goods"] = dict(base=base_tr, duty=sum(float(r["est_duty_cad"] or 0) for r in imp),
                          free_pct=sum(float(r["value_cad"]) for r in imp if r["mfn_rate"].strip().lower() == "free") / base_tr * 100)
v["duty_tr_goods"]["rate"] = v["duty_tr_goods"]["duty"] / base_tr * 100
v["duty_rate_ratio"] = v["duty_ca_goods"]["rate"] / v["duty_tr_goods"]["rate"]
cl = [r for r in imp if r["hs10"][:2] in ("61", "62")]
v["clothing_duty_rate"] = sum(float(r["est_duty_cad"] or 0) for r in cl) / sum(float(r["value_cad"]) for r in cl) * 100

# provinces: top products, plain names, aircraft lines combined
NAMES = {"880240": "Aircraft", "880230": "Aircraft", "720429": "Steel scrap", "480100": "Newsprint", "901380": "Optical instruments",
         "870390": "Cars", "847710": "Plastic-moulding machines", "071340": "Lentils", "071320": "Chickpeas", "100119": "Durum wheat",
         "120190": "Soybeans", "841121": "Aircraft engines", "270112": "Coal", "071339": "Other pulses"}
pt = [r for r in csv.DictReader(open(f"{W}/trade/out/province_top_hs6.csv")) if r["flow"] == "domestic_exports"]
v["province_products"] = {}
for p in ("Quebec", "Ontario", "Saskatchewan", "British Columbia", "Alberta"):
    agg = {}
    for r in sorted([r for r in pt if r["province"] == p], key=lambda r: int(r["rank_2025"])):
        n = NAMES.get(r["hs6"])
        if n:
            agg[n] = agg.get(n, 0) + float(r["value_2025"])
    v["province_products"][p] = sorted(agg.items(), key=lambda kv: -kv[1])[:3]
# Cars: every passenger-car line (HS 8703.21 to 8703.90; 8703.10 is snow vehicles), summed from the full
# StatCan file, the same way the aircraft lines are combined
_code = {"Quebec": "QC", "Ontario": "ON", "Saskatchewan": "SK", "British Columbia": "BC", "Alberta": "AB"}
_cars = {}
for r in csv.reader(open(f"{W}/tariffs/outputs/domexports_TR_2025_hs6_by_province.csv", encoding="utf-8")):
    if r[0].startswith("2025") and r[2] == "TR" and r[1].startswith("8703") and r[1] != "870310":
        _cars[r[3]] = _cars.get(r[3], 0) + float(r[5])
for p, items in v["province_products"].items():
    v["province_products"][p] = sorted([(n, _cars.get(_code[p], 0) if n == "Cars" else x) for n, x in items], key=lambda kv: -kv[1])
v["sk_lentil_drop_pct"] = (1 - v["sk_lentils_m"]["2025"] / v["sk_lentils_m"]["2022"]) * 100

# travel
v["ca_arrivals_2019"] = bd["2019"]
v["ca_arrivals_2025_vs_2019"] = bd["2025"] / bd["2019"]

# energy plans (Türkiye Ministry of Energy goals; EPİAŞ installed capacity)
ep = open(f"{W}/energy/raw/round3/epias.txt").read()
v["tr_solar_mw_dec2025"] = float(re.search(r"Güneş\s+(\d{2}\.\d{3})\s*$", ep, re.M).group(1).replace(".", ""))
v["tr_wind_mw_dec2025"] = float(re.search(r"Rüzgar\s+(\d{2}\.\d{3})\s*$", ep, re.M).group(1).replace(".", ""))
v["tr_wind_solar_gw_dec2025"] = (v["tr_solar_mw_dec2025"] + v["tr_wind_mw_dec2025"]) / 1000
er = open(f"{W}/energy/results.md").read()
v["ca_uranium_world_share_pct"] = float(re.search(r"That was \*\*(\d+)% of world production\*\*", er).group(1))

# defence: 2025 brokering permit for Turkish ammunition to Ukraine
dr = open(f"{W}/defence/results.md").read()
v["brokering_ukraine_2025"] = float(re.search(r"ECL 2-3 \(ammunition\), \$([\d,]+) authorized", dr).group(1).replace(",", ""))

for k, d in json.load(open(os.path.join(os.path.dirname(OUT), "facts.json"))).items():
    if not k.startswith("_"):
        v[k] = d["value"]
json.dump(v, open(OUT, "w"), indent=1, ensure_ascii=False)
for k in ("ca_share_of_tr_imports_pct", "tr_buys", "tr_population", "tr_median_age", "deficit_2025", "deficit_ytd_2025", "deficit_ytd_2026",
          "ytd_exports_change_pct", "ytd_imports_change_pct", "duty_ca_goods", "duty_tr_goods", "duty_rate_ratio", "clothing_duty_rate",
          "province_products", "sk_lentil_drop_pct", "ca_arrivals_2025_vs_2019", "tr_wind_solar_gw_dec2025", "ca_uranium_world_share_pct",
          "brokering_ukraine_2025"):
    print(k, v[k])
