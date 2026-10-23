# Canada-Türkiye goods trade: results from official raw data

Access date for every source: 2026-10-23. All values are nominal Canadian dollars, customs basis, not seasonally adjusted, unless stated. Exports = total exports (domestic exports plus re-exports) unless stated. Rounded to C$0.1 million or 1 decimal percent in this file; full precision is in the CSV/JSON files in `out/`. Latest month available: August 2026 (StatCan release 2026-10-06).

## Sources and how the numbers were built

- Main source: Statistics Canada Canadian International Merchandise Trade (CIMT) database, pulled through the StatCan Web Data Service (WDS) endpoint `https://www150.statcan.gc.ca/t1/wds/rest/getDataFromCubePidCoordAndLatestNPeriods`. These are the back-end cubes of the CIMT web application:
  - 12-10-0147 (domestic exports and re-exports, by province of origin, country, HS2 chapter, monthly from 1988-01)
  - 12-10-0150 (imports, by province of clearance, country of origin, HS2, monthly from 1988-01)
  - 12-10-0148 and 12-10-0151 (same at HS6, monthly from 2014-01; pulled for 2021-01 to 2026-08)
  - Türkiye is country member 382. Annual values are sums of the 12 monthly values.
- Cross-check tables (full CSV downloads): 12-10-0171-01 (trade by country and NAPCS section, annual 1999-2025) `https://www150.statcan.gc.ca/n1/tbl/csv/12100171-eng.zip`, and 12-10-0173-01 (by province and country) `https://www150.statcan.gc.ca/n1/tbl/csv/12100173-eng.zip`.
- CPI: table 18-10-0005-01, Canada all-items annual average (2002=100) `https://www150.statcan.gc.ca/n1/tbl/csv/18100005-eng.zip`.
- Exchange rate: Bank of Canada annual average USD/CAD (FXAUSDCAD) `https://www.bankofcanada.ca/valet/observations/FXAUSDCAD/json`. 2025 = 1.3978.
- Mirror check: UN Comtrade public API, Canada and Türkiye as reporters, annual totals in USD.
- Checks passed: annual totals built from the CIMT monthly HS2 cubes equal table 12-10-0171 to within C$0.03 million in every year 1999-2025 (exact in most years; small gaps in 2001, 2003, 2005 are rounding/revision level). Province totals for 2025 equal table 12-10-0173 exactly. HS6 sums for 2025 come to C$1,120.7M exports and C$3,197.1M imports; the gap to the HS2 total on exports (C$16.7M) is HS chapters 98 and 99 (special classification provisions), which have no HS6 detail.
- Not reachable from this environment: the CIMT web application at www5.statcan.gc.ca (connection reset) and the ISED Trade Data Online report engine (form loads, report requests return HTTP 405 or the blank form). The WDS cubes above hold the same CIMT data, so no figure depends on those two sites.
- Table 12-10-0011 (monthly, principal partners) was checked: it does not list Türkiye separately, so it is not used.

Caveats that apply throughout:
- Customs basis, not balance-of-payments basis. StatCan publishes BOP-basis figures only for principal partners, not Türkiye, so BOP figures for Türkiye are not available from StatCan.
- Imports are recorded by country of origin, not the country goods were shipped from. Exports are by country of final destination as declared.
- Re-exports (foreign goods passing through Canada without transformation) are included in total exports. They were unusually high in 2025: C$108.0M, up from C$53.2M in 2024.
- Province of import is the province of clearance (where customs cleared the goods), not where the goods are consumed. Province of export is province of origin (production). Provincial exports are domestic exports only.
- Monthly data for 2025 and 2026 can still be revised by StatCan. The annual tables 12-10-0171/0173 were dated 2026-08-04; WDS cubes reflect the 2026-10-06 release, and the two agree for 2025.
- Mirror data do not match: Türkiye (TurkStat via UN Comtrade) reports exports to Canada of US$1,577.7M in 2025 versus Canada's reported imports from Türkiye of US$2,288.1M; Türkiye reports imports from Canada of US$1,162.8M versus Canada's reported exports of US$814.8M. Likely reasons (not verified item by item): Canada records imports by country of origin, so Turkish-made goods shipped via the EU or US still count as Türkiye in Canada's data but may be recorded by Türkiye as exports to the EU or US; Canadian goods sold to Türkiye through third-country traders count as Canadian origin in Türkiye's imports but not as exports to Türkiye in Canada's data; Türkiye values imports CIF (including freight and insurance) while Canada values exports FOB; and timing and valuation differ. Both datasets are official; the gap reflects methods, not an error in either. Canada's own figures are used for every headline number here.

## 1. Trade every year, 1990 to 2026 YTD

