# Türkiye as a market for Canada: research results

Thread: market size, incomes, imports, macro risks, investment flows, treaties.
All sources accessed 2026-10-23 unless stated otherwise. Scripts are in `scripts/`, raw downloads in `raw/`, computed tables in `outputs/`.

## Access notes (read first)

- **TurkStat (data.tuik.gov.tr and veriportali.tuik.gov.tr) could not be read directly.** The old host redirects to a JavaScript-only portal, its API returns "Erişim engellendi" (access denied), and WebFetch was refused by robots.txt. Every TurkStat number below (population, fertility, income survey) comes from news reports that quote TurkStat releases. They are marked **[TurkStat via news]** and should be spot-checked against the bulletin before publishing. TurkStat bulletin link (not readable by us): https://data.tuik.gov.tr/Bulten/Index?p=Adrese-Dayali-Nufus-Kayit-Sistemi-Sonuclari-2025-53899&dil=1
- **Türkiye's goods imports by partner** come from UN Comtrade, which publishes the customs data Türkiye itself reports (TurkStat is the national compiler). Its totals can differ slightly from TurkStat's headline press release.
- The Türkiye Treasury rating page (hmb.gov.tr) is JavaScript-only, so ratings come from news reports of agency announcements.
- Blocked or not answered: trade.gov.tr (Ministry of Trade bulletin, needed for the official "intermediate goods" share), aa.com.tr, the UNCTAD treaty page for "Canada-Turkey BIT (2009)", and the GAC Türkiye FTA consultation page (connection reset). The GAC claim "up from $1B in 2022" was therefore checked only against the raw StatCan table, not the page itself.

## 1. Population

| | Türkiye | Canada |
|---|---|---|
| Population | 86,092,168 (end 2025) | 41,798,407 (Jul 1, 2026) |
| Recent growth | 0.50% in 2025 | 0.46% (Jul 2025 to Jul 2026) |
| Median age | 34.9 | 40.9 |
| Ages 0 to 14 | 20.4% | 15.0% |
| Ages 15 to 64 | 68.5% | 65.0% |
| Ages 65+ | 11.1% | 20.0% |
| Fertility (2025) | 1.42 | 1.26 |

Sources:
- Türkiye total, growth (5.0 per thousand, up from 3.4), median age (34.9, up from 34.4), Istanbul, urban share: [TurkStat via news] Turkish Minute, 2026-02-09, https://www.turkishminute.com/2026/02/09/turkeys-population-surpasses-86-million-in-2025/ ; growth also in Hronika, https://hronika.kz/?p=9848
- Türkiye age shares (20.4 / 68.5 / 11.1): [TurkStat via news] BRTK, https://brtk.net/?p=1175126 . Dependency ratio 46%: Hronika, above.
- Türkiye fertility 1.42 in 2025 (1.49 in 2024; 2.38 in 2001), births 895,374: [TurkStat "Birth Statistics, 2025" via news] https://turkishminute.com/2026/05/21/turkeys-fertility-rate-falls-to-1-42-children-per-woman/
- Mid-2026: TurkStat put the population at 86.3 million on July 1, 2026 (released Aug 20, 2026): [TurkStat via news] https://www.hurriyetdailynews.com/turkiyes-population-soars-to-86-3-mln-official-data-says-225841
- Canada population: StatCan table 17-10-0009-01, https://www150.statcan.gc.ca/n1/tbl/csv/17100009-eng.zip . Canada's age structure and median age: StatCan 17-10-0005-01 (July 1, 2026 estimates), https://www150.statcan.gc.ca/n1/tbl/csv/17100005-eng.zip . Canada fertility 1.26 (2025): StatCan 13-10-0418-01, https://www150.statcan.gc.ca/n1/tbl/csv/13100418-eng.zip . Shares and growth calculated in `scripts/compute.py`.

**Is Türkiye still growing?** Yes, slowly: +427,224 people in 2025 (0.50%), about the same pace as Canada right now. Fertility has been below replacement (2.1) for nine years in a row and is falling.

