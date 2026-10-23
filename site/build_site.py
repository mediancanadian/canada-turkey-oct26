#!/usr/bin/env python3
"""Build index.html, the explorable page for "Talking trade with Türkiye" (The Median Canadian, week 2).

Every number shared with the slides is read from slides/values.json, which slides/values.py computes from the
analysis outputs; the page only adds detail read from the same output files. The page is one self-contained file
(styles, script and data inline) apart from the three logo images.

Run from anywhere:  python3 site/build_site.py   (needs Python 3 and pyproj)
Writes index.html and data/site.json, data/references.json and data/chapters.json.
"""
import csv, html, json, re
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
A = ROOT / "analysis"
V = json.load(open(ROOT / "slides/values.json", encoding="utf-8"))
SITE = "https://sjvadrevu.github.io/canada-turkey-oct26/"
REPO = "https://github.com/sjvadrevu/canada-turkey-oct26"
HUB = "https://sjvadrevu.github.io/the-median-canadian/"
E = html.escape


# ---------------------------------------------------------------- number formats (rounded half up, as on the slides)
def nf(v, d=0):
    q = Decimal(repr(float(v))).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"{q:,.{d}f}"


def bn(x, d=1):
    return f"${nf(x / 1e9, d)} billion"


def mn(x, d=0):
    return f"${nf(x / 1e6, d)} million"


def ubn(x, d=0):
    return f"US${nf(x / 1e9, d)} billion"


def ordinal(n):
    return f"{n}{'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"


def pct(x, d=0):
    return f"{nf(x, d)}%"


def rows(path, enc="utf-8"):
    return list(csv.DictReader(open(path, encoding=enc)))


