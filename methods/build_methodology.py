#!/usr/bin/env python3
"""Write METHODOLOGY.md, with the table of every published number filled from slides/values.json and data/site.json,
so the table always matches what the slides and the page show. Run from anywhere: python3 methods/build_methodology.py"""
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
V = json.load(open(ROOT / "slides/values.json", encoding="utf-8"))
S = json.load(open(ROOT / "data/site.json", encoding="utf-8"))


def nf(v, d=0):
    q = Decimal(repr(float(v))).quantize(Decimal(1).scaleb(-d), rounding=ROUND_HALF_UP)
    return f"{q:,.{d}f}"


B = lambda x, d=1: f"${nf(x / 1e9, d)} billion"
M = lambda x, d=0: f"${nf(x / 1e6, d)} million"
UB = lambda x, d=1: f"US${nf(x / 1e9, d)} billion"
UM = lambda x, d=0: f"US${nf(x / 1e6, d)} million"
P = lambda x, d=0: f"{nf(x, d)}%"

TB = {d["name"]: d for d in V["tr_buys"]}
mil = dict(zip(V["military_years"], V["military_m"]))
arr = dict(zip(V["ca_arrivals_years"], V["ca_arrivals"]))
ca_sup = next(s for s in S["suppliers"] if s["n"] == "Canada")
dc, dt = V["duty_ca_goods"], V["duty_tr_goods"]
shrink = (1 - V["deficit_ytd_2026"] / V["deficit_ytd_2025"]) * 100