**How fast is it aging?** TurkStat "Population Projections, 2023-2100" (released 2024-07-30), main scenario [TurkStat via news, https://www.alomaliye.com/2024/07/30/nufus-projeksiyonlari-2023-2100/ and https://www.dailysabah.com/turkiye/turkiyes-population-expected-to-diminish-below-77-million-by-2100/news/amp]:
- Population 88.19 million in 2030 and 93.77 million in 2050. Growth until the mid-2050s, then decline to below 77 million by 2100. In the low scenario the peak is 89.96 million in 2044.
- Median age 34 (2023), 44.8 (2050), 52.2 (2100).
- Ages 65+: just over 10% (2023), 23.1% (2050), 33.6% (2100). Ages 0 to 14: 21.4% (2023), 15.1% (2050).
- In other words, Türkiye in 2050 will be older than Canada is today (Canada's 65+ share is 20.0% now).

**Cities:** Istanbul 15,754,053 (18.3% of the country) [TurkStat via news, Turkish Minute above]. 93.6% of people live in province and district centres, which is TurkStat's urban measure. The World Bank's own urban estimate is 89.5% for Türkiye and 82.9% for Canada (2025; https://api.worldbank.org/v2/country/TUR;CAN/indicator/SP.URB.TOTL.IN.ZS?format=json). The two definitions differ.

## 2. Incomes and consumers

IMF World Economic Outlook, **October 2026** edition (the datamapper reports "World Economic Outlook (October 2026)", last modified 2026-10-08). API: https://www.imf.org/external/datamapper/api/v1/NGDPD/TUR/CAN (same pattern for the other indicators). Output: `outputs/imf_weo_oct2026_tur_can.csv`.

| 2025 (IMF) | Türkiye | Canada |
|---|---|---|
| GDP, USD bn | 1,603 | 2,321 |
| GDP per person, USD | 18,676 | 55,796 |
| GDP per person, PPP $ | 44,208 | 67,054 |
| GDP, PPP $ bn | 3,794 | 2,790 |
| Real growth | 3.7% | 1.9% |
| Unemployment | 8.3% | 6.9% |

- Canada's GDP per person is 2.99 times Türkiye's at market exchange rates but only 1.52 times in PPP terms. Prices in Türkiye are low, so local purchasing power is much higher than the dollar figure suggests. Measured in PPP, Türkiye's whole economy is larger than Canada's.
- IMF 2026 projections: Türkiye GDP USD 1,818 bn and USD 21,079 per person. Canada GDP USD 2,490 bn and USD 60,105 per person.
- World Bank GNI per person (Atlas method, 2025): Türkiye USD 16,300, Canada USD 56,420. https://api.worldbank.org/v2/country/TUR;CAN/indicator/NY.GNP.PCAP.CD?format=json

**Household consumption** (World Bank WDI, NE.CON.PRVT.CD, current USD, 2025; https://api.worldbank.org/v2/country/TUR;CAN/indicator/NE.CON.PRVT.CD?format=json): Türkiye USD 873.8 bn, Canada USD 1,294.1 bn. Divided by IMF population, that is about USD 10,181 per person in Türkiye and USD 31,107 in Canada. Türkiye's consumer market is about two thirds the size of Canada's in dollars, spread across twice as many people.

**Minimum wage 2026** (Turkish Ministry of Labour and Social Security, valid 2026-01-01 to 2026-12-31; https://www.csgb.gov.tr/poco-pages/asgari-ucret/):
- Gross TRY 33,030.00 per month. Net TRY 28,075.50 per month. Total employer cost TRY 40,874.63 with no premium incentive.
- Net in CAD: about CAD 848 per month at the 2026 average rate (33.127 TRY per CAD) and CAD 795 at the Oct 22, 2026 rate (35.3357).
- Net in USD: about USD 611 at the 2026 average and USD 567 at Oct 22, 2026 rates (via Bank of Canada USD/CAD).
- FX source: Bank of Canada Valet FXCADTRY and FXUSDCAD. Calculated in `scripts/compute.py`.
- The value in CAD falls through the year as the lira weakens, because the lira amount is fixed for 12 months.

**Income distribution** [TurkStat income distribution statistics, 2025 survey, via news, https://www.turkiyetoday.com/nation/turkiyes-top-earners-capture-48-of-income-as-inequality-edges-lower-3211937]:
- Gini 0.410 (0.413 a year earlier).
- The top 20% receive 48.0% of income and the bottom 20% receive 6.4%. The S80/S20 ratio is 7.5.
- Mean household disposable income is TRY 662,414 per year (+76.7% in lira terms). Per person it is TRY 332,882.
- Comparison on a common basis (World Bank Gini): Türkiye 43.7 (2023), Canada 31.5 (2022). https://api.worldbank.org/v2/country/TUR;CAN/indicator/SI.POV.GINI?format=json

**Middle-class size:** no official TurkStat or government measure found. Skipped as instructed.

## 3. Türkiye's imports

Source: UN Comtrade, Türkiye as reporter (code 792), annual 2025, all goods. Partner query: https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=792&period=2025&flowCode=M&cmdCode=TOTAL&partner2Code=0&motCode=0&customsCode=C00 . Script: `scripts/imports.py`. Output: `outputs/tur_imports_2025_by_partner.csv`.

**Total goods imports 2025: USD 365.4 bn** (USD 344.0 bn in 2024).

Top suppliers in 2025: China USD 49.6 bn (13.6%), Russia 42.4 (11.6%), Germany 30.1 (8.2%), USA 18.1 (4.9%), Switzerland 15.7 (4.3%), Italy 15.7 (4.3%), France 12.9 (3.5%). A further 5.7% is coded "Special Categories" (partner withheld).

| Supplier, 2025 | USD bn | Share | Rank* | FTA with Türkiye? |
|---|---|---|---|---|
| USA | 18.08 | 4.95% | 4 | No |
| UK | 7.26 | 1.99% | 11 | Yes, in force 2021 |
| Canada | 1.16 | 0.32% | 47 | No, in negotiation |
| Australia | 0.59 | 0.16% | 58 | No |

*Rank among countries, excluding "Special Categories" and "areas nes". In 2024 Canada supplied USD 1.22 bn (0.35%).

FTA and treaty status: UNCTAD Investment Policy Hub, Türkiye agreements list, https://investmentpolicy.unctad.org/international-investment-agreements/countries/214/t-rkiye (read via WebFetch):
- UK: Turkey-United Kingdom FTA, signed 2020-12-29, in force 2021-04-20.
- USA: no FTA. A 1985 BIT is in force.
- Australia: no FTA. A 2005 BIT is in force (since 2009).
- Canada: FTA "in negotiations", per Global Affairs Canada (https://international.canada.ca/en/services/business/trade/agreements-negotiations/investment-agreements).

**What Türkiye imports** (HS chapters, 2025, Comtrade; `outputs/tur_imports_2025_hs2_world.csv`):
- Energy (HS 27): USD 62.5 bn, 17.1%. Includes refined petroleum (HS 2710) at USD 17.6 bn and coal (HS 2701) at USD 4.6 bn.
- Machinery (HS 84): USD 41.6 bn, 11.4%.
- Vehicles (HS 87): USD 36.9 bn, 10.1%.
- Electrical equipment (HS 85): USD 30.0 bn, 8.2%.
- Gold and precious metals (HS 71): USD 28.1 bn, 7.7%. Non-monetary gold alone (HS 7108) was USD 23.1 bn.
- Iron and steel (HS 72): USD 22.2 bn, 6.1%.
- The official "intermediate goods" share (broad economic categories) was not obtained, because trade.gov.tr was blocked.

**What Canada sells to Türkiye** (Türkiye's import records, 2025; `outputs/tur_imports_2025_hs2_canada.csv`):
- Vegetables and pulses (HS 07): 15.9%.
- Aircraft (HS 88): 15.0%.
- Instruments (HS 90): 11.6%.
- Machinery (HS 84): 10.8%.
- Gold (HS 71): 8.4%.
- Canada's own count (GAC, https://www.international.gc.ca/country-pays/turkiye/relations.aspx?lang=eng, modified 2026-10-06): Canadian exports were CAD 1.1 bn and imports from Türkiye CAD 3.2 bn in 2025, for two-way trade of over CAD 4.3 bn.

## 4. Risks

**Inflation** (TurkStat CPI, as listed by the central bank TCMB, https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Statistics/Inflation+Data/Consumer+Prices ; full monthly series from 2005 in `outputs/tur_cpi_monthly_tcmb.csv`):
- Year-on-year inflation was 10.35% in Jan 2018.
- It peaked at **85.51% in Oct 2022**, then reached 64.77% in Dec 2023 and 75.45% in May 2024.
- It fell to 30.89% in Dec 2025 and **29.73% in Sep 2026** (1.84% month on month). This confirms the 29.73% figure in the brief.
- Chaining the monthly changes, prices rose about 13.3 times between Dec 2017 and Sep 2026. This is approximate because the monthly figures are rounded.
- IMF forecast for average inflation: 31.2% in 2026 and 26.5% in 2027 for Türkiye, against 2.8% in 2026 for Canada.
- Cross-check: the OECD series (https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_PRICES@DF_PRICES_ALL,1.0/TUR.M.N.CPI.PA._T.N.GY?startPeriod=2018-01) matches the TCMB figures to two decimals for 2018 to 2025.

**Policy rate** (TCMB one-week repo, https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Core+Functions/Monetary+Policy/Central+Bank+Interest+Rates/1+Week+Repo ; `outputs/tcmb_policy_rate_1w_repo.csv`):
- **36.00%, effective 2026-10-23** (previously 37.00% from 2026-01-23).
- The peak was 50.00% (2024-03-22 to 2024-12-27).
- The rate was as low as 8.50% in Feb 2023, when inflation was above 50%.

**Exchange rate, Turkish lira per Canadian dollar** (Bank of Canada):
- Annual averages: 2015 2.13, 2017 2.81, 2020 5.18, 2022 12.59, 2024 23.92, 2025 28.17, 2026 to Oct 22 33.13. Latest: 35.3357 on 2026-10-22.
- Sources: FXCADTRY daily (https://www.bankofcanada.ca/valet/observations/FXCADTRY/json), FXATRYCAD annual, and the legacy noon-rate series IEXA5802 and IEXE5802 for 2015 to 2016 (https://www.bankofcanada.ca/valet/observations/group/LEGACY_ANNUAL_RATES/json).
- The 2015 to 2016 values come from the legacy noon series, which uses a different basis from the daily average series used since 2017. The difference is small next to the size of the move.
- Script: `scripts/fx.py`. Outputs: `outputs/fx_try_per_cad_annual.csv`, `outputs/fx_lira_loss.csv`.

| Horizon to Oct 22, 2026 | TRY per CAD then | Lira value lost vs CAD |
|---|---|---|
| 1 year (2025-10-22) | 30.03 | 15.0% |
| 5 years (2021-10-22) | 7.776 | 78.0% |
| 10 years (2016-10-21) | 2.316 | 93.4% |

**What this means:**
- One Canadian dollar buys 4.5 times as many lira as five years ago and 15.3 times as many as ten years ago.
- On paper, this makes Turkish goods cheaper in Canada and Canadian goods dearer for Turkish buyers.
- However, Turkish prices also rose about 13-fold since Dec 2017, so much of the lira's fall has been offset by domestic inflation. The real (inflation-adjusted) change in competitiveness is much smaller than the nominal drop.
- For a Canadian exporter, revenue earned in lira loses value quickly unless prices are reset often or set in hard currency.
- Turkish wages and incomes, converted to CAD, are unstable from month to month.

**Current account** (IMF WEO Oct 2026):
- Türkiye: deficit of USD 30.1 bn in 2025 (1.9% of GDP), projected at USD 51.9 bn in 2026 (2.9% of GDP).
- Canada: deficit of 0.9% of GDP in 2025, projected at 0.1% in 2026.
- An official CBRT balance-of-payments page was not reached. The IMF figure is used.

**External debt** (TCMB, "Developments in External Debt Statistics of Türkiye, 2026 Q2", https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Statistics/Balance+of+Payments+and+Related+Statistics/External+Debt , PDF in `raw/tcmb/`):
- Gross external debt was **USD 539.0 bn** at end Q2 2026, up 3.5% on the quarter.
- Short-term debt was USD 170.7 bn.
- Public sector USD 197.9 bn, private sector USD 318.0 bn, central bank USD 23.1 bn.
- Currency mix: 48.9% in USD, 28.8% in EUR, 12.2% in TRY.
- Against the IMF's 2026 GDP projection, that is about 30% of GDP. This is our ratio, mixing a quarter-end stock with annual GDP.

**Sovereign credit ratings:** Türkiye is rated three notches below investment grade at all three major agencies. Canada is rated at the top.

| Agency | Türkiye | Canada |
|---|---|---|
| S&P | BB- stable | AAA |
| Moody's | Ba3 stable | Aaa |
| Fitch | BB- stable | AA+ stable |
| DBRS | not checked | AAA |

- Türkiye, S&P: affirmed BB-/B stable, reported 2026-04-19. https://hurriyetdailynews.com/s-p-affirms-turkiyes-ratings-outlook-stable-221211
- Türkiye, Moody's: Ba3 stable, periodic review with no action on 2026-07-24. https://www.hurriyetdailynews.com/moodys-completes-periodic-review-of-turkiye-takes-no-rating-action-224798
- Türkiye, Fitch: BB- stable, affirmed July 2026 (reported 2026-07-18). https://www.hurriyetdailynews.com/fitch-affirms-turkiyes-bb-rating-with-stable-outlook-224514
- These are news reports of agency announcements. The Türkiye Treasury rating page could not be rendered.
- Canada: Finance Canada, Spring Economic Update 2026, Annex 3: "AAA (equivalent) by Moody's, S&P, and DBRS, and AA+ by Fitch". https://budget.canada.ca/update-miseajour/2026/report-rapport/anx3-en.html
- Canada, Fitch: affirmed AA+ stable on 2026-07-14 (news: https://investinglive.com/forex/fitch-affirms-canada-at-aa-with-a-stable-outlook/).

## 5. Investment, both ways

Source: StatCan table 36-10-0008-01, total book value, CAD millions. https://www150.statcan.gc.ca/n1/tbl/csv/36100008-eng.zip (table page: https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610000801). Output: `outputs/fdi_canada_turkiye_2010_2025.csv`.

| Year | Canada in Türkiye | Türkiye in Canada |
|---|---|---|
| 2010 | 1,536 | .. |
| 2011 | 913 | x |
| 2012 | 911 | -1 |
| 2013 | 1,502 | 74 |
| 2014 | 743 | .. |
| 2015 | 968 | -1 |
| 2016 | 1,080 | .. |
| 2017 | 1,491 | .. |
| 2018 | 1,358 | .. |
| 2019 | -5,874 | 203 |
| 2020 | -5,582 | 101 |
| 2021 | 1,707 | 78 |
| 2022 | 992 | 75 |
| 2023 | 2,856 | 154 |
| 2024 | 4,126 | 214 |
| 2025 | 3,315 | 233 |

".." means not available and "x" means suppressed for confidentiality (StatCan symbols).

**Reconciling the two GAC statements.** Both are consistent with the raw table:
- "$3.3B in 2025, down 19.7% from 2024" (GAC relations page): CAD 3,315 m against CAD 4,126 m is -19.7%. Confirmed.
- "Up from $1B in 2022": CAD 992 m in 2022. Confirmed. 2025 is 3.3 times 2022.
- The story is a jump from 2022 to a peak in 2024, then one year of decline. GAC's wording "in steady decline in recent years" is not supported by the table: only 2025 fell.
- In 2019 and 2020 the Canadian position was negative (about CAD -5.9 bn and -5.6 bn), driven by a negative equity component (CAD -5.7 bn). StatCan does not say why. The series is volatile and likely dominated by a few large firms.
- Turkish investment in Canada is small: CAD 233 m in 2025.

**Canadian companies in Türkiye (officially documented):**
- **Eldorado Gold** runs the Kışladağ mine (168,701 oz of gold produced in 2025) and the Efemçukuru mine (72,482 oz) in Türkiye. Together they are 49.4% of the company's 488,268 oz in 2025. Source: Eldorado Q4 2025 Financial and Operational Data, https://www.eldoradogold.com/sites/eldorado-gold/files/2026-02/ELD%20Q4%202025%20Financial%20and%20Operational%20Data.pdf
- **Alamos Gold, Kirazlı (investment risk case):**
  - ICSID Case No. ARB/21/33, registered 2021-06-07. https://icsid.worldbank.org/cases/case-database/case-detail?CaseNo=ARB/21/33
  - The claimants were Alamos's **Dutch** subsidiaries, using the **Netherlands-Türkiye BIT (1986)**, not a Canadian treaty.
  - UNCTAD lists USD 1 bn claimed, over the alleged non-renewal of mining licences. https://investmentpolicy.unctad.org/investment-dispute-settlement/cases/1119/alamos-gold-v-turkey
  - A hearing was held in London, Oct 7 to 18, 2024. The tribunal issued a "decision on jurisdiction and liability" on 2025-06-18; its content is not public. The case was suspended by agreement of the parties on 2025-07-02, and ICSID still shows its status as "Pending".
  - Alamos then sold the Turkish subsidiary (Kirazlı, Ağı Dağı, Çamyurt) to Tümad for **USD 470 m**: USD 160 m at closing, then USD 160 m and USD 150 m on the first and second anniversaries. The sale was announced 2025-09-14 and closed 2025-10-27. The arbitration stays suspended and "will be discontinued with prejudice after certain contractual milestones are reached". Sources: https://s24.q4cdn.com/779615370/files/doc_news/2025/Sept/20250914-Alamos-Announces-Sale-of-Turkish-Projects_FINAL.pdf and https://s24.q4cdn.com/779615370/files/doc_news/2025/Oct/20251027-Alamos-Announces-Closing-of-Sale-of-Turkish-ProjectsFinal.pdf
  - The second payment falls due around Oct 27, 2026, which is the one-year anniversary implied by the closing date.
- **Bombardier:** only news and Turkish investment agency items from about 2017 were found (rail plans with Bozankaya). There is no company filing confirming current operations. Treat as an unverified lead.

## 6. Treaties

- **Investment treaty (FIPA/BIT): no Canada-Türkiye agreement is in force.**
  - Global Affairs Canada's full list of investment and trade agreements has no Canada-Türkiye FIPA in any status. The only Türkiye entry is the "Canada-Türkiye Free Trade Agreement, Status: In negotiations". https://international.canada.ca/en/services/business/trade/agreements-negotiations/investment-agreements
  - UNCTAD's Türkiye list also shows no agreement with Canada. Türkiye has 140 BITs.
  - The premise "FIPA signed 2009, in force 2015" is **not supported**. The 2009 date belongs to the tax treaty (next point).
  - UNCTAD has a page titled "Canada-Turkey BIT (2009)" (ID 648) that we could not open. It may record a signed agreement that never entered into force. Check it before stating anything stronger than "not in force".
  - The Alamos case shows the practical effect: the company had to sue through Dutch subsidiaries.
- **Tax treaty: yes.** Signed 2009-07-14 and in force 2011-05-04. It applies to withholding taxes on amounts paid on or after 2012-01-01, and to other taxes for years beginning on or after 2012-01-01. Source: Finance Canada, https://www.canada.ca/en/department-finance/programs/tax-policy/tax-treaties/notices/2011/turkey-entry-force.html
- **FTA:** Canada tabled a notice of intent to negotiate on 2026-09-21. Talks were first announced in a joint statement on 2026-07-07, and public consultations ran from 2026-07-31 to 2026-09-14. Source: GAC page modified 2026-10-09, https://www.international.gc.ca/trade-commerce/trade-agreements-accords-commerciaux/agr-acc/turkiye/fta-ale/info.aspx?lang=eng (saved in `raw/gac/`).

## Balance sheet for the "85 million consumers" pitch

**Supports it:**
- About 86 million people, younger than Canada (median 34.9 against 40.9), still growing slowly, and 93.6% living in cities.
- GDP per person in PPP terms is two thirds of Canada's.
- Real growth is faster than Canada's (3.7% against 1.9% in 2025).
- Canada's market share is tiny (0.32%, rank 47), so there is room to grow. The UK has shown an FTA route.

**Cuts against it:**
- In dollars, consumers spend about USD 10,200 per person a year, a third of Canada's level. The net minimum wage is worth about CAD 800 to 850 a month.
- Income is concentrated: the top 20% receive 48% of income.
- Inflation is near 30%, the policy rate is 36%, and the lira lost 78% against the CAD in 5 years.
- The ratings are three notches below investment grade, and gross external debt is USD 539 bn.
- Fertility is 1.42, so the population is projected to peak in the mid-2050s and age quickly.
- There is no Canada-Türkiye investment treaty in force, and the largest recent Canadian mining dispute ended in a sale under arbitration.