# ---------------------------------------------------------------- references (official and primary sources only)
REFS = {
    "pmo-1023": ("Prime Minister's Office. Prime Minister Carney's historic visit to Türkiye launches new Strategic Partnership. News release, October 23, 2026.",
                 "https://www.pm.gc.ca/en/news/news-releases/2026/10/23/prime-minister-carneys-historic-visit-turkiye-launches-new-strategic"),
    "pmo-joint": ("Prime Minister's Office. Statement by Prime Minister Carney and President Recep Tayyip Erdoğan. October 22, 2026.",
                  "https://www.pm.gc.ca/en/news/statements/2026/10/22/statement-prime-minister-carney-and-president-recep-tayyip-erdogan"),
    "pmo-readout": ("Prime Minister's Office. Prime Minister Carney meets with President of Türkiye Recep Tayyip Erdoğan. Readout, October 22, 2026.",
                    "https://www.pm.gc.ca/en/news/readouts/2026/10/22/prime-minister-carney-meets-president-turkiye-recep-tayyip-erdogan"),
    "pmo-1006": ("Prime Minister's Office. Prime Minister Carney to visit Türkiye to advance partnership across trade and investment, energy, and defence. News release, October 6, 2026.",
                 "https://www.pm.gc.ca/en/news/news-releases/2026/10/06/prime-minister-carney-visit-turkiye-advance-partnership-across-trade"),
    "pmo-251029": ("Prime Minister's Office. Prime Minister Carney strengthens trade and economic partnerships with Singapore. News release, October 29, 2025.",
                   "https://www.pm.gc.ca/en/news/news-releases/2025/10/29/prime-minister-carney-strengthens-trade-and-economic-partnerships"),
    "energy-js": ("Natural Resources Canada and Türkiye's Ministry of Energy and Natural Resources. Joint statement on cooperation in the field of energy. October 2026.",
                  "https://www.newswire.ca/news-releases/joint-statement-between-the-minister-of-energy-and-natural-resources-of-canada-and-the-minister-of-energy-and-natural-resources-of-turkiye-on-cooperation-in-the-field-of-energy-892792181.html"),
    "statcan-cimt": ("Statistics Canada. Canadian International Merchandise Trade (CIMT): monthly exports by province of origin and imports by province of clearance, by country and HS product, 1988 to August 2026 (tables 12-10-0147, 12-10-0148, 12-10-0150 and 12-10-0151, read through Statistics Canada's Web Data Service).",
                     "https://www150.statcan.gc.ca/n1/en/catalogue/71-607-X2021004"),
    "statcan-171": ("Statistics Canada. Table 12-10-0171-01, international merchandise trade by country and product section, annual, 1999 to 2025.",
                    "https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1210017101"),
    "statcan-cimt-files": ("Statistics Canada. Canadian International Merchandise Trade, 2025 data files: domestic exports by HS8 and imports by HS10.",
                           ["https://www150.statcan.gc.ca/n1/pub/71-607-x/2021004/zip/CIMT-CICM_Dom_Exp_2025.zip",
                            "https://www150.statcan.gc.ca/n1/pub/71-607-x/2021004/zip/CIMT-CICM_Imp_2025.zip"]),
    "comtrade": ("United Nations. UN Comtrade database: Türkiye's imports in 2025 by partner, as reported by Türkiye.",
                 "https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=792&period=2025&flowCode=M&cmdCode=TOTAL&partner2Code=0&motCode=0&customsCode=C00"),
    "comtrade-hs": ("United Nations. UN Comtrade database: Türkiye's imports in 2025 by HS chapter, from the world and from Canada, as reported by Türkiye.",
                    ["https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=792&period=2025&flowCode=M&cmdCode=AG2&partnerCode=0&partner2Code=0&motCode=0&customsCode=C00",
                     "https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=792&period=2025&flowCode=M&cmdCode=AG2&partnerCode=124&partner2Code=0&motCode=0&customsCode=C00"]),
    "turkstat": ("Turkish Statistical Institute (TurkStat). Address Based Population Registration System results, 2025.",
                 "https://veriportali.tuik.gov.tr/en/press/53899"),
    "cbsa": ("Canada Border Services Agency. Customs Tariff 2026 (T2026-2).",
             "https://www.cbsa-asfc.gc.ca/trade-commerce/tariff-tarif/2026/menu-eng.html"),
    "tr-tariff": ("Türkiye Ministry of Trade. 2026 Import Regime Decision (No. 3350) and Additional Customs Duty Decision (No. 3351), consolidated annexes.",
                  "https://ticaret.gov.tr/ithalat/ithalat-mevzuati/ithalat-rejimi-karari-igv-karari-ve-ithalat-tebligleri/1-ithalat-rejimi-kararikarar-sayisi3350karar-metni-ve-tablolar-konsolide-edilmis-olup-gunceldir"),
    "tr-schedule": ("Resmî Gazete (Official Gazette of Türkiye). Decision No. 10781, 2026 Turkish Customs Tariff Schedule, December 30, 2025.",
                    "https://www.resmigazete.gov.tr/eskiler/2025/12/20251230M1-2.pdf"),
    "wto-tpr": ("World Trade Organization. Trade Policy Review: Türkiye, report by the Secretariat, WT/TPR/S/439, 2023 (inward processing).",
                "https://www.wto.org/english/tratop_e/tpr_e/s439_e.pdf"),
    "census": ("Statistics Canada. 2021 Census of Population, table 98-10-0356-01 (ethnic or cultural origin) and place of birth tables.",
               "https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810035601"),
    "guinness": ("Guinness World Records. Most countries flown to by an airline (Turkish Airlines, 120 countries, September 2023 to September 2024).",
                 "https://www.guinnessworldrecords.com/world-records/736843-most-countries-flown-by-a-commercial-airline"),
    "aci": ("Airports Council International World. World's busiest airports, 2025 passenger rankings. July 15, 2026.",
            "https://aci.aero/2026/07/15/worlds-busiest-airports-atlanta-holds-asia-climbs-strong-demand-while-asia-pacific-growth-reshape-the-rankings/"),
    "ktb": ("Türkiye Ministry of Culture and Tourism. Border statistics, yearly bulletins: arriving foreign visitors by nationality, 2010 to 2025.",
            "https://yigm.ktb.gov.tr/TR-249709/yillik-bultenler.html"),
    "cta-25": ("Canadian Transportation Agency. Determination A-2025-25, Turkish Airlines request for extra weekly flights. February 14, 2025.",
               "https://otc-cta.gc.ca/eng/ruling/a-2025-25"),
    "cta-77": ("Canadian Transportation Agency. Determination A-2025-77. April 29, 2025.",
               "https://otc-cta.gc.ca/eng/ruling/a-2025-77"),
    "transat": ("Air Transat. News release on flights from Montréal to Istanbul, May 29, 2026.",
                "https://www.transat.com/en-CA/corporate/media/news-releases/124611"),
    "ircc-pr": ("Immigration, Refugees and Citizenship Canada. Open data: permanent residents by country of citizenship, 2015 to 2026.",
                "https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP-PR-Citz.xlsx"),
    "ircc-study": ("Immigration, Refugees and Citizenship Canada. Open data: study permit holders on December 31 by country of citizenship.",
                   "https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP_annual-TR-Study-IS_CITZ_year_end.xlsx"),
    "ircc-work": ("Immigration, Refugees and Citizenship Canada. Open data: work permit holders on December 31 by country of citizenship, International Mobility Program (all purposes) and Temporary Foreign Worker Program.",
                  ["https://www.ircc.canada.ca/opendata-donneesouvertes/data/en_odp_annual-tr-work-imp_citz_year_end_all_purpose.xlsx",
                   "https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP_annual-TR-work-TFW_CITZ_year_end.xlsx"]),
    "ircc-quake": ("Immigration, Refugees and Citizenship Canada. Temporary public policy for nationals of Türkiye and Syria affected by the earthquakes of February 6, 2023.",
                   "https://www.canada.ca/en/immigration-refugees-citizenship/corporate/mandate/policies-operational-instructions-agreements/public-policies/turkiye-syria-earthquake-2023.html"),
    "menr-2023": ("Türkiye Ministry of Energy and Natural Resources. Nuclear power goals: 7.2 GW added by 2035 and over 20 GW by 2050. September 25, 2023.",
                  "https://enerji.gov.tr/news-detail?id=21184"),
    "menr-2024": ("Türkiye Ministry of Energy and Natural Resources. 120,000 MW of wind and solar capacity by 2035. November 4, 2024.",
                  "https://enerji.gov.tr/news-detail?id=21392"),
    "menr-candu": ("Türkiye Ministry of Energy and Natural Resources. TÜNAŞ and AtkinsRéalis memorandum on CANDU technology. March 2026.",
                   "https://enerji.gov.tr/news-detail?id=31758"),
    "atkins": ("AtkinsRéalis. Trade release on the CANDU assessment in Türkiye. March 3, 2026.",
               "https://www.atkinsrealis.com/en/media/trade-releases/2026/2026-03-03-a"),
    "invest-tr": ("Presidency of the Republic of Türkiye, Investment Office. Energy sector: Net Zero 2053 and the Akkuyu plant.",
                  "https://www.invest.gov.tr/en/Sectors/Pages/energy.aspx"),
    "pris": ("International Atomic Energy Agency. Power Reactor Information System (PRIS): Türkiye's reactors under construction, Akkuyu units 1 to 4.",
             "https://pris-stats.iaea.org/"),
    "epias": ("EPİAŞ (Energy Exchange Istanbul). Türkiye electricity market daily bulletin, December 14, 2025: installed capacity.",
              "https://www.epias.com.tr/wp-content/uploads/2025/12/epias-bulten-14.12.2025.pdf"),
    "epdk": ("Energy Market Regulatory Authority of Türkiye (EPDK). 2025 Natural Gas Market Development Report: imports by country.",
             "https://www.epdk.gov.tr/Detay/DownloadDocument?id=fSTHy8vYN/Q="),
    "cer-lng": ("Canada Energy Regulator. Liquefied natural gas exports, shipment detail.",
                "https://www.cer-rec.gc.ca/open/imports-exports/liquefied-natural-gas-exports-detail.csv"),
    "nrcan-u": ("Natural Resources Canada. Uranium and nuclear power facts (2024 production and world share).",
                "https://natural-resources.canada.ca/minerals-mining/mining-data-statistics-analysis/minerals-metals-facts/uranium-nuclear-power-facts"),
    "gac-mil": ("Global Affairs Canada. Reports on Exports of Military Goods, 2010 to 2025 (exports to Türkiye by year; 2025 report, table 16, brokering permits).",
                "https://international.canada.ca/en/global-affairs/corporate/reports/export-import-controls/strategic-goods-2025"),
    "gac-2021": ("Global Affairs Canada. Statement from Minister Garneau on the cancellation of export permits to Turkey. April 12, 2021.",
                 "https://www.canada.ca/en/global-affairs/news/2021/04/statement-fromminister-garneauto-announce-the-cancellation-of-export-permits-to-turkey.html"),
    "gac-1108": ("Global Affairs Canada. Notice to Exporters No. 1108: export permit applications for Türkiye. January 2024.",
                 "https://www.international.gc.ca/trade-commerce/controls-controles/notices-avis/1108.aspx?lang=eng"),
    "nato-exp": ("NATO. Defence expenditure of NATO countries, 2026 estimates (military personnel).",
                 "https://www.nato.int/content/dam/nato/webready/documents/finance/def-exp-2026-en.pdf"),
    "ancc": ("Armenian National Committee of Canada. Submission to the Canada-Türkiye free trade agreement consultation. September 24, 2026.",
             "https://anccanada.org/ancc-calls-on-canada-to-protect-export-controls-in-canada-turkey-fta/"),
}
ORDER = []


