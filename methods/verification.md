# Verification record

Every claim in the post was checked by a separate checker who had not done the analysis, working from the saved raw files and the official pages. The reports are kept in full in `analysis/check/`, with the scripts the checkers used to recompute numbers (`analysis/check/scripts/`).

## 1. The research (October 23, 2026): `analysis/check/check-report.md`

207 claims across the six research threads were tested by recomputing them from the raw files or reading the official source: 175 confirmed, 15 errors, 10 resting on a source that could not be confirmed, and 7 stated more strongly than the source supports. The errors that touch a published number were handled as follows:

- Türkiye's 2025 imports are US$365.4 billion in both UN Comtrade and TurkStat; the post says US$365 billion.
- The airports supported the 2025 requests for extra Turkish Airlines flights; only Air Canada and Air Transat opposed them, as the post says.
- The 21-flight limit is confirmed by the PMO's release and the Prime Minister's remarks; the post says "up to 21".
- Canada's rank among Türkiye's suppliers depends on whether "Other Asia, nes" counts as a partner: 47th if it does, 46th if not. The page uses 47th and states the rule (N10 in METHODOLOGY.md).
- The average duty on Canadian goods is 6.4% when both the duty and the value leave out durum wheat, as the slide does; dividing by all goods, durum included, gives 6.3%.

Numbers the checker could confirm only in news reports (for example Turkish Airlines' weekly frequencies) are not used in the post.

## 2. The first slide set: `analysis/check/slides-check.md`

The rendered slides were checked against the analysis. Findings that changed the slides include: the partnership was "launched" in Ankara, while the air agreement and memorandums were "signed"; and a claim that the United States share of Canada's exports was the lowest in 27 years was dropped, because older records go back further than the table used.

## 3. The final slide set: `analysis/check/slides-check-4.md`

All nine slides were checked again after the last round of edits. Fixes made before publishing:

- Cover: "first bilateral visit", the PMO's exact words, because the Prime Minister had been to Ankara for the NATO summit in July 2026.
- Closing slide: the line about duties staying the same was replaced, because duties changed in 2026 without a deal (Türkiye's rate on green lentils rose to 19.3% on May 1).
- Provinces: Ontario's cars now count every passenger-car line ($43 million).
- Duties: the bars say "Estimated duty", and the clothing line says "could".
- Travel and energy: facts carry their year (Turkish Airlines flew to 120 countries in 2024; Canada produced about a quarter of the world's uranium in 2024).
- Defence: the Armenian National Committee of Canada's request is about a trade deal.

## 4. The page and the post text: `analysis/check/site-check.md`

The page (`index.html`) and the caption, short description, story line and message were checked by a separate checker, who rendered the page at 390 px and 1280 px in light and dark mode and clicked every control. The post text had no errors. The 13 fixes it asked for were all made:

- What came out of the visit: the defence item is the memorandum connecting the two countries' defence companies; the statement of intent on defence cooperation was signed in July 2026. The legal item is a dialogue the leaders called for.
- Defence cards: five years of ranks and destination counts corrected (2010, 2011, 2012, 2023 and 2024); the parser had counted a summary row and missed two rows (see the note in `analysis/defence/results.md`).
- References: the work permit source links both files the chart uses; the Statistics Canada trade source links the CIMT catalogue page, since the tables are read through the Web Data Service; UN Comtrade links the exact queries.
- Travel: the airline note adds WestJet's support and the Agency's refusals (slide 6 adds WestJet too); the work permit note gives the numbers and no longer implies one cause.
- Wording: every number comes from an official or primary source, and the table in METHODOLOGY.md covers the slides and chapter text; "Türkiye's first nuclear plant"; "of Türkiye's imports"; a map legend that reads right in light and dark mode; Canada ranked among Türkiye's trading partners.

Minor points also changed: acronyms spelled out at first use, "Scroll to learn more", durum wheat named at the duty base, plain names for products and metropolitan areas, what the trips chart counts, a comparison label for Canada's LNG, exact values under $10,000, chart scales with less empty space, a legend for the defence bands, citation numbers that stay on their line and a scroll cue on the province list.

## Built-in checks

The builders stop with an error if a check fails:

- `slides/make_slides.py`: any text past its space, a headline or line over two lines, labels too close, the logo missing, or a banned word.
- `site/build_site.py`: a number on the page that differs from the slides, provinces that do not add to Canada's total, product groups that do not match the slides, a reference never cited, an em dash, or a banned word (now, today, currently, won, lost, our analysis, contrast framing).
