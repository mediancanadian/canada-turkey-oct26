# Canada and Türkiye: people and travel links (research thread)

Prepared 2026-10-23. All sources accessed 2026-10-23 unless noted. Raw files, scripts and outputs are in ../people (raw/, scripts/, outputs/, manifest.json with SHA-256 of every file).

Context: the 2026-10-22 joint statement by Prime Minister Carney and President Erdoğan commits to "ratify the Canada-Türkiye Air Transport Agreement", "strengthen cooperation on consular issues and migration", "explore measures to facilitate travel and mobility" and "support cultural exchanges and diaspora engagement". Source: https://www.pm.gc.ca/en/news/statements/2026/10/22/statement-prime-minister-carney-and-president-recep-tayyip-erdogan

## Data rules to carry into the post

- IRCC open data: values 0 to 5 are shown as "--" (suppressed); all other values are rounded to the nearest 5, so parts may not sum to totals. Category totals below are sums of rounded monthly cells and are approximate. The visitor visa file uses a slightly different rule: counts 1 to 4 suppressed, 0 and 5 shown as reported, others rounded to 5. IRCC 2026 figures are January to August only and preliminary.
- 2021 Census: StatCan randomly rounds counts to multiples of 5. Ethnic origin, place of birth and the immigration tables come from the long-form (25% sample) questionnaire. Mother tongue and home language are short-form (100%).
- Ethnic origin "Turkish" is self-reported ancestry. Place of birth "Turkey" counts everyone born there, whatever their ethnicity (for example Kurdish, Armenian or Assyrian people born in Türkiye are included).
- IRCC and StatCan files still label the country "Turkey". Türkiye's border bulletins count people by nationality (passport), not by where they live.

## 1. Turkish Canadians, 2021 Census

Sources:
- Ethnic origin: Table 98-10-0356-01, https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810035601
- Place of birth by period of immigration: Table 98-10-0302-01, https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810030201
- Mother tongue: Table 98-10-0181-01, https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810018101
- Language spoken at home: Table 98-10-0201-01, https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810020101

All data came from the StatCan WDS API. The tidy table is outputs/census_turkish_by_geo.csv.

| Geography | Turkish origin (total) | Single origin | Born in Türkiye | Turkish mother tongue | Turkish spoken at home |
|---|---|---|---|---|---|
| Canada | 76,745 | 40,925 | 43,130 | 51,010 | 57,610 |
| Ontario | 43,555 | 24,340 | 25,995 | 30,725 | 34,620 |
| Quebec | 15,620 | 7,765 | 8,340 | 9,500 | 10,970 |
| British Columbia | 8,075 | 4,020 | 4,250 | 5,530 | 6,085 |
| Alberta | 6,670 | 3,565 | 3,135 | 3,860 | 4,310 |
| Manitoba | 885 | 300 | 335 | 335 | 370 |
| Saskatchewan | 695 | 430 | 310 | 365 | 455 |
| Nova Scotia | 665 | 305 | 455 | 400 | 455 |
| New Brunswick | 320 | 90 | 165 | 135 | 150 |
| N.L. | 160 | 45 | 85 | 75 | 95 |
| P.E.I. | 50 | 30 | 30 | 75 | 80 |
| Toronto CMA | 28,490 | 16,650 | 18,135 | 21,030 | 23,995 |
| Montréal CMA | 13,895 | 7,140 | 7,735 | 8,765 | 10,170 |
| Vancouver CMA | 6,300 | 3,360 | 3,505 | 4,775 | 5,330 |
| Ottawa-Gatineau CMA | 4,805 | 2,385 | 2,435 | 3,140 | 3,365 |
| Edmonton CMA | 3,430 | 2,040 | 1,765 | 2,070 | 2,300 |
| Calgary CMA | 2,695 | 1,375 | 1,230 | 1,635 | 1,805 |
| Kitchener-Cambridge-Waterloo CMA | 2,375 | 1,470 | 1,480 | 1,915 | 2,085 |
| Hamilton CMA | 2,275 | 1,135 | 1,195 | 1,490 | 1,670 |

Notes on the table:
- Multiple-origin responses for Turkish in Canada: 35,820.
- "Born in Türkiye" includes immigrants, non-permanent residents and non-immigrants.
- Mother tongue counts single and multiple responses together (single responses only: 44,190).
- "Spoken at home" counts Turkish spoken most often or regularly at home.
- The territories each have 25 or fewer people in any of these columns.