def links(k):
    u = REFS[k][1]
    return u if isinstance(u, list) else [u]


def cite(keys):
    nums = []
    for k in keys.split(","):
        k = k.strip()
        assert k in REFS, k
        if k not in ORDER:
            ORDER.append(k)
        nums.append(ORDER.index(k) + 1)
    links = ",".join(f'<a href="#ref-{n}" aria-label="Reference {n}">{n}</a>' for n in sorted(set(nums)))
    return f'<sup class="cite">{links}</sup>'


# ---------------------------------------------------------------- data for the explorable charts
D = {}

# chapter names: plain words for the HS chapters that appear in the charts
HS2 = {
    "07": "Vegetables, incl. lentils and chickpeas", "08": "Fruit and nuts", "10": "Cereals", "12": "Oilseeds",
    "15": "Fats and oils", "17": "Sugar and sweets", "18": "Cocoa and chocolate", "20": "Prepared fruit and vegetables",
    "26": "Ores", "27": "Energy: oil, gas and coal", "28": "Inorganic chemicals", "29": "Organic chemicals", "30": "Medicines",
    "31": "Fertilizers", "33": "Perfumes and cosmetics", "36": "Explosives and fireworks", "38": "Other chemical products",
    "39": "Plastics", "40": "Rubber", "44": "Wood", "47": "Wood pulp", "48": "Paper and paperboard", "52": "Cotton",
    "54": "Synthetic yarn", "55": "Synthetic fibres", "57": "Carpets", "61": "Knitted clothing", "62": "Other clothing",
    "63": "Other textile goods", "64": "Footwear", "68": "Stone and cement goods", "69": "Ceramics", "70": "Glass",
    "71": "Gold, gems and jewellery", "72": "Iron and steel", "73": "Steel goods", "74": "Copper", "76": "Aluminum",
    "84": "Machinery and engines", "85": "Electrical equipment", "86": "Railway equipment", "87": "Cars and parts",
    "88": "Aircraft and parts", "89": "Ships and boats", "90": "Optical and medical instruments", "93": "Arms and ammunition",
    "94": "Furniture", "95": "Toys and sports goods", "98": "Special classifications", "99": "Other",
}
H2DESC = {r["hs2"]: r["description"] for r in rows(A / "trade/out/hs2_chapters_2021_2025.csv")}


def hs2name(c):
    if c in HS2:
        return HS2[c]
    d = H2DESC.get(c, f"Chapter {int(c)}").split(" - ", 1)[-1]
    return re.split(r"[;,]", d)[0].strip()


# 1. what Türkiye buys, and Canada's part (UN Comtrade, as reported by Türkiye, US dollars)
wi = {r["hs2"]: float(r["usd"]) for r in rows(A / "market/outputs/tur_imports_2025_hs2_world.csv")}
ci = {r["hs2"]: float(r["usd"]) for r in rows(A / "market/outputs/tur_imports_2025_hs2_canada.csv")}
assert abs(sum(wi.values()) - V["tr_imports_world_usd"]) < 1 and abs(sum(ci.values()) - V["tr_imports_from_ca_usd"]) < 1
D["buys"] = [dict(c=c, n=hs2name(c), w=wi[c], ca=ci.get(c, 0)) for c in wi]

# 2. who sells to Türkiye
PNAME = {"Russian Federation": "Russia", "USA": "United States", "United States of America": "United States", "Rep. of Korea": "South Korea",
         "Areas, nes": "Areas not specified", "China, Hong Kong SAR": "Hong Kong", "Türkiye": "Türkiye", "Viet Nam": "Vietnam",
         "United Arab Emirates": "United Arab Emirates", "Iran": "Iran", "Switzerland": "Switzerland", "Kazakhstan": "Kazakhstan"}
# ranks among trading partners: rows UN Comtrade records without a partner ("Special Categories", "Areas, nes") are left out;
# "Other Asia, nes" is a trading partner in UN Comtrade and stays in
NONC = {"Special Categories", "Areas, nes"}
part_all = sorted(rows(A / "market/outputs/tur_imports_2025_by_partner.csv"), key=lambda p: -float(p["usd"]))
unalloc_pct = sum(float(p["usd"]) for p in part_all if p["partner"] in NONC) / V["tr_imports_world_usd"] * 100
part = [p for p in part_all if p["partner"] not in NONC]
for i, p in enumerate(part, 1):
    p["crank"] = i
D["suppliers"] = [dict(r=p["crank"], n=PNAME.get(p["partner"], p["partner"]), v=float(p["usd"]), s=float(p["usd"]) / V["tr_imports_world_usd"] * 100)
                  for p in part if p["crank"] <= 12 or p["partner"] == "Canada"]
ca_rank = next(p["crank"] for p in part if p["partner"] == "Canada")
assert ca_rank == 47, ca_rank

# 3. share of Canada's goods sold to the United States
D["usShare"] = dict(y=V["us_share_years"], v=V["us_share_series"])

# 4. Canada-Türkiye trade, 1988 to 2025, plus January to August
D["trade"] = dict(y=V["series_years"], x=V["series_exports_b"], m=V["series_imports_b"])
yt = json.load(open(A / "trade/out/results_totals.json"))["ytd"]

# 5. what Canada sold and bought, 2025, by everyday group with five years of values
h2 = {r["hs2"]: r for r in rows(A / "trade/out/hs2_chapters_2021_2025.csv")}
YRS = [2021, 2022, 2023, 2024, 2025]


def groups(col, defs, extra_n):
    used = {c for _, cs in defs for c in cs}
    out = [dict(n=n, cs=cs, v=[sum(float(h2[c][f"{col}_{y}"]) for c in cs) for y in YRS]) for n, cs in defs]
    rest = sorted((c for c in h2 if c not in used), key=lambda c: -float(h2[c][f"{col}_2025"]))[:extra_n]
    out += [dict(n=hs2name(c), cs=[c], v=[float(h2[c][f"{col}_{y}"]) for y in YRS]) for c in rest]
    return out


D["sold"] = groups("exports", [("Lentils, chickpeas, vegetables", ["07"]), ("Machinery and engines", ["84"]), ("Aircraft and parts", ["88"]),
                               ("Optical instruments", ["90"]), ("Cars and parts", ["87"])], 5)
D["bought"] = groups("imports", [("Machinery and appliances", ["84"]), ("Steel and steel goods", ["72", "73"]), ("Fruit, nuts and food", ["08", "20"]),
                                 ("Medicines", ["30"]), ("Clothing", ["61", "62"])], 5)