T = "analysis/trade/out/"
R = [
    # id, number as published, where, source file, how it is computed
    ("Türkiye's goods imports, 2025", UB(V["tr_imports_world_usd"], 0), "Slide 2, site 1", "analysis/market/outputs/tur_imports_2025_hs2_world.csv",
     "Sum of Türkiye's imports from all partners over the 96 HS chapters (UN Comtrade, reported by Türkiye)."),
    ("Canada's share of Türkiye's imports", P(V["ca_share_of_tr_imports_pct"], 1), "Slide 2, site 1", "analysis/market/outputs/tur_imports_2025_hs2_canada.csv",
     f"Imports from Canada ({UB(V['tr_imports_from_ca_usd'], 2)}) divided by imports from all partners."),
    ("Türkiye's population, end of 2025", f"{nf(V['tr_population'] / 1e6)} million", "Slide 2, site 1", "analysis/market/results-followup.md",
     "TurkStat Address Based Population Registration System, 2025."),
    *[(f"Türkiye's imports of {n.lower()}, and from Canada", f"{UB(d['world'])}; {UM(d['canada'])}", "Slide 2 bars, site 1", "analysis/market/outputs/",
       "Sum of the HS chapters in the group (Energy 27, Machinery 84, Gold and jewellery 71, Aircraft 88, Lentils and other vegetables 07).")
      for n, d in TB.items()],
    ("Share of Canada's goods sold to the US, 2025", P(V["us_share_pct"]), "Slide 2, site 1", "analysis/trade/out/x171_all_sections_extract.csv",
     "Exports to the United States divided by exports to all countries, all product sections, StatCan table 12-10-0171. 2025 is the smallest share since at least 1999, when the table starts."),
    ("Canada's rank among Türkiye's suppliers", "47th", "Site 1", "analysis/market/outputs/tur_imports_2025_by_partner.csv",
     "Rank by value among trading partners; rows recorded without a partner (\"Special Categories\", \"Areas, nes\") are left out, and \"Other Asia, nes\" counts as a partner (it would be 46th without it)."),
    ("Trade deficit with Türkiye, 2025", B(V["deficit_2025"]), "Slide 3, site 2", T + "annual_totals_1988_2026ytd.csv",
     f"Imports ({B(V['tr_imports_2025'], 2)}) minus total exports, domestic plus re-exports ({B(V['tr_exports_2025'], 2)})."),
    ("Deficit change, January to August 2026", f"shrank by almost a quarter ({nf(shrink, 1)}%)", "Slide 3, site 2", "analysis/trade/out/results_totals.json",
     f"January to August deficit: {B(V['deficit_ytd_2025'], 2)} in 2025, {B(V['deficit_ytd_2026'], 2)} in 2026."),
    ("Exports and imports, January to August 2026", f"+{nf(V['ytd_exports_change_pct'])}%; {nf(V['ytd_imports_change_pct'])}%", "Slide 3, site 2", "analysis/trade/out/results_totals.json",
     "Change against January to August 2025."),
    ("Goods sold to Türkiye by group, 2025", "; ".join(f"{k} ${v}M" for k, v in V["receipt_goods_to_tr"].items()), "Slide 3, site 2", T + "hs2_chapters_2021_2025.csv",
     "Total exports by HS chapter (07, 84, 88, 90, 87), rounded to $ million; everything else is the total minus the groups."),
    ("Goods bought from Türkiye by group, 2025", "; ".join(f"{k} ${v:,}M" for k, v in V["receipt_goods_to_ca"].items()), "Slide 3, site 2", T + "hs2_chapters_2021_2025.csv",
     "Imports by HS chapter (84; 72 and 73; 08 and 20; 30; 61 and 62), rounded to $ million."),
    ("Last year Canada sold Türkiye more than it bought", str(V["last_surplus_year"]), "Site 2", T + "annual_totals_1988_2026ytd.csv", "Latest year with exports above imports."),
    ("Türkiye's duty on Canadian lentils", P(V["lentil_duty_pct"], 1), "Slide 4, site 3", "analysis/tariffs/outputs/ca_exports_to_TR_2025_est_tr_duty.csv",
     "Highest 2026 rate (customs duty plus additional customs duty) on the lentil lines Canada sold in 2025, Türkiye's 2026 import regime."),
    ("Canada's duty on Turkish clothing", f"about {P(V['clothing_duty_rate'])}", "Slide 4, site 3", "analysis/tariffs/outputs/ca_imports_from_TR_2025_est_mfn_duty.csv",
     "Estimated duty on HS chapters 61 and 62 divided by their 2025 value, regular (most-favoured-nation) rates of the 2026 Customs Tariff."),
    ("Canadian-made goods sold to Türkiye (duty base)", B(dc["base"]), "Slide 4, site 3", "analysis/tariffs/outputs/ca_exports_to_TR_2025_est_tr_duty.csv",
     "2025 domestic exports by HS8 line, without durum wheat (HS 1001)."),
    ("Share duty-free / paying duty, Canadian goods", f"{P(dc['free_pct'])} / {P(100 - dc['free_pct'])}", "Slide 4, site 3", "same", "Value of lines with a 0% total rate over the base."),
    ("Estimated duty on Canadian goods", f"{M(dc['duty'])}, {P(dc['rate'], 1)}", "Slide 4, site 3", "same", "Sum over lines of 2025 value times the 2026 rate; divided by the base."),
    ("Turkish goods sold to Canada (duty base)", B(dt["base"]), "Slide 4, site 3", "analysis/tariffs/outputs/ca_imports_from_TR_2025_est_mfn_duty.csv", "2025 imports from Türkiye by HS10 line."),
    ("Share duty-free / paying duty, Turkish goods", f"{P(dt['free_pct'])} / {P(100 - dt['free_pct'])}", "Slide 4, site 3", "same", "Value of lines with a Free rate over the base."),
    ("Estimated duty on Turkish goods", f"{M(dt['duty'])}, {P(dt['rate'], 1)}", "Slide 4, site 3", "same", "Sum over lines of 2025 value times the 2026 regular rate; divided by the base."),
    ("Three largest selling provinces' share", f"three-quarters ({P(V['top3_share_pct'], 1)})", "Slide 5, site 4", T + "provinces_2021_2025.csv",
     "Quebec, Ontario and Saskatchewan's 2025 domestic exports to Türkiye over Canada's."),
    *[(f"{n}: sales to Türkiye and top products, 2025", f"{M(next(d['value'] for d in V['provinces'] if d['name'] == n))}; " + "; ".join(f"{p} {M(v)}" for p, v in V["province_products"][n]),
       "Slide 5, site 4", T + "provinces_2021_2025.csv; " + T + "province_top_hs6.csv",
       "Domestic exports by province of origin. Product groups combine their HS6 lines (aircraft 8802.30 and 8802.40; cars every line 8703.21 to 8703.90).")
      for n in ("Quebec", "Ontario", "Saskatchewan", "British Columbia", "Alberta")],
    ("Saskatchewan's lentil sales, 2022 to 2025", f"fell by almost two-thirds ({P(V['sk_lentil_drop_pct'], 1)})", "Slide 5, site 4", "analysis/trade/results.md",
     f"${nf(V['sk_lentils_m']['2022'], 1)}M in 2022 to ${nf(V['sk_lentils_m']['2025'], 1)}M in 2025."),
    ("Countries Turkish Airlines flew to", str(V["tk_countries"]), "Slide 6, site 5", "slides/facts.json", "Guinness World Records, September 2023 to September 2024."),
    ("Weekly flights for each country", f"{V['flights_old_per_week']} before, up to {V['flights_new_per_week']}", "Slide 6, site 5", "slides/facts.json", "PMO news release, October 23, 2026."),
    ("Trips to Türkiye by Canadians", f"{nf(arr[2019])} in 2019; {nf(arr[2025])} in 2025", "Slide 6, site 5", "analysis/people/outputs/turkiye_border_canada.json",
     "Arriving visitors with Canadian nationality, Türkiye's border statistics."),
    ("Istanbul Airport passengers, 2025", f"{nf(V['ist_passengers_2025'] / 1e6, 1)} million", "Site 5", "slides/facts.json", "ACI World 2025 rankings (8th)."),
    ("People of Turkish origin in Canada, 2021", nf(V["turkish_origin_canada"]), "Site 5", "analysis/people/outputs/census_turkish_by_geo.csv", "2021 Census, Turkish ethnic or cultural origin, single and multiple responses."),
    ("Türkiye's nuclear goals", f"{V['tr_nuclear_goal_2035_gw']} GW by 2035; over {V['tr_nuclear_goal_2050_gw']} GW by 2050", "Slide 7, site 6", "slides/facts.json", "Türkiye Ministry of Energy, September 25, 2023."),
    ("Akkuyu plant under construction", f"{V['akkuyu_gw']} GW", "Slide 7, site 6", "slides/facts.json", "Invest in Türkiye; IAEA PRIS (four units under construction)."),
    ("Wind and solar capacity, December 2025", f"{nf(V['tr_wind_solar_gw_dec2025'])} GW", "Slide 7, site 6", "analysis/energy/raw/round3/epias.txt", "EPİAŞ daily bulletin, December 14, 2025: wind plus solar installed capacity."),
    ("Wind and solar goal for 2035", f"{V['tr_wind_solar_goal_2035_gw']} GW", "Slide 7, site 6", "slides/facts.json", "Türkiye Ministry of Energy, November 4, 2024."),
    ("Canada's share of world uranium, 2024", f"about a quarter ({P(V['ca_uranium_world_share_pct'])})", "Slide 7, site 6", "analysis/energy/results.md", "Natural Resources Canada, uranium and nuclear power facts."),
    ("Türkiye's gas imports, 2025", f"{nf(V['tr_gas_total_bcm'], 1)} billion m³", "Site 6", "analysis/energy/results.md", "EPDK 2025 Natural Gas Market Development Report, imports by country."),
    ("Canada's LNG exports, 2025", f"{nf(V['ca_lng_2025_bcm'], 1)} billion m³ (about {P(V['ca_lng_vs_tr_gas_pct'])} of Türkiye's gas imports)", "Site 6", "analysis/energy/outputs/cer_lng_summary.txt",
     "Canada Energy Regulator LNG shipment detail, gas equivalent."),
    ("Military exports to Türkiye", f"{M(mil[2019] * 1e6)} in 2019; {M(mil[2024] * 1e6)} in 2024", "Slide 8, site 7", "analysis/defence/outputs/exports_turkiye_2010_2025.csv",
     "Global Affairs Canada, Reports on Exports of Military Goods, value of exports to Türkiye by year."),
    ("Permits cancelled in April 2021", str(V["permits_cancelled_2021"]), "Slide 8, site 7", "slides/facts.json", "Global Affairs Canada statement, April 12, 2021."),
    ("Brokering permit for Ukraine, 2025", M(V["brokering_ukraine_2025"]), "Slide 8, site 7", "analysis/defence/results.md", "2025 Report on Exports of Military Goods, table 16."),
    ("First round of free trade talks", V["fta_round_dates"] + ", 2026", "Slide 9, site 8", "slides/facts.json", "PMO news release, October 23, 2026."),
]