Born in Türkiye, Canada, by immigrant status and period of immigration (98-10-0302-01):

| Group | Count |
|---|---|
| Total born in Türkiye | 43,130 |
| Immigrants | 35,270 |
| Arrived before 1980 | 3,140 |
| 1980 to 1990 | 3,145 |
| 1991 to 2000 | 6,495 |
| 2001 to 2010 | 8,950 |
| 2011 to 2015 | 3,390 |
| 2016 to 2021 | 10,150 |
| Non-permanent residents (May 2021) | 7,175 |
| Non-immigrants (born Canadian citizens abroad) | 685 |

The 2016 to 2021 period (about 5.4 years) has the most arrivals of any period. It accounts for 29% of all immigrants born in Türkiye. In Toronto CMA, 4,540 of 14,405 immigrants born in Türkiye arrived in 2016 to 2021, and 3,540 non-permanent residents were born in Türkiye.

## 2. New permanent residents from Türkiye, 2015 to 2026

Source: IRCC, "Permanent Residents: Monthly IRCC Updates", Canada: Permanent Residents by Country of Citizenship (data to August 2026; dataset modified 2026-10-20), https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP-PR-Citz.xlsx. Catalogue page: https://open.canada.ca/data/en/dataset/f7e5498e-0ad8-4417-85c9-9b8aff9b9eda

Rank is computed among about 219 citizenship rows, excluding "Not stated" (outputs/pr_turkey_by_year.csv).

| Year | New PRs, citizens of Türkiye | Rank | Share of all PRs |
|---|---|---|---|
| 2015 | 870 | 51 | 0.32% |
| 2016 | 920 | 48 | 0.31% |
| 2017 | 1,110 | 41 | 0.39% |
| 2018 | 2,080 | 32 | 0.65% |
| 2019 | 2,830 | 26 | 0.83% |
| 2020 | 2,120 | 18 | 1.15% |
| 2021 | 4,625 | 17 | 1.14% |
| 2022 | 2,420 | 35 | 0.55% |
| 2023 | 2,070 | 35 | 0.44% |
| 2024 | 2,450 | 35 | 0.51% |
| 2025 | 1,895 | 37 | 0.48% |
| 2026 Jan to Aug | 4,420 | 14 | 1.68% |

The 2026 monthly figures rise sharply: Jan 160, Feb 210, Mar 260, Apr 235, May 385, Jun 830, Jul 920, Aug 1,425. All of these are rounded.

By immigration category, from https://www.ircc.canada.ca/opendata-donneesouvertes/data/ODP-PR-Citz_immcat.csv. These are sums of rounded monthly cells, so they are approximate. Each year also has 23 to 55 suppressed cells, which are counted as 0 here.

| Year | Protected persons in Canada | Economic (all) | Sponsored family |
|---|---|---|---|
| 2019 | 1,805 | 650 | 250 |
| 2021 | 3,000 | 1,120 | 290 |
| 2023 | 785 | 860 | 325 |
| 2024 | 1,225 | 680 | 425 |
| 2025 | 995 | 510 | 275 |
| 2026 Jan to Aug | 3,725 | 390 | 215 |

Most of the 2026 increase is people already in Canada whose refugee claims were accepted and who then became permanent residents (protected persons). It is not new economic immigration. See section 3 for the IRB decisions behind this.

Province of intended destination: IRCC's open data does not cross citizenship with province or CMA, so there is no breakdown of Türkiye-citizen PRs by destination. The 2021 Census place-of-birth table in section 1 is the best official substitute.

New citizens born in Türkiye. Source: IRCC Operational Processing, https://www.ircc.canada.ca/opendata-donneesouvertes/data/Open%20Data%20-%20New%20Citizens%20by%20COB%20en.xlsx

| Year | New citizens | Rank |
|---|---|---|
| 2023 | 3,335 | 29 |
| 2024 | 4,335 | 17 |
| 2025 | 2,900 | 21 |
| 2026 Jan to Aug | 1,675 | 29 |

## 3. Temporary residents and asylum