for g, key in ((D["sold"], "receipt_goods_to_tr"), (D["bought"], "receipt_goods_to_ca")):
    for x in g[:5]:
        assert round(x["v"][-1] / 1e6) == V[key][x["n"]], (x["n"], x["v"][-1], V[key][x["n"]])

# 6. duties by chapter, 2025 trade at 2026 rates (Canadian goods without durum wheat, as on the slide)
exp = rows(A / "tariffs/outputs/ca_exports_to_TR_2025_est_tr_duty.csv")
imp = rows(A / "tariffs/outputs/ca_imports_from_TR_2025_est_mfn_duty.csv")


def duty_chapters(rs, code, dutiable):
    agg = {}
    for r in rs:
        c = r[code][:2]
        a = agg.setdefault(c, dict(c=c, n=hs2name(c), v=0.0, d=0.0, p=0.0))
        val = float(r["value_cad"]); a["v"] += val; a["d"] += float(r["est_duty_cad"] or 0)
        if dutiable(r):
            a["p"] += val
    return sorted(agg.values(), key=lambda a: -a["d"])


exp_nd = [r for r in exp if not r["hs8"].startswith("1001")]
D["dutyCA"] = duty_chapters(exp_nd, "hs8", lambda r: float(r["total_pct"] or 0) > 0)
D["dutyTR"] = duty_chapters(imp, "hs10", lambda r: r["mfn_rate"].strip().lower() != "free")
D["dutyTot"] = dict(ca=V["duty_ca_goods"], tr=V["duty_tr_goods"])
assert abs(sum(a["d"] for a in D["dutyCA"]) - V["duty_ca_goods"]["duty"]) < 1
assert abs(sum(a["d"] for a in D["dutyTR"]) - V["duty_tr_goods"]["duty"]) < 1

# 7. provinces: sales 2021 to 2025, top products, people of Turkish origin, map
PCODE = {"British Columbia": "BC", "Alberta": "AB", "Saskatchewan": "SK", "Manitoba": "MB", "Ontario": "ON", "Quebec": "QC",
         "New Brunswick": "NB", "Nova Scotia": "NS", "Prince Edward Island": "PE", "Newfoundland and Labrador": "NL",
         "Yukon": "YT", "Northwest Territories": "NT", "Nunavut": "NU"}
pv = {r["geo"]: r for r in rows(A / "trade/out/provinces_2021_2025.csv")}
cen = {r["geography"]: r for r in rows(A / "people/outputs/census_turkish_by_geo.csv")}
# top products: the slide's named groups for the five largest sellers, plain names for the top lines elsewhere,
# and every passenger-car line summed (the same way as on the slide)
OTHER_NAMES = {"720429": "Steel scrap", "480100": "Newsprint", "901590": "Surveying equipment parts", "843860": "Food-processing machinery",
               "151590": "Vegetable oils", "841191": "Aircraft engine parts", "870390": "Cars", "310100": "Fertilizer", "081190": "Frozen fruit",
               "843143": "Drilling machinery parts", "470321": "Wood pulp", "902620": "Pressure gauges", "300212": "Blood products",
               "071339": "Other pulses", "300490": "Medicines"}
cars = {}
for r in csv.reader(open(A / "tariffs/outputs/domexports_TR_2025_hs6_by_province.csv", encoding="utf-8")):
    if r[0].startswith("2025") and r[2] == "TR" and r[1].startswith("8703") and r[1] != "870310":
        cars[r[3]] = cars.get(r[3], 0) + float(r[5])
ptop = {}
for r in rows(A / "trade/out/province_top_hs6.csv"):
    if r["flow"] == "domestic_exports" and int(r["rank_2025"]) <= 3 and float(r["value_2025"]) > 0:
        ptop.setdefault(r["province"], []).append((r["hs6"], float(r["value_2025"])))
D["prov"] = []
for name, code in PCODE.items():
    r = pv.get(name, {})
    sales = [float(r.get(f"domestic_exports_{y}", 0) or 0) for y in YRS]
    if name in V["province_products"]:
        prods = [dict(n=n, v=x) for n, x in V["province_products"][name]]
    else:
        prods = [dict(n=OTHER_NAMES[h], v=cars.get(code, x) if h == "870390" else x) for h, x in ptop.get(name, []) if h in OTHER_NAMES]
        prods.sort(key=lambda d: -d["v"])
    c = cen.get(name, {})
    D["prov"].append(dict(n=name, c=code, s=sales, imp=float(r.get("imports_clearance_2025", 0) or 0), p=prods,
                          tk=float(c.get("eth_total") or 0), born=float(c.get("pob_total") or 0)))
assert abs(sum(p["s"][-1] for p in D["prov"]) - V["domestic_exports_2025"]) < 2, "provinces do not add to Canada"
for p in D["prov"]:
    if p["n"] in V["province_products"]:
        assert [d["n"] for d in p["p"]] == [n for n, _ in V["province_products"][p["n"]]]
D["cities"] = [dict(n=k.split(" (CMA)")[0].replace(" - ", "–"), v=float(r["eth_total"])) for k, r in cen.items() if "(CMA)" in k and r["eth_total"]]
D["skLentils"] = dict(y=[int(y) for y in V["sk_lentils_m"]], v=list(V["sk_lentils_m"].values()))


def province_paths():
    from pyproj import Transformer
    topo = json.load(open(ROOT / "slides/data/base.json"))
    sx, sy = topo["transform"]["scale"]; tx, ty = topo["transform"]["translate"]
    arcs = []
    for arc in topo["arcs"]:
        x = y = 0; pts = []
        for dx, dy in arc:
            x += dx; y += dy; pts.append((x * sx + tx, y * sy + ty))
        arcs.append(pts)

    def ring(idx):
        out = []
        for i in idx:
            a_ = arcs[i] if i >= 0 else list(reversed(arcs[~i]))
            out.extend(a_ if not out else a_[1:])
        return out
    geoms = topo["objects"]["provs"]["geometries"]
    allpts = [p for g in geoms for poly in ([g["arcs"]] if g["type"] == "Polygon" else g["arcs"]) for r in poly for p in ring(r)]
    minx, maxx = min(p[0] for p in allpts), max(p[0] for p in allpts)
    miny, maxy = min(p[1] for p in allpts), max(p[1] for p in allpts)
    W = 600; sc = W / (maxx - minx); H = (maxy - miny) * sc
    out = {}
    for g in geoms:
        d = ""
        for poly in ([g["arcs"]] if g["type"] == "Polygon" else g["arcs"]):
            for r in poly:
                pts = ring(r)
                if len(pts) < 4:
                    continue
                pts = pts[::3] + [pts[-1]]
                xy = [((x - minx) * sc, (maxy - y) * sc) for x, y in pts]
                if max(a for a, _ in xy) - min(a for a, _ in xy) < 1.2 and max(b for _, b in xy) - min(b for _, b in xy) < 1.2:
                    continue
                d += "M" + "L".join(f"{a:.1f},{b:.1f}" for a, b in xy) + "Z"
        out[g["properties"]["p"]] = d
    return dict(w=W, h=round(H, 1), paths=out)


