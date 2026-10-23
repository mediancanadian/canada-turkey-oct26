# Talking trade with Türkiye

Week 2 of The Median Canadian: an explorable page on what the Canada-Türkiye Strategic Partnership of October 2026 means for Canadians, built from official data.

- Page: https://sjvadrevu.github.io/canada-turkey-oct26/
- All posts: https://sjvadrevu.github.io/the-median-canadian/ (the link in the Instagram bio)

Everything behind the page and the Instagram slides is here: every analysis script, every output table, the independent checks and the steps to rebuild it from the official sources. Nothing is hidden, so anyone can reproduce or challenge any number.

- **[METHODOLOGY.md](METHODOLOGY.md):** what was measured and how, and a table of every published number (N1 to N47) with the file it comes from and how it is computed.
- **[REPRODUCE.md](REPRODUCE.md):** environment, downloads and run order.
- **[data/SOURCES.md](data/SOURCES.md):** every source with its link and licence.
- **[methods/verification.md](methods/verification.md):** the independent checks of every claim and what they changed.

## What the page shows

- **What was agreed:** the strategic partnership, the air transport agreement, the energy statement, defence cooperation, export finance, free trade talks and legal cooperation, each with its source.
- **The opportunity:** what Türkiye's 86 million people buy from the world and the part from Canada, by product; Türkiye's suppliers, with Canada 47th; Canada's reliance on the United States since 1999.
- **Trade deficit:** Canada's trade with Türkiye from 1988 to 2025, and what Canada sells and buys, with five years for each product group.
- **Duties:** estimated duties each way, by product, 2025 trade at 2026 rates.
- **Find your province:** each province's sales to Türkiye from 2021 to 2025, its top products, goods from Türkiye clearing customs there, and people of Turkish origin.
- **Travel:** the new flight limits, trips to Türkiye by Canadians since 2010, and people from Türkiye in Canada: permanent residents, students, workers and the 2021 Census by city.
- **Energy:** Türkiye's nuclear and wind and solar goals, where its gas comes from, and Canada's energy sales to Türkiye.
- **Defence:** Canadian military exports to Türkiye from 2010 to 2025, with the suspension, cancellations and reopening.
- **What comes next:** dates from October 29, 2026 to the 2027 trade mission.

## Files

| Path | What it is |
|---|---|
| `index.html` | The page (one file: HTML, CSS, JavaScript and data), built by `site/build_site.py` |
| `site/` | Page builder, styles and script |
| `data/site.json`, `data/chapters.json`, `data/references.json` | The page's chart data, chapter headings and reference list |
| `data/SOURCES.md` | Every source with link and licence |
| `slides/values.py`, `slides/values.json`, `slides/facts.json` | Every number on the slides and the page, computed from the analysis outputs; facts with their sources |
| `slides/make_slides.py`, `slides/out/` | The slide builder and the published slides (JPG) |
| `slides/photos/`, `slides/photos_used.json` | The slide photos (Wikimedia Commons, credited in NOTICE) |
| `analysis/<topic>/` | One folder per research thread (trade, tariffs, market, energy, defence, people, photos): `scripts/`, `results.md` (findings and method), manifests of downloaded files, and output tables |
| `analysis/check/` | Scripts and reports of the independent checks |
| `methods/` | Verification record and the METHODOLOGY.md builder |

## Licence

- **Code:** Apache License 2.0 (LICENSE and NOTICE).
- **Text, charts and slides:** CC BY 4.0 (LICENSE-CONTENT.md).
- **Photos in the slides:** Wikimedia Commons, each under its own licence, listed in NOTICE.
- **Data:** belongs to its publishers and is used under their terms (data/SOURCES.md).

The Median Canadian. A curious Canadian explaining Canada through numbers, every week.