Sources (all accessed 2026-10-23):
- Study permit holders, catalogue page: https://open.canada.ca/data/en/dataset/90115b00-f9b8-49e8-afa3-b4cff8facaee
- Study permit holders on Dec 31: https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP_annual-TR-Study-IS_CITZ_year_end.xlsx
- Study permits by year effective: https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP-TR-Study-IS_CITZ_sign_date.xlsx
- Work permit holders, catalogue page: https://open.canada.ca/data/en/dataset/360024f2-17e9-4558-bfc1-3616485d65b9
- All IMP work permit holders on Dec 31: https://www.ircc.canada.ca/opendata-donneesouvertes/data/en_odp_annual-tr-work-imp_citz_year_end_all_purpose.xlsx
- TFWP work permit holders on Dec 31: https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP_annual-TR-work-TFW_CITZ_year_end.xlsx
- IMP permits by year effective: https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP-TR-Work-IMP%20CITZ.xlsx
- TFWP permits by year effective: https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP-TR-Work-TFWP%20CITZ.xlsx

Ranks are among all citizenships.

Permit holders who are citizens of Türkiye, valid on December 31 (the year-end files only go to 2024):

| Year | Study permit (rank) | IMP work permit, all purposes (rank) | TFWP work permit (rank) |
|---|---|---|---|
| 2015 | 2,195 (21) | 1,145 (41) | 60 (64) |
| 2016 | 2,840 (19) | 1,680 (33) | 70 (46) |
| 2017 | 3,785 (18) | 3,440 (22) | 105 (41) |
| 2018 | 4,315 (16) | 4,755 (20) | 120 (43) |
| 2019 | 4,685 (16) | 6,060 (20) | 140 (44) |
| 2020 | 3,535 (19) | 5,800 (18) | 145 (43) |
| 2021 | 4,775 (19) | 4,995 (20) | 145 (49) |
| 2022 | 4,890 (22) | 9,185 (18) | 230 (49) |
| 2023 | 5,725 (26) | 24,740 (11) | 180 (70) |
| 2024 | 4,650 (30) | 27,500 (12) | 175 (72) |

People whose permits became effective in each year:

| Year | Study (rank) | IMP (rank) | TFWP |
|---|---|---|---|
| 2015 | 1,615 (19) | 375 (48) | 30 |
| 2019 | 3,245 (16) | 1,085 (37) | 110 |
| 2022 | 3,190 (23) | 1,615 (32) | 165 |
| 2023 | 4,165 (25) | 10,640 (14) | 270 |
| 2024 | 2,445 (30) | 4,620 (26) | 85 |
| 2025 | 2,545 (28) | 1,425 (41) | 100 |
| 2026 Jan to Aug | 1,695 (28) | 1,795 (37) | 70 |

Things to keep in mind when using these figures:
- The "all purposes" IMP file includes permits that are not for a job offer. IRCC publishes a separate "for work purposes only" version. I did not download it because the connection was reset, so I cannot say how much of the 2023 to 2024 jump is refugee-claimant or humanitarian permits.
- In 2023, IRCC ran temporary special measures for Turkish and Syrian nationals after the February 2023 earthquakes, extended to January 3, 2024. Page dated 2023-10-03, modified 2026-05-01: https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/operational-bulletins-manuals/updates/2023-earthquakes-turkiye-syria.html. The 2023 IMP spike happened at the same time. No IRCC file links the two directly.
- Study permit holders from Türkiye fell from 5,725 (2023) to 4,650 (2024). Over the same period the national total fell only from 1,037,165 to 996,375 after the 2024 study permit cap. Türkiye's rank fell from 16th (2018 to 2019) to 30th (2024).

Asylum claimants who are citizens of Türkiye. Source: IRCC, Asylum Claimants: Monthly IRCC Updates (data to August 2026; dataset modified 2026-10-22), https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP-Asylum-Top_25_CITZ_Office_Type_last_year.xlsx. Catalogue page: https://open.canada.ca/data/en/dataset/b6cbcf4d-f763-4924-a2fb-8cc4a06e3de4

