# Week 2 site check: Talking trade with Türkiye (index.html) and post text

Checked 2026-10-23 (16:20 to 16:55) by an independent checker. Files checked:
- index.html, current version 16:24:50 (md5 9199e714…). It was rebuilt from site/build_site.py in a scratch copy and is byte-identical; the embedded `<script id="data">` equals data/site.json.
- The page changed once during the check. The 16:18 version became the 16:24 version, with two sentences edited in chapter 1: the US-share sentence and the supplier footnote. Chart data (data/site.json) did not change, so every card and chart check applies to both versions. Both sentences are rechecked below against the 16:24 version.
- post text (md5 7876e2ee…, 16:20).

Evidence used: slides/values.json, slides/facts.json, the analysis outputs, the raw files in analysis/<thread>/raw/ (not in the repository), the published slides (slides/out/*-of-9.jpg, 15:48 render, identical to slides/out) and live official pages (pm.gc.ca, otc-cta.gc.ca, canada.ca, aci.aero, guinnessworldrecords.com, transat.com, natural-resources.canada.ca, international.canada.ca, international.gc.ca, comtradeapi.un.org, statcan.gc.ca). No checked file was edited. No news site was used as evidence.

Rendering: Playwright Chromium at 390 px and 1280 px, light and dark. Every visit item, both tabs of every toggle, every bar, every map province (all 13, by map and by chip), every year of every line and column chart (keyboard and click), every milestone button and every numbered marker were clicked and the card text recorded.

Verdicts: OK; ERROR (with fix); OVERSTATED; UNCLEAR.

## Must fix

1. **Visit list, "Defence": the statement of intent was not agreed in Ankara.** The item, under "What the two countries agreed in Ankara", reads "A statement of intent on defence cooperation and a memorandum that connects Canadian and Turkish defence companies." The Statement of Intent on Defence Cooperation was signed in July 2026, at the NATO Summit. Evidence: PMO release 2026-10-23, quick facts: "In July 2026, the two countries also signed a Statement of Intent on Defence Cooperation"; joint statement 2026-10-22: "building on the recently signed Statement of Intent on Defence Cooperation"; PM remarks 2026-10-22: "When we met here in July for the NATO Summit, we ... signed a new framework for defence cooperation". Fix: "A memorandum that connects Canadian and Turkish defence companies. It builds on a statement of intent on defence cooperation signed in July 2026."
2. **Defence chart cards: wrong ranks and destination counts in five years.** Errors: 2010 "19th largest of 81" should be **of 80**. 2011 "24th of 88" should be **of 87**. 2012 "20th largest of 78" should be **19th of 78**. 2023 "60th largest of 77" should be **61st of 78**. 2024 "4th largest of 77" should be **of 78**. Causes:
   - parse_2010_2013.py counts the row "Not Ranked" from Chart 1 (exports by HDI level) as a destination. That row is $305,340 and $18,537 in 2010 and 2011, and $9,284,339 and $1,446,902 in 2012 and 2013.
   - The same script misses Kuwait in 2012 and 2013, because the cell reads "$ 868,481" with a space.
   - parse_reports.py misses one Table 6 row in both 2023 and 2024. Its parsed sums are $2,112.8M and $2,484.9M; the table totals are $2,143.4M and $2,503.8M.
   - My own parse matches each report's grand total exactly: 2010 $408,513,736; 2011 $634,542,198; 2012 $1,042,277,613; 2013 $681,366,082. For 2023 and 2024 it gives 78 rows summing to $2,143,422,892 and $2,503,825,159.
   - In 2012 the 18 destinations above Türkiye run from Saudi Arabia to Thailand ($6.54M); Türkiye is 19th at $5,865,162.
   - defence/outputs/table6_ranks.json already has 78 and 61. check-report.md flagged the 2023 rank of 61.
   - Fix analysis/defence/outputs/exports_turkiye_2010_2025.csv, then rebuild.
3. **Reference 22 (IRCC work permits) links the wrong file.** The Workers series adds IRCC's *all-purpose* IMP holders (en_odp_annual-tr-work-imp_citz_year_end_all_purpose.xlsx; 2024: 27,500) to TFWP holders (EN_ODP_annual-TR-work-TFW_CITZ_year_end.xlsx; 2024: 175), giving 27,675. Reference 22 links en_odp_annual-tr-work-imp_citz_year_end.xlsx, the *work-purposes-only* file (2024: 13,640), which IRCC says excludes asylum claimants and H&C holders. Evidence: people/scripts/manifest.py lines 17-18; tr_ranks.py line 14; results-followup.md section 3. Fix: link both files the data use. Optionally relabel the tab "Work permits": 13,860 of the 27,500 IMP holders in 2024 held permits for asylum, H&C and similar reasons.
4. **Reference 10 (StatCan CIMT), cited 12 times, opens an error page.** https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1210014701 returns "Error #1: No view found ... Invalid request" (fetched 2026-10-23). StatCan's metadata marks cubes 12-10-0147, 0148, 0150 and 0151 as "CIMT - Default view 01 - INVISIBLE" (trade/raw/meta_121001xx.json). Fix: link the Canadian International Merchandise Trade database (catalogue 71-607-X), and say the cubes were read through StatCan's Web Data Service.
5. **Reference 6 (UN Comtrade) does not show what it describes.** The bare endpoint https://comtradeapi.un.org/public/v1/preview/C/A/HS returns 500 unrelated records (the first has reporterCode 70) and nothing on Türkiye. Fix: link the query used, https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=792&period=2025&flowCode=M&cmdCode=TOTAL&partner2Code=0&motCode=0&customsCode=C00 (market/manifest.json), and its HS2 version, or the Comtrade Plus page.
6. **Travel footnote on the 2025 flight requests is one-sided against its own source.** The page says "In 2025, Air Canada and Air Transat opposed extra Turkish Airlines flights; the Toronto and Montréal airports supported them", citing A-2025-25 and A-2025-77. In A-2025-77 (April 29, 2025), Air Canada opposed and **WestJet supported**; Air Transat did not file. The Agency turned down both requests. Fix: "In 2025, Turkish Airlines twice asked for extra flights. Air Canada and Air Transat opposed; WestJet and the Toronto and Montréal airports supported. The Canadian Transportation Agency turned both down." This adds to the slide 6 line and does not contradict it.
7. **OVERSTATED: "Work permits rose after the February 2023 earthquakes, when Canada eased rules for people from Türkiye."** Two problems:
   - The sentence presents the earthquake measures as the cause. people/results-followup.md section 3 finds that about 38% of the 2022 to 2024 rise was permits held for non-work purposes (asylum claimants, H&C). For the rest, the link to the policy is "an inference from timing, not a published figure".
   - The policy covered nationals of Türkiye **and Syria already in Canada with temporary status** (fee waivers, eased work and study permit rules; IRCC public policy of March 15, 2023, read live).
   - Fix: "Work permits held by citizens of Türkiye rose from 9,415 at the end of 2022 to 27,675 at the end of 2024. Most of the rise came from permits issued from August 2023 to January 2024, while Canada eased rules for people from Türkiye and Syria already in Canada after the February 2023 earthquakes, and from permits held by asylum claimants."
8. **OVERSTATED: the method claims in "How this was done" and the footer.** The page says "Every number on this page is computed from official records by the scripts in the GitHub repository" and "Every number is computed from official data". Three problems:
   - Some numbers come from non-government sources: 120 countries (Guinness World Records), 84.4 million passengers (ACI World), the October 29 start date (Air Transat).
   - Many are typed facts in slides/facts.json, not computed by scripts: 7.2, 20 and 120 GW, 4.8 GW, 12 and 21 flights, 29 permits, $125 million, and the dates.
   - METHODOLOGY.md's table lists 47 numbers (N1 to N47), not every number shown in the cards.
   - Fix: "Every number comes from an official or primary source listed in the References. The numbers built from data tables are computed by the scripts in the GitHub repository, which also holds the full method (METHODOLOGY.md) and a table of the main published numbers."
9. **Subject unclear: "Its first nuclear plant, Akkuyu (4.8 gigawatts), is being built by Russia's Rosatom."** (Energy paragraph.) The sentence before names both Türkiye and Canada ("Canada's CANDU reactors"). Fix: "Türkiye's first nuclear plant, Akkuyu (4.8 gigawatts), is being built by Russia's Rosatom."
10. **Subject unclear in cards: "of its imports" and "of its gas imports".** This affects every supplier card (for example "Canada US$1.16 billion sold to Türkiye in 2025, 0.3% of its imports") and every gas card. Fix: "of Türkiye's imports" and "of Türkiye's gas imports" (site.js lines 185-186 and 326).
11. **Map legend is wrong in light mode.** "Sales to Türkiye in 2025: brighter means more." In light mode the fill is #2378b5 at higher opacity over a light background, so more sales means a *darker* blue (screenshot el-390-light-provMap: Quebec and Ontario darkest). The legend is right in dark mode and on slide 5. Fix: "deeper blue means more", or set the wording per theme.
12. **UNCLEAR: Canada's rank among Türkiye's suppliers.** The rank (47th) counts "Other Asia, nes" (UN Comtrade's entry for Taiwan, US$1.49 billion, 38th) as a partner. Without it Canada is 46th (METHODOLOGY.md N10; check-report.md). The 16:24 version changed the footnote to "Ranks among trading partners ... recorded without a partner", which now matches the method. The Canada supplier card still says "the 47th most of any country" (site.js line 185). Fix the card: "the 47th largest of Türkiye's trading partners". Optionally add to the footnote: "Taiwan, which UN Comtrade lists as 'Other Asia, not elsewhere specified', counts as a partner."
13. **OVERSTATED: visit list, "Legal cooperation: A dialogue on mutual legal assistance and extradition."** The joint statement says the leaders "underscored the importance of initiating a dialogue". No dialogue was agreed or launched. Fix: "The leaders called for starting a dialogue on mutual legal assistance in criminal cases and extradition."

The detailed verdicts follow (sections 1 to 16). The "Minor" list and "Could not check" are at the end of the file.

---

## 1. Header, dek, meta and stamp

| Claim | Verdict | Evidence / fix |
|---|---|---|
| Kicker "The Median Canadian · Week 2" | OK | Style guide line 3: week 2 is Canada and Türkiye |
| Title "Talking trade with Türkiye" | OK | Same as slide 1; PMO 2026-10-23 announces first FTA round, trade mission, EDC MOU |
| Dek "A Canadian PM's first bilateral visit brought agreements on flights, energy and defence. Here is what they mean for Canadians." | OK (minor notes) | Exact slide 1 wording. "first bilateral visit" is the PMO's word (releases 2026-10-06 and 2026-10-23, readout and remarks 2026-10-22). Two minor notes: (a) "agreements on ... energy" calls the ministers' joint statement an agreement (raised on slide 1 already, accepted); (b) the website rule asks for "PM" to be spelled out on first use (style guide line 81): "A Canadian prime minister's first bilateral visit ..." |
| Meta description and og:description (same sentence plus "Explore what they mean for Canadians: trade, duties, provinces, travel, energy and defence.") | OK | Same notes as the dek |
| og:image slides/out/...-1-of-9.jpg | OK | File exists; .gitignore drops only slides/out/*.png, so the JPG is published |
| Stamp "Trade data to August 2026 · Official statements to October 23, 2026" | OK | CIMT cubes end 2026-08 (meta_12100147.json); latest PMO release 2026-10-23 |
| "Scroll to start ↓" | Minor | Style guide line 102: a prompt says what the reader gets ("start what?"). Use "Scroll to learn more ↓" |

## 2. The visit ("What the two countries agreed in Ankara")

| Claim | Verdict | Evidence / fix |
|---|---|---|
| Tag "The visit, October 22 and 23, 2026" | OK | Joint statement and readout dated Ankara 2026-10-22; release dated Istanbul 2026-10-23 says the PM "concluded" the visit. (The 2026-10-06 release announced travel "from October 21 to 24", which includes travel days.) |
| "The first bilateral visit to Türkiye by a Canadian prime minister." [5, 2] | OK | Exact PMO wording in both cited releases |
| Heading "What the two countries agreed in Ankara" | Minor | Once must-fix 1 and 13 are made, two items still are not joint agreements: the 2027 trade mission is a Canadian announcement, and Erdoğan's visit is an invitation. Consider "What came out of the visit" |
| Strategic Partnership: "A three-year action plan in four areas: defence, energy, the economy, and social and diplomatic ties. The foreign ministers oversee it, with a strategic dialogue every year." [1] | OK (minor wording) | Joint statement: a "three-year Action Plan anchored in four pillars" (trade, investment and innovation; energy and climate; defence and security; government-to-government dialogue and people-to-people ties); the leaders "agreed, through their Foreign Ministers, to oversee the implementation"; "establish an annual Canada-Türkiye Strategic Dialogue". The PM's own words are closer to plain English: "trade and investment, defence and security, energy, and the ties between our peoples" |
| Air Transport Agreement: "Signed in Ankara. Each country's airlines may run up to 21 passenger flights a week, up from 12, to any city in the other country. Cargo flights have no limit." [2, 3] | OK (UNCLEAR note) | Readout (Ankara, 10-22): the leaders "signed the newly expanded Canada-Türkiye Air Transport Agreement". Release 10-23: "up to 21 weekly passenger-combination flights per country", "unlimited access to all points in each country", "unlimited weekly all-cargo flights". Note: the joint statement lists "ratify the Canada-Türkiye Air Transport Agreement" as a to-do, so "may run" (present tense) assumes the limits apply before ratification. The PMO also uses the present ("increases"), so this is acceptable |
| Energy: "The two energy ministers signed a joint statement on liquefied natural gas, nuclear power, renewables, clean technology and critical minerals. It has no commitments to buy or sell." [2, 4] | OK | Ministers' statement (signed in Ankara 22/10/2026) has sections on LNG, nuclear, clean power (renewables, clean technologies, CCS, geothermal) and minerals; LNG text only agrees to "facilitate further discussions" with "potential long-term off-takers" |
| Defence: "A statement of intent on defence cooperation and a memorandum that connects Canadian and Turkish defence companies." [1, 2] | **ERROR** | Must fix 1: the statement of intent dates from July 2026 |
| Export finance: "Export Development Canada and Türk Eximbank signed a memorandum to support business opportunities in other countries." [3, 2] | OK | Release: MOU "to cooperate on projects in third countries"; readout: "to support commercial opportunities in third-country markets" |
| Free trade talks: "The first round runs from November 30 to December 4, 2026, in Ankara." [2] | OK | Release 10-23, same dates and city |
| Legal cooperation: "A dialogue on mutual legal assistance and extradition." [1] | **OVERSTATED** | Must fix 13 |
| Next visits: "A Canadian trade mission to Türkiye in 2027, led by the trade minister, and an invitation for President Erdoğan to visit Canada." [2, 1] | OK | Release: trade mission in 2027 "to be led by the Minister of International Trade"; joint statement: "Türkiye welcomed the invitation" |
| Accordion | OK | All eight open and close; aria-expanded toggles; the sign changes from "+" to "−" |

## 3. Chapter 1, The opportunity

| Claim | Verdict | Evidence / fix |
|---|---|---|
| Heading "Türkiye is a big market where Canada sells little" | OK | Same as slide 2 |
| "Türkiye imported US$365 billion of goods in 2025, and 0.3% came from Canada." [6] | OK | 365,369,912,607; Canada 1,162,832,980 = 0.318% (market/outputs CSVs; equals Comtrade raw per check-report) |
| "Canada sold 72% of its goods to the United States in 2025, its smallest share since at least 1999." [7] (16:24 wording) | OK | 562,698,185.1 / 778,004,358.6 = 72.33%; lowest in 1999 to 2025 (next lowest 2020 73.28%, 2011 73.64%). Table 12-10-0011 gives 1997 81.8% and 1998 84.8%, so "since at least 1999" holds. The 16:18 wording ("in records going back to 1999") implied that records start in 1999; it is fixed |
| "Canada's government wants to double sales to other countries within a decade." [8] | OK | PMO 2025-10-29 (Singapore): "the government's ambitious new mission to double our non-U.S. exports in the next decade" (fetched) |
| Chart title "What Türkiye's 86 million people bought in 2025, and the part from Canada" [6, 9] | OK | Population 86,092,168 (TurkStat ABPRS 2025, check-report) |
| Tab "Türkiye's top buys": 15 chapters, values and cards | OK | All 15 bars and cards match tur_imports_2025_hs2_world.csv and _canada.csv. Examples: energy US$62.5B, Canada US$38M, 0.06%; optical US$7.73B, Canada US$135M, 1.7%; aircraft US$5.42B, US$175M, 3.2% |
| Tab "Canada's top sales": 15 chapters | OK | Order matches the Canada CSV (HS 07 US$185M, 88 US$175M, 90 US$135M, 84 US$125M, 71 US$97M, ...). Card: vegetables US$1.09B from the world, US$185M from Canada, 17.0% (184.75/1,085.94 = 17.01%) |
| Chapter names | OK (minor) | "Vegetables, incl. lentils and chickpeas" for HS 07, "Energy: oil, gas and coal" for HS 27 and the others are fair plain names. Minor: "Cars and parts" for HS 87 also covers trucks and tractors; "Vehicles and parts" is more exact |
| Chart title "Who sells to Türkiye: Canada was its 47th-largest supplier in 2025" [6] | OK with the 16:24 footnote | 47th among trading partners, counting "Other Asia, nes" (Taiwan); 46th without it. The card still says "of any country" (must fix 12) |
| Supplier bars 1 to 12, gap "13th to 46th", 47 Canada | OK | Values and shares match tur_imports_2025_by_partner.csv after dropping "Special Categories" and "Areas, nes" (China 13.57%, Russia 11.60%, Germany 8.24%, US 4.95%, ...) |
| Supplier cards | OK (wording) | Numbers right. "of its imports" is must fix 10 |
| Footnote (16:24) "Ranks among trading partners. Another 5.7% of Türkiye's imports was recorded without a partner." | OK | Special Categories 20,816.0M + Areas nes 87.8M = 5.72%; consistent with the ranking |
| Chart "Share of Canada's goods sold to the United States, 1999 to 2025" [7] and its cards | OK | All 27 years match values.json us_share_series (stepped through with the keyboard: 2025 72.3%, 2002 87.1%, 1999 86.7%); y axis 0 to 100% |
| Footnote on two sets of records [6, 10] | OK | Comtrade (Türkiye's imports, US$, CIF) and CIMT (Canada's exports, C$) |

## 4. Chapter 2, Trade deficit

| Claim | Verdict | Evidence / fix |
|---|---|---|
| Heading "Canada buys more from Türkiye than it sells" | OK | 2025 imports $3,197.3M against exports $1,137.4M |
| "The trade deficit was $2.1 billion in 2025. It shrank by almost a quarter from January to August 2026." [10] | OK (minor wording) | $2,059,962,307. Jan to Aug deficit 1,522.0M (2025) to 1,164.8M (2026), down 23.5%. Same wording as slide 3. The earlier slide check noted it can read as a change *during* those months; the paragraph below makes the comparison clear |
| "Canada sold Türkiye $1.14 billion of goods in 2025 and bought $3.20 billion." | OK | 1,137,350,532; 3,197,312,839 |
| "The last year Canada sold more than it bought was 2011." | OK | 2011: 1,271.5M sold, 1,122.7M bought; deficit every year from 2012 to 2025 and in Jan to Aug 2026 |
| "From January to August 2026, Canada sold 8% more to Türkiye and bought 14% less than a year earlier." | OK | +7.68%, -13.66% (results_totals.json) |
| Line chart, 1988 to 2025, every year's card | OK | All 38 cards match series_exports_b and series_imports_b; surplus and deficit labels flip correctly (surplus 1988 to 1997 and 2007 to 2011). y axis $0B to $5B, data max $3.18B: correct, but 36% headroom (minor, see layout) |
| "What Canada sold and bought in 2025" bars and cards, both tabs | OK | All 20 bars and cards match hs2_chapters_2021_2025.csv. Sold: 07 $221.7M (19.5%), 84 $188.0M, 88 $176.2M, 90 $99.7M, 87 $82.7M, 72 $56.4M, 85 $45.4M, 27 $39.7M, 10 $32.6M, 48 $25.4M. Bought: 84 $405.2M (12.7%), 72+73 $308.1M, 08+20 $258.6M, 30 $247.3M, 61+62 $220.1M, 87, 85, 76, 57, 89. Five-year mini bars and labels match |
| Footnote "all exports to Türkiye (made in Canada or re-exported) and imports from Türkiye. Figures for 2026 can still be revised." [10] | OK | Total exports basis (trade/results.md line 25) |

## 5. Chapter 3, Duties

| Claim | Verdict | Evidence / fix |
|---|---|---|
| Heading "A trade deal could help farmers and shoppers" | OK | Hedged takeaway; same as slide 4 |
| "Türkiye charges 19.3% on Canadian lentils, and Canada about 17% on Turkish clothing." [11, 12] | OK | Red lentils (07134095, $115.2M) and green lentils (07134094, $41.2M) are at 19.3%; seed lentils 0%; organic lines 14.5%. Clothing: duty $38.32M on $220.14M = 17.4% (HS 61 and 62) |
| "On the Canadian-made goods sold to Türkiye in 2025, duties come to an estimated $64 million, 6.4% on average." | OK (minor) | Recomputed from ca_exports_to_TR_2025_est_tr_duty.csv without HS 1001: base $1,000.53M, duty $64.41M, 6.44%. Minor: the base leaves out durum wheat (footnote), so "Canadian-made goods" is not the full $1.03 billion. Add "other than durum wheat" to the sentence, or "(without durum wheat)" to the card title "$1.00 billion" |
| "On Turkish goods sold to Canada, they come to about $105 million, 3.3%." | OK | $105.32M on $3,197.31M = 3.29% |
| "Lower duties could also bring Canadian clothing makers more competition." | OK | Hedged with "could" (slide 4 wording) |
| Summary card, Canadian goods: "$1.00 billion · 47% duty-free · 53% pays duty · $64 million, 6.4%" | OK | Duty-free share 46.64% |
| Summary card, Turkish goods: "$3.20 billion · 67% · 33% · $105 million, 3.3%" | OK | 67.05% |
| 12 bars per tab and their cards | OK | All 24 recomputed. Canadian side: 07 $36.4M on $221.0M (16.5%, 91% pay); 87 $6.57M on $66.6M; 84 $5.07M on $134.7M (50% pay); 10 $1.91M on $3.80M (canary seed 50%); 71 $0.947M on $2.21M (42.8%). Turkish side: 62 $19.21M on $111.24M (17.3%); 61 $19.11M on $108.90M (17.5%); 57 $14.12M on $106.92M (13.2%); 87 $7.61M on $151.39M |
| Footnote: durum wheat left out because it "can enter Türkiye duty-free when used to make exports" [15] | OK | Inward processing regime (WTO TPR S/439; tariffs/results.md line 163) |
| Footnote: "Türkiye's 10% rate on green lentils ended on April 30, 2026; since May 1, green lentils pay 19.3%, like red lentils." [11] | OK | Import regime list I footnote 5: 10% until 2026-04-30 (tariffs/results.md line 107) |
| Footnote: "Canada's figure uses its regular rates; anti-dumping duties and surtaxes on some steel come on top." [12] | OK | MFN rates; nine SIMA measures and steel surtax quotas name Türkiye (tariffs/results.md) |
| Chart heading "Estimated duty by product, 2025 trade at 2026 rates" | OK | No citation on the heading itself; the paragraph above and the footnote cite the sources |

## 6. Chapter 4, Who sells (provinces)

| Claim | Verdict | Evidence / fix |
|---|---|---|
| Heading "Three provinces have the most at stake" | OK | Same as slide 5 |
| "Quebec, Ontario and Saskatchewan make three-quarters of Canada's sales to Türkiye." [10] | OK | 789.4M of 1,029.35M domestic exports = 76.7% (provinces_2021_2025.csv). This holds on the domestic-exports basis that the footnote names (on total exports it would be 69%) |
| "Saskatchewan's lentil sales to Türkiye fell by almost two-thirds from 2022 to 2025." [10] | OK | 366.0M to 130.0M, down 64.5% |
| 13 province cards (each checked by chip and by map path; chip and path highlight stay in step) | OK, except NWT | Sales, five-year mini bars, shares, imports cleared and census counts all match the CSVs. Examples: Quebec $310M (30.1%), imports $1.17B, 15,620 of Turkish origin, 8,340 born in Türkiye; Ontario $275M (26.7%), $1.39B, 43,555, 25,995; Saskatchewan $205M (19.9%), $59M, 695, 310; B.C. $111M, $196M, 8,075, 4,250; Alberta $82M, $135M, 6,670, 3,135. Yukon and Nunavut show "No recorded sales" (0 in 2025); Nunavut cleared $5.86M (provinces CSV) |
| NWT: "$3,000 of goods made in Northwest Territories ..., 0.00% of Canada's total" | Minor | The value is $2,500 (values.json). money() rounds to thousands, and the share displays as 0.00%. Show "$2,500, less than 0.01% of Canada's total" |
| Top products, the five largest sellers | OK | Same as slide 5 (Quebec aircraft $162M = 880240 + 880230; Ontario cars $43M = all of 8703.21 to 8703.90). They match province_top_hs6.csv |
| Top products, other provinces | OK (minor names) | NL: steel scrap $25.2M, newsprint $1.19M, surveying-equipment parts $0.55M. NS: cars $2.8M (8703 lines summed), fertilizer $1.8M, frozen fruit $1.56M. MB: blood products $2.29M, other pulses $1.24M, medicines $1.09M. NB: drilling-machinery parts $681K, wood pulp $539K, pressure gauges $194K. PEI: food-processing machinery $68K, vegetable oils $61K, "Turbine parts" $28K. Minor: HS 841191 is parts of turbojets and turboprops, so "Aircraft engine parts" is clearer than "Turbine parts". HS 071339 is beans not elsewhere specified ("Other pulses" is acceptable, and it is the slide's term for Alberta) |
| Map shading | OK in dark, **ERROR in light** | Must fix 11 (legend says "brighter"; light mode is darker for more) |
| Footnote: "Goods made in each province, by province of origin, 2025. Turkish origin: people who reported Turkish ethnic or cultural origin, alone or with others, in the 2021 Census." [10, 16] | OK | eth_total is single plus multiple responses |
| Yukon "15 people of Turkish origin and 20 people born in Türkiye" | OK | That is what the census shows (random rounding to 5; people born in Türkiye can report other origins). Reads oddly but is right |

## 7. Chapter 5, Travel and people

| Claim | Verdict | Evidence / fix |
|---|---|---|
| Heading "Canadians get more choice of flights" | OK | Same as slide 6 |
| "Istanbul is a global hub: Turkish Airlines flew to 120 countries in 2024, more than any other airline." [17] | OK | Guinness (fetched): "Most countries flown to by an airline", Turkish Airlines, 120, "based on the past year from September 2023 to September 2024", achieved 21 October 2024. The reference states the period |
| "The new agreement allows up to 21 flights a week for each country, up from 12, to any city." [2] | OK | PMO release (see section 2; ratification note there) |
| "Istanbul Airport handled 84.4 million passengers in 2025, eighth in the world." [18] | OK | ACI World, 15 July 2026 (fetched): IST 84,437,710, rank 8 (7 in 2024) |
| Flights graphic: "12 passenger flights a week for each country before, up to 21 under the new agreement"; bar widths 57% and 100% | OK | 12/21 = 57.1% |
| Chart "Trips to Türkiye by Canadians each year, 2010 to 2025" [19], all 16 cards | OK (minor) | Values match turkiye_border_canada.json. I re-ranked the 2025 bulletin sheet "C-Mil Göre G.Yabancı" (only the "TOPLAM" aggregate dropped): 2010 29th, 2012 31st, 2014 35th, 2019 52nd, 2025 31st, all as shown. Minor: the page never says what is counted (entries into Türkiye on Canadian passports, including Canadians living abroad and repeat trips; people/results.md line 253), which the slide check asked the website to explain |
| People chart, Permanent residents, all 11 cards | OK | pr_turkey_by_year.csv: 2015 870 (51st) ... 2021 4,625 (17th) ... 2025 1,895 (37th) |
| People chart, Students, 10 cards | OK | study_dec31: 2015 2,195 (21st) ... 2024 4,650 (30th) |
| People chart, Workers, 10 cards | **ERROR (source)** | The numbers are right for all-purpose IMP plus TFWP (2024: 27,500 + 175 = 27,675). The reference links the wrong file (must fix 3), and the label overstates (about half are asylum or H&C permit holders) |
| "76,745 people in Canada reported Turkish origin in the 2021 Census. Where they lived, by city:" and 11 bars | OK (minor) | All 11 match census_turkish_by_geo.csv (Toronto 28,490 ... Québec 260). Minor: these are census metropolitan areas; "by metropolitan area" is more exact |
| Footnote: "In 2025, Air Canada and Air Transat opposed extra Turkish Airlines flights; the Toronto and Montréal airports supported them." [23, 24] | **OVERSTATED (incomplete)** | Must fix 6: WestJet supported in A-2025-77; both requests were denied |
| Footnote: "Air Transat starts flying from Montréal to Istanbul on October 29, 2026." [25] | OK | Transat release, May 29, 2026 (fetched): from October 29, 2026, year-round, twice weekly, A330 |
| Footnote: "Work permits rose after the February 2023 earthquakes, when Canada eased rules for people from Türkiye." [26] | **OVERSTATED** | Must fix 7 |
| Footnote: "Permanent residents are shown to 2025; IRCC's 2026 figures run to August." [20] | OK | pr_turkey_by_year.csv has 2026 (4,420, partial). Minor: spell out IRCC on first use |

## 8. Chapter 6, Energy

| Claim | Verdict | Evidence / fix |
|---|---|---|
| Heading "Türkiye's nuclear plans open a door for Canada" | OK | Same as slide 7 |
| "Türkiye aims for over 20 gigawatts of nuclear power by 2050 and is studying Canada's CANDU reactors." [27, 28] | OK | MENR 2023-09-25 "over 20 GW ... by the end of 2050"; TÜNAŞ and AtkinsRéalis MOU of March 2026 for "a detailed assessment of the applicability of Canada's CANDU reactor technology" |
| "Its first nuclear plant, Akkuyu (4.8 gigawatts), is being built by Russia's Rosatom." [29, 30] | **ERROR (subject)** | Must fix 9. Facts OK: four VVER-1200 units under construction (PRIS); Invest in Türkiye gives 4.8 GW |
| "Türkiye also plans 120 gigawatts of wind and solar power by 2035 and net zero emissions by 2053." [31, 29] | OK | MENR 2024-11-04 "120 thousand megawatts of solar and wind installed capacity by 2035"; Invest in Türkiye "Net Zero 2053" |
| "In 2024, Canada produced about a quarter of the world's uranium." [32] | OK | NRCan (fetched): "24% of global production in 2024" |
| Power bars and cards (5) | OK (minor) | 39.228 GW (EPİAŞ 14.12.2025: solar 24,682 + wind 14,546 MW); 120; 4.8; 7.2; "over 20". "About three times December 2025": 120 / 39.2 = 3.06, OK. "By the end of 2035, Türkiye wants 7.2 gigawatts of nuclear power, including Akkuyu": the source says an *addition* of 7.2 GW, and Türkiye had no operating reactor, so the total is 7.2 GW including Akkuyu (inference, OK). Minor: "Canada's CANDU reactors are being studied for it" ties the study to the 2050 goal. AtkinsRéalis says the MOU supports plans "adding three additional nuclear reactors", so write "studied for Türkiye's new reactors" |
| Gas bars and cards (8) [34, 35] | OK (wording) | Russia 21.16, Azerbaijan 11.918, US LNG 9.473, Iran 7.702, Algeria LNG 4.441, Nigeria LNG 0.874, others 2.767 (465 mcm of it Turkmen pipeline gas, so "mostly LNG" is right); total 58.335; shares 36%, 20%, 16%, 13%, 8%, 1%, 5%. "of its gas imports" is must fix 10 |
| Canada LNG bar and card: "Canada 3.1 billion m³ of liquefied natural gas exported in 2025, all of it, about 5% of what Türkiye imported." | Minor (wording) | 3.11 bcm (CER, marine; 3.14 with trucks); 3.11 / 58.335 = 5.3%. The phrase "all of it" is clumsy, and a reader of a chart titled "Where Türkiye's natural gas came from" may take the blue bar as a supplier. Suggest the label "For comparison: all of Canada's LNG exports in 2025" and the card "Canada exported 3.1 billion m³ of liquefied natural gas in 2025, to all buyers, equal to about 5% of Türkiye's gas imports. None went to Türkiye." (EPDK lists Canada at 0) |
| Energy sales columns 2021 to 2025 and cards [10] | OK | HS 27 total exports: 139.0, 156.1, 60.7, 2.7, 39.7 ($M). "Mostly coal from British Columbia" for 2025: B.C. coal (270112) $37.4M of $39.7M |
| Footnote: "The energy statement the two countries signed in October 2026 has no commitments to buy or sell. Türkiye's state nuclear company and AtkinsRéalis signed a memorandum in March 2026 to study CANDU technology for Türkiye." [4, 28, 36] | OK | See section 2; AtkinsRéalis release 2026-03-03 (fetched) |

## 9. Chapter 7, Defence

| Claim | Verdict | Evidence / fix |
|---|---|---|
| Heading "Military sales to Türkiye are back, with conditions" | OK | Notice 1108 (fetched): applications "reviewed on a case-by-case basis"; end-use assurances; exports $107.9M in 2024 and $60.8M in 2025 |
| "Canada's government says linking the two defence industries will create jobs and exports." [2] | OK | Release: the MOU "will connect Canadian and Turkish companies ..., creating good jobs at home, export opportunities abroad" |
| "Türkiye has NATO's second-largest military." [2, 37] | OK | Release: "NATO's second-largest standing military"; NATO 2026e personnel 395,800 |
| "Canada's military exports to Türkiye are mostly imaging and targeting equipment." [38] | OK | ECL 2-15 and 2-5 dominate every large year (2019: $116.0M and $59.8M; 2024: $104.6M and $23.8M; 2025: $58.5M and $56.5M of $60.8M) |
| Column values 2010 to 2025 | OK | All 16 match the report tables (values.json military_m) |
| Card ranks and "of N destinations" | **ERROR in 2010, 2011, 2012, 2023, 2024** | Must fix 2. The other years are correct: 2013 29th of 91, 2014 26th of 91, 2015 22nd of 90, 2016 25th of 94, 2017 5th of 90, 2018 3rd of 89, 2019 3rd of 82, 2020 3rd of 83, 2021 39th of 77, 2022 62nd of 77, 2025 7th of 84 (2025 Figure 2 order: Saudi Arabia, Germany, Poland, Ukraine, United Kingdom, Netherlands, Türkiye) |
| 2026 column: "No figures yet. No 2026 figures have been published." | Minor | "yet" is relative to the present (time-relative rule). Use "No figures published for 2026" |
| Band "Open / Suspended / Reopened" (to Oct 2019, to Jan 2024, after) | OK | Boundaries at 2019.75 and 2024.0. Matches the 2019 suspension and Notice 1108 (2024-01-23) |
| Milestones 1 to 5 (buttons and circles both select the right year: 2019, 2021, 2024, 2025, 2026) | OK | Same text as slide 8. "Permit to broker $125 million of Turkish ammunition for Ukraine": 2025 report Table 16 (fetched) lists destination Ukraine, ECL 2-3, $125,000,000, origin Türkiye. "Reopened case by case. Türkiye must say if goods will go to a country outside NATO": Notice 1108 asks for that statement where a Turkish government body is the end user (Ukraine excepted); a simplification, accepted on the slide |
| Footnote: "The reports leave out most exports to the United States, which need no permit, so ranks are among other destinations." [38] | OK | 2025 report data notes |
| Footnote: "The Armenian National Committee of Canada asks that Canada keep full control of export permits in a trade deal." [39] | OK | ANCC 2026-09-24: "Preserve Canada's full authority over export and brokering permits" |
| Footnote: "Canada can cancel permits if goods are misused." [40, 41] | OK | Notice 1108; Garneau statement 2021-04-12 |

## 10. Chapter 8, What comes next

| Claim | Verdict | Evidence / fix |
|---|---|---|
| Heading "Free trade talks start in Ankara on November 30" | OK | Release 10-23 |
| "A deal could lower duties in both countries. Once its terms are public, we will break them down in a new post." | OK | Style guide line 37 allows the follow-up promise |
| Oct 29: Air Transat starts Montréal to Istanbul [25] | OK | Transat release |
| Nov 9 to 20: Türkiye hosts COP31, the UN climate conference, in Antalya [1] | OK | Joint statement: "to be held in Antalya on 9-20 November 2026" |
| Nov 30 to Dec 4: first round of free trade talks, in Ankara [2] | OK | Release |
| 2027: Canadian trade mission to Türkiye, led by the trade minister [2] | OK | Release; remarks name Minister Sidhu |
| "Date to be set: President Erdoğan visits Canada" [1] | Minor | Joint statement: "Türkiye welcomed the invitation ... at a mutually convenient time"; the readout speaks of a state visit "in the near future". No visit is set, so "Invitation for President Erdoğan to visit Canada" is exact (same wording as slide 9, so optional) |

## 11. "How this was done" and footer

| Claim | Verdict | Evidence / fix |
|---|---|---|
| "Every number on this page is computed from official records by the scripts in the GitHub repository" | **OVERSTATED** | Must fix 8 |
| "... which also holds the full method (METHODOLOGY.md) and a table of every published number." | UNCLEAR | METHODOLOGY.md (16:22, untracked; the GitHub repo holds only "Initial commit" with README) lists N1 to N47. It does not cover the card figures (ranks, years, products). The file must be pushed before the link is true; and "the main published numbers" is accurate |
| "News stories were used only to find official documents." | OK | No news outlet in the references. newswire.ca is NRCan's own release on Cision's wire ("News provided by Natural Resources Canada"); I found no canada.ca copy |
| Trade, Duties, Travel and people, Energy, Defence source summaries | OK (minor) | Match the references. Travel leaves out Guinness, ACI and Air Transat; Energy leaves out Invest in Türkiye and AtkinsRéalis; Defence leaves out NATO. Minor: EPİAŞ, IAEA and IRCC are not spelled out |
| Caveat "Two sets of trade records ... timing, valuation and currency" | OK | |
| Caveat "Türkiye charges duty on the value including freight and insurance ... so the Canadian-goods figure is a low estimate. Duties charged per tonne are left out." | Minor | CIF valuation pushes the estimate up. Duty relief regimes beyond durum (inward processing; the civil-aircraft end-use assumption of 0%) push the other way (tariffs/results.md line 163). "is likely on the low side" is safer. The per-tonne point is OK (results.md line 130) |
| Caveat "The reports count permits used, and leave out most exports to the United States." | OK | defence/results.md lines 7 to 9 |
| Caveat "Monthly trade for 2026 can still be revised." | OK | |
| Footer "Every number is computed from official data; methods and code are on GitHub." | **OVERSTATED** | Must fix 8 |
| Footer licence line; link to REPO/blob/main/LICENSE | UNCLEAR | LICENSE (Apache 2.0) exists locally since 16:22 but is untracked and not pushed; the link works only after the push |

## 12. References (41) and citations

No news sites. Each link was fetched on 2026-10-23 (status, title and content checked).

| # | Reference | Verdict | Evidence / fix |
|---|---|---|---|
| 1 | PMO joint statement, Oct 22, 2026 | OK | Title matches |
| 2 | PMO news release, Oct 23, 2026 | OK | |
| 3 | PMO readout, Oct 22, 2026 | OK | |
| 4 | NRCan and MENR energy joint statement (newswire.ca) | OK (minor) | Not a news outlet: Cision wire carrying "News provided by Natural Resources Canada". Use a canada.ca copy if one appears |
| 5 | PMO news release, Oct 6, 2026 | Minor | Full title "Prime Minister Carney to visit Türkiye to advance partnership across trade and investment, energy, and defence" |
| 6 | UN Comtrade | **ERROR** | Must fix 5 |
| 7 | StatCan 12-10-0171-01 | OK | |
| 8 | PMO news release, Oct 29, 2025 | Minor | Full title ends "... partnerships with Singapore"; the URL redirects to the shorter slug and works |
| 9 | TurkStat ABPRS 2025 | OK | Page loads (script-rendered); check-report confirmed the figure |
| 10 | StatCan CIMT tables 12-10-0147 etc. | **ERROR** | Must fix 4 (error page). The description also names four tables but links one |
| 11 | Türkiye Ministry of Trade import regime 3350/3351 | OK | |
| 12 | CBSA Customs Tariff 2026 | OK | |
| 13 | Resmî Gazete, Decision 10781, Dec 30, 2025 | OK | PDF: "Karar Sayısı: 10781, 30 Aralık 2025" |
| 14 | StatCan CIMT 2025 data files, "domestic exports (HS8) and imports (HS10)" | Minor | Links only CIMT-CICM_Imp_2025.zip; add the domestic exports file |
| 15 | WTO TPR WT/TPR/S/439, 2023 | OK | PDF dated 1 February 2023 |
| 16 | StatCan 2021 Census 98-10-0356-01 | OK | |
| 17 | Guinness World Records | OK | Period matches the page |
| 18 | ACI World, July 15, 2026 | OK | |
| 19 | Türkiye Ministry of Culture and Tourism yearly bulletins | Could not open | Empty reply and fetch error; the saved bulletins were used |
| 20 | IRCC PR by citizenship | OK | "January 2015 - August 2026"; Turkey 2026 total 4,420 |
| 21 | IRCC study permit holders on Dec 31 | OK | Turkey 2024 4,650 |
| 22 | IRCC IMP and TFWP holders on Dec 31 | **ERROR** | Must fix 3. The linked file is "IMP work permit holders (for work purposes only)", Turkey 2024 13,640; the chart shows 27,675 |
| 23 | CTA A-2025-25, Feb 14, 2025 | OK | |
| 24 | CTA A-2025-77, Apr 29, 2025 | OK (see must fix 6) | |
| 25 | Air Transat release | Minor | Add the date (May 29, 2026) |
| 26 | IRCC earthquake public policy | OK | Title "Temporary Public Policy for nationals of Türkiye and Syria affected by the earthquakes of February 6, 2023" |
| 27 | MENR Sep 25, 2023 | OK | |
| 28 | MENR CANDU memorandum, March 2026 | OK | |
| 29 | Invest in Türkiye energy page | OK | |
| 30 | IAEA PRIS: Türkiye | Minor | The old link redirects (302) to the generic https://pris-stats.iaea.org home page; link the new Türkiye page |
| 31 | MENR Nov 4, 2024 | OK | |
| 32 | NRCan uranium facts | OK | |
| 33 | EPİAŞ daily bulletin Dec 14, 2025 | OK | |
| 34 | EPDK 2025 natural gas report | OK | "2025 Yılı Doğal Gaz Piyasası Gelişim Raporu" |
| 35 | CER LNG shipment detail CSV | OK | |
| 36 | AtkinsRéalis Mar 3, 2026 | OK | |
| 37 | NATO defence expenditure 2026 | OK | PDF loads |
| 38 | GAC Reports on Exports of Military Goods, 2010 to 2025 | Minor | Links the 2025 report only |
| 39 | ANCC submission, Sep 24, 2026 | OK | Advocacy group, cited only for its own position |
| 40 | GAC Notice to Exporters 1108 | OK | Issued 2024-01-23, modified 2024-01-29 |
| 41 | GAC Garneau statement, Apr 12, 2021 | OK | |

Citation placement: every superscript was checked against the sentence it follows. All support their sentences except:
- [1, 2] on the Defence item (the sources date the statement of intent to July: must fix 1);
- [1] on Legal cooperation (must fix 13);
- [22] on the people chart (must fix 3);
- [23, 24] on the CTA sentence (incomplete: must fix 6).

Minor numbering issue: references 1, 3 and 4 are first cited inside the collapsed visit items, so the first visible superscript reads "2,5".

## 13. Wording rules (whole page, all card texts, hidden items, aria labels and meta)

| Rule | Verdict | Evidence |
|---|---|---|
| No em dashes | OK | No U+2014 or &mdash; (build asserts it; I rescanned). En dashes appear only in CMA names (Ottawa–Gatineau, Kitchener–Cambridge–Waterloo) |
| No "now", "today", "currently" | OK | The only hit is the URL parameter "current=TR". "No figures yet" (2026 defence card) is relative to the present: minor |
| No "won", "lost", "carried", "beat" | OK | None |
| No "our analysis", "our estimate" | OK | Only "we will break them down in a new post" (allowed) |
| No contrast framing ("X, not Y") | OK | None found (", not", "rather than", "instead of", "not only" all absent) |
| No contractions (post text) | OK | None on the page or in the post text |
| Subject clear where two countries are named | **ERROR** | "Its first nuclear plant" (must fix 9); "of its imports" and "of its gas imports" (must fix 10); "Canada's CANDU reactors are being studied for it" (minor). "Canada's government" is used correctly in chapters 1 and 7 |
| First-time claim uses the source's word | OK | "first bilateral visit" in the dek, the visit lead, meta and caption; "first nuclear plant" for Akkuyu matches Invest in Türkiye |
| Plain news-style English | Minor | Clumsy: "of liquefied natural gas exported in 2025, all of it, about 5% ..." (gas card); "Scroll to start". Jargon not spelled out at first use: PM, IRCC, LNG (first visible use is in the gas chart), EPİAŞ, IAEA |

## 14. Charts, layout and console

| Check | Verdict | Evidence |
|---|---|---|
| Console and page errors | OK | No console messages, page errors or failed requests at 390 and 1280, light and dark |
| Sideways scrolling | OK | scrollWidth equals clientWidth (390 and 1280). The only elements past the edge are the province chips, inside their own horizontal scroller (.chips overflow-x:auto) |
| Light and dark themes | OK | Body background and text tokens switch; the wordmark switches to logo-dark.png; the charts read well in both (screenshots charts-*.png in my scratch folder) |
| SVG labels clipped or overlapping | OK (two minor) | No text outside any SVG viewBox and no text overlapping another, at either width (bbox check). Minor: (a) at 390 px the "Reopened" band label runs 8 px past its band, to the SVG's right edge; (b) at 390 px the value label above the selected column sits mostly over the neighbouring column for end years. For example "1,895" (2025) sits mostly over the 2024 bar: 13 to 33% overlap with the selected column, because the label is right-anchored at the column centre |
| Scales match data | OK | All bars start at 0; every bar width was checked against the card values. Line and column axes: US share 0 to 100%; trade $0 to $5B (max $3.18B); trips 0 to 500K (max 321K); PR 0 to 5K (max 4,625); energy $0 to $200M (max $156M); defence $0 to $200M (max $151M). Minor: scale() jumps from 2.5 to 5, which leaves 36 to 40% empty space in the trade and trips charts |
| Axis year labels | OK | Labels thin out at 390 px and the selected year is bold; no collisions |
| Map | OK in dark; light-mode legend wrong (must fix 11) | All 13 paths are clickable and keyboard focusable; selection outline and chip stay in step |
| Desktop typography | Minor | At 1280 px the citation "6" after "came from Canada." wraps to a line of its own (chapter 1 line) |
| Chip row at 390 px | Minor | The scrollbar is hidden, so only the cut-off fourth chip shows that more provinces exist |

## 15. Site against slides (shared numbers)

Every number the site shares with the slides is read from slides/values.json by both builders, and they agree:
- Slide 2: US$365B, 0.3%, 86 million, and the five chapters with their Canada parts; 72%; the goal to double sales.
- Slide 3: $2.1B deficit, almost a quarter, +8% and -14%, and the ten receipt lines.
- Slide 4: 19.3%, about 17%, $1.0B, 47/53, $64M, 6.4%, $3.2B, 67/33, $105M, 3.3%.
- Slide 5: province totals and top products, three-quarters, almost two-thirds.
- Slide 6: 120 countries in 2024, 21 and 12, 139,164 and 321,271, the CTA line.
- Slide 7: over 20 GW, 7.2 GW, 4.8 GW, 39 GW, 120 GW, a quarter of the uranium, the energy statement line.
- Slide 8: $151M in 2019, $108M in 2024, the five milestones, the ANCC and cancellation lines.
- Slide 9: the four dates.

Differences are precision and labels only, for example $1.14 billion against $1.1 billion, and "Machinery and engines" against "Machinery". Nothing on the page contradicts a slide.

Three fixes above add detail to text the slides also carry, without contradicting them: the CTA line (must fix 6), the light-mode legend (must fix 11) and the visit's Defence item (must fix 1; slide 8's milestone 5 "Agreement to link the two countries' defence industries" is correct).

## 16. Post text (week03/build/post-text.md)

| Part | Verdict | Evidence / fix |
|---|---|---|
| "Canada's trade talks with Türkiye, in numbers 🇨🇦📊" | OK | Playbook caption template |
| "Mark Carney's visit on October 22 and 23, 2026, the first bilateral visit to Türkiye by a Canadian prime minister, brought agreements on flights, energy and defence." | OK (minor) | Dates as in section 2; exact PMO phrase. Same "agreements on ... energy" note as the dek |
| "Swipe to see 👉" and the eight bullets | OK | Bullets equal the headlines of slides 2 to 9 word for word |
| "For the full story and more insights, the link is in the bio 🔗" | OK | Template |
| Short description | OK | Each item maps to a slide; "the return of military sales" matches slide 8 |
| Story line "Week 2: Talking trade with Türkiye 🇨🇦🇹🇷" | OK | Template example |
| WhatsApp "For those curious about Canada's trade talks with Türkiye, here is my quick analysis: <post link>" | OK | Template wording; "<post link>" must be replaced with the post's URL when sent |
| Em dashes, contractions, now/today, won/lost/carried/beat | OK | None |

## Minor

Wording:
1. Dek and caption: "agreements on flights, energy and defence" calls the energy joint statement an agreement. This was raised on slide 1 and accepted; keep it knowingly.
2. Spell out jargon at its first use on the website (style guide line 81): "PM" in the dek, "IRCC" (travel footnote), "LNG" (first visible in the gas chart), "EPİAŞ" and "IAEA" ("How this was done").
3. "Scroll to start ↓" should be "Scroll to learn more ↓" (style guide line 102).
4. Visit heading "What the two countries agreed in Ankara". After must fix 1 and 13, the trade mission is still a Canadian announcement and Erdoğan's trip an invitation. Consider "What came out of the visit".
5. Strategic Partnership pillars: the PM's own wording is plainer ("trade and investment, defence and security, energy, and the ties between our peoples").
6. Air Transport Agreement: the joint statement says the leaders agreed to "ratify" it, so "may run up to 21" assumes the limits already apply. The PMO uses the present tense too ("increases"), so this is acceptable; "will allow" is safer.
7. (Resolved in the 16:24 version: "its smallest share since at least 1999".)
8. "Cars and parts" for HS 87 (Türkiye's buys and Canada's sales) also covers trucks and tractors: "Vehicles and parts".
9. Duties: the $1.00 billion base and the $64 million leave out durum wheat. Say so in the sentence or the card title, beyond the footnote.
10. Caveat "so the Canadian-goods figure is a low estimate" should be "is likely on the low side". Duty relief regimes can push the true figure down.
11. NWT card: "$3,000 ... 0.00%" should be "$2,500, less than 0.01%". money() rounds values under $10,000 to the nearest thousand.
12. PEI "Turbine parts" (HS 841191, parts of turbojets and turboprops) should be "Aircraft engine parts".
13. Trips chart: add what is counted ("entries into Türkiye on Canadian passports, including Canadians living abroad and repeat trips").
14. Tab "Workers" should be "Work permits": about half the 2024 holders held permits linked to asylum or H&C cases.
15. "Where they lived, by city" should be "by metropolitan area" (census metropolitan areas).
16. Power card: "Canada's CANDU reactors are being studied for it" should be "... for Türkiye's new reactors" (AtkinsRéalis: the MOU supports plans for "three additional nuclear reactors").
17. Gas chart: label the Canada bar "For comparison: all of Canada's LNG exports in 2025". Reword its card: "Canada exported 3.1 billion m³ of liquefied natural gas in 2025, to all buyers, equal to about 5% of Türkiye's gas imports. None went to Türkiye."
18. Defence 2026 card "No figures yet" should be "No figures published for 2026" ("yet" is time-relative).
19. Timeline "Date to be set: President Erdoğan visits Canada" should be "Invitation for President Erdoğan to visit Canada". This is optional, since slide 9 uses the same wording.
20. WhatsApp message: replace "<post link>" with the post's URL when sending.

References:

21. Fix the titles and links of these references:
    - Ref 5: full title "... to advance partnership across trade and investment, energy, and defence".
    - Ref 8: add "with Singapore" to the title.
    - Ref 10: names four tables but links one (see must fix 4).
    - Ref 14: add the domestic exports zip.
    - Ref 25: add the date, May 29, 2026.
    - Ref 30: PRIS now redirects to the generic pris-stats.iaea.org home page.
    - Ref 38: describes 16 reports but links the 2025 report.
    - Ref 4: newswire.ca is acceptable (NRCan's own release); switch to canada.ca if a copy appears.
22. References 1, 3 and 4 are first cited inside the collapsed visit items, so the first visible superscript is "2,5".

Layout:

23. At 390 px the "Reopened" band label runs 8 px past its band, to the chart's right edge.
24. At 390 px the value label of an end-year column sits mostly over the column beside it (for example "1,895" for 2025 over the 2024 bar). Anchor it at the column's right edge instead of its centre.
25. At 1280 px the citation "6" after "came from Canada." wraps onto a line of its own.
26. Charts have extra empty space: scale() rounds 3.2 up to 5, so the trade chart runs to $5B (data peak $3.18B) and the trips chart to 500K (peak 321K). A step at 4 would fit better.
27. The province chip row hides its scrollbar, so at 390 px only a cut-off fourth chip shows that more provinces exist.

## Could not check

- The Türkiye Ministry of Culture and Tourism bulletin page (reference 19, yigm.ktb.gov.tr) gave an empty reply and a fetch error. I rechecked the 2010 to 2025 values and ranks from the saved 2025 bulletin instead.
- The GitHub repository and the live GitHub Pages site. METHODOLOGY.md, LICENSE, NOTICE and REPRODUCE.md were created at 16:22 to 16:24 and are untracked; the remote has only the initial commit. The page's links to METHODOLOGY.md and blob/main/LICENSE can only be confirmed after the push. methods/verification.md, named in README.md, does not exist yet.
- The Turkish tariff annexes (ticaret.gov.tr, Resmî Gazete) were not re-read line by line. I relied on the tariff outputs, which I recomputed, and on check-report.md for the rate readings.
- The text of the NATO expenditure PDF (image-based); I relied on check-report.md, which read the table images.
- Whether the expanded Air Transport Agreement applies before ratification. No official treaty text or Transport Canada page was found (people/results.md section 5).
- A canada.ca copy of the October 22 energy joint statement. A search found none.