Full table T1 below (1988 and 1989 are also in `out/annual_totals_1988_2026ytd.csv`).

Key figures, 2025: exports C$1,137.4M (domestic C$1,029.4M, re-exports C$108.0M), imports C$3,197.3M, two-way C$4,334.7M, balance -C$2,060.0M (a deficit for Canada).

2026 January to August vs 2025 January to August:
- Exports C$753.3M vs C$699.6M (+7.7%). Domestic exports +12.4%; re-exports -31.4%.
- Imports C$1,918.1M vs C$2,221.7M (-13.7%).
- Two-way C$2,671.4M vs C$2,921.3M (-8.6%).
- Balance -C$1,164.8M vs -C$1,522.0M.

Growth of two-way trade to 2025 (nominal):

| Period | Total change | Yearly (CAGR) | Exports CAGR | Imports CAGR | Real CAGR (CPI) |
|---|---|---|---|---|---|
| 5 yr (2020-2025) | +40.6% | 7.1% | -1.4% | 11.5% | 3.2% |
| 10 yr (2015-2025) | +79.1% | 6.0% | 0.1% | 9.5% | 3.3% |
| 15 yr (2010-2025) | +178.6% | 7.1% | 2.0% | 10.5% | 4.6% |
| 25 yr (2000-2025) | +684.8% | 8.6% | 6.1% | 10.0% | 6.3% |

Real growth deflates two-way trade by Canada's all-items CPI (18-10-0005). CPI rose 19.9% from 2020 to 2025 and 29.7% from 2015 to 2025. CPI is a consumer price index, not a trade price index, so the real figures are a rough guide only.

Check on the PMO line "Bilateral trade has increased by almost 50% in the past five years" (pm.gc.ca/en/node/54279): two-way trade rose 40.6% from 2020 to 2025 and 42.9% from 2020 to 2024. Reuters used "nearly 50%". The StatCan data give about 41%, so "almost 50%" is generous; the PMO does not state its base year or source.

Almost all of the growth is on the import side. Canadian exports to Türkiye peaked in 2019 (C$1,616.1M) and in 2025 were below their 2015 level in nominal terms (C$1,137.4M vs C$1,126.7M, essentially flat).

## 2. Share and rank, 2025

From table 12-10-0171-01, ranking 256 partners ("Canada" as a partner, meaning returned Canadian goods, and "High Seas" excluded):
- Two-way trade: Türkiye ranks 27th, with 0.28% of Canada's goods trade (C$4.33B of C$1,566.9B).
- Exports: 31st, 0.15% of Canada's exports (C$1.14B of C$778.0B).
- Imports: 27th, 0.41% of Canada's imports (C$3.20B of C$788.9B).

Neighbours in the two-way ranking, 2025 (C$ billions): 24 Ireland 6.01, 25 Poland 5.34, 26 Singapore 4.94, 27 Türkiye 4.33, 28 Hong Kong 4.13, 29 South Africa 4.12, 30 Bangladesh 4.07.

Rank over time (two-way): 28th in 2015, 26th in 2020, 26th in 2024, 27th in 2025. Share of two-way trade: 0.23% (2015), 0.29% (2020), 0.28% (2024), 0.28% (2025).

Reuters (2026-10-21) wrote "less than 0.3% of Canada's total merchandise trade, or C$4.34 billion ($3.09 billion)". This matches StatCan: C$4.3347B and 0.28%; at the Bank of Canada 2025 average rate it is US$3.10B.

## 3. What Canada sells and buys

### GAC fact sheet check

The Global Affairs Canada page "Canada-Türkiye relations" (international.gc.ca/country-pays/turkiye/relations.aspx, date modified 2026-10-06) figures match StatCan table 12-10-0171-01 exactly. GAC uses **NAPCS 2022 sections** (North American Product Classification System), the product grouping in that table, not HS chapters.

| GAC figure | StatCan 12-10-0171, 2025 | NAPCS section |
|---|---|---|
| Exports $1.1B | C$1,137.4M | All sections (total exports) |
| Imports $3.2B | C$3,197.3M | All sections |
| Two-way "over $4.3B" | C$4,334.7M | |
| Agri-food $287M | C$287.2M | C11 Farm, fishing and intermediate food products |
| Aircraft/transport equipment $273M | C$273.4M | C21 Aircraft and other transportation equipment and parts |
| Industrial machinery $151M | C$150.6M | C17 Industrial machinery, equipment and parts |
| Consumer goods $1.27B | C$1,270.2M | C22 Consumer goods |
| Metal and non-metallic mineral products $480M | C$479.7M | C14 |
| Forestry, building and packaging $316M | C$315.7M | C16 |

