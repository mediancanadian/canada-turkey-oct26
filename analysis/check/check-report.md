# Week 03 fact-check: Canada-Türkiye strategic partnership

Checked 2026-10-23 by an independent checker. Every claim below was tested against the saved raw files, by re-running my own scripts on the raw data, or against the live official page where the saved copy was missing or empty.

My scripts are in ../check/scripts:
- chk_trade.py, chk_trade_hs6.py, chk_trade_misc.py
- chk_tariffs.py, chk_tariff_groups.py
- chk_energy.py
- chk_defence.py, chk_defence2.py
- chk_people.py, chk_people_tr.py
- chk_market.py

Verdicts:
- **OK**: reproduced or confirmed in the source.
- **ERROR**: wrong value or wrong statement.
- **UNVERIFIED**: rests on news or on a source that could not be read.
- **OVERSTATED**: stated more strongly than the source supports.

## Scorecard

| Thread | Claims checked | OK | ERROR | UNVERIFIED | OVERSTATED |
|---|---|---|---|---|---|
| Trade | 34 | 32 | 1 | 0 | 1 |
| Tariffs | 36 | 32 | 3 | 1 | 0 |
| Energy | 38 | 29 | 6 | 3 | 0 |
| Defence | 30 | 26 | 2 | 2 | 0 |
| People | 33 | 26 | 2 | 2 | 3 |
| Market | 36 | 30 | 1 | 2 | 3 |

## 1. Trade (trade/results.md)

Evidence:
- WDS cubes: trade/raw/wds/hs2_*.json and hs6_*.json
- Annual tables: trade/raw/x171/12100171.csv and trade/raw/x173/
- CPI: trade/raw/x005/18100005.csv
- Exchange rate: trade/raw/boc_FXAUSDCAD.json
- Mirror data: trade/raw/comtrade/
- Web pages: trade/raw/web/

| Claim | Verdict | Correct value / note | Evidence |
|---|---|---|---|
| Annual totals 1990-2025 (T1) | OK | All years reproduce to C$0.1M (checked 2010-2026 in full) | chk_trade.py |
| 2025 exports 1,137.4; dom 1,029.4; re-exp 108.0; imp 3,197.3; two-way 4,334.7; bal -2,060.0 | OK | Same | chk_trade.py |
| Jan-Aug 2026 vs 2025: exp +7.7%, dom +12.4%, re-exp -31.4%, imp -13.7%, two-way -8.6% | OK | Same | chk_trade.py |
| CAGR table, 5/10/15/25 years, incl. real CAGR and CPI rises 19.9% / 29.7% | OK | Same | chk_trade.py |
| 2020-2025 +40.6%; 2020-2024 +42.9% vs PMO "almost 50%" | OK | Same | chk_trade.py; raw/web/54d835a2.html |
| "Exports in 2025 were below their 2015 level (C$1,137.4M vs C$1,126.7M)" | ERROR | 2025 is 0.9% **above** 2015. Say "about the same as 2015" | chk_trade.py |
| Exports peaked in 2019 (C$1,616.1M) | OK | Same | chk_trade.py |
| Rank 27th, 0.28% of two-way trade (C$4.33B of C$1,566.9B) | OK | 27 of 256; 0.277% | chk_trade.py; 12100171.csv |
| Exports 31st 0.15%; imports 27th 0.41% | OK | Same | chk_trade.py |
| Neighbours 24-30 (Ireland to Bangladesh) | OK | Same | chk_trade.py |
| Rank over time 28/26/26/27; shares 0.23/0.29/0.28/0.28% | OK | Same | chk_trade.py |
| Reuters C$4.34B = US$3.10B at 1.3978 | OK | 3.10 | chk_trade_misc.py |
| GAC NAPCS figures (287, 273, 151, 1,270, 480, 316) | OK | Exact match to 12-10-0171 | chk_trade_hs6.py; raw/web/2a1087a0.html |
| 2024 NAPCS values; farm exports -45%; aircraft more than tripled | OK | 521.1 to 287.2; 84.4 to 273.4 | chk_trade_hs6.py |
| HS6 sums 1,120.7 exp / 3,197.1 imp; gap 16.7 | OK | Same | chk_trade_hs6.py |
| Top-15 concentration 64% / 75% exp, 28% / 32% imp | OK | 63.9 / 74.5 / 28.1 / 31.8 | chk_trade_hs6.py |
| Top 15 HS6 lists for exports and imports, 2024 and 2025 | OK | All values reproduce | chk_trade_hs6.py |
| Lentils 340.7 / 486.6 / 436.0 / 324.0 / 172.6 | OK | 2022 is 486.9 total (486.6 domestic). Trivial | chk_trade_hs6.py |
| Scrap 166.6 to 54.4; soybeans 113.2 to 19.3; aircraft 162.0 | OK | Same | chk_trade_hs6.py |
| Top 10 HS2 chapters, both flows | OK | Same | chk_trade_misc.py |
| Province table T4 (dom. exports, imports, 5-yr averages) | OK | Same | chk_trade_hs6.py |
| SK lentils by year; AB lentils 42.6; SK chickpeas 26.5; SK durum 22.1 | OK | Same | chk_trade_hs6.py |
| QC aircraft 162.0, QC scrap 29.2 (5-yr 116.4); ON 901380 50.8, 870390 29.0 | OK | Same | chk_trade_hs6.py |
| BC 841121 42.2; coal 37.4 (5-yr 78.0); NL vessel 79.2 | OK | Same | chk_trade_hs6.py |
| ON + QC cleared 80% of imports | OK | 79.9% | chk_trade_hs6.py |
| Doubling table (2x, C$10B, US$10B, US$5B; 5-yr and 10-yr rates) | OK | Same | chk_trade_misc.py |
| Doubling in about 12 years at 6.0% | OK | 11.9 years | chk_trade_misc.py |
| Import/export ratios by 5-year block and by year; 2025 highest since 1988 | OK | Same | chk_trade.py |
| Jan-Aug ratio 2.55 vs 3.18 | OK | Same | chk_trade.py |
| Mirror figures US$1,577.7M / 2,288.1M / 1,162.8M / 814.8M | OK | Same | raw/comtrade/total_r*_2025.json |
| Erdoğan target is "most likely US$" | OK | Labelled as an inference, as it should be | tariffs/raw/official/il_we-aim...txt |
| "'almost 50%' is generous" | OVERSTATED (tone) | Neutral version: "StatCan data show 41%" | |