| Year | Claimants | All countries | Rank* |
|---|---|---|---|
| 2015 | 265 | 16,040 | 10 |
| 2016 | 1,100 | 23,835 | 4 |
| 2017 | 2,200 | 50,360 | 4 |
| 2018 | 1,845 | 55,015 | 7 |
| 2019 | 2,025 | 64,010 | 8 |
| 2020 | 570 | 23,680 | 9 |
| 2021 | 1,770 | 24,870 | 5 |
| 2022 | 9,465 | 91,645 | 3 |
| 2023 | 6,365 | 143,315 | 4 |
| 2024 | 2,690 | 171,870 | 13 |
| 2025 | 1,285 | 113,105 | 20 |
| 2026 Jan to Aug | 390 | 37,775 | 20 |

*The rank is computed only among the 25 countries in IRCC's 2025 top-25 file, so ranks for earlier years are among those 25, not among all countries. IRCC ranks Türkiye 20th for 2025.

IRB Refugee Protection Division decisions on claims where Türkiye is the country of alleged persecution. Sources: https://www.irb-cisr.gc.ca/en/statistics/protection/Pages/RPDStat2015.aspx to RPDStat2026.aspx (2026 data to June 30). Output file: outputs/irb_turkiye_rates.json.

| Year | Referred | Accepted | Rejected | Acceptance rate (accepted / finalized) | All-country acceptance rate | Pending at year end |
|---|---|---|---|---|---|---|
| 2019 | 1,939 | 2,043 | 66 | 94.4% | 58.9% | 1,696 |
| 2022 | 5,611 | 1,355 | 27 | 93.4% | 62.2% | 5,386 |
| 2023 | 9,413 | 4,943 | 95 | 94.0% | 71.8% | 9,533 |
| 2024 | 3,401 | 4,866 | 184 | 89.2% | 63.3% | 7,435 |
| 2025 | 1,337 | 4,057 | 227 | 87.5% | 63.0% | 4,106 |
| 2026 to Jun 30 | 248 | 922 | 104 | 76.9% | 44.3% | 3,156 |

"Finalized" also includes abandoned and withdrawn claims.

IRB figures are not rounded the way IRCC's are. IRB counts claims referred to it; IRCC counts claimants. The two series measure different things and should not be mixed.

How to read this neutrally: claims from Türkiye peaked in 2022 and 2023 and have fallen about 86% from 2022 to 2025 (IRCC series). Acceptance rates have been well above the all-country average throughout. The accepted cases now feed the 2026 rise in protected-person PRs (section 2).

## 4. Visitors

Visa rules: citizens of Türkiye need a visitor visa. The canada.ca entry requirements page (modified 2026-07-31) lists Türkiye among visa-required countries. Türkiye is not on the list of visa-required countries whose citizens may get an eTA instead when flying, which has 17 countries: Antigua and Barbuda, Argentina, Brazil, Costa Rica, Indonesia, Malaysia, Mexico, Morocco, Panama, Philippines, St. Kitts and Nevis, St. Lucia, St. Vincent and the Grenadines, Seychelles, Thailand, Trinidad and Tobago, Uruguay. Source: https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada/entry-requirements-country.html. The idea that some Turkish citizens qualify for an eTA is not supported by the current official page.

Visitor visas (V-1 counterfoil only) approved for citizens of Türkiye. Source: IRCC Operational Processing, https://www.ircc.canada.ca/opendata-donneesouvertes/data/Open%20Data%20-%20OPS%20TRV%20V-1%20Approved%20en.xlsx. Data as of September 1, 2026.

| Year | Visas approved | Rank | All countries |
|---|---|---|---|
| 2023 | 21,695 | 14 | 1,757,430 |
| 2024 | 19,155 | 13 | 1,458,045 |
| 2025 | 12,770 | 15 | 1,048,125 |
| 2026 Jan to Aug | 8,645 | 16 | 816,745 |

The file counts visas issued, not visits. IRCC does not publish applications or refusal rates by country in this file, so approval rates cannot be calculated from it.

Residents of Türkiye entering Canada. Source: StatCan Table 24-10-0050-01, Non-resident visitors entering Canada, by country of residence (vector v1277195166), https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2410005001

| Year | Visitors (residents of Türkiye) |
|---|---|
| 2015 | 19,638 |
| 2016 | 24,181 |
| 2017 | 23,478 |
| 2018 | 22,599 |
| 2019 | 25,211 |
| 2020 | 5,565 |
| 2021 | 7,139 |
| 2022 | 11,798 |
| 2023 | 23,399 |
| 2024 | 20,709 |
| 2025 | 27,274 |
| 2026 Jan to Aug | 20,104 |