D["map"] = province_paths()

# 8. travel and people
bd = json.load(open(A / "people/outputs/turkiye_border_canada.json"))
D["trips"] = dict(y=[int(y) for y in bd["annual_arrivals_canadian_nationals"]], v=list(bd["annual_arrivals_canadian_nationals"].values()),
                  rank=[bd["rank_among_nationalities"][y] for y in bd["annual_arrivals_canadian_nationals"]])
assert D["trips"]["v"] == V["ca_arrivals"]
prr = rows(A / "people/outputs/pr_turkey_by_year.csv")
tmp = json.load(open(A / "people/outputs/temp_residents_turkey.json"))
D["people"] = dict(
    pr=dict(y=[int(r["year"]) for r in prr if int(r["year"]) <= 2025], v=[float(r["turkey_pr"]) for r in prr if int(r["year"]) <= 2025],
            rank=[int(r["rank"]) for r in prr if int(r["year"]) <= 2025]),
    study=dict(y=[int(y) for y in tmp["study_dec31"]], v=[d["turkey"] for d in tmp["study_dec31"].values()], rank=[d["rank"] for d in tmp["study_dec31"].values()]),
    work=dict(y=[int(y) for y in tmp["imp_dec31"]], v=[tmp["imp_dec31"][y]["turkey"] + tmp["tfwp_dec31"][y]["turkey"] for y in tmp["imp_dec31"]]),
)
pr_last_full = max(y for y in D["people"]["pr"]["y"] if y <= 2025)
work22, work24 = (D["people"]["work"]["v"][D["people"]["work"]["y"].index(y)] for y in (2022, 2024))
assert (work22, work24) == (9415, 27675), (work22, work24)

# 9. energy
gas_names = {"United States (LNG)": "United States, as LNG", "Algeria (LNG)": "Algeria, as LNG", "Nigeria (LNG)": "Nigeria, as LNG",
             "Others (LNG mostly)": "Others, mostly LNG"}
D["gas"] = [dict(n=gas_names.get(k, k), v=x) for k, x in sorted(V["tr_gas_imports_bcm"].items(), key=lambda kv: -kv[1]) if "Others" not in k]
D["gas"] += [dict(n=gas_names[k], v=x) for k, x in V["tr_gas_imports_bcm"].items() if "Others" in k]
D["gasCA"] = V["ca_lng_2025_bcm"]
D["power"] = dict(ws=V["tr_wind_solar_gw_dec2025"], wsGoal=V["tr_wind_solar_goal_2035_gw"], nucBuild=V["akkuyu_gw"],
                  nuc2035=V["tr_nuclear_goal_2035_gw"], nuc2050=V["tr_nuclear_goal_2050_gw"])
D["energyX"] = dict(y=YRS, v=[float(h2["27"][f"exports_{y}"]) for y in YRS])

# 10. defence
mil = rows(A / "defence/outputs/exports_turkiye_2010_2025.csv")
D["mil"] = [dict(y=int(r["year"]), v=float(r["turkiye_value_cad"]), r=int(r["turkiye_rank_non_us"]), n=int(r["destinations_with_exports"])) for r in mil]
assert [round(d["v"] / 1e6, 6) for d in D["mil"]] == [round(x, 6) for x in V["military_m"]]
MILESTONES = V["defence_milestones"]

# ---------------------------------------------------------------- chapter text (shared numbers from values.json)
fy = V["fta_round_dates"]
ytd_x, ytd_m = V["ytd_exports_change_pct"], abs(V["ytd_imports_change_pct"])
peak_y = V["us_share_peak_year"]
assert V["us_share_2025_is_lowest"], "2025 is no longer the smallest US share since 1999"
three_q = "three-quarters" if 73 <= V["top3_share_pct"] <= 78 else pct(V["top3_share_pct"])
sk_drop = "almost two-thirds" if 60 <= V["sk_lentil_drop_pct"] < 66.7 else pct(V["sk_lentil_drop_pct"])
deficit_shrink = 1 - V["deficit_ytd_2026"] / V["deficit_ytd_2025"]
assert 0.2 <= deficit_shrink < 0.25, deficit_shrink
quarter = "almost a quarter"

CH = []


def chapter(n, k, h, reveal, body, anchor_extra=""):
    CH.append(dict(n=n, k=k, h=h))
    return (f'<section class="panel" id="s{n}"{anchor_extra}><div class="story2"><article class="ch" id="c{n}"><span class="chN">{n}</span>'
            f'<span class="chK">{E(k)}</span>\n        <h2 class="chH">{E(h)}</h2>\n        <p class="reveal">{reveal}</p>\n{body}</article></div></section>')


visit_items = [
    ("Strategic Partnership", "A three-year action plan in four areas: defence, energy, the economy, and social and diplomatic ties. The foreign ministers oversee it, with a strategic dialogue every year." + cite("pmo-joint")),
    ("Air Transport Agreement", f"Signed in Ankara. Each country's airlines may run up to {V['flights_new_per_week']} passenger flights a week, up from {V['flights_old_per_week']}, to any city in the other country. Cargo flights have no limit." + cite("pmo-1023,pmo-readout")),
    ("Energy", "The two energy ministers signed a joint statement on liquefied natural gas (LNG), nuclear power, renewables, clean technology and critical minerals. It has no commitments to buy or sell." + cite("energy-js,pmo-1023")),
    ("Defence", "A memorandum that connects Canadian and Turkish defence companies. It builds on a statement of intent on defence cooperation signed in July 2026." + cite("pmo-1023,pmo-joint")),
    ("Export finance", "Export Development Canada and Türk Eximbank signed a memorandum to help Canadian and Turkish companies team up on projects in other countries." + cite("pmo-1023,pmo-readout")),
    ("Free trade talks", f"The first round runs from {fy}, 2026, in Ankara." + cite("pmo-1023")),
    ("Legal cooperation", "The leaders called for starting a dialogue on mutual legal assistance in criminal cases and extradition." + cite("pmo-joint")),
    ("Next visits", "A Canadian trade mission to Türkiye in 2027, led by the trade minister, and an invitation for President Erdoğan to visit Canada." + cite("pmo-1023,pmo-joint")),
]
visit = ('<section class="panel" id="visit"><span class="tag">The visit, October 22 and 23, 2026</span>'
         '<h2>What came out of the visit</h2>'
         f'<p class="lead3">The first bilateral visit to Türkiye by a Canadian prime minister.{cite("pmo-1006,pmo-1023")} Tap an item for what it does.</p>'
         '<ul class="agree" id="agree">' +
         "".join(f'<li><button type="button" aria-expanded="false"><b>{E(t)}</b><span class="ar" aria-hidden="true">+</span></button><p hidden>{d}</p></li>' for t, d in visit_items) +
         '</ul></section>')