## 2. Tariffs (tariffs/results.md)

Evidence:
- Outputs: tariffs/outputs/*.csv
- CBSA and SIMA: tariffs/raw/official/sima/*.txt, sima_mif_menu.txt, cn25-24-eng.html.txt, 1163.txt, sor2025-148.txt
- Turkish tariff: tariffs/raw/tr/rejim/I say*.xlsx, tariffs/raw/tr/xl/igv_EK-1.xlsx
- WTO: tariffs/raw/wto/

| Claim | Verdict | Correct value / note | Evidence |
|---|---|---|---|
| Canada MFN duty about CA$105.3M, 3.3% of CA$3,197.3M | OK | 105.3M, 3.29% | chk_tariffs.py |
| 10.0% on dutiable goods; dutiable value CA$1,053.4M | OK | Same | chk_tariffs.py |
| 67.1% of value duty-free | OK | 67.1% | chk_tariffs.py |
| Clothing 38.3M + carpets 14.1M is about half the duty | OK | 49.8% | chk_tariffs.py |
| Section 1b product-group table (19 rows) | OK | All values, free shares and duties reproduce | chk_tariff_groups.py |
| Tugs CA$2.8M; dairy CA$1.9M | OK | 2.85; 1.85 | chk_tariff_groups.py |
| Türkiye duty about CA$101.9M, 9.9% of CA$1,029.4M | OK | 101.9M, 9.90% | chk_tariffs.py |
| Durum gives about CA$37.2M | ERROR | **CA$37.5M** (28.82M x 130%) | chk_tariffs.py |
| Excluding durum CA$64.4M, 6.4% | ERROR | CA$64.4M is right, but the rate is **6.3%** | chk_tariffs.py |
| 45.3% of export value faces 0% | OK | 45.3% | chk_tariffs.py |
| Lentils CA$30.9M; chickpeas CA$3.5M; IGV part CA$9.0M | OK | Same | chk_tariffs.py |
| Lentils (red, green), chickpeas 19.3%; seed lines 0%; footnote 5 sets 10% to 2026-04-30 | OK | DÜ column | raw/tr/rejim List I, sheet 7.FASIL |
| Durum 130%, and the same 130% for EU/UK | OK | AB,BK and DÜ columns both 130 | List I, sheet 10.FASIL |
| Aircraft 2.7% with the civil end-use footnote; turboprops 0 or 3.6%; 8477.10 1.7% + IGV 5%; 8436.21 1.7% + IGV 15%; cocoa 8% | OK | Same | outputs/tr_2026_rates_DU_all.csv; igv_EK-1.xlsx |
| Cars (8703.90/.24/.23) CA$55.2M | ERROR | **CA$57.7M** domestic exports in these lines | chk_tariffs.py; domexports_to_TR_2025_hs8.csv |
| Other Turkish export values in the 2a table (162.0, 54.4, 50.8, 46.1, 37.4, 28.6/28.8, 19.3, 17.7, 12.5, 11.5, 5.8) | OK | Same | domexports_to_TR_2025_hs8.csv |
| IGV Ek-1 has about 4,600 rows | OK | 4,647 | igv_EK-1.xlsx |
| WTO simple average 17.3% (ag 39.9, non-ag 13.6) | OK | Same | raw/wto/TR_tariff_profile.pdf |
| 9 SIMA measures name Türkiye (8 steel, 1 pasta) | OK | CSWP3, RB1, COR2, DWP, HSS, OCTG2, OCTG5, SS, SW; page modified 2026-09-17 | sima_mif_menu.txt |
| "All others" rates: 41.0, 45.8, 26.1 + 200.46 TRY/t, 89, 37.4, 67.9, 47.9, 45.0, 99.9 + 0.09 TRY/kg | OK | All match | sima/*.txt |
| CITT dates: RB1 2026-06-02, OCTG2 2026-10-07 (Borusan excluded), OCTG5 2026-04-21, SS 2026-01-14, SW 2026-01-02, DWP 2024-03-20, CSWP3 2024-10-16 / 2026-03-27 | OK | Same | sima/*.txt; citt_*.html |
| HSS continued 2025-07-16 | OK | Saved .txt is empty; the live CITT page confirms | canada.ca CITT release (live) |
| COR2 continued by RR-2025-004 (July 2026) | UNVERIFIED | Saved cscb.ca copy is a Cloudflare challenge page. The CBSA COR2 page (modified 2025-08-22) and the CBSA initiation notice show only the 2025 initiation | tariffs/raw/official/tribunal-continues-finding...html; live CBSA cor22025-ni |
| COR3 (Türkiye) terminated 2025-07-16 | OK | Same | raw/official/menu-eng.html |
| Pasta SIMA duties CA$34,099 on CA$19.5M (2024) | OK | Same | sima_stats.txt |
| SIMA-listed lines CA$92.4M; TRQ classes CA$220.1M; pipe 52.4, plate 50.0 | OK | Same | outputs csv |
| TRQ: 50% surtax; quota cut to 20% (non-FTA) and 75% (non-CUSMA FTA); extended to 2027-06-27 | OK | Same | cn25-24-eng.html.txt |
| Türkiye not in Schedule 3 | OK | Not listed | sor2025-148.txt |
| Year 2 quarter dates; quota examples (rebar 13,445.1 t 29%, pipe 10,369.2 t 21%, coated 18,732.8 t 37%, plate 5,201.2 t 36%) | OK | Same | 1163.txt |
| Derivative surtax 25% from 2025-12-26; non-stackable; vehicle exemption to 2027-07-01 | OK | Same | cn25-33.txt |
| GPT withdrawn 2015-01-01 (SOR/2013-161 lists Turkey); CBSA shows MFN only | OK | Same | sor2013-161.txt; cbsa_countries2.txt |
| Türkiye has 22 FTAs, incl. EFTA, UK, Korea, Singapore, Malaysia, Chile | OK | The EC list counts Syria (suspended) among the 22 | raw/cu/policy...txt |
| Customs Union modernisation proposed Dec 2016; no negotiating directives | OK | Same | raw/cu/policy...txt |
| WTO TPR quote on "reluctant" RTA partners | OK | Same | raw/wto/tpr_s439_e.txt |
| CETA removes duties on 99% of lines | OK | Same | raw/cu/ec_ceta.html |
| Consultation ran 2026-07-31 to 2026-09-14; exploratory talks 2026-06-08; negotiations launched 2026-07-07 | OK | Same | Gazette notice .txt; consultation .txt; PMO 2026-07-07 .txt |
| DFATD Act s.10(2.1) supply-management text | OK | Same | g3-04801.txt |
| Erdoğan quote "$3 billion ... $5 billion ... $10 billion" | OK | Same | il_we-aim...txt |

## 3. Energy (energy/results.md and results-followup.md)

| Claim | Verdict | Correct value / note | Evidence |
|---|---|---|---|
| Oct 22 statement wording (LNG, civil nuclear, COP31 Antalya 9-20 Nov) | OK | Same | raw/pm_statement...html |
| Ministers' text "leverage Canada's growing LNG export capacity", "long-term off-takers"; no CANDU, Sinop or working group | OK | Same | raw/nrcan_jointstatement_newswire.html |
| EPDK 2025: consumption 59.07 bcm (+10.99%); production 3.11 bcm (2.81 Sakarya); imports 58.34 bcm (+11.73%) | OK | Same | raw/epdk/epdk2025.txt |
| Pipeline 41.25 (70.7%), 6.82 spot; LNG 17.09 (29.3%), 12.56 spot | OK | Same | epdk2025.txt |
| Import shares: Russia 36.3, Azerbaijan 20.4, US 16.2, Iran 13.2, Algeria 7.6, Nigeria 1.5, others 4.7, Canada 0 | OK | Same | EPDK Table 2.2 |
| "Others (LNG mostly)" | OK | Includes 465 mcm of Turkmen pipeline gas | EPDK Table 2.2 |
| Long-term LNG only from Algeria and Oman; US 75% of spot LNG, Nigeria 7%; 11 spot suppliers | OK | Same | epdk2025.txt |
| Storage 6.3 bcm and LNG storage 1.05 million m3 | OK | Same | epdk2025.txt |
| Energy balance: production 55,016; imports 128,437; exports 12,304; net imports 70.3% | OK | Same | raw/etkb/denge_2024_r1.xlsx |
| Energy bill US$62.47B; 17% of imports | OK | 62.466B; 17.1% | followup comtrade_TUR_WORLD_M_HS27_2025.json |
| Total 2025 imports "US$365.5 billion" | ERROR | **US$365.4B** (365.37, the same value in Comtrade and TurkStat 53911). The market thread uses 365.4 | market/raw/followup/press_53911_en.txt |
| Akkuyu: 4 units under construction; start dates; 1,114 MWe | OK | Same | raw/pris/reactors_TR.json |
| MENR PP: 66.25 / 79 / 85 / 95 / 100%; gas share of power 18.9% to 15% | OK | Same | raw/etkb/pp.txt |
| Akkuyu start-up Dec 2026, original target 2023, cost >US$20B, 12.35 c/kWh | UNVERIFIED | News only; already labelled | |
| PRIS world fleet: 417 operating, 78 under construction | OK | Same | raw/pris/world_statistics.json |
| 26 CANDU-design units operating (17 Canada, 9 abroad) | OK | Same | outputs/pris_summary.txt; nrcan html |
| "India runs 18 more PHWRs... That gives 46 PHWRs" | ERROR | 26 + 18 = 44. The 46 also counts Argentina's 2 Atucha units (Siemens KWU design). Add them, or drop the 46 | outputs/pris_summary.txt |
| LNG Canada Phase 1 14 MTPA; Woodfibre 2.1 MTPA (2027); Ksi Lisims 12 MTPA | OK | Same | raw/cer/snap_2024_lngfuture.html |
| Cedar LNG 3.3 MTPA | ERROR | CER says **3 MTPA**, in service late 2028 | snap_2024_lngfuture.html |
| First LNG exports June 2025 | OK | CER text, plus first Kitimat record 2025-06 | raw/cer/market-snapshot...2025.html |
| 2025 LNG exports 3.11 bcm, shares by destination | OK | Marine only. With truck exports to the US the total is 3.14 bcm (matches the CER xlsx). The US row (0.06) is marine only | chk_energy.py |
| Jan-Aug 2026 9.10 bcm; QINGCHENG records excluded | OK | 9.10 marine; 9.15 with trucks | chk_energy.py |
| Canada 2025 LNG is about 5% of Türkiye's gas imports | OK | 5.3% | chk_energy.py |
| Uranium 14.3 kt, 24% of world, about 90% exported, 2nd exporter, 33% of US purchases | OK | Same | raw/followup/nrcan_uranium...html |
| CER 16.9 kt is U3O8 (14,327 x 1.1792 = 16,895) | OK | Same | chk_energy.py |
| Canada 685 Mt; -10% vs 2005; -0.3% vs 2023; 17 t per person; oil and gas 30% | OK | Oil and gas 208 of 685 Mt = 30% | followup/CAN_NIR_2026_partA_ec2d.pdf |
| Türkiye 584.5 Mt (+5.3%), 6.8 t per person, energy 71.8% | OK | Excludes LULUCF; 517.4 Mt with LULUCF | followup/TUR_NIR_2026_p1-40.txt; ghg/eb2c2d.html |
| "A Canadian emits about 2.5 times" (results.md) | ERROR | **2.4x** (16.6 / 6.83). The follow-up fixes it; results.md still says 2.5 | chk_energy.py |
| "643 Mt cap is above 2024 level of 584.5 Mt" (results.md) | ERROR | Mixes bases. The NDC is net (incl. LULUCF): compare with 517.4 Mt, a rise of about 24%. Fixed in the follow-up, not in results.md | followup/TUR_NDC3_2035.txt |
| Coal (2701) values and tonnes, 2022-2025, USD | OK | Same | raw/comtrade/*.json; followup comtrade_CAN_TUR_X_*.json |
| CAD conversion table 2015-2025 | OK | Spot-checked 2023 and 2025 | followup/comtrade + BoC |
| "Coal is 97 to 100% of HS 27 in every year except 2024" | ERROR | 2023: 96.2%; 2025: 94.2% | followup comtrade_CAN_TUR_X_2023/2025.json |
| No 284410 or 284420 uranium exports | OK | Only 284440 appears | followup HS6 files |
| Chromium 9,300 / 9,000 kt, 2nd, world 51,000 kt, reserves 27,000 kt | OK | Same | raw/minerals/mcs2026-chromium.txt |
| Boron 950 Mt reserves; "73%" not usable | OK | Same | mcs2026-boron.txt |
| Gazprom extension, Iran contract expiry, 1,500 US cargoes, East Canada LNG | UNVERIFIED | News only; already labelled | |
| Beylikova 694 Mt is an ore tonnage, not a reserve | OK | Correctly caveated | |

## 4. Defence (defence/results.md and results-followup.md)

| Claim | Verdict | Correct value / note | Evidence |
|---|---|---|---|
| Values 2010-2025 (4.34 ... 60.76M) | OK | All match the report tables | defence/raw/reports/*.txt |
| Ranks 2010-2022 (19, 24, 20, 29, 26, 22, 25, 5, 3, 3, 3, 39, 62) | OK | Reproduced from each destination table | chk_defence.py and inline parses |
| 2023 rank 60 | ERROR | **61** (Table 6; the thread's own outputs/table6_ranks.json also says 61) | chk_defence2.py |
| 2024 rank 4 (4.3%); 2025 rank 7 (3.0%) | OK | 4.31%; 2.97% | chk_defence2.py; 2025 Table 3 |
| Shares 2010-2023 | OK | Same, within rounding | outputs csv |
| ECL 2-5 / 2-15 values by year | OK | Same | outputs csv |
| 2025: 3 denials, 20 permits utilized, 17 issued, brokering CA$125M (2-3, Türkiye origin, Ukraine) | OK | Same | report_2025.html.txt lines 257-259, 495, 602, 740 |
| Oct 2019 suspension; Apr 16 2020 presumptive denial; Oct 5 2020 investigation | OK | Same | rep_2020.txt p.11-12 |
| 29 permits cancelled; 6 Group 2 applications denied in 2021 | OK | Same | rep_2020.txt l.492; rep_2021.txt l.455, 571 |
| Review: "credible evidence"; Bayraktar TB2; WESCAM; surveillance and targeting in Syria | OK | Same | raw/review.txt |
| Notice 1108: issued 2024-01-23, modified 2024-01-29; "no longer in place"; "excepting Ukraine" | OK | Same | gac_notice_1108.html(.txt) |
| No official link to the Sweden ratification | OK | Correctly labelled as reported | |
| Joint statement defence quotes; DSRB nine leaders | OK | Same | pmo_joint_statement_20261022.html.txt; pmo_dsrb_declaration...txt |
| NATO core % GDP: Canada 1.41 / 2.03 / 2.13, Türkiye 2.08 / 2.33 / 2.85; NATO 2.86, Europe and Canada 2.53 | OK | Read from the Table 3 image | raw/nato_pages/p-07.png |
| Real change 2026e +5.95% / +25.86% | OK | Same | p-07.png |
| Personnel 70.6 / 77.1k and 343.9 / 395.8k | OK | Same | p-11.png |
| "US$10.054 billion, about 48% above 2024 (US$7.1 billion)" | ERROR | 10.054 / 7.1 = **+41.6%**. The 48% is the TİM basis (10.016 / 6.735 = +48.7%). Do not mix the two sources | defence/raw/ikv.txt; TİM xlsx |
| TİM 2024 6.735B; 2025 10.016B (+48.7%); Jan-Sep 2026 6.926B (+15.6%); 4.2% of exports; Dec 2.571B | OK | Same | followup/tim_*.xlsx |
| SSB US$10.054B figure | UNVERIFIED | News (Anadolu via istiklal) only | |
| Armenian motion vote 153 to 68 | UNVERIFIED | The saved Hansard shows the motion carried; the vote count is news only | openparl_20040421*.html |
| FAAE Report 9 quotes ("default toward hesitance", Wescam "still approved") | OK | Same | followup/faae_report9_2021.txt |
| Section title "tested trust" | Wording | Editorial frame. Suggest "Defence ties and past export restrictions" | |

## 5. People (people/results.md and results-followup.md)

| Claim | Verdict | Correct value / note | Evidence |
|---|---|---|---|
| Census: 76,745 / 40,925 / 35,820; born in Türkiye 43,130; mother tongue 51,010 (44,190 single); home 57,610 | OK | Same | raw/wds_98100*.json |
| Province and CMA table | OK | Matches outputs/census_turkish_by_geo.csv, built from the WDS files | |
| Period of immigration rows; 2016-2021 is 29% of immigrants | OK | 28.8% | wds_98100302_pob_turkey.json |
| PR by year and rank (870 ... 4,420; ranks 51 ... 14) | OK | Ranks identical. Counts within ±5 from rounded cells (e.g. 2017 1,115 vs 1,110) | chk_people.py |
| 2026 monthly PR values | OK | Same | chk_people.py |
| PR by category (protected persons, economic, family) | OK | Same | chk_people.py |
| New citizens 3,335 / 4,335 / 2,900 / 1,675 and ranks 29 / 17 / 21 / 29 | OK | Same | chk_people.py |
| Study, IMP, TFWP holders and ranks | OK | Same | outputs/temp_residents_turkey.json; ircc xlsx |
| Asylum 265 ... 390; rank caveat | OK | Same | ircc/asylum_top25_lastyear.xlsx |
| Fall of about 86%, 2022 to 2025 | OK | 86.4% | |
| IRB table (2019, 2022-2026) | OK | Same | raw/irb/rpd_*.html |
| Visas 21,695 / 19,155 / 12,770 / 8,645 and ranks 14 / 13 / 15 / 16; -41% | OK | Same | chk_people.py |
| Visitors from Türkiye by year; Jan-Aug +8.1%; 0.09% of 29.6M | OK | Same | outputs/travel_results.json |
| "Visits from Türkiye are at a record high (27,274 in 2025)" | OVERSTATED | Verified only as the highest since 2015 (the series pulled starts in 2015) | travel_results.json |
| Canadian arrivals in Türkiye and ranks 2015-2025 | OK | All reproduced | chk_people_tr.py |
| Record 321,271 in 2025 | OK | Highest in the 2010-2025 bulletin | sinir_2025.xlsx |
| 12 weekly flights per country; 9 east and 3 west | OK | A-2025-25 / A-2025-77 text (A-2024-140 itself was not saved) | raw/followup/a-2025-*.html |
| "Canadian airlines and airports opposed" (results.md lines 274-275 and 295) | ERROR | ADM and GTAA **supported**. Only Air Canada and Air Transat opposed. The follow-up fixes it; results.md still has the error | followup/a-2025-25.html |
| "21 is not confirmed by a Canadian official source" (results.md line 296) | ERROR (outdated) | PMO release (2026-10-23) and PM remarks (2026-10-22) say 12 to "up to 21" | followup/pmo_release_2026-10-23.html |
| Use Canada's wording "up to 21" | OK | Same | |
| CTA rulings A-2024-45, A-2025-25, A-2025-77, A-2026-59: dates and outcomes | OK | Same | followup/a-*.html |
| Air Transat: Toronto 3 weekly; Montréal 2 weekly from 2026-10-29 (A330) | OK | Same | Transat release 124611 (live) |
| Turkish Airlines 15 weekly in summer 2026; "direct flights already exceed the old 12 cap" | OVERSTATED | Trade press only; no CTA ruling found | |
| Work permit split: +18,315; 62% / 38%; earthquake window about 12,510 | OK | Same | outputs/work_permit_split_turkey.json |
| "Job-offer permits barely moved" | OVERSTATED | TFWP holders went from 145 to 230 to 180 to 175. Small in count, but the 2022 level was +59% on 2021. "Stayed small (under 300)" is safer | |
| Order in Council 2026-0976 | UNVERIFIED | Bloomberg Tax lead only | |
| Earthquake link to the IMP spike | UNVERIFIED | Timing inference only; correctly labelled | |

## 6. Market (market/results.md and results-followup.md)

| Claim | Verdict | Correct value / note | Evidence |
|---|---|---|---|
| Türkiye population 86,092,168; median age 34.9; 93.6% urban; Istanbul 15.75M | OK | TurkStat release | followup/press_53899_en.txt |
| Fertility 1.42; Gini 0.410; top 20% 48.0% | OK | Same | press_58018 / 53993 |
| Projections 88.19M (2030) / 93.77M (2050) | OK | Same | press_53699 |
| Canada 41,798,407 (2026-07-01); +0.46%; fertility 1.26 | OK | Same | raw/statcan/17100009.csv, 13100418.csv |
| Mid-2026 86.3M | UNVERIFIED | News only | |
| IMF: GDP, per person, PPP, growth, unemployment, current account | OK | Same | outputs/imf_weo_oct2026_tur_can.csv; raw/imf |
| Ratios 2.99 (nominal) and 1.52 (PPP); PPP per person is two thirds | OK | 0.66 | chk_market.py |
| IMF inflation 31.2% (2026) and 26.5% (2027) vs Canada 2.8% | OK | Same | raw/imf/PCPIPCH.json |
| World Bank GNI 16,300 / 56,420; consumption 873.8 / 1,294.1; per person 10,181 / 31,107; Gini 43.7 / 31.5; urban 89.5 / 82.9 | OK | Same | raw/wb/*.json |
| Minimum wage net TRY 28,075.50 = CAD 848 / 795 | OK | Same | chk_market.py |
| Türkiye imports US$365.4B (344.0 in 2024) | OK | Same | raw/comtrade |
| Canada 0.32%, 47th | ERROR (method) | 0.32% is right. 47th holds only if "Other Asia, nes" (Taiwan) counts as a country. The stated rule ("excluding Special Categories and areas nes") gives **46th**; Australia 57th, not 58th. Fix the note or the rank | chk_market.py |
| 2024 Canada US$1.22B (0.35%) | OK | Same | chk_market.py |
| USA 4th (4.95%); UK 11th (1.99%) | OK | Same | chk_market.py |
| HS2 shares (energy 17.1, machinery 11.4, vehicles 10.1, ...) | OK | Same | outputs/tur_imports_2025_hs2_world.csv |
| Canada's mix (HS07 15.9, HS88 15.0, ...) | OK | Same | outputs/tur_imports_2025_hs2_canada.csv |
| BEC 68.4 / 15.0 / 16.2 | OK | Same | followup/press_53911_en.txt |
| CPI 10.35 / 85.51 (Oct 2022) / 64.77 / 75.45 / 30.89 / 29.73 | OK | Same | outputs/tur_cpi_monthly_tcmb.csv |
| Prices rose about 13.3x, Dec 2017 to Sep 2026 | OK | 13.33 | chk_market.py |
| Policy rate 36% from 2026-10-23; peak 50%; 8.5% in Feb 2023 (inflation 55%) | OK | Same | outputs csv; raw/tcmb/policy_rate.html |
| Lira loss vs CAD: 15.0% (1 year), 78.0% (5 years), 93.4% (10 years); x4.5 and x15.3 | OK | 10-year figure uses the legacy noon rate 0.4317 CAD/TRY on 2016-10-21 | raw/boc/*.json |
| Annual TRY per CAD averages | OK | Same | outputs/fx_try_per_cad_annual.csv |
| Current account US$30.1B (IMF) / 30.276B (TCMB); 12-month US$42.1B; Aug surplus US$4.05B | OK | Same | followup/tcmb PDF |
| External debt 539.0 / 170.7 / 197.9 / 318.0; currency mix 48.9 / 28.8 / 12.2; about 30% of GDP | OK | 29.6% | raw/tcmb/developments_external_debt.pdf |
| Ratings BB- / Ba3 / BB-, stable; three notches below investment grade | OK | Treasury page (modified 2026-04-14) | followup/hmb_credit_ratings.json |
| Canada AAA / Aaa / AA+ / AAA | OK | Same | raw/finance_canada/seu2026_annex3... |
| Fitch "affirmed July 2026" (results.md) | UNVERIFIED | News only. The follow-up says the outlook was cut from Positive to Stable in April 2026 (also news). Use the follow-up wording or no date | |
| FDI stocks 992 (2022), 4,126 (2024), 3,315 (2025); -19.7%; 3.3x; Türkiye in Canada 233 | OK | Same | raw/statcan/36100008.csv |
| GAC "steady decline" not supported | OK | Correct reading | trade/raw/web/2a1087a0.html |
| Eldorado 168,701 + 72,482 of 488,268 oz = 49.4% | OK | Same | raw/company/eldorado_q4_2025.txt |
| Alamos: Dutch BIT; registered 2021-06-07; decision 2025-06-18; suspended 2025-07-02; US$470M sale | OK | Same | raw/icsid/case_ARB-21-33.html; raw/company/alamos_*.pdf |
| "The largest recent Canadian mining dispute ended in a sale under arbitration" | OVERSTATED | The case is suspended, not ended ("Pending"), and will be discontinued only after milestones | ICSID page |
| Tax treaty signed 2009-07-14; in force 2011-05-04; applies from 2012-01-01 | OK | Same | Finance Canada notice (live) |
| No Canada-Türkiye investment treaty in force | OK | Same. UNCTAD page 648 could not be opened (permission timed out) | UNCTAD Türkiye list (thread copy) |
| FTA notice of intent 2026-09-21; consultations 2026-07-31 to 2026-09-14 | OK | Same | raw/gac/gac_canada_turkiye_fta_status.html |
| "85 million consumers pitch" heading | Wording | Population is 86.1M. Fine if it quotes the pitch; otherwise use 86 million | |

## 7. Inconsistencies between threads

| Item | Where | Issue | Fix |
|---|---|---|---|
| Türkiye total imports 2025 | Energy 365.5 vs market 365.4 | Rounding error in energy | Use US$365.4B |
| Canada's exports to Türkiye, 2025 | Trade C$1,137.4M (total) and US$814.8M (Canada-reported); tariffs C$1,029.4M (domestic); market US$1.16B (Türkiye-reported CIF) | Three different bases appear across the threads | Label each one: "Türkiye's records" vs "Canada's records", and total vs domestic exports |
| Canada LNG 2025 | Energy 3.11 bcm (marine) vs CER xlsx 3.14 bcm | Basis difference, already noted | Say "about 3.1 bcm" |
| Per-person emissions ratio | Energy results 2.5 vs follow-up 2.4 | Unrounded figures give 2.4 | Use 2.4 |
| Türkiye defence exports | Defence results (SSB 10.054 vs 7.1, "48%") vs follow-up (TİM 10.016 vs 6.735, 48.7%) | Growth rate taken from the other source | Use TİM throughout |
| Flights 12 to 21 | People results ("not confirmed") vs follow-up (PMO confirms) | results.md is out of date | Use the follow-up |
| Exports doubling target | Trade and tariffs both treat $3B/$10B as probably US$ | Consistent; inference only | Keep "currency not stated" |
| FTA dates | Tariffs, market and trade | Consistent: exploratory 2026-06-08, launch 2026-07-07, notice 2026-09-21 | None |

## 8. Errors that must be fixed

1. **Trade:** 2025 exports (C$1,137.4M) are slightly **above** 2015 (C$1,126.7M), not below. Say "about the same".
2. **Tariffs:**
   - Durum duty is CA$37.5M, not 37.2M.
   - The ex-durum rate is 6.3%, not 6.4%.
   - Car exports (8703.90/.24/.23) were CA$57.7M, not 55.2M.
3. **Tariffs:** the COR2 continuation (RR-2025-004, July 2026) is unverified. The saved source is a Cloudflare page. Confirm on citt-tcce.gc.ca, or say "expiry review under way".
4. **Energy:**
   - Total imports are US$365.4B, not 365.5B.
   - Cedar LNG is 3 MTPA (CER), not 3.3.
   - 26 + 18 = 44, so "46 PHWRs" needs Argentina's 2 Atucha units named.
   - Coal is 94 to 100% of HS 27 (2023: 96%; 2025: 94%), not "97 to 100%".
5. **Energy (results.md):** use the per-person ratio of 2.4, not 2.5. Compare the 643 Mt NDC cap with the net 517.4 Mt (about +24%), not with the gross 584.5 Mt.
6. **Defence:**
   - The 2023 rank is 61, not 60.
   - "US$10.054B, about 48% above US$7.1B" is wrong: that is +41.6%. Use TİM's US$6.73B to US$10.02B (+48.7%).
7. **People (results.md):**
   - Airports did not oppose; ADM and GTAA supported, and only Air Canada and Air Transat opposed.
   - The 21-flight figure is now confirmed by the PMO; use "up to 21".
8. **Market:** with the stated exclusion rule, Canada is 46th, not 47th. It is 47th only if "Other Asia, nes" (Taiwan) is counted; say which.
9. **Overstated wording to soften:**
   - "record" visits from Türkiye: say "highest since 2015".
   - "flights already exceed the 12 cap": trade press only.
   - "Alamos dispute ended": it is suspended.
   - "job-offer permits barely moved": say "stayed under 300".
   - "almost 50% is generous": say "StatCan shows 41%".
   - Defence title "tested trust".
10. **News-only numbers to label in the post:**
    - Akkuyu timeline and cost.
    - Gazprom and Iran contracts, and the US LNG cargoes.
    - SSB US$10.054B.
    - The 153 to 68 vote.
    - Fitch, Moody's and S&P action dates.
    - Turkish Airlines frequencies.
    - OIC 2026-0976.
    - The mid-2026 population of 86.3M.

Blocked during this check:
- UNCTAD treaty page 648 (WebFetch permission timed out).
- CBSA COR2 measure page (WebFetch permission timed out). The CBSA COR2 initiation notice was read live.