2026 January to August is up 8.1% on January to August 2025 (18,596). Residents of Türkiye were 0.09% of all 29.6 million non-resident visitors in 2025.

Canadians visiting Türkiye, from two official sources that measure different things:

| Year | Türkiye border count, Canadian nationals arriving (rank among nationalities) | StatCan visits to Türkiye by Canadian residents (thousands) |
|---|---|---|
| 2015 | 187,615 (37) | n/a |
| 2016 | 106,285 (43) | n/a |
| 2017 | 81,196 (55) | n/a |
| 2018 | 108,272 (57) | 119 |
| 2019 | 139,164 (52) | 18 |
| 2020 | 34,210 (52) | 0 |
| 2021 | 72,034 (47) | 0 |
| 2022 | 197,416 (44) | 41 |
| 2023 | 248,868 (40) | 71 |
| 2024 | 302,728 (33) | 111 |
| 2025 | 321,271 (31) | 99 |

Sources and notes for this table:
- Türkiye Ministry of Culture and Tourism, annual border bulletin 2025, sheet "C-Mil Göre G.Yabancı", https://yigm.ktb.gov.tr/Eklenti/145395,2025yilliksinirbultenixlsx.xlsx?0. The bulletin index is at https://yigm.ktb.gov.tr/TR-249709/yillik-bultenler.html.
- The August 2026 monthly bulletin, https://yigm.ktb.gov.tr/Eklenti/151440,ag-stos-2026-bultenixls.xls?0, gives Canadian arrivals for January to August of 190,894 (2024), 203,297 (2025) and 209,176 (2026), up 2.9%. August alone: 37,260 (2025) and 34,008 (2026).
- StatCan: Table 24-10-0080-01, all trip purposes, quarterly visits summed, https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2410008001. Values are in thousands with quality flag E (use with caution). Spending: $158.4 million in 2025 and $288.7 million in 2024 (CAD, quality E).
- The two series differ a lot. Türkiye counts every border entry on a Canadian passport, including Canadian nationals living outside Canada and repeat entries. StatCan's survey covers only Canadian residents and is flagged as unreliable. The StatCan 2019 to 2021 values look implausibly low. Do not compare the two series directly, and treat the StatCan series as weak.

## 5. Flights and the air transport agreement

Current agreement:
- The Canadian Transportation Agency's page lists the "Agreement Between the Government of Canada and the Government of the Republic of Turkey on Air Transport", dated March 13, 2009, with status "Applied administratively". An Agreed Minute was reached ad referendum on March 13, 2009. Designations: Air Canada (April 30, 1997), Turkish Airlines (March 13, 2009), Air Transat (diplomatic note, November 25, 2010). Routes are confidential until the agreement definitively enters into force. Source: https://otc-cta.gc.ca/eng/transport-agreement/turkey
- Passenger capacity: "each country may allocate among its designated air carriers twelve weekly flights". This is from CTA Determination A-2024-140, 2024-09-17, which granted Turkish Airlines one extra weekly flight for October 2024 (13 a week). Source: https://otc-cta.gc.ca/eng/ruling/a-2024-140
- Cargo: on 2023-12-15, Transport Canada announced that all-cargo flights would rise from 3 to 7 weekly for each country. Source: https://www.canada.ca/en/transport-canada/news/2023/12/canadians-to-benefit-from-expanded-air-transport-agreements-with-ethiopia-jordan-and-turkiye.html
- Original 2009 release (no frequency figures given): https://www.canada.ca/en/news/archive/2009/03/canada-turkey-successfully-conclude-air-transport-agreement.html

What the new agreement changes:
- On 2026-05-12, Haber.aero, citing a statement by Türkiye's Directorate General of Civil Aviation (SHGM), reported that passenger frequencies rise from 12 to 21 weekly per side and cargo becomes unlimited with fifth-freedom rights. This is a lead only: https://haber.aero/en/Aero-Agenda/Frequency-increase-on-the-Turkey-Canada-route./ A rise from 12 to 21 (+75%) fits the Canadian Press description of "could nearly double flights".
- I found no Transport Canada or CTA page confirming the 21 figure, and no official text of the revised agreement. The CTA page still shows the 2009 agreement as applied administratively.
- The October 22 statement only commits to "ratify".

