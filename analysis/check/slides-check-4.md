# Week 03 slides check 4: Canada and Türkiye (9 slides)

Checked 2026-10-23 against build/out/*-of-9.png (15:24 render), build/slides.html, values.json, facts.json, photos_used.json and the research folders. All nine slides checked. The 15:35 re-render changed only the cover lead; both versions are covered.

## Slide 1: cover

| Claim | Verdict | Fix | Evidence |
|---|---|---|---|
| "Talking trade with Türkiye" | OK | | PMO release 2026-10-23: FTA first round announced, trade mission, EDC MOU (people/raw/followup/pmo_release_2026-10-23.html) |
| "The first official visit by a Canadian PM" (15:24 render) | OVERSTATED, fixed in the 15:35 render | Every PMO text says "first bilateral visit"; the joint statement says "the first visit of a Head of Government between two countries". Carney was in Ankara in July 2026 for the NATO Summit (PMO 2026-10-06), so "first official visit" can be contested. The 15:35 render now says "first bilateral visit", which matches. Style guide line 99 still says the government uses "first official visit"; it should say "first bilateral visit" | PMO 2026-10-06 (tariffs/raw/official/...2026_10_06...txt); 10-22 readout and remarks; 10-23 release; defence/raw/pmo_joint_statement_20261022.html.txt |
| New lead (15:35): "brought agreements on flights, energy and defence" | OVERSTATED (minor) | Flights: signed Air Transport Agreement. Defence: MOU, which the PM calls an "agreement". Energy: a signed joint statement of intentions, which slide 7 itself calls a "statement" with no volumes. Option: "brought an air agreement, a defence MOU and an energy statement", or keep "agreements" as an umbrella term knowingly | pmo_release_2026-10-23.html ("signed a joint statement"); energy/results.md line 30 |
| New cover layout (15:35) | Minor | Lead is now two 44 px lines (about 85 characters) plus a third line "Here is what they mean for Canadians." Style guide line 73 asks for one 44 px line (about 40 characters) "and nothing more"; line 72's own example has two sentences, so the guide conflicts. Nothing is clipped | PNG 1 (15:35); style guide lines 72 to 73 |
| Kicker "Week 2" | OK | | Style guide line 3: week 2 is Canada and Türkiye; the wildfire post was held back |
| Layout (520 px block, 2-line 120 px headline, 1 line under it) | OK | Nothing clipped or overlapping | PNG 1 |
| Credit "Photo: Nicoleon, CC0" | OK | Matches photos_used.json key 1 (Anıtkabir) | photos_used.json |

## Slide 2: the opportunity

| Claim | Verdict | Fix | Evidence |
|---|---|---|---|
| Türkiye imported US$365 billion of goods in 2025 | OK | 365,369,912,607 | market/raw/comtrade/tur_imports_2025_partners.json (partner 0, TOTAL) |
| 0.3% came from Canada | OK | 1,162,832,980 / 365.37B = 0.318% | same file, partner 124 |
| Energy US$62.5B, Canada US$38M | OK | HS 27: 62,465,580,162; Canada 37,624,468 | tur_imports_2025_hs2.json; tur_imports_2025_from_can_hs2.json |
| Machinery US$41.6B, Canada US$125M | OK | HS 84: 41,644,032,072; 125,163,673 | same |
| Gold and jewellery US$28.1B, Canada US$97M | OK | HS 71: 28,110,541,146; 97,184,796 | same |
| Aircraft US$5.4B, Canada US$175M | OK | HS 88: 5,421,505,809; 174,969,182 | same |
| Lentils and other vegetables US$1.1B, Canada US$185M | OK | HS 07: 1,085,939,342; 184,747,311 | same |
| Bar lengths | OK | 560 px = US$62.5B; 41.6B = 373 px, 28.1B = 252 px, 5.4B = 49 px, 1.1B = 9.7 px, all match the SVG. Canada slivers are a 3 px minimum (true widths under 1 px except lentils) | slides.html s2 SVG |
| Category choice | Note | The five rows are neither Türkiye's top imports nor Canada's top lines (Canada's no. 3 in Türkiye's data is optical instruments, HS 90, US$135M; energy is no. 11). Fine as a selection, but the note reads as if these are what Türkiye mainly buys. Optional: "Five of the things Türkiye's 86 million people bought" | tur_imports_2025_hs2_canada.csv |
| 86 million people | OK | 86,092,168 on 31 Dec 2025 (TurkStat ABPRS) | market/results-followup.md line 13 |
| 72% of Canada's goods went to the US in 2025 | OK | 562,698,185.1 / 778,004,358.6 = 72.33% | trade/raw/x171/12100171.csv (recomputed) |
| Goal to double other exports within a decade | OK | PMO 2025-10-29 (Singapore release): "the government's ambitious new mission to double our non-U.S. exports in the next decade". Minor wording: the source is the government's goal, so "and the government wants to double..." attributes it more exactly than "Canada... wants" | Fetched pm.gc.ca page; facts.json non_us_exports_goal |
| Mirror data vs slide 3 | Note | Slide 2 uses Türkiye's import records in US dollars (US$1.16B from Canada); slide 3 uses StatCan exports in Canadian dollars (C$1.14B). "Aircraft US$175M" here and "Aircraft and parts $176M" on slide 3 look like one figure in two currencies but are different records. Putting "as Türkiye records it" in the card note (not only the source line) would prevent the question | tur_imports_2025_hs2_canada.csv; values.json receipt_goods_to_tr |
| Number repeats | Minor | "125" appears here (machinery, US$125M) and on slide 8 ($125 million ammunition permit). Different facts, but the style guide bars a number on two slides | style guide line 71 |
| Credit "---=XEON=---, CC BY 3.0" | OK | Matches photos_used.json key 2 | photos_used.json |

## Slide 3: trade deficit

| Claim | Verdict | Fix | Evidence |
|---|---|---|---|
| Canada buys more from Türkiye than it sells | OK | 2025: bought 3,197.3M, sold 1,137.4M; deficit every year since 2012 and in Jan to Aug 2026 | trade/out/annual_totals_1988_2026ytd.csv |
| Deficit $2.1 billion in 2025 | OK | 2,059,962,307 | same, balance column |
| Shrank by almost a quarter, Jan to Aug 2026 | OK | 1,522.0M to 1,164.8M, down 23.5%. Wording note: "from January to August 2026" can read as a change during those months. Clearer: "From January to August 2026 it was almost a quarter smaller than a year earlier" | trade/out/results_totals.json (ytd) |
| Sold: lentils, chickpeas, vegetables $222M; machinery and engines $188M; aircraft and parts $176M; optical instruments $100M; cars and parts $83M | OK | HS 07 221.7; HS 84 188.0; HS 88 176.2; HS 90 99.7; HS 87 82.7. These are the top five chapters | trade/out/hs2_chapters_2021_2025.csv (recomputed) |
| Sold: everything else $368M; total $1.1 billion | OK (rounding) | True residual is 368.9M ($369M); the builder forces it to $368M so the lines add to 1,137. Lines add to $1,137M = $1.1 billion either way | same; values.py receipt() |
| Bought: machinery and appliances $405M; steel and steel goods $308M; fruit, nuts and food $259M; medicines $247M; clothing $220M; everything else $1,758M; total $3.2 billion | OK | HS 84 405.2; HS 72+73 308.1; HS 08+20 258.6; HS 30 247.3; HS 61+62 220.1; residual 1,757.95. Lines add to 3,197 | same |
| +8% exports, -14% imports, Jan to Aug 2026 vs 2025 | OK | +7.68%; -13.66% | results_totals.json pct_change |
| Repeats | OK | No number twice on the slide. $3.2 billion reappears on slide 4, which the style guide allows (trade totals on the duties slide) | style guide line 71 |
| Layout | OK | Two-line first row on the left; totals sit at different heights but nothing is clipped | PNG 3 |
| Credit "Maxime Laterreur, CC BY 4.0" | OK | Matches photos_used.json key 3 | photos_used.json |

## Slide 4: duties

| Claim | Verdict | Fix | Evidence |
|---|---|---|---|
| Türkiye charges 19.3% on Canadian lentils | OK | Red and green lentil lines are 19.3% (96% of lentil value); seed lentils 0%, organic lines about 14.5%. Green lentils were 10% until 2026-04-30, so 19.3% holds from May 1, 2026 | tariffs/outputs/ca_exports_to_TR_2025_est_tr_duty.csv; tariffs/results.md lines 106 to 107 |
| Canada about 17% on Turkish clothing | OK | 38.3M duty on 220.1M = 17.4% (rates 18%, 17%, 16%) | ca_imports_from_TR_2025_est_mfn_duty.csv; tariffs/results.md line 33 |
| $1.0 billion base; 47% duty-free / 53% pays duty | OK | Domestic exports 1,029.35M minus durum 28.8M = 1,000.5M; duty-free 46.6% | recomputed from the export duty csv |
| Duty $64 million, 6.4% on average | OK | 64.4M / 1,000.5M = 6.44% | same |
| $3.2 billion base; 67% duty-free / 33% pays duty | OK | 3,197.3M; duty-free 67.1% (values.json 67.05%) | import duty csv |
| Duty $105 million, 3.3% on average | OK | 105.3M / 3,197.3M = 3.29% | same |
| Label "Duty paid" | Minor | These are estimates (2025 trade at 2026 rates); "Estimated duty: $64 million" matches the footnote. "6.4% on average" is over all goods including duty-free ones (dutiable goods average 12.1%); "6.4% of the total" is clearer | tariffs/results.md lines 14, 160 |
| Bar geometry | OK | Canada bar 267 px vs Türkiye 858 px (0.31 = 1,000.5 / 3,197.3); splits 46% and 67% | slides.html s4 rects |
| Durum wheat footnote | OK | Durum 130%, about C$37.5M duty on C$28.8M. "Can enter duty-free when used to make exports" matches the inward processing regime; the share that does is unconfirmed, which "can" covers | tariffs/results.md lines 117, 160, 163 |
| "A trade deal could help farmers and shoppers" | OK | Hedged takeaway; the style guide uses this exact line as its example. Supported by 19.3% on lentils and about 17% on clothing | style guide line 42 |
| "Lower duties would also bring Canadian clothing makers more competition" | OVERSTATED (minor) | A forecast with no source; "would" states it as certain. Use "could also bring" | no source in tariffs/results.md |
| Credit "Fumikas Sagisavas, CC0" | OK | Matches photos_used.json key 4 | photos_used.json |

## Slide 5: who sells

| Claim | Verdict | Fix | Evidence |
|---|---|---|---|
| Quebec, Ontario and Saskatchewan make three-quarters of sales | OK | 789.4M of 1,029.35M domestic exports = 76.7%. Holds only on the domestic-exports basis named in the source line (on total exports it would be 69%) | trade/out/provinces_2021_2025.csv |
| Province totals: B.C. $111M, Alberta $82M, Saskatchewan $205M, Quebec $310M, Ontario $275M | OK | 111.3; 81.5; 205.3; 309.5; 274.6 | same |
| Quebec: aircraft $162M, steel scrap $29M, newsprint $16M | OK | 880240 101.9 + 880230 60.1 = 162.0; 29.2; 15.7 | trade/out/province_top_hs6.csv |
| Ontario: "Cars $29M" | ERROR | Counts only HS 870390 (29.0M). Ontario's top five also include HS 870324, also cars (11.3M). Aircraft lines are combined for Quebec, so cars should be combined too. All Ontario car lines (HS 8703.21 to 8703.90, excluding 8703.10 snow vehicles) total 43.3M: "Cars $43M". This also removes the duplicate "$29M" (Quebec steel scrap and Ontario cars), which the style guide bars on one slide | province_top_hs6.csv ranks 2 and 5; tariffs/raw/statcan/CIMT-CICM_Dom_Exp_2025/ODPFN018_202512N.csv (TR, ON, 8703 lines summed); values.py NAMES map lacks 870324 |
| Ontario: optical instruments $51M, plastic-moulding machines $12M | OK | 50.8; 12.5 (ranks above cocoa 11.5 either way) | same |
| B.C.: aircraft engines $42M, coal $37M | OK | HS 841121 (turboprop engines) 42.2; HS 270112 37.4 | same |
| Alberta: lentils $43M, durum wheat $7M, other pulses $4M | OK | 42.6; 6.6; 4.0 | same |
| Saskatchewan: lentils $130M, chickpeas $26M, durum wheat $22M | OK | 130.0; 26.5; 22.1 | same |
| Saskatchewan lentils down almost two-thirds, 2022 to 2025 | OK | 366.0M to 130.0M = down 64.5%. 2022 is the peak year (2021 start would give 61.7%); the years are stated, so it is accurate | trade/results.md line 105 |
| "Brighter means more" | OK | Fill opacity rises with value (Quebec 0.95, Ontario 0.89, Saskatchewan 0.76, B.C. 0.56, Alberta 0.48) | make_slides.py fill(); slides.html s5 |
| Leader lines and labels | OK | Each dot sits inside its province; no label overlaps | PNG 5 |
| Credit "Janusz Sobolewski, CC BY 2.0" | OK | Matches photos_used.json key 5 | photos_used.json |

## Slide 6: travel

| Claim | Verdict | Fix | Evidence |
|---|---|---|---|
| Turkish Airlines flies to 120 countries, more than any other airline | OVERSTATED (minor) | The Guinness record is for September 2023 to September 2024 (achieved 21 October 2024). Present tense presents a 2024 count as current. Use "In 2024, Turkish Airlines flew to 120 countries, more than any other airline" | guinnessworldrecords.com record 736843 (fetched); facts.json tk_countries. No copy is saved in the research folders |
| "Istanbul is a global hub" | OK | Istanbul Airport 84.4M passengers in 2025, 8th in the world (ACI World) | facts.json ist_passengers_2025 (cited, not saved in research folders) |
| Up to 21 flights a week for each country, up from 12, to any city | OK | PMO 10-23: "up to 21 weekly passenger-combination flights per country" and "unlimited access to all points in each country"; "increases weekly passenger flights from 12 to up to 21" | people/raw/followup/pmo_release_2026-10-23.html |
| Cargo flights have no limit | OK | "unlimited weekly all-cargo flights" | same |
| "Canadians get more choice of flights" | OK | The agreement raises the cap and Air Transat adds Montréal to Istanbul from Oct 29. Whether other airlines add flights is not yet known; the line is acceptable as a takeaway | PMO release; people/results.md line 269 |
| Trips chart: 139,164 in 2019; 321,271 in 2025 | OK | Türkiye border bulletin, Canadian nationals arriving. All 16 points reproduce (2019 y = 174.6, 2025 y = 49.7 on a 0 baseline at y = 270, 68.6 px per 100k) | people/outputs/turkiye_border_canada.json; people/results.md lines 235 to 250; slides.html s6 polyline |
| "Trips to Türkiye by Canadians" | OK with note | The count is border entries on Canadian passports (includes Canadians living abroad and repeat entries), not Canadian residents' trips. Plain label is fair; the website should say what is counted | people/results.md line 253 |
| Axis | OK | Zero baseline drawn (no "0" label); gridlines at 100k steps match the data | slides.html s6 |
| In 2025, Air Canada and Air Transat opposed extra Turkish Airlines flights; Toronto and Montréal airports supported them | OK | CTA ruling A-2025-25 (2025-02-14, request for +5 weekly in 2025): Air Canada and Air Transat opposed; ADM and GTAA supported. Air Canada opposed again in A-2025-77 | people/raw/followup/a-2025-25.html; people/results-followup.md lines 22 to 33 |
| Source line "Transportation Agency" | Minor | Use the full name, "Canadian Transportation Agency" | |
| Repeats | Minor | "120" (countries) here and "120 GW" on slide 7; "12" (flights) here and "$12M" on slide 5. Coincidental figures, flagged only because the style guide bars any number on two slides | style guide line 71 |
| Credit "Siyuan He, public domain" | OK | Matches photos_used.json key 6 (Flickr Public Domain Mark) | photos_used.json |

## Slide 7: energy

| Claim | Verdict | Fix | Evidence |
|---|---|---|---|
| Over 20 GW of nuclear by 2050 | OK | Ministry, 25 Sep 2023: "adding over 20 gigawatts (GW) of nuclear energy capacity to its energy mix by the end of 2050" | enerji.gov.tr news-detail?id=21184 (fetched; no saved copy in energy/) |
| 7.2 GW by 2035: addition or total? | OK | Official wording is an addition: "the targeted addition of 7.2 GW of nuclear capacity by the end of 2035". Türkiye had no operating reactor then (PRIS lists all four Akkuyu units as under construction), so the addition equals a 7.2 GW total and Akkuyu's 4.8 GW counts toward it | same page; energy/outputs/pris_summary.txt |
| Chart draws 7.2 GW correctly | OK | Nuclear track is 0 to 20 GW over 860 px; marker at 309.6 px = 7.2 GW; Akkuyu bar 206.4 px = 4.8 GW. Drawn as a level reached by 2035, which matches the zero base. The 2050 box ends at 20 GW for a goal of "over 20", acceptable as the floor | slides.html s7 rects and line |
| 4.8 GW being built by Russia's Rosatom | OK | Akkuyu 4 x VVER-1200 (PRIS 4 x 1,114 MW net, 4.8 GW gross); owner Akkuyu Nuclear JSC, a Rosatom company; supplier Atomenergomash | pris_summary.txt; energy/results.md line 117 |
| 39 GW wind and solar in December 2025 | OK | EPİAŞ daily report 14.12.2025: solar 24,682 MW + wind 14,546 MW = 39,228 MW | energy/raw/round3/epias.txt line 112 to 118 |
| Goal 120 GW by 2035 | OK | Minister Bayraktar, 4 Nov 2024: "We will reach 120 thousand megawatts of solar and wind installed capacity by 2035" | enerji.gov.tr news-detail?id=21392 (fetched) |
| Wind and solar bar | OK | 281.1 / 860 px = 32.7% = 39.2 / 120 | slides.html s7 |
| Studying Canada's CANDU reactors | OK | TÜNAŞ and AtkinsRéalis MoU, 3 Mar 2026, for "a detailed assessment of the applicability of Canada's CANDU reactor technology in Türkiye" | energy/results.md lines 37 to 39 |
| Canada produces about a quarter of the world's uranium | OK (tense) | NRCan: "24% of global production in 2024". The guide asks the tense to match the data year: "In 2024, Canada produced about a quarter of the world's uranium" | energy/raw/followup/nrcan_uranium_nuclear_power_facts.html |
| The October 2026 energy statement sets no volumes | OK | "No volumes, prices, buyers or contracts are named." Clarity note: say what kind ("sets no purchase amounts for gas or uranium") | energy/results.md line 30 |
| Headline "open a door for Canada" | OK | Figure of speech, mild; backed by the CANDU assessment MoU and the joint statement on "Canadian nuclear technology" | energy/results.md lines 31, 38 |
| Credit "Robert T Bell, CC BY 2.0" | OK | Matches photos_used.json key 7 (Darlington) | photos_used.json |

## Slide 8: defence

| Claim | Verdict | Fix | Evidence |
|---|---|---|---|
| Military sales back, with conditions | OK | Notice to Exporters 1108 (Jan 2024): presumptive denial lifted, case-by-case review, end-use assurances; exports C$107.9M in 2024 and C$60.8M in 2025 | defence/results.md line 71; defence/outputs/exports_turkiye_2010_2025.csv |
| Government says linking the industries will create jobs and exports | OK | PMO 10-23: the defence MOU "will connect Canadian and Turkish companies so they can build together, creating good jobs at home, export opportunities abroad" | pmo_release_2026-10-23.html |
| NATO's second-largest military | OK | PMO: "NATO's second-largest standing military"; NATO 2026e personnel 395,800 (second to the US) | pmo_release; defence/results.md lines 115 to 125 |
| Mostly imaging and targeting equipment | OK | ECL 2-15 (imaging) and 2-5 (fire control) dominate every high year: 2019 $116.0M and $59.8M; 2024 $104.6M and $23.8M | defence/results.md line 36 |
| $151M in 2019, $108M in 2024 | OK | 151.4M; 107.9M | exports_turkiye_2010_2025.csv |
| Line chart | OK | Points at mid-year (2010 at x 35.6, 51.2 px a year); zero baseline at y 140; 2019 y 39.7 and 2024 y 68.5 match; all 16 values reproduce | slides.html s8 polyline |
| 1 Oct 2019: new permits suspended after Türkiye's Syria operation | OK | Marker at 2019.75 | defence/results.md line 61 |
| 2 Apr 2021: 29 permits cancelled; review found credible evidence that Canadian sensors were used in Nagorno-Karabakh | OK | Garneau statement and review, 12 Apr 2021; 29 cancelled per GAC reports. The review also names Libya and Syria; naming one is accurate | defence/results.md lines 64 to 66 |
| 3 Jan 2024: reopened case by case; Türkiye must say if goods will go to a country outside NATO | OK (simplified) | Notice 1108 asks for that statement where a Turkish government end user is identified, and excepts Ukraine. Acceptable simplification; "Türkiye's government must say" would be closer | defence/results.md line 71 |
| 4 2025: permit to broker $125 million of Turkish ammunition for Ukraine | OK | GAC 2025 report Table 16: ECL 2-3, origin Türkiye, destination Ukraine, $125,000,000 authorized. Marker placed mid-2025 (exact date not published) | defence/results.md line 44 |
| 5 Oct 2026: agreement to link the defence industries | OK | MOU on defence sector partnerships; PM remarks call it an "agreement" | pmo_release; pmo_remarks_2026-10-22.html |
| Open / Suspended / Reopened bar | OK | Suspended from 2019.75 to 2024.0; Reopened from 2024.0 | slides.html s8 rects |
| ANCC asks that Canada keep full control of export permits | OK | ANCC, 24 Sep 2026: "Preserve Canada's full authority over export and brokering permits". Context note: the request is about the trade deal; "in a trade deal" would make that clear | defence/raw/ancc_20260924.html.txt |
| Canada can cancel permits if goods are misused | OK | Notice 1108: GAC may suspend or cancel permits on credible evidence of misuse | defence/results.md line 71 |
| Repeats | Minor | "$125 million" also matches slide 2's US$125M | |
| Credit "DJLeamen, CC0" | OK | Matches photos_used.json key 8 | photos_used.json |

## Slide 9: what comes next

| Claim | Verdict | Fix | Evidence |
|---|---|---|---|
| Free trade talks start in Ankara on November 30 | OK | PMO 10-23: first round "from November 30 to December 4, 2026, in Ankara" | pmo_release_2026-10-23.html; facts.json fta_round_dates |
| "Until a deal takes effect, duties stay the same." | ERROR | Duties change without a deal, and did in 2026: Türkiye raised green lentils from 10% to 19.3% on May 1, 2026 ("Turkish pulse and grain duties change often by decree"); Canada added anti-dumping duties on Turkish steel wire (Jan 2), steel strapping (Jan 14) and oil-well pipe (Apr 21) and extended the steel surtax quota to 2027. Use "Starting talks does not change any duties." | tariffs/results.md lines 17, 62 to 69, 107, 163 |
| "Once its terms are public, we will break them down in a new post" | OK | Plain follow-up promise as the style guide allows | style guide line 37 |
| October 29: Air Transat starts Montréal to Istanbul | OK | Air Transat release: 2 weekly, year-round from October 29, 2026, A330 | people/results.md line 269; facts.json |
| November 9 to 20: Türkiye hosts COP31 in Antalya | OK | Joint statement: COP31 "to be held in Antalya on 9-20 November 2026" | defence/raw/pmo_joint_statement_20261022.html.txt |
| 2027: trade mission led by the trade minister | OK | PMO: "a Canadian trade mission to Türkiye in 2027, to be led by the Minister of International Trade"; PM remarks: "Minister Sidhu will lead" | pmo_release; pmo_remarks |
| Date to be set: President Erdoğan visits Canada | OK | Joint statement: "Türkiye welcomed the invitation for President Erdoğan to visit Canada at a mutually convenient time" | joint statement |
| Order of events | OK | Oct 29, Nov 9 to 20, (talks Nov 30 in the headline), 2027, date to be set | PNG 9 |
| Credit "Levi Meir Clancy, CC0" | OK | Matches photos_used.json key 9 (Antalya) | photos_used.json |

## Whole deck

| Check | Verdict | Notes |
|---|---|---|
| Em dashes | OK | None in slides.html (no U+2014, U+2013 or &mdash;) |
| now, today, currently | OK | None |
| Contrast or negation framing | OK | No "X, not Y". Slide 2 headline pairs "big market" with "sells little" as its takeaway; slide 6 reports both sides of the CTA case neutrally. "Sets no volumes" (slide 7) and "have no limit" (slide 6) are plain negatives, acceptable |
| Same number twice on one slide | ERROR | Slide 5: "$29M" twice (Quebec steel scrap, Ontario cars). Fixed by "Cars $43M" |
| Number on two slides | Minor | 125 (slides 2 and 8), 120 (6 and 7), 12 (5 and 6), 1.1 (US$1.1B on 2, $1.1 billion on 3), 29 (29 permits on 8, $29M on 5). All different facts; $3.2 billion on 3 and 4 is allowed by the guide |
| Claims stronger than sources | See slides | Slide 9 duties line (ERROR); slide 1 new lead "agreements on ... energy"; slide 4 "would also bring"; slide 6 present-tense 120 countries; slide 7 present-tense uranium share |
| Chart scales and labels | OK | Slides 2, 4, 6, 7, 8 recomputed from the SVG; every bar, point and marker matches its value; line charts start at zero |
| Clipping and overlap | OK | None found on PNGs 1 to 9 |
| Photo credits | OK | All nine credits match photos_used.json (key 1b is not used on a slide) |
| Render tracked | Note | Text checked on the 15:24 render; the 15:35 re-render changes only the cover lead (diffed) |

## Must-fix list

1. Slide 9: "Until a deal takes effect, duties stay the same" is contradicted by 2026 duty changes on both sides. Use "Starting talks does not change any duties."
2. Slide 5: Ontario "Cars $29M" counts only HS 870390; all Ontario car lines total $43.3M. Use "Cars $43M". This also clears the duplicate $29M.
3. Slide 1 (15:35): "agreements on flights, energy and defence" calls the energy joint statement an agreement; reword or accept knowingly. Update style guide line 99 to "first bilateral visit".
4. Slide 6: "In 2024, Turkish Airlines flew to 120 countries" (Guinness period Sep 2023 to Sep 2024).
5. Slide 4: "would also bring" to "could also bring"; consider "Estimated duty" for "Duty paid".
6. Slide 7: "In 2024, Canada produced about a quarter of the world's uranium."
7. Minor: slide 6 source line "Canadian Transportation Agency"; slide 2 "the government wants to double"; slide 8 ANCC "in a trade deal".