Note that "agri-food" in GAC's text is NAPCS section C11, which excludes processed food and beverages (those sit in C22 Consumer goods). Also, "Consumer goods" C22 includes pharmaceuticals, clothing, carpets, jewellery and processed food, which is why it is so large.

The same NAPCS sections in 2024: exports C11 C$521.1M, C14 C$183.5M, C17 C$178.3M, C21 C$84.4M; imports C22 C$1,065.6M, C14 C$715.7M, C17 C$263.8M, C16 C$257.7M. So in one year Canada's farm exports to Türkiye fell by 45% (C$521.1M to C$287.2M), and aircraft exports more than tripled (C$84.4M to C$273.4M).

### By HS chapter and product

HS6 detail comes from CIMT cubes 12-10-0148 (exports) and 12-10-0151 (imports). Product descriptions come from the HS nomenclature list (UN Comtrade reference file). Concentration: the top 15 HS6 lines were 64% of exports in 2025 (75% in 2024) but only 28% of imports (32% in 2024). Canada sells Türkiye a few bulk and big-ticket items; it buys a wide spread of manufactured goods.

Main shifts 2024 to 2025:
- Lentils (HS 071340) fell from C$324.0M to C$172.6M. Lentil exports were C$340.7M (2021), C$486.6M (2022), C$436.0M (2023).
- Alloy steel scrap (720429) fell from C$166.6M to C$54.4M; soybeans (120190) from C$113.2M to C$19.3M.
- Aircraft (880240 and 880230, mostly from Quebec) went from zero in the top 15 to C$162.0M combined. Aircraft sales are lumpy single deliveries; one year's figure says little about trend.
- On imports, flat-rolled steel (721049) dropped from C$201.7M (2024) out of the top 15 and tugs (890400, C$128.3M in 2024) also dropped out, while medicaments (300490) rose from C$104.5M to C$179.3M and blood products/vaccines-type items (300215) reached C$62.1M. Ship imports (tugs in 2024, a fish-processing vessel in 2025, C$79.2M cleared in Newfoundland and Labrador) are also one-off deliveries.

## 4. By province

Exports: domestic exports by province of origin. Imports: by province of clearance (customs office), which is not necessarily the province where the goods are used. Values in table T4; top products in T5.

- Quebec (C$309.5M) and Ontario (C$274.6M) were the largest exporters to Türkiye in 2025, then Saskatchewan (C$205.3M). Over 2021-2025 on average, Saskatchewan was first (C$357.6M a year), Quebec second (C$309.7M), Ontario third (C$197.3M).
- Saskatchewan's exports are mainly pulses and grain: lentils C$130.0M in 2025 (5-year average C$284.2M), chickpeas C$26.5M, durum wheat C$22.1M. Saskatchewan's lentil exports to Türkiye were C$339.6M (2021), C$366.0M (2022), C$319.0M (2023), C$266.2M (2024), C$130.0M (2025). Alberta also exports lentils (C$42.6M in 2025).
- Quebec: aircraft (C$162.0M in 2025 across 880240 and 880230) and steel scrap (C$29.2M, down from a 5-year average of C$116.4M).
- Ontario: optical instruments (901380, C$50.8M), passenger vehicles (870390, C$29.0M).
- British Columbia: small turboprop engines (841121, C$42.2M) and coal (270112, C$37.4M, 5-year average C$78.0M).
- Imports cleared: Ontario C$1,386.1M and Quebec C$1,168.2M together cleared 80% of 2025 imports from Türkiye.

## 5. What doubling would take

Base: 2025 two-way trade of C$4,334.7M (US$3,101.1M at the 2025 Bank of Canada average of 1.3978).

What was said about the target (news used only for the wording; none of these numbers is used as data):
- The Canadian Press (Craig Lord, 2026-10-22): "Erdogan said he hopes trade between the two countries will roughly double to $10 billion". No currency given.
- Reuters (Maria Cheng and Tuvan Gumrukcu, 2026-10-21, updated 2026-10-22): "The two sides expected to raise their trade volume from $3 billion first to $5 billion and then to $10 billion." No timeframe. The same Reuters story gives Canada's figure as "C$4.34 billion ($3.09 billion)", so Reuters's "$" is US dollars, and the $3 billion starting point is the US-dollar value of the C$4.3B.
- Al Jazeera/Anadolu/Reuters (2026-10-22) quote Erdoğan: trade "which currently stands at around $3bn, to $5bn initially", then $10bn.
- Reading: the starting point "around $3 billion" only fits US dollars (C$4.3B = US$3.1B), so the $10B goal is most likely US dollars. No source states the currency outright, so this is an inference. Also note that going from US$3B to US$10B is more than tripling, not "roughly doubling"; "double" fits only the intermediate US$5B step or a C$ reading. No timeframe was given by any source.