s1 = chapter(1, "The opportunity", "Türkiye is a big market where Canada sells little",
             f"Türkiye imported {ubn(V['tr_imports_world_usd'])} of goods in 2025, and {pct(V['ca_share_of_tr_imports_pct'], 1)} came from Canada.{cite('comtrade')}",
             f'''        <p class="chP">Canada sold {pct(V["us_share_pct"])} of its goods to the United States in 2025, its smallest share since at least 1999. Canada's government wants to double sales to other countries within a decade.{cite("statcan-171,pmo-251029")}</p>
        <div class="sub"><h3>What Türkiye's {nf(V["tr_population"] / 1e6)} million people bought in 2025, and the part from Canada{cite("comtrade-hs,turkstat")}</h3>
          <div class="seg" id="buySeg" role="tablist"><button type="button" role="tab" class="on" data-k="w">Türkiye's top buys</button><button type="button" role="tab" data-k="ca">Canada's top sales</button></div>
          <div class="hbars" id="buyBars"></div><div class="xcard" id="buyCard"></div>
        </div>
        <div class="sub"><h3>Who sells to Türkiye: Canada was its {ordinal(ca_rank)}-largest supplier in 2025{cite("comtrade")}</h3>
          <div class="hbars" id="supBars"></div><div class="xcard" id="supCard"></div>
          <p class="fnote">Ranks among trading partners. Another {pct(unalloc_pct, 1)} of Türkiye's imports was recorded without a partner.{cite("comtrade")}</p>
        </div>
        <div class="sub"><h3>Share of Canada's goods sold to the United States, 1999 to 2025{cite("statcan-171")}</h3>
          <div class="chart" id="usLine"></div><div class="xcard" id="usCard"></div>
        </div>
        <p class="fnote">Türkiye's own import records, in US dollars. Canada's export records, used in the next chapter, are in Canadian dollars and value goods a little differently, so the two do not match exactly.{cite("comtrade,statcan-cimt")}</p>
''')

s2 = chapter(2, "Trade deficit", "Canada buys more from Türkiye than it sells",
             f"The trade deficit was {bn(V['deficit_2025'])} in 2025. It shrank by {quarter} from January to August 2026.{cite('statcan-cimt')}",
             f'''        <p class="chP">Canada sold Türkiye {bn(V["tr_exports_2025"], 2)} of goods in 2025 and bought {bn(V["tr_imports_2025"], 2)}. The last year Canada sold more than it bought was {V["last_surplus_year"]}. From January to August 2026, Canada sold {pct(ytd_x)} more to Türkiye and bought {pct(ytd_m)} less than a year earlier.{cite("statcan-cimt")}</p>
        <div class="sub"><h3>Canada's goods trade with Türkiye, 1988 to 2025, billions of dollars{cite("statcan-cimt")}</h3>
          <div class="lg"><span><i class="k-ca"></i>Canada sold</span><span><i class="k-tr"></i>Canada bought</span></div>
          <div class="chart" id="tradeLine"></div><div class="xcard" id="tradeCard"></div>
        </div>
        <div class="sub"><h3>What Canada sold and bought in 2025{cite("statcan-cimt")}</h3>
          <div class="seg" id="goodsSeg" role="tablist"><button type="button" role="tab" class="on" data-k="sold">Sold to Türkiye</button><button type="button" role="tab" data-k="bought">Bought from Türkiye</button></div>
          <div class="hbars" id="goodsBars"></div><div class="xcard" id="goodsCard"></div>
        </div>
        <p class="fnote">Statistics Canada customs records: all exports to Türkiye (made in Canada or re-exported) and imports from Türkiye. Figures for 2026 can still be revised.{cite("statcan-cimt")}</p>
''')

dc, dt = V["duty_ca_goods"], V["duty_tr_goods"]
s3 = chapter(3, "Duties", "A trade deal could help farmers and shoppers",
             f"Türkiye charges {pct(V['lentil_duty_pct'], 1)} on Canadian lentils, and Canada about {pct(V['clothing_duty_rate'])} on Turkish clothing.{cite('tr-tariff,cbsa')}",
             f'''        <p class="chP">On the Canadian-made goods sold to Türkiye in 2025, durum wheat aside, duties come to an estimated {mn(dc["duty"])}, {pct(dc["rate"], 1)} on average. On Turkish goods sold to Canada, they come to about {mn(dt["duty"])}, {pct(dt["rate"], 1)}. Lower duties could also bring Canadian clothing makers more competition.{cite("tr-tariff,tr-schedule,cbsa,statcan-cimt-files")}</p>
        <div class="sub"><h3>Estimated duty by product, 2025 trade at 2026 rates</h3>
          <div class="seg" id="dutySeg" role="tablist"><button type="button" role="tab" class="on" data-k="ca">Canadian goods</button><button type="button" role="tab" data-k="tr">Turkish goods</button></div>
          <div id="dutySum"></div>
          <div class="hbars" id="dutyBars"></div><div class="xcard" id="dutyCard"></div>
        </div>
        <p class="fnote">Each product line's 2025 value times its 2026 duty rate. Canadian goods leave out durum wheat, which can enter Türkiye duty-free when used to make exports.{cite("wto-tpr")} Türkiye's 10% rate on green lentils ended on April 30, 2026; since May 1, green lentils pay 19.3%, like red lentils.{cite("tr-tariff")} Canada's figure uses its regular rates; anti-dumping duties and surtaxes on some steel come on top.{cite("cbsa")}</p>
''')

s4 = chapter(4, "Who sells", "Three provinces have the most at stake",
             f"Quebec, Ontario and Saskatchewan make {three_q} of Canada's sales to Türkiye.{cite('statcan-cimt')}",
             f'''        <p class="chP">Saskatchewan's lentil sales to Türkiye fell by {sk_drop} from 2022 to 2025.{cite("statcan-cimt")}</p>
        <div class="sub" id="province"><h3>Find your province: what it sells to Türkiye</h3>
          <div class="chips" id="provChips"></div>
          <div class="mapgrid"><div class="provmap" id="provMap"></div><div class="xcard" id="provCard"></div></div>
          <div class="lg"><span><i class="k-ramp"></i>Sales to Türkiye in 2025: the stronger the blue, the more</span></div>
        </div>
        <p class="fnote">Goods made in each province, by province of origin, 2025. Turkish origin: people who reported Turkish ethnic or cultural origin, alone or with others, in the 2021 Census.{cite("statcan-cimt,census")}</p>
''')