Current direct routes, as of October 2026:
- Air Transat (official release): Toronto to Istanbul, 3 weekly, launched 2025. Montréal to Istanbul, 2 weekly (Tuesday and Thursday), year-round from October 29, 2026, on an A330. Together that is up to 5 weekly. Source: https://www.transat.com/en-CA/corporate/media/news-releases/124611
- Turkish Airlines (trade press leads, because the official turkishairlines.com press room was blocked): summer 2026 frequencies are Toronto 7 weekly, Montréal 4, Vancouver 4. For winter 2026/27, Montréal and Vancouver go to 5 weekly from December 7, 2026, and Toronto is 7 weekly from December 12. Sources: https://www.travelweek.ca/?p=192957 (2026-06-02) and https://www.aeroroutes.com/eng/260701-tknw26ca (2026-07-01).
- Air Canada: no nonstop flight to Türkiye was found. Air Canada announced an interline deal with Pegasus Airlines on 2026-02-19, connecting through European hubs to Istanbul Sabiha Gökçen and İzmir. Source (GlobeNewswire release via Barchart): https://www.barchart.com/story/news/305120/air-canada-expands-travel-options-to-turkiye-through-new-partnership-with-pegasus-airlines
- Things to check before publishing:
  - Turkish Airlines' reported 15 weekly flights in summer 2026 is more than the old cap of 12, so either the revised limits were already being applied or extra-bilateral authority was granted. I did not find the CTA decision for 2026.
  - In 2025 the CTA refused Turkish Airlines' request for 5 extra weekly summer flights, after Air Canada, Air Transat, Aéroports de Montréal and the GTAA objected. This is a lead (ch-aviation, 2025-03-03): https://www.ch-aviation.com/news/151000-canada-rejects-turkish-airlines-request-for-more-summer-ops. The CTA determination itself should be pulled.
  - This shows that Canadian carriers and airports have opposed added Turkish Airlines capacity, which is a point to include for neutrality.
- StatCan air passenger origin-destination: the only O-D tables StatCan publishes cover the transborder (US) market (for example 23-10-0245, which ends in 2018). I found no official Canada-Türkiye O-D passenger table.

## 6. Türkiye's people as an opportunity (people link only)

- I found no official StatCan, IRCC or TurkStat dataset comparing which countries Turkish students choose. The comparable figures (for example UNESCO UIS outbound mobility) are outside the allowed source list, so I did not use them.
- Canada-side official data show Türkiye's position among study permit holders on December 31 slipping from 16th in 2018 to 2019 to 30th in 2024, while total holders from Türkiye stayed between about 4,650 and 5,725 from 2019 to 2024.

## Balance points (neutral framing)

Points that support the "opportunity" framing:
- The Turkish community is sizeable and growing: 76,745 people of Turkish origin, and the most immigrants born in Türkiye arrived in 2016 to 2021.
- Visits from Türkiye are at a record high (27,274 in 2025).
- Canadian nationals entering Türkiye reached a record 321,271 in 2025.
- Direct flights already exceed the old 12-a-week cap, and Montréal gets new Air Transat service in October 2026.

Points that call for caution:
- Türkiye was a large source of asylum claims, with 9,465 claimants in 2022 and 6,365 in 2023. Ranks are only partly verifiable because IRCC's file lists just the 2025 top 25, so a country outside that list could have ranked higher in earlier years.
- Much of the 2026 PR rise comes from refugee claims accepted in Canada, not economic immigration.
- Turkish citizens still need visas, and visa approvals fell 41% from 2023 to 2025.
- Canadian airlines and airports opposed more Turkish Airlines capacity in 2025.
- The new frequency figure (21) comes from the Turkish side and is not confirmed by a Canadian official source.

## Gaps and blocked items

- The turkishairlines.com press room was blocked (permission not granted).
- The Canadian Press article could not be fetched (thecanadianpressnews.ca client error). The CTV page returned no body text.
- IRCC "IMP for work purposes only" and "PR by citizenship and category" XLSX files: connection resets. The CSV versions were used for categories.
- There is no IRCC open data by citizenship and province of destination, and none on visitor visa applications or refusals by country.
- The TurkStat outbound student data was not searched (time).