| Target | Level in C$ | Multiple of 2025 | Yearly growth needed over 5 yr | over 10 yr |
|---|---|---|---|---|
| Double 2025 (C$) | C$8.67B | 2.00x | 14.9% | 7.2% |
| C$10B | C$10.00B | 2.31x | 18.2% | 8.7% |
| US$10B (at 2025 rate 1.3978) | C$13.98B | 3.22x | 26.4% | 12.4% |
| US$5B intermediate step | C$6.99B | 1.61x | 10.0% | 4.9% |

Actual past growth of two-way trade, nominal C$: 7.1% a year over 2020-2025, 6.0% over 2015-2025, 8.6% over 2000-2025. At the 10-year pace (6.0%), two-way trade would double in about 12 years (around 2037). Doubling within 10 years needs 7.2% a year, a bit above the past decade's pace; doubling in 5 years needs about twice the past pace. Past growth was driven by imports; exports grew 0.1% a year over 2015-2025.

## 6. Is the trade gap growing?

Yes, over the long run and in 2025; it narrowed in the first eight months of 2026.

- Canada ran a surplus with Türkiye in most years to 1997 and again 2007-2011. The deficit opened from 2012 and widened sharply from 2021.
- Imports-to-exports ratio, averaged over five-year blocks (sum of imports divided by sum of exports): 1991-1995 0.58; 1996-2000 0.88; 2001-2005 1.54; 2006-2010 0.77; 2011-2015 1.27; 2016-2020 1.41; 2021-2025 2.50.
- Annual ratio: 1.52 (2020), 2.42 (2021), 2.48 (2022), 2.31 (2023), 2.50 (2024), 2.81 (2025, highest on record since 1988). The "about 3x" description fits 2025 (2.81x) better than earlier years.
- Balance: -C$636.3M (2020), -C$1,636.2M (2021), -C$1,895.9M (2022), -C$1,616.2M (2023), -C$1,887.9M (2024), -C$2,060.0M (2025).
- 2026 Jan-Aug: ratio 2.55 vs 3.18 in Jan-Aug 2025; deficit -C$1,164.8M vs -C$1,522.0M. Partial-year data, so not yet a trend.
- Using Türkiye's mirror data the picture is different: Türkiye records a surplus with Canada of only US$414.9M in 2025 (US$1,577.7M exports, US$1,162.8M imports, ratio 1.36). Which side's figures are used changes the size of the "gap" a lot; see the caveat on mirror data above.

## Tables
### T1 Annual totals (C$ millions, customs basis)

