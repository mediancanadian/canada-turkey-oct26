# Reproduce

## Quick rebuild from the committed outputs

The output tables of every research thread are in the repository, so the numbers, slides and page rebuild without downloading anything. From the repository root:

```
pip install -r requirements.txt
python3 -m playwright install chromium
python3 slides/values.py
python3 slides/make_slides.py
python3 site/build_site.py
python3 methods/build_methodology.py
```

- `slides/values.py` reads `analysis/*/out*` and `slides/facts.json` and writes `slides/values.json`, the numbers shared by the slides and the page.
- `slides/make_slides.py` writes `slides/out/the-median-canadian-canada-turkiye-n-of-9.png` and `.jpg`, a contact sheet and a fit report (it stops if any text runs past its space).
- `site/build_site.py` writes `index.html` and `data/*.json`. It stops if a shared number no longer matches the slides, if the provinces do not add to Canada's total, if a reference is never cited, or if the page breaks a wording rule.
- `methods/build_methodology.py` rewrites the table of published numbers in METHODOLOGY.md.

Python 3.11 or newer. Two inputs are small extracts of larger Statistics Canada files, made from the raw files below: `analysis/trade/out/x171_all_sections_extract.csv` (table 12-10-0171, all product sections, partners "All countries" and "United States") and `analysis/tariffs/outputs/domexports_TR_2025_hs6_by_province.csv` (2025 domestic exports to Türkiye by HS6 and province).

## Full rebuild from the official sources

Raw downloads go into each thread's `raw/` folder, which git ignores because of their size (about 1.7 GB in all). Every file is listed with its link in the thread's `manifest.json`, and each `results.md` gives the method step by step. Scripts send a generic user agent and no personal details.

System tools: `curl`, `unzip`, `pdftotext` and `pdftoppm` (poppler), and `tesseract` for the scanned Turkish tariff decisions.

1. **trade** (Statistics Canada CIMT): `sh scripts/00_download.sh raw`, then `01_fetch_hs2.py`, `02_fetch_hs6.py`, `03_analyse_totals.py`, `04_analyse_hs6.py`, `05_tables_md.py`, run from `analysis/trade/`.
2. **tariffs** (CBSA Customs Tariff 2026, Türkiye's 2026 import regime, CIMT 2025 data files): download the files in `manifest.json` into `raw/`, then `01_extract_tr.py`, `02_ocr_tr.sh`, `04_tr_rates.py`, `05_ca_duty_estimate.py`, `06_tr_duty_estimate.py`, `07_steel_sima_coverage.py`, run from `analysis/tariffs/` (`03_pagecode.sh` is a helper for `02`).
3. **market** (UN Comtrade, TurkStat, Bank of Canada): `imports.py`, `fx.py`, `compute.py`.
4. **energy** (Türkiye's energy ministry, EPDK, EPİAŞ, IAEA, CER, NRCan): `tr_energy_balance.py`, `cer_lng.py`, `cer_lng_clean.py`, `pris_summary.py`, `comtrade_summary.py`.
5. **defence** (Global Affairs Canada reports 2010 to 2025): `parse_2010_2013.py`, `parse_reports.py`, `rank_table6.py`, `build_table.py`.
6. **people** (IRCC open data, Türkiye's border statistics, 2021 Census, IRB): `ircc_xlsx.py` helpers, `turkiye_border.py`, `travel.py`, `census.py`, `census_table.py`, `pr_rank.py`, `tr_ranks.py`, `pr_category.py`, and the follow-up scripts in `scripts/followup/`.

Then run the quick rebuild above. Monthly 2026 trade and IRCC data are revised over time, so a later download can differ slightly for 2026.

## Checks

`analysis/check/scripts/` holds the scripts the independent checkers used to recompute claims from the raw files; their reports are in `analysis/check/` and summarised in `methods/verification.md`.
