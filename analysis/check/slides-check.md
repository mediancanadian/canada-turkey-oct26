# Week 03 slides check: Canada and Türkiye (9 slides)

Checked 2026-10-23 against the rendered PNGs (build/out, 12:52) and build/slides.html. slide_text.txt is stale (for example slide 4 says "Canada buys" where the image says "Bought from Türkiye") and was not used. Numbers were recomputed from trade/raw/x171/12100171.csv, trade/raw/x011/12100011.csv, trade/out/annual_totals_1988_2026ytd.csv, tariffs/outputs/*.csv, energy/outputs/cer_lng_summary.txt, energy/results.md, defence/outputs/exports_turkiye_2010_2025.csv and the saved PMO pages (defence/raw/pmo_joint_statement_20261022.html.txt, people/raw/followup/pmo_release_2026-10-23.html, pmo_remarks_2026-10-22.html).

Global checks: no em dashes in slides.html; no "now", "today" or "currently"; no "X, not Y" framing.

## Slide 1: cover

| Claim | Verdict | Correct value or fix | Evidence |
|---|---|---|---|
| NATO allies since 1952 | OK | Türkiye joined 1952 (Canada 1949) | facts.json, NATO page |
| "the two countries signed it in Ankara on October 22, 2026" | OVERSTATED | The joint statement says the leaders "launched" the partnership; nothing was signed for the partnership itself (the air agreement and MOUs were signed). Use "launched it in Ankara on October 22, 2026" | pmo_joint_statement_20261022.html.txt |
| Source line: PMO joint statement, Oct 22, 2026 | OK | | same |

## Slide 2: US share

| Claim | Verdict | Correct value or fix | Evidence |
|---|---|---|---|
| 72% of goods exports to the US in 2025 | OK | 72.33% (562.7B of 778.0B) | 12100171.csv |
| "lowest share in 27 years of records" | OVERSTATED | It is the lowest in table 12-10-0171, which starts in 1999. Table 12-10-0011 goes back to 1997 (81.8%), and older StatCan trade records exist with lower US shares before the 1989 FTA. Use "the lowest since at least 1997" or "the lowest in this Statistics Canada series, which starts in 1999" | 12100171.csv; 12100011.csv |
| 87% in 2002 | OK | 87.13%, the series peak | 12100171.csv |
| Chart line matches data | OK | All 27 points reproduce | values.json vs recompute |
| Axis 50% to 100% (not zero) | OK with note | Line chart, gridlines labelled; acceptable. A 0 to 100% axis would show the fall as smaller | image |
| Advisory | Note | Jan to Aug 2026 share is 68.6%, below 2025. The claim is about full years, so it holds, but the website should mention it | 12100011.csv |

## Slide 3: scale

| Claim | Verdict | Correct value or fix | Evidence |
|---|---|---|---|
| Two-way trade $4.3 billion in 2025 | OK | 4,334.7M; also in PMO release | annual_totals csv; pmo_release |
| A year of trade equals 3 days of sales to the US | OK | 2.81 days (4.33B / (562.7B / 365)). "Under 3 days" is more exact | recompute |
| Strip width | OK | Bar is 2.81/365 of the strip | make_slides.py v_year_strip |

## Slide 4: imbalance

| Claim | Verdict | Correct value or fix | Evidence |
|---|---|---|---|
| Bought almost three times as much as sold | OK | Ratio 2.81 | annual_totals csv |
| "widest gap in the records, which start in 1988" | OVERSTATED (minor) | True for both ratio (2.81, next 2.50 in 2024) and dollar gap (2.06B) in the 1988 to 2025 series. "Records start in 1988" holds for these StatCan tables only. Use "the widest since at least 1988" | recompute |
| $3.2 billion bought, $1.1 billion sold | OK | 3,197.3M; 1,137.4M | same |
| Label "Bought from Tür" | ERROR (visual) | Label is clipped at the SVG edge. Shorten or move left | PNG 4 |
| Axis starts at zero | OK | | make_slides.py v_lines |
| Repeated number | Minor | "1988" in subtitle and chart title | |

## Slide 5: duties

| Claim | Verdict | Correct value or fix | Evidence |
|---|---|---|---|
| Lentils are Canada's top export | OK | HS 071340 C$172.6M vs aircraft C$162.0M split over two HS6 lines | tariffs export csv |
| Lentils 19.3% | OK with note | Red and green lentils 19.3%; seed 0% (in footnote); organic 14.5%. Green lentils were 10% until 2026-04-30, so "2026 rates" is 19.3% only from May 1 | tariffs/results.md lines 106 to 108 |
| Aircraft Free | OVERSTATED (minor) | 0% only under the civil-aircraft end-use relief; base rate 2.7%. Add "(civil)" or a footnote | tariffs/results.md line 111; csv note |
| Steel scrap Free | OK | 0% | csv |
| Optical instruments 2.4% | OK with note | 2.38% is an average of 0% and 4.7% lines. The footnote names only carpets and clothing as averages; add optical instruments | csv note "avg of 2 lines" |
| Medicines, turbine parts, fishing ship Free | OK | All lines Free | imports csv |
| Carpets 13.2%, clothing 17.4% | OK | 13.20%; 17.41% | imports csv |
| Two in three dollars enter duty-free | OK | 67.1% | imports csv |
| Card title "Duty paid" | Minor | These are tariff rates, estimates. "Duty rate on each country's main goods" | |

## Slide 6: provinces

| Claim | Verdict | Correct value or fix | Evidence |
|---|---|---|---|
| Three provinces make three-quarters of sales | OK | 76.7% of domestic exports (C$1,029.4M) | provinces csv |
| QC $310M aircraft, ON $275M optical instruments, SK $205M lentils, B.C. $111M, AB $82M | OK | 309.5, 274.6, 205.3, 111.3, 81.5 | values.json; province_top_hs6.csv |
| "Lower duties would help their farmers and makers, and bring Canadian clothing and steel makers more competition" | OVERSTATED | A forecast not in any source. Quebec's aircraft and steel scrap already enter Türkiye free, Ontario's optical goods face about 2.4%. Turkish steel in Canada is mostly MFN-free; its barriers are SIMA duties and TRQ surtaxes, which an FTA does not automatically remove. Neutral option: "Türkiye's 19.3% lentil duty falls mostly on Saskatchewan and Alberta. Quebec's aircraft already enter duty-free." | tariffs/results.md; v_receipts data |
| "Darker means more" | ERROR (visual) | On the map, larger values are brighter (Quebec is the lightest). Use "Brighter means more" | PNG 6; make_slides.py fill() |
| Basis | Note | Domestic exports (1,029.4M), not total exports (1,137.4M). Source line says so; fine | |

## Slide 7: energy

| Claim | Verdict | Correct value or fix | Evidence |
|---|---|---|---|
| Türkiye imports 70% of its energy | OK | 70.3% net imports, 2024 balance | energy/outputs/tr_energy_balance_2024.txt |
| "Canada sells uranium, reactors and gas" | OVERSTATED | Canada exports uranium (about 90% of output) and gas (LNG since June 2025). It has not sold a reactor abroad in years and sells none of the three to Türkiye (coal is the only energy export). The PM's own words: "from LNG to civilian nuclear technology". Use "Canada has uranium, reactor technology and gas to sell" | energy/results.md lines 31, 153, 200 to 231; pmo_remarks |
| Canada's 2025 LNG equals 5% of Türkiye's gas imports | OK | 3.11 / 58.3 bcm = 5.3% (marine basis) | cer_lng_summary.txt; EPDK |
| Gas bars: Russia 21.2, Azerbaijan 11.9, US LNG 9.5, Iran 7.7, Algeria 4.4, Others 3.6 | OK | Others = Nigeria 0.87 + others 2.77 = 3.64 | energy/results.md |
| Canada bar width | OK | 3.11 on the same scale as the 58.3 stack | v_gas |
| "shipped almost entirely to Asia" | OK | 98.1% to Korea, Japan, China, Taiwan; 1.9% US | cer_lng_summary.txt |
| Energy statement "sets out intentions, with no volumes" | OK | No volumes, prices or buyers named | energy/results.md line 30 |

## Slide 8: defence

| Claim | Verdict | Correct value or fix | Evidence |
|---|---|---|---|
| Fell to almost nothing in 2021 | OK | 2021 C$0.93M (2022 0.06M, 2023 0.12M) | exports_turkiye csv |
| Resumed in 2024 | OK | C$107.9M | same |
| $151M (2019), $108M (2024) | OK | 151.4; 107.9 | same |
| 2021: 29 permits cancelled | OK | Announced 2021-04-12 | defence/results.md line 66 |
| 2024: case-by-case review | OK | Notice 1108, Jan 2024. The label sits right of the 2021 dashed line with no 2024 marker; consider a small tick at 2024 | gac_notice_1108.html.txt |
| "A Canadian review found Canadian drone sensors used in Nagorno-Karabakh, Libya and Syria" | OVERSTATED (minor) | The review found "credible evidence" that the sensors "have been used". Use "A 2021 Global Affairs Canada review found credible evidence that Canadian drone sensors were used in..." | defence/raw/review.txt lines 104 to 108 |
| US exports excluded from the reports | OK | | GAC reports |
| Axis from zero | OK | | v_military |
| Kicker "Trust" | Wording | Editorial frame (flagged in the prior check). "Defence" is neutral | |

## Slide 9: next steps

| Claim | Verdict | Correct value or fix | Evidence |
|---|---|---|---|
| "Trade talks start in November" | OK (official) | PMO release 2026-10-23: first round "from November 30 to December 4, 2026, in Ankara". PM remarks also say "next month". facts.json cites only Canadian Press; change its source to the PMO release. Consider "start November 30" | pmo_release_2026-10-23.html |
| Timeline row "November 2026: first round" | OK, ordering ERROR | COP31 (Nov 9 to 20) comes before the talks (Nov 30). List COP31 first, or use "Nov 30 to Dec 4" | same |
| COP31 Antalya, November 9 to 20 | OK | | joint statement |
| "Up to 21 flights a week each way, up from 12" | OVERSTATED (wording) | PMO: "up to 21 weekly passenger-combination flights per country". "Each way" is not the source's term; use "per country" | pmo_release |
| "Once in force" | OK | Agreement signed; the joint statement says the leaders agreed to "ratify" it | joint statement |
| 15% a year to double in five years, twice the last five years' pace | OK | 14.9% vs 7.1% (2020 to 2025), ratio 2.1 | values.json; trade/results.md |
| Doubling framing | Note | No source sets a five-year doubling goal (Erdoğan's target has no timeframe, and US$3B to US$10B is more than double). The conditional "would take" is fine; do not attribute a five-year goal to anyone | trade/results.md lines 116 to 119 |
| Repeated number | Minor | "November" three times | |

## Must-fix list

1. Slide 4: "Bought from Tür" label is clipped. Shorten or move it.
2. Slide 6: "Darker means more" is backwards; the map shows more as brighter.
3. Slide 6: replace the "Lower duties would help... steel makers more competition" line (forecast, wrong for aircraft and steel).
4. Slide 7: "Canada sells uranium, reactors and gas" overstated; use "has uranium, reactor technology and gas to sell".
5. Slide 1: "signed it" should be "launched it".
6. Slide 2: "lowest share in 27 years of records" should be "lowest since at least 1997" (or name the 1999 series).
7. Slide 9: reorder the timeline (COP31 Nov 9 to 20 before talks Nov 30); "each way" should be "per country"; update facts.json fta source to the PMO release.
8. Slide 8: "found credible evidence that... were used".
9. Slide 5: mark aircraft as civil end-use and add optical instruments to the "average rate" note.
10. Slide 4: "widest since at least 1988" (minor).