| Year | Exports | of which re-exports | Imports | Two-way | Balance | Imports/exports |
|---|---|---|---|---|---|---|
| 1990 | 160.7 | 3.8 | 84.4 | 245.1 | 76.3 | 0.53 |
| 1991 | 100.4 | 6.6 | 66.0 | 166.3 | 34.4 | 0.66 |
| 1992 | 139.3 | 4.6 | 68.0 | 207.3 | 71.3 | 0.49 |
| 1993 | 160.2 | 8.5 | 82.5 | 242.7 | 77.7 | 0.51 |
| 1994 | 147.4 | 7.4 | 119.8 | 267.2 | 27.6 | 0.81 |
| 1995 | 291.0 | 10.2 | 150.1 | 441.1 | 140.9 | 0.52 |
| 1996 | 265.1 | 7.7 | 152.2 | 417.3 | 112.9 | 0.57 |
| 1997 | 335.2 | 5.5 | 194.5 | 529.6 | 140.7 | 0.58 |
| 1998 | 226.0 | 14.0 | 249.8 | 475.8 | -23.7 | 1.10 |
| 1999 | 214.7 | 17.3 | 250.8 | 465.5 | -36.1 | 1.17 |
| 2000 | 259.8 | 13.0 | 292.6 | 552.4 | -32.9 | 1.13 |
| 2001 | 172.6 | 3.8 | 315.3 | 487.9 | -142.6 | 1.83 |
| 2002 | 268.7 | 7.4 | 400.4 | 669.1 | -131.7 | 1.49 |
| 2003 | 273.3 | 11.8 | 466.6 | 739.9 | -193.3 | 1.71 |
| 2004 | 372.1 | 14.3 | 609.9 | 982.0 | -237.8 | 1.64 |
| 2005 | 486.7 | 29.2 | 637.3 | 1124.0 | -150.6 | 1.31 |
| 2006 | 548.2 | 19.5 | 625.0 | 1173.2 | -76.8 | 1.14 |
| 2007 | 672.5 | 20.4 | 561.9 | 1234.4 | 110.7 | 0.84 |
| 2008 | 1236.4 | 23.9 | 703.1 | 1939.5 | 533.3 | 0.57 |
| 2009 | 891.5 | 80.0 | 632.3 | 1523.8 | 259.2 | 0.71 |
| 2010 | 841.7 | 18.2 | 714.2 | 1555.9 | 127.5 | 0.85 |
| 2011 | 1271.5 | 21.1 | 1122.7 | 2394.2 | 148.8 | 0.88 |
| 2012 | 851.0 | 38.6 | 1479.1 | 2330.1 | -628.1 | 1.74 |
| 2013 | 888.3 | 21.9 | 1318.9 | 2207.2 | -430.6 | 1.48 |
| 2014 | 1062.5 | 26.2 | 1410.2 | 2472.7 | -347.7 | 1.33 |
| 2015 | 1126.7 | 24.4 | 1293.5 | 2420.2 | -166.8 | 1.15 |
| 2016 | 1152.5 | 26.7 | 1367.8 | 2520.3 | -215.3 | 1.19 |
| 2017 | 1265.4 | 38.8 | 1785.7 | 3051.0 | -520.3 | 1.41 |
| 2018 | 1329.3 | 62.8 | 2337.3 | 3666.7 | -1008.0 | 1.76 |
| 2019 | 1616.1 | 51.9 | 1964.6 | 3580.7 | -348.5 | 1.22 |
| 2020 | 1223.1 | 35.7 | 1859.3 | 3082.4 | -636.3 | 1.52 |
| 2021 | 1151.5 | 27.6 | 2787.8 | 3939.3 | -1636.2 | 2.42 |
| 2022 | 1282.3 | 46.6 | 3178.2 | 4460.6 | -1895.9 | 2.48 |
| 2023 | 1231.3 | 58.2 | 2847.5 | 4078.8 | -1616.2 | 2.31 |
| 2024 | 1258.1 | 53.2 | 3146.0 | 4404.1 | -1887.9 | 2.50 |
| 2025 | 1137.4 | 108.0 | 3197.3 | 4334.7 | -2060.0 | 2.81 |
| 2026 (Jan-Aug YTD) | 753.3 | 51.9 | 1918.1 | 2671.4 | -1164.8 | 2.55 |

### T2-exports Top 10 HS chapters, exports, 2025 (with 2024)

| HS2 | Chapter | 2025 | Share 2025 | 2024 |
|---|---|---|---|---|
| 07 | Edible vegetables and certain roots and tubers | 221.7 | 19.5% | 392.6 |
| 84 | Nuclear reactors, boilers, machinery and mechani... | 188.0 | 16.5% | 125.4 |
| 88 | Aircraft, spacecraft, and parts thereof | 176.2 | 15.5% | 32.9 |
| 90 | Optical, photographic, cinematographic, measurin... | 99.7 | 8.8% | 136.4 |
| 87 | Vehicles other than railway or tramway rolling-s... | 82.7 | 7.3% | 55.2 |
| 72 | Iron and steel | 56.4 | 5.0% | 167.7 |
| 85 | Electrical machinery and equipment and parts the... | 45.4 | 4.0% | 50.5 |
| 27 | Mineral fuels, mineral oils and products of thei... | 39.7 | 3.5% | 2.7 |
| 10 | Cereals | 32.6 | 2.9% | 1.9 |
| 48 | Paper and paperboard; articles of paper pulp, of... | 25.4 | 2.2% | 27.0 |

### T2-imports Top 10 HS chapters, imports, 2025 (with 2024)

| HS2 | Chapter | 2025 | Share 2025 | 2024 |
|---|---|---|---|---|
| 84 | Nuclear reactors, boilers, machinery and mechani... | 405.2 | 12.7% | 321.0 |
| 30 | Pharmaceutical products | 247.3 | 7.7% | 130.7 |
| 73 | Articles of iron or steel | 163.0 | 5.1% | 127.1 |
| 08 | Edible fruit and nuts; peel of citrus fruit or m... | 158.3 | 4.9% | 159.1 |
| 87 | Vehicles other than railway or tramway rolling-s... | 151.4 | 4.7% | 136.9 |
| 72 | Iron and steel | 145.1 | 4.5% | 471.0 |
| 85 | Electrical machinery and equipment and parts the... | 127.4 | 4.0% | 116.1 |
| 76 | Aluminum and articles thereof | 125.7 | 3.9% | 74.6 |
| 62 | Articles of apparel and clothing accessories, no... | 111.2 | 3.5% | 114.8 |
| 61 | Articles of apparel and clothing accessories, kn... | 108.9 | 3.4% | 115.9 |