s5 = chapter(5, "Travel", "Canadians get more choice of flights",
             f"Istanbul is a global hub: Turkish Airlines flew to {V['tk_countries']} countries in 2024, more than any other airline.{cite('guinness')}",
             f'''        <p class="chP">The new agreement allows up to {V["flights_new_per_week"]} flights a week for each country, up from {V["flights_old_per_week"]}, to any city. Istanbul Airport handled {nf(V["ist_passengers_2025"] / 1e6, 1)} million passengers in 2025, eighth in the world.{cite("pmo-1023,aci")}</p>
        <div class="flights" id="flights"></div>
        <div class="sub"><h3>Trips to Türkiye by Canadians each year, 2010 to 2025{cite("ktb")}</h3>
          <div class="chart" id="tripLine"></div><div class="xcard" id="tripCard"></div>
          <p class="fnote" style="margin-top:6px">Arrivals of Canadian citizens at Türkiye's borders.</p>
        </div>
        <div class="sub"><h3>People from Türkiye in Canada{cite("ircc-pr,ircc-study,ircc-work,census")}</h3>
          <div class="seg" id="pplSeg" role="tablist"><button type="button" role="tab" class="on" data-k="pr">Permanent residents</button><button type="button" role="tab" data-k="study">Students</button><button type="button" role="tab" data-k="work">Work permits</button></div>
          <div class="chart" id="pplCols"></div><div class="xcard" id="pplCard"></div>
          <p class="chP" style="margin-top:12px">{nf(V["turkish_origin_canada"])} people in Canada reported Turkish origin in the 2021 Census. Where they lived, by metropolitan area:</p>
          <div class="hbars" id="cityBars"></div>
        </div>
        <p class="fnote">In 2025, Air Canada and Air Transat opposed extra Turkish Airlines flights; WestJet and the Toronto and Montréal airports supported them. The Canadian Transportation Agency turned down both requests.{cite("cta-25,cta-77")} Air Transat starts flying from Montréal to Istanbul on {V["air_transat_montreal_istanbul_start"]}, 2026.{cite("transat")} Work permit holders rose from {nf(work22)} at the end of 2022 to {nf(work24)} at the end of 2024. The count includes permits held by asylum claimants, and Canada eased rules after the February 2023 earthquakes for people from Türkiye and Syria already in Canada.{cite("ircc-work,ircc-quake")} Permanent residents are shown to 2025; IRCC's 2026 figures run to August.{cite("ircc-pr")}</p>
''')

pw = D["power"]
s6 = chapter(6, "Energy", "Türkiye's nuclear plans open a door for Canada",
             f"Türkiye aims for over {V['tr_nuclear_goal_2050_gw']} gigawatts of nuclear power by 2050 and is studying Canada's CANDU reactors.{cite('menr-2023,menr-candu')}",
             f'''        <p class="chP">Türkiye's first nuclear plant, Akkuyu ({nf(pw["nucBuild"], 1)} gigawatts), is being built by Russia's Rosatom. Türkiye also plans {pw["wsGoal"]} gigawatts of wind and solar power by 2035 and net zero emissions by {V["tr_net_zero_year"]}. In 2024, Canada produced about a quarter of the world's uranium.{cite("invest-tr,pris,menr-2024,nrcan-u")}</p>
        <div class="sub"><h3>Türkiye's power goals, gigawatts{cite("epias,menr-2024,menr-2023,pris")}</h3>
          <div class="hbars" id="powBars"></div><div class="xcard" id="powCard"></div>
        </div>
        <div class="sub"><h3>Where Türkiye's natural gas came from in 2025, billion cubic metres{cite("epdk,cer-lng")}</h3>
          <div class="hbars" id="gasBars"></div><div class="xcard" id="gasCard"></div>
        </div>
        <div class="sub"><h3>Canada's energy sales to Türkiye (oil, gas and coal), millions of dollars{cite("statcan-cimt")}</h3>
          <div class="chart" id="enCols"></div><div class="xcard" id="enCard"></div>
        </div>
        <p class="fnote">The energy statement the two countries signed in October 2026 has no commitments to buy or sell. Türkiye's state nuclear company and AtkinsRéalis signed a memorandum in March 2026 to study CANDU technology for Türkiye.{cite("energy-js,menr-candu,atkins")}</p>
''')

s7 = chapter(7, "Defence", "Military sales to Türkiye are back, with conditions",
             f"Canada's government says linking the two defence industries will create jobs and exports.{cite('pmo-1023')}",
             f'''        <p class="chP">Türkiye has NATO's second-largest military. Canada's military exports to Türkiye are mostly imaging and targeting equipment.{cite("pmo-1023,nato-exp,gac-mil")}</p>
        <div class="sub"><h3>Canadian military exports to Türkiye each year, millions of dollars{cite("gac-mil")}</h3>
          <div class="chart" id="milCols"></div>
          <div class="lg"><span><i class="k-open"></i>Permits open, then reopened case by case from January 2024</span><span><i class="k-sus"></i>New permits suspended</span></div>
          <div class="xcard" id="milCard"></div>
          <ol class="miles" id="miles"></ol>
        </div>
        <p class="fnote">The reports leave out most exports to the United States, which need no permit, so ranks are among other destinations.{cite("gac-mil")} The Armenian National Committee of Canada asks that Canada keep full control of export permits in a trade deal.{cite("ancc")} Canada can cancel permits if goods are misused.{cite("gac-1108,gac-2021")}</p>
''')

s8 = chapter(8, "What comes next", f"Free trade talks start in Ankara on {V['fta_round_month']}",
             "A deal could lower duties in both countries. Once its terms are public, we will break them down in a new post.",
             f'''        <ol class="tl" id="timeline">
          <li><span class="w">{V["air_transat_montreal_istanbul_start"]}</span><span class="i">Air Transat starts flights from Montréal to Istanbul</span>{cite("transat")}</li>
          <li><span class="w">{V["cop31_dates"]}</span><span class="i">Türkiye hosts COP31, the UN climate conference, in Antalya</span>{cite("pmo-joint")}</li>
          <li><span class="w">{fy}</span><span class="i">First round of free trade talks, in Ankara</span>{cite("pmo-1023")}</li>
          <li><span class="w">2027</span><span class="i">Canadian trade mission to Türkiye, led by the trade minister</span>{cite("pmo-1023")}</li>
          <li><span class="w">Date to be set</span><span class="i">President Erdoğan visits Canada</span>{cite("pmo-joint")}</li>
        </ol>
''')