rows = "\n".join(f"| N{i} | {r[0]} | {r[1]} | {r[2]} | `{r[3]}` | {r[4]} |" for i, r in enumerate(R, 1))
text = f"""# Methodology

How every number in the week 2 post (the Instagram slides and the page at https://sjvadrevu.github.io/canada-turkey-oct26/) was produced, so anyone can check or challenge it.

## The question

The Canada-Türkiye Strategic Partnership was launched on October 22, 2026, during the first bilateral visit to Türkiye by a Canadian prime minister. The post asks what the agreements mean for Canadians: what each country sells the other, what duties a trade deal could cut, which provinces have the most at stake, what changes for travel, what Türkiye's energy plans could mean for Canadian companies, and why military sales were stopped and restarted. It sets out benefits both ways and the pitfalls for Canada.

## Data and method, by chapter

1. **The opportunity.** Türkiye's 2025 imports by partner and HS chapter, as reported by Türkiye to UN Comtrade (US dollars). Canada's share is Canada's row over the world total. Ranks are among countries. Canada's own export records (Statistics Canada, table 12-10-0171) give the share of Canada's goods sold to the United States from 1999 to 2025.
2. **Trade deficit.** Statistics Canada's Canadian International Merchandise Trade (CIMT) monthly cubes by country and HS chapter (tables 12-10-0147 and 12-10-0150), summed to years from 1988 and checked against table 12-10-0171. Exports are total exports (domestic exports plus re-exports); imports are by country of origin. The January to August comparison uses the same months of 2025 and 2026.
3. **Duties.** Every 2025 trade line (Canadian domestic exports to Türkiye at HS8, imports from Türkiye at HS10, from the CIMT data files) is matched to its 2026 duty: Türkiye's customs duty plus additional customs duty from its 2026 import regime, and Canada's regular rate from the 2026 Customs Tariff. Estimated duty is value times rate, summed. Durum wheat is left out of the Canadian side because Türkiye lets it in duty-free when it is used to make exports (inward processing), so a duty on it would overstate what is paid. Duties charged per tonne and anti-dumping duties are left out.
4. **Who sells.** CIMT domestic exports by province of origin, 2021 to 2025, and the top HS6 lines for each province in 2025. Product groups combine their HS6 lines (aircraft 8802.30 and 8802.40; passenger cars 8703.21 to 8703.90). People of Turkish origin and people born in Türkiye are from the 2021 Census.
5. **Travel.** Weekly flight limits from the PMO's description of the expanded Air Transport Agreement; Canadian Transportation Agency rulings for the 2025 requests for extra flights; Türkiye's border statistics for arrivals of Canadian nationals, 2010 to 2025; IRCC open data for permanent residents, study permit holders and work permit holders who are citizens of Türkiye.
6. **Energy.** Türkiye's energy ministry for its nuclear and wind and solar goals; EPİAŞ for installed wind and solar capacity in December 2025; the IAEA for reactors under construction; Türkiye's energy regulator (EPDK) for 2025 gas imports by country; the Canada Energy Regulator for Canada's 2025 LNG exports; Natural Resources Canada for Canada's 2024 uranium production and its share of the world; CIMT for Canada's energy sales to Türkiye (HS chapter 27).
7. **Defence.** Global Affairs Canada's Reports on Exports of Military Goods, 2010 to 2025, for the value of exports to Türkiye, its rank among destinations other than the United States and the 2025 brokering permit; Global Affairs Canada statements and notices for the 2019 suspension, the 2021 cancellations and the 2024 reopening.
8. **What comes next.** Dates from the PMO's news release and joint statement of October 22 and 23, 2026, and Air Transat's news release.

News reports were used only to find official documents; no number comes from a news story.

## Every published number

Values are filled by `methods/build_methodology.py` from `slides/values.json` (written by `slides/values.py`) and `data/site.json` (written by `site/build_site.py`), the same files the slides and the page read.

| ID | Number | As published | Where | Source file | How it is computed |
|---|---|---|---|---|---|
{rows}

The page adds explorable detail from the same files: every HS chapter of Türkiye's imports, every supplier's rank, every year of trade, duty by HS chapter, every province, every year of trips, residents, students, workers, energy sales and military exports. Each chart names its source in a numbered reference.

## Caveats

- **Two sets of trade records.** Türkiye records imports from Canada in US dollars, including freight and insurance, when goods arrive; Canada records exports in Canadian dollars when they leave. The two totals differ. Each chapter says which one it uses.
- **Duty estimates.** Türkiye charges duty on the value including freight and insurance, which Canadian export values leave out, so the Canadian-goods estimate is low. Tariff rates in Türkiye change by decree; the rates are those in force on the file dates. Green lentils paid 10% until April 30, 2026, and 19.3% from May 1.
- **Imports by province** are by province of customs clearance, which is not always where goods are used.
- **Military exports.** The reports count exports under permits; most exports to the United States need no permit and are left out, so ranks are among other destinations.
- **2026 data.** Monthly trade for 2026 can still be revised. IRCC's 2026 figures run to August and are not shown on the yearly charts.
- **Rounding.** IRCC rounds counts to the nearest 5; values from 0 to 5 are hidden.

## How to challenge a number

Find its ID in the table, open the source file named there, and rerun the step in REPRODUCE.md. The independent checks of every claim are in `methods/verification.md`.

The Median Canadian. A curious Canadian explaining Canada through numbers, every week.
"""
assert chr(0x2014) not in text
(ROOT / "METHODOLOGY.md").write_text(text, encoding="utf-8")
print("wrote METHODOLOGY.md with", len(R), "numbers")
