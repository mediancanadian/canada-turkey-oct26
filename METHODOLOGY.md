# Methodology

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
| N1 | Türkiye's goods imports, 2025 | US$365 billion | Slide 2, site 1 | `analysis/market/outputs/tur_imports_2025_hs2_world.csv` | Sum of Türkiye's imports from all partners over the 96 HS chapters (UN Comtrade, reported by Türkiye). |
| N2 | Canada's share of Türkiye's imports | 0.3% | Slide 2, site 1 | `analysis/market/outputs/tur_imports_2025_hs2_canada.csv` | Imports from Canada (US$1.16 billion) divided by imports from all partners. |
| N3 | Türkiye's population, end of 2025 | 86 million | Slide 2, site 1 | `analysis/market/results-followup.md` | TurkStat Address Based Population Registration System, 2025. |
| N4 | Türkiye's imports of energy, and from Canada | US$62.5 billion; US$38 million | Slide 2 bars, site 1 | `analysis/market/outputs/` | Sum of the HS chapters in the group (Energy 27, Machinery 84, Gold and jewellery 71, Aircraft 88, Lentils and other vegetables 07). |
| N5 | Türkiye's imports of machinery, and from Canada | US$41.6 billion; US$125 million | Slide 2 bars, site 1 | `analysis/market/outputs/` | Sum of the HS chapters in the group (Energy 27, Machinery 84, Gold and jewellery 71, Aircraft 88, Lentils and other vegetables 07). |
| N6 | Türkiye's imports of gold and jewellery, and from Canada | US$28.1 billion; US$97 million | Slide 2 bars, site 1 | `analysis/market/outputs/` | Sum of the HS chapters in the group (Energy 27, Machinery 84, Gold and jewellery 71, Aircraft 88, Lentils and other vegetables 07). |
| N7 | Türkiye's imports of aircraft, and from Canada | US$5.4 billion; US$175 million | Slide 2 bars, site 1 | `analysis/market/outputs/` | Sum of the HS chapters in the group (Energy 27, Machinery 84, Gold and jewellery 71, Aircraft 88, Lentils and other vegetables 07). |
| N8 | Türkiye's imports of lentils and other vegetables, and from Canada | US$1.1 billion; US$185 million | Slide 2 bars, site 1 | `analysis/market/outputs/` | Sum of the HS chapters in the group (Energy 27, Machinery 84, Gold and jewellery 71, Aircraft 88, Lentils and other vegetables 07). |
| N9 | Share of Canada's goods sold to the US, 2025 | 72% | Slide 2, site 1 | `analysis/trade/out/x171_all_sections_extract.csv` | Exports to the United States divided by exports to all countries, all product sections, StatCan table 12-10-0171. 2025 is the smallest share since at least 1999, when the table starts. |
| N10 | Canada's rank among Türkiye's suppliers | 47th | Site 1 | `analysis/market/outputs/tur_imports_2025_by_partner.csv` | Rank by value among trading partners; rows recorded without a partner ("Special Categories", "Areas, nes") are left out, and "Other Asia, nes" counts as a partner (it would be 46th without it). |
| N11 | Trade deficit with Türkiye, 2025 | $2.1 billion | Slide 3, site 2 | `analysis/trade/out/annual_totals_1988_2026ytd.csv` | Imports ($3.20 billion) minus total exports, domestic plus re-exports ($1.14 billion). |
| N12 | Deficit change, January to August 2026 | shrank by almost a quarter (23.5%) | Slide 3, site 2 | `analysis/trade/out/results_totals.json` | January to August deficit: $1.52 billion in 2025, $1.16 billion in 2026. |
| N13 | Exports and imports, January to August 2026 | +8%; -14% | Slide 3, site 2 | `analysis/trade/out/results_totals.json` | Change against January to August 2025. |
| N14 | Goods sold to Türkiye by group, 2025 | Lentils, chickpeas, vegetables $222M; Machinery and engines $188M; Aircraft and parts $176M; Optical instruments $100M; Cars and parts $83M; Everything else $368M | Slide 3, site 2 | `analysis/trade/out/hs2_chapters_2021_2025.csv` | Total exports by HS chapter (07, 84, 88, 90, 87), rounded to $ million; everything else is the total minus the groups. |
| N15 | Goods bought from Türkiye by group, 2025 | Machinery and appliances $405M; Steel and steel goods $308M; Fruit, nuts and food $259M; Medicines $247M; Clothing $220M; Everything else $1,758M | Slide 3, site 2 | `analysis/trade/out/hs2_chapters_2021_2025.csv` | Imports by HS chapter (84; 72 and 73; 08 and 20; 30; 61 and 62), rounded to $ million. |
| N16 | Last year Canada sold Türkiye more than it bought | 2011 | Site 2 | `analysis/trade/out/annual_totals_1988_2026ytd.csv` | Latest year with exports above imports. |
| N17 | Türkiye's duty on Canadian lentils | 19.3% | Slide 4, site 3 | `analysis/tariffs/outputs/ca_exports_to_TR_2025_est_tr_duty.csv` | Highest 2026 rate (customs duty plus additional customs duty) on the lentil lines Canada sold in 2025, Türkiye's 2026 import regime. |
| N18 | Canada's duty on Turkish clothing | about 17% | Slide 4, site 3 | `analysis/tariffs/outputs/ca_imports_from_TR_2025_est_mfn_duty.csv` | Estimated duty on HS chapters 61 and 62 divided by their 2025 value, regular (most-favoured-nation) rates of the 2026 Customs Tariff. |
| N19 | Canadian-made goods sold to Türkiye (duty base) | $1.0 billion | Slide 4, site 3 | `analysis/tariffs/outputs/ca_exports_to_TR_2025_est_tr_duty.csv` | 2025 domestic exports by HS8 line, without durum wheat (HS 1001). |
| N20 | Share duty-free / paying duty, Canadian goods | 47% / 53% | Slide 4, site 3 | `same` | Value of lines with a 0% total rate over the base. |
| N21 | Estimated duty on Canadian goods | $64 million, 6.4% | Slide 4, site 3 | `same` | Sum over lines of 2025 value times the 2026 rate; divided by the base. |
| N22 | Turkish goods sold to Canada (duty base) | $3.2 billion | Slide 4, site 3 | `analysis/tariffs/outputs/ca_imports_from_TR_2025_est_mfn_duty.csv` | 2025 imports from Türkiye by HS10 line. |
| N23 | Share duty-free / paying duty, Turkish goods | 67% / 33% | Slide 4, site 3 | `same` | Value of lines with a Free rate over the base. |
| N24 | Estimated duty on Turkish goods | $105 million, 3.3% | Slide 4, site 3 | `same` | Sum over lines of 2025 value times the 2026 regular rate; divided by the base. |
| N25 | Three largest selling provinces' share | three-quarters (76.7%) | Slide 5, site 4 | `analysis/trade/out/provinces_2021_2025.csv` | Quebec, Ontario and Saskatchewan's 2025 domestic exports to Türkiye over Canada's. |
| N26 | Quebec: sales to Türkiye and top products, 2025 | $310 million; Aircraft $162 million; Steel scrap $29 million; Newsprint $16 million | Slide 5, site 4 | `analysis/trade/out/provinces_2021_2025.csv; analysis/trade/out/province_top_hs6.csv` | Domestic exports by province of origin. Product groups combine their HS6 lines (aircraft 8802.30 and 8802.40; cars every line 8703.21 to 8703.90). |
| N27 | Ontario: sales to Türkiye and top products, 2025 | $275 million; Optical instruments $51 million; Cars $43 million; Plastic-moulding machines $12 million | Slide 5, site 4 | `analysis/trade/out/provinces_2021_2025.csv; analysis/trade/out/province_top_hs6.csv` | Domestic exports by province of origin. Product groups combine their HS6 lines (aircraft 8802.30 and 8802.40; cars every line 8703.21 to 8703.90). |
| N28 | Saskatchewan: sales to Türkiye and top products, 2025 | $205 million; Lentils $130 million; Chickpeas $26 million; Durum wheat $22 million | Slide 5, site 4 | `analysis/trade/out/provinces_2021_2025.csv; analysis/trade/out/province_top_hs6.csv` | Domestic exports by province of origin. Product groups combine their HS6 lines (aircraft 8802.30 and 8802.40; cars every line 8703.21 to 8703.90). |
| N29 | British Columbia: sales to Türkiye and top products, 2025 | $111 million; Aircraft engines $42 million; Coal $37 million | Slide 5, site 4 | `analysis/trade/out/provinces_2021_2025.csv; analysis/trade/out/province_top_hs6.csv` | Domestic exports by province of origin. Product groups combine their HS6 lines (aircraft 8802.30 and 8802.40; cars every line 8703.21 to 8703.90). |
| N30 | Alberta: sales to Türkiye and top products, 2025 | $82 million; Lentils $43 million; Durum wheat $7 million; Other pulses $4 million | Slide 5, site 4 | `analysis/trade/out/provinces_2021_2025.csv; analysis/trade/out/province_top_hs6.csv` | Domestic exports by province of origin. Product groups combine their HS6 lines (aircraft 8802.30 and 8802.40; cars every line 8703.21 to 8703.90). |
| N31 | Saskatchewan's lentil sales, 2022 to 2025 | fell by almost two-thirds (64.5%) | Slide 5, site 4 | `analysis/trade/results.md` | $366.0M in 2022 to $130.0M in 2025. |
| N32 | Countries Turkish Airlines flew to | 120 | Slide 6, site 5 | `slides/facts.json` | Guinness World Records, September 2023 to September 2024. |
| N33 | Weekly flights for each country | 12 before, up to 21 | Slide 6, site 5 | `slides/facts.json` | PMO news release, October 23, 2026. |
| N34 | Trips to Türkiye by Canadians | 139,164 in 2019; 321,271 in 2025 | Slide 6, site 5 | `analysis/people/outputs/turkiye_border_canada.json` | Arriving visitors with Canadian nationality, Türkiye's border statistics. |
| N35 | Istanbul Airport passengers, 2025 | 84.4 million | Site 5 | `slides/facts.json` | ACI World 2025 rankings (8th). |
| N36 | People of Turkish origin in Canada, 2021 | 76,745 | Site 5 | `analysis/people/outputs/census_turkish_by_geo.csv` | 2021 Census, Turkish ethnic or cultural origin, single and multiple responses. |
| N37 | Türkiye's nuclear goals | 7.2 GW by 2035; over 20 GW by 2050 | Slide 7, site 6 | `slides/facts.json` | Türkiye Ministry of Energy, September 25, 2023. |
| N38 | Akkuyu plant under construction | 4.8 GW | Slide 7, site 6 | `slides/facts.json` | Invest in Türkiye; IAEA PRIS (four units under construction). |
| N39 | Wind and solar capacity, December 2025 | 39 GW | Slide 7, site 6 | `analysis/energy/raw/round3/epias.txt` | EPİAŞ daily bulletin, December 14, 2025: wind plus solar installed capacity. |
| N40 | Wind and solar goal for 2035 | 120 GW | Slide 7, site 6 | `slides/facts.json` | Türkiye Ministry of Energy, November 4, 2024. |
| N41 | Canada's share of world uranium, 2024 | about a quarter (24%) | Slide 7, site 6 | `analysis/energy/results.md` | Natural Resources Canada, uranium and nuclear power facts. |
| N42 | Türkiye's gas imports, 2025 | 58.3 billion m³ | Site 6 | `analysis/energy/results.md` | EPDK 2025 Natural Gas Market Development Report, imports by country. |
| N43 | Canada's LNG exports, 2025 | 3.1 billion m³ (about 5% of Türkiye's gas imports) | Site 6 | `analysis/energy/outputs/cer_lng_summary.txt` | Canada Energy Regulator LNG shipment detail, gas equivalent. |
| N44 | Military exports to Türkiye | $151 million in 2019; $108 million in 2024 | Slide 8, site 7 | `analysis/defence/outputs/exports_turkiye_2010_2025.csv` | Global Affairs Canada, Reports on Exports of Military Goods, value of exports to Türkiye by year. |
| N45 | Permits cancelled in April 2021 | 29 | Slide 8, site 7 | `slides/facts.json` | Global Affairs Canada statement, April 12, 2021. |
| N46 | Brokering permit for Ukraine, 2025 | $125 million | Slide 8, site 7 | `analysis/defence/results.md` | 2025 Report on Exports of Military Goods, table 16. |
| N47 | First round of free trade talks | November 30 to December 4, 2026 | Slide 9, site 8 | `slides/facts.json` | PMO news release, October 23, 2026. |

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