how = f'''<section class="panel"><details class="how" id="how"><summary>How this was done</summary>
  <h3>In plain words</h3>
  <p>Every number on this page comes from an official or primary source. The numbers built from data tables are computed by the scripts in the <a href="{REPO}">GitHub repository</a>, which also holds the full method (METHODOLOGY.md) with a table of the numbers in the slides and the chapter text. News stories were used only to find official documents.</p>
  <ul>
    <li><b>Trade:</b> Statistics Canada's customs records by country, province and product, and Türkiye's own import records from UN Comtrade.</li>
    <li><b>Duties:</b> the 2026 Canadian Customs Tariff and Türkiye's 2026 import regime, applied line by line to 2025 trade.</li>
    <li><b>Travel and people:</b> Türkiye's border statistics, Canadian Transportation Agency rulings, open data from Immigration, Refugees and Citizenship Canada (IRCC) and the 2021 Census.</li>
    <li><b>Energy:</b> Türkiye's energy ministry, EPİAŞ (Türkiye's energy exchange), the International Atomic Energy Agency (IAEA), Türkiye's energy regulator, the Canada Energy Regulator and Natural Resources Canada.</li>
    <li><b>Defence:</b> Global Affairs Canada's Reports on Exports of Military Goods for 2010 to 2025 and its notices to exporters.</li>
  </ul>
  <h3>Caveats</h3>
  <ul>
    <li><b>Two sets of trade records.</b> Türkiye records what it imports from Canada in US dollars when goods arrive; Canada records what it exports in Canadian dollars when goods leave. The totals differ for timing, valuation and currency.</li>
    <li><b>Duties are estimates.</b> Türkiye charges duty on the value including freight and insurance, which Canadian export values leave out, so the Canadian-goods figure is a low estimate. Duties charged per tonne are left out.</li>
    <li><b>Military exports.</b> The reports count permits used, and leave out most exports to the United States.</li>
    <li><b>2026 is preliminary.</b> Monthly trade for 2026 can still be revised.</li>
  </ul>
</details>
<div class="refsec" id="references"><h3>References</h3><p class="lead3">Small numbers in the text link here.</p><ol class="refs" id="refList">@@REFS@@</ol></div>
</section>'''

body = "\n".join([visit, s1, s2, s3, s4, s5, s6, s7, s8, how])
refs_html = "".join(f'<li id="ref-{i + 1}">{E(REFS[k][0])} ' + " ".join(f'<a href="{E(u)}" target="_blank" rel="noopener">{E(u)}</a>' for u in links(k)) + '</li>' for i, k in enumerate(ORDER))
unused = [k for k in REFS if k not in ORDER]
assert not unused, f"references never cited: {unused}"
body = body.replace("@@REFS@@", refs_html)

D["miles"] = MILESTONES
D["fmt"] = dict(caRank=ca_rank, prLastFull=pr_last_full)

# ---------------------------------------------------------------- page
css = (ROOT / "site/site.css").read_text(encoding="utf-8")
js = (ROOT / "site/site.js").read_text(encoding="utf-8")
title = "Talking trade with Türkiye"
desc = ("A Canadian prime minister's first bilateral visit brought agreements on flights, energy and defence. "
        "Explore what they mean for Canadians: trade, duties, provinces, travel, energy and defence.")
page = f'''<!doctype html>
<html lang="en-CA"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)} · The Median Canadian</title>
<meta name="description" content="{E(desc)}">
<meta name="color-scheme" content="light dark">
<link rel="icon" type="image/png" href="logo-icon.png"><link rel="apple-touch-icon" href="logo-icon.png">
<meta property="og:type" content="article"><meta property="og:site_name" content="The Median Canadian">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{SITE}"><meta property="og:image" content="{SITE}slides/out/the-median-canadian-canada-turkiye-1-of-9.jpg">
<style>
{css}
</style>
</head><body>
<main>
  <header class="top">
    <div>
      <div class="brandrow"><a href="{HUB}" aria-label="The Median Canadian, all posts"><picture><source srcset="logo-dark.png" media="(prefers-color-scheme: dark)"><img src="logo.png" alt="The Median Canadian" width="1536" height="491"></picture></a></div>
      <span class="tag">The Median Canadian · Week 2</span>
      <h1>{E(title)}</h1>
      <p class="dek">A Canadian prime minister's first bilateral visit brought agreements on flights, energy and defence. Here is what they mean for Canadians.</p>
    </div>
    <div class="stamp">Trade data to <b>August 2026</b><br>Official statements to <b>October 23, 2026</b></div>
  </header>
  <a class="scrollcue" href="#visit">Scroll to learn more <span aria-hidden="true">↓</span></a>
{body}
  <div class="foot">Sources: Statistics Canada, UN Comtrade, the Canada Border Services Agency, Türkiye's trade, energy and tourism ministries, Global Affairs Canada, IRCC, the Prime Minister's Office and others, listed in the <a href="#references">References</a>. Every number comes from an official or primary source; methods and code are on <a href="{REPO}">GitHub</a>.
    <div class="sig2"><img src="logo-icon.png" alt="" width="627" height="618"><span><b>The Median Canadian</b> · A curious Canadian explaining Canada through numbers, every week. <a href="{HUB}">All posts</a></span></div>
    <div style="margin-top:6px">Text and charts: <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">CC BY 4.0</a>, share and adapt with credit. Code: <a href="{REPO}/blob/main/LICENSE" target="_blank" rel="noopener">Apache 2.0</a>. Data belongs to its publishers, each under its own licence.</div>
  </div>
</main>
<script id="data" type="application/json">{json.dumps(D, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")}</script>
<script>
{js}
</script>
</body></html>
'''
# wording rules from the style guide, checked on every word of the page
assert chr(0x2014) not in page, "em dash in page"
plain = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", "", page, flags=re.S)))
for pat in (r"\bnow\b", r"\btoday\b", r"\bcurrently\b", r"\bour (analysis|estimate|count)\b", r"\bwon\b", r"\blost\b", r", not "):
    hits = re.findall(r".{0,40}" + pat + r".{0,40}", plain, re.I)
    assert not hits, (pat, hits)
(ROOT / "index.html").write_text(page, encoding="utf-8")
(ROOT / "data").mkdir(exist_ok=True)
json.dump(D, open(ROOT / "data/site.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump([dict(n=i + 1, key=k, text=REFS[k][0], url=links(k)) for i, k in enumerate(ORDER)],
          open(ROOT / "data/references.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(CH, open(ROOT / "data/chapters.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"wrote index.html {len(page) / 1024:.0f} KB, {len(ORDER)} references, {len(CH)} chapters")