### T3 Top 15 HS6, total exports, 2025

| # | HS6 | Product | C$ M | Share |
|---|---|---|---|---|
| 1 | 071340 | Vegetables, leguminous; lentils, shelled, whether or no... | 172.6 | 15.4% |
| 2 | 880240 | Aeroplanes and other aircraft, except unmanned; of an u... | 101.9 | 9.1% |
| 3 | 880230 | Aeroplanes and other aircraft, except unmanned; of an u... | 60.1 | 5.4% |
| 4 | 720429 | Ferrous waste and scrap; of alloy steel (excluding stai... | 54.4 | 4.9% |
| 5 | 901380 | Optical devices, appliances and instruments; n.e.c. in ... | 50.9 | 4.5% |
| 6 | 841121 | Turbo-propellers; of a power not exceeding 1100kW | 46.1 | 4.1% |
| 7 | 870390 | Vehicles; for transport of persons (other than those of... | 37.7 | 3.4% |
| 8 | 270112 | Coal; bituminous, whether or not pulverised, but not ag... | 37.4 | 3.3% |
| 9 | 100119 | Cereals; wheat and meslin, durum wheat, other than seed | 28.8 | 2.6% |
| 10 | 071320 | Vegetables, leguminous; chickpeas (garbanzos), shelled,... | 28.8 | 2.6% |
| 11 | 841112 | Turbo-jets; of a thrust exceeding 25kN | 25.3 | 2.3% |
| 12 | 120190 | Soya beans; other than seed, whether or not broken | 19.3 | 1.7% |
| 13 | 480100 | Newsprint; made of fibres obtained essentially by a che... | 17.7 | 1.6% |
| 14 | 870323 | Vehicles; with only spark-ignition internal combustion ... | 17.7 | 1.6% |
| 15 | 870324 | Vehicles; with only spark-ignition internal combustion ... | 17.3 | 1.5% |

### T3 Top 15 HS6, total exports, 2024

| # | HS6 | Product | C$ M | Share |
|---|---|---|---|---|
| 1 | 071340 | Vegetables, leguminous; lentils, shelled, whether or no... | 324.0 | 26.4% |
| 2 | 720429 | Ferrous waste and scrap; of alloy steel (excluding stai... | 166.6 | 13.6% |
| 3 | 120190 | Soya beans; other than seed, whether or not broken | 113.2 | 9.2% |
| 4 | 901380 | Optical devices, appliances and instruments; n.e.c. in ... | 99.2 | 8.1% |
| 5 | 071320 | Vegetables, leguminous; chickpeas (garbanzos), shelled,... | 50.2 | 4.1% |
| 6 | 841121 | Turbo-propellers; of a power not exceeding 1100kW | 39.8 | 3.2% |
| 7 | 870324 | Vehicles; with only spark-ignition internal combustion ... | 27.7 | 2.3% |
| 8 | 480100 | Newsprint; made of fibres obtained essentially by a che... | 19.3 | 1.6% |
| 9 | 880730 | Aircraft and spacecraft; parts of aeroplanes, helicopte... | 16.6 | 1.4% |
| 10 | 071339 | Vegetables, leguminous; n.e.c. in item no. 0713.3, shel... | 14.4 | 1.2% |
| 11 | 180500 | Cocoa; powder, not containing added sugar or other swee... | 10.1 | 0.8% |
| 12 | 870390 | Vehicles; for transport of persons (other than those of... | 9.3 | 0.8% |
| 13 | 870323 | Vehicles; with only spark-ignition internal combustion ... | 9.1 | 0.7% |
| 14 | 841122 | Turbo-propellers; of a power exceeding 1100kW | 7.3 | 0.6% |
| 15 | 300390 | Medicaments; (not containing antibiotics, hormones, alk... | 7.0 | 0.6% |

### T3 Top 15 HS6, imports, 2025

| # | HS6 | Product | C$ M | Share |
|---|---|---|---|---|
| 1 | 300490 | Medicaments; consisting of mixed or unmixed products n.... | 179.3 | 5.6% |
| 2 | 890200 | Fishing vessels, factory ships and other vessels; for p... | 79.2 | 2.5% |
| 3 | 841191 | Turbines; parts of turbo-jets and turbo-propellers | 71.9 | 2.2% |
| 4 | 570242 | Carpets and other textile floor coverings; woven, (not ... | 70.9 | 2.2% |
| 5 | 711319 | Jewellery; of precious metal (excluding silver) whether... | 67.9 | 2.1% |
| 6 | 300215 | Blood, human or animal, antisera, other blood fractions... | 62.1 | 1.9% |
| 7 | 441114 | Medium density fibreboard (MDF), of a thickness exceedi... | 49.6 | 1.6% |
| 8 | 720851 | Iron or non-alloy steel; (not in coils), flat-rolled, o... | 47.7 | 1.5% |
| 9 | 200979 | Juice; apple, of a Brix value exceeding 20, unfermented... | 47.0 | 1.5% |
| 10 | 870880 | Vehicle parts; suspension systems and parts thereof (in... | 42.6 | 1.3% |
| 11 | 760429 | Aluminium; alloys, bars, rods and profiles, other than ... | 40.5 | 1.3% |
| 12 | 730820 | Iron or steel; structures and parts thereof, towers and... | 38.1 | 1.2% |
| 13 | 854430 | Insulated electric conductors; ignition wiring sets and... | 35.7 | 1.1% |
| 14 | 480300 | Tissue, towel, napkin stock or similar; for household o... | 32.4 | 1.0% |
| 15 | 880730 | Aircraft and spacecraft; parts of aeroplanes, helicopte... | 32.2 | 1.0% |

### T3 Top 15 HS6, imports, 2024

| # | HS6 | Product | C$ M | Share |
|---|---|---|---|---|
| 1 | 721049 | Iron or non-alloy steel; flat-rolled, width 600mm or mo... | 201.7 | 6.4% |
| 2 | 890400 | Tugs and pusher craft | 128.3 | 4.1% |
| 3 | 300490 | Medicaments; consisting of mixed or unmixed products n.... | 104.5 | 3.3% |
| 4 | 570242 | Carpets and other textile floor coverings; woven, (not ... | 74.4 | 2.4% |
| 5 | 720916 | Iron or non-alloy steel; in coils, flat-rolled, width 6... | 65.5 | 2.1% |
| 6 | 271012 | Petroleum oils and oils from bituminous minerals, not c... | 60.9 | 1.9% |
| 7 | 711319 | Jewellery; of precious metal (excluding silver) whether... | 60.7 | 1.9% |
| 8 | 441114 | Medium density fibreboard (MDF), of a thickness exceedi... | 55.5 | 1.8% |
| 9 | 841191 | Turbines; parts of turbo-jets and turbo-propellers | 48.9 | 1.6% |
| 10 | 080222 | Nuts, edible; hazelnuts or filberts (corylus spp.), fre... | 36.5 | 1.2% |
| 11 | 854430 | Insulated electric conductors; ignition wiring sets and... | 35.7 | 1.1% |
| 12 | 720917 | Iron or non-alloy steel; in coils, flat-rolled, width 6... | 35.4 | 1.1% |
| 13 | 284019 | Borates; disodium tetraborate (refined borax), other th... | 32.2 | 1.0% |
| 14 | 620462 | Trousers, bib and brace overalls, breeches and shorts; ... | 29.9 | 0.9% |
| 15 | 870880 | Vehicle parts; suspension systems and parts thereof (in... | 29.6 | 0.9% |

### T4 Provinces (C$ millions)

| Province | Dom. exports 2025 | Avg 2021-25 | Imports 2025 (clearance) | Avg 2021-25 |
|---|---|---|---|---|
| Canada | 1029.4 | 1153.4 | 3197.3 | 3031.4 |
| Newfoundland and Labrador | 27.3 | 8.1 | 88.4 | 61.7 |
| Prince Edward Island | 0.5 | 0.8 | 8.0 | 1.6 |
| Nova Scotia | 10.3 | 7.7 | 46.4 | 60.8 |
| New Brunswick | 2.3 | 27.4 | 9.5 | 29.9 |
| Quebec | 309.5 | 309.7 | 1168.2 | 1108.1 |
| Ontario | 274.6 | 197.3 | 1386.1 | 1348.7 |
| Manitoba | 6.7 | 17.3 | 94.1 | 63.2 |
| Saskatchewan | 205.3 | 357.6 | 59.4 | 34.6 |
| Alberta | 81.5 | 109.0 | 135.1 | 102.7 |
| British Columbia | 111.3 | 118.5 | 196.3 | 217.7 |
| Yukon | 0.0 | 0.0 | 0.0 | 0.0 |
| Northwest Territories | 0.0 | 0.0 | 0.0 | 0.0 |
| Nunavut | 0.0 | 0.0 | 5.9 | 2.4 |

### T5 Top 3 HS6 per province, 2025 (C$ millions; 5-yr avg in brackets)

| Province | Flow | Products |
|---|---|---|
| Newfoundland and Labrador | Exports | 720429 Ferrous waste and scrap; of  25.2 (5.0); 480100 Newsprint; made of fibres ob 1.2 (2.8); 901590 Surveying equipment; parts a 0.6 (0.1) |
| Newfoundland and Labrador | Imports | 890200 Fishing vessels, factory shi 79.2 (33.8); 283620 Carbonates; disodium carbona 4.3 (5.3); 281000 Oxides of boron; boric acids 1.7 (3.2) |
| Prince Edward Island | Exports | 843860 Machinery; industrial, for t 0.1 (0.0); 151590 Fixed vegetable fats and oil 0.1 (0.0); 841191 Turbines; parts of turbo-jet 0.0 (0.0) |
| Prince Edward Island | Imports | 850164 Electric generators 8.0 (1.6) |
| Nova Scotia | Exports | 870390 Vehicles; for transport of p 2.4 (1.0); 310100 Fertilizers, animal or veget 1.8 (0.9); 081190 Fruit, edible; fruit and nut 1.6 (0.7) |
| Nova Scotia | Imports | 190219 Food preparations; pasta, un 13.2 (7.9); 760429 Aluminium; alloys, bars, rod 3.7 (4.4); 841290 Engines; parts, for engines  3.5 (0.7) |
| New Brunswick | Exports | 843143 Boring or sinking machinery; 0.7 (0.2); 470321 Wood pulp; chemical wood pul 0.5 (0.9); 902620 Instruments and apparatus; f 0.2 (0.1) |
| New Brunswick | Imports | 392590 Plastics; builders' ware, n. 1.5 (0.3); 842199 Machinery; parts for filteri 1.5 (0.3); 870193 Tractors; n.e.c. in heading  0.6 (1.2) |
| Quebec | Exports | 880240 Aeroplanes and other aircraf 101.9 (30.2); 880230 Aeroplanes and other aircraf 60.1 (17.9); 720429 Ferrous waste and scrap; of  29.2 (116.4) |
| Quebec | Imports | 300490 Medicaments; consisting of m 111.2 (60.8); 841191 Turbines; parts of turbo-jet 40.8 (30.3); 854430 Insulated electric conductor 35.5 (27.4) |
| Ontario | Exports | 901380 Optical devices, appliances  50.8 (30.0); 870390 Vehicles; for transport of p 29.0 (9.3); 847710 Machinery; injection-mouldin 12.5 (4.3) |
| Ontario | Imports | 300490 Medicaments; consisting of m 68.1 (16.5); 300215 Blood, human or animal, anti 62.1 (16.8); 570242 Carpets and other textile fl 53.4 (61.7) |
| Manitoba | Exports | 300212 Blood, human or animal, anti 2.3 (1.6); 071339 Vegetables, leguminous; n.e. 1.2 (1.0); 300490 Medicaments; consisting of m 1.1 (0.5) |
| Manitoba | Imports | 841191 Turbines; parts of turbo-jet 23.4 (14.8); 730820 Iron or steel; structures an 22.3 (12.3); 853690 Electrical apparatus; n.e.c. 3.8 (0.8) |
| Saskatchewan | Exports | 071340 Vegetables, leguminous; lent 130.0 (284.2); 071320 Vegetables, leguminous; chic 26.5 (31.9); 100119 Cereals; wheat and meslin, d 22.1 (17.0) |
| Saskatchewan | Imports | 284019 Borates; disodium tetraborat 12.4 (13.1); 730629 Iron or steel (excluding cas 10.4 (3.5); 853710 Boards, panels, consoles, de 6.9 (1.4) |
| Alberta | Exports | 071340 Vegetables, leguminous; lent 42.6 (67.8); 100119 Cereals; wheat and meslin, d 6.6 (4.3); 071339 Vegetables, leguminous; n.e. 4.0 (2.3) |
| Alberta | Imports | 843149 Machinery; parts of machines 15.1 (7.6); 730629 Iron or steel (excluding cas 9.8 (14.5); 843139 Machinery; parts of the mach 7.0 (2.9) |
| British Columbia | Exports | 841121 Turbo-propellers; of a power 42.2 (10.0); 270112 Coal; bituminous, whether or 37.4 (78.0); 841869 Refrigerating or freezing eq 3.4 (0.7) |
| British Columbia | Imports | 841810 Refrigerators and freezers;  8.8 (7.6); 081110 Fruit, edible; strawberries, 7.9 (4.3); 890332 Motorboats; (other than outb 6.3 (1.7) |
| Northwest Territories | Exports | 870324 Vehicles; with only spark-ig 0.0 (0.0) |
| Nunavut | Imports | 252329 Cement 2.5 (0.5); 283325 Sulphates 1.1 (0.4); 252210 Quicklime 0.9 (0.3) |
