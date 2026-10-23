# Follow-up: closing the official-source gaps (Türkiye market thread)

Accessed 2026-10-23. Raw files in `raw/followup/`, scripts in `scripts/` (`tuik_press.py`, `tuik_search.py`).

## Access note: TurkStat is now readable

The TurkStat data portal serves its press releases through a public JSON API: `https://veriportali.tuik.gov.tr/api/en/press/<id>`. It needs only the `X-Requested-With: XMLHttpRequest` header, with no login. The human-readable page for each release is `https://veriportali.tuik.gov.tr/en/press/<id>`. Every figure below marked **[TurkStat, confirmed]** was read from the release text itself. No figure in this file comes from news.

## 1. TurkStat figures: all confirmed, no replacements needed

| Figure (results.md) | TurkStat value | Release (id, date) |
|---|---|---|
| Population end-2025 | 86,092,168 (31 Dec 2025) | ABPRS 2025 (53899, 2026-02-09) |
| Growth | +427,224 people; "5 per thousand" (3.4 in 2024) | 53899 |
| Median age | 34.9 (34.4 in 2024) | 53899 |
| Ages 0-14 / 15-64 / 65+ | 20.4% / 68.5% / 11.1% | 53899 |
| Dependency ratio | 46.0% (child 29.7, elderly 16.2) | 53899 |
| Istanbul | 15,754,053 (18.3% of the total) | 53899 |
| Urban (province and district centres) | 93.6% | 53899 |
| Total fertility 2025 | 1.42 (2.38 in 2001); 895,374 live births | Birth Statistics 2025 (58018, 2026-05-21) |
| Gini | 0.410 (down 0.003) | Income Distribution 2025 (53993, 2025-12-26) |
| Top / bottom 20% share | 48.0% / 6.4%; S80/S20 7.5 | 53993 |
| Mean household disposable income | TRY 662,414; equivalised TRY 332,882 | 53993 |
| Projections (main scenario) | 88,188,221 (2030); 93,774,618 (2050); growth to the mid-2050s, then below 77M by 2100 | Population Projections 2023-2100 (53699, 2024-07-30) |
| Low scenario peak | 89,959,486 in 2044 | 53699 |
| Projected median age | 34 (2023), 44.8 (2050), 52.2 (2100) | 53699 |
| Projected 65+ share | 23.1% (2050), 33.6% (2100) | 53699 |

Corrections and caveats:
- Growth: TurkStat states "5 per thousand". 0.50% is our own rounding (427,224 / 85,664,944 = 0.499%), so say "about 0.5%".
- The 2025 income survey measures **2024 incomes** (the release says so). Label it "2025 survey (2024 incomes)".
- The Birth Statistics release calls fertility below replacement "for the last nine years", which matches results.md.
- The mid-2026 figure of 86.3M was not checked. It is still news-sourced.
- UN WPP, World Bank, Eurostat and OECD were not needed.

## 2. Credit ratings

**Türkiye, official table.** The Ministry of Treasury and Finance "Credit Ratings" page shows **Fitch BB- Stable, Moody's Ba3 Stable, S&P BB- Stable**. The page was last modified 2026-04-14. Source: https://en.hmb.gov.tr/credit-ratings (read via the site's API, https://en.hmb.gov.tr/portal/v2//pages?slug=credit-ratings ; saved as `hmb_credit_ratings.json`).

**Action dates.** The agencies' own pages were blocked (S&P 403, Moody's behind Cloudflare, Fitch's JavaScript page and WebFetch permission not answered). The page does not give action dates, so these still come only from news:
- Fitch: outlook raised to Positive (reported 2026-01-24), then **revised back to Stable on about 2026-04-13**. Source: QNB Invest research note, https://www.qnbinvest.com.tr/investodak/qnbarastirma/fitch-ratings-turkiyenin-kredi-notu-gorunumunu-pozitiften-duragana-revize-etti . The Treasury page change on 2026-04-14 fits this date. The affirmation that results.md dates to July 2026 is from Hurriyet only.
- **Correction for results.md:** Fitch's Stable outlook came from a downgrade of the outlook from Positive in April 2026. It was not a plain affirmation.
- Moody's (no action 2026-07-24) and S&P (affirmed, reported 2026-04-19): dates are from news only.

**Canada.** No new official source was reached. Keep results.md (Finance Canada SEU 2026 Annex 3).

## 3. Current account: TCMB official

Source: TCMB, Balance of Payments Developments, August 2026 (PDF created 2026-10-12), and `bop.xls` Tables 3 and 4. https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Statistics/Balance+of+Payments+and+Related+Statistics/Balance+of+Payments+Statisticss/

| | TCMB | IMF WEO (results.md) |
|---|---|---|
| 2025 annual | -USD 30,276 m (provisional) | -USD 30.1 bn |
| 12 months to Aug 2026 | -USD 42,103 m | n/a |
| Jan-Aug 2026 | -USD 31,498 m | n/a |
| 2026 full year | n/a | -USD 51.9 bn (forecast) |

- The two agree on 2025: USD 30.3 bn (TCMB) against USD 30.1 bn (IMF).
- The 12-month deficit has widened every month except April and May 2026.
- August 2026 alone showed a surplus of USD 4,053 m (the tourism season).

## 4. Canada-Türkiye investment treaty

- UNCTAD's Türkiye country page (WebFetch, 2026-10-23) lists 140 BITs (84 in force). **There is no Canada row in any status.** Signed-but-not-in-force treaties such as Chile 1998 and Colombia 2014 do appear in the same list. https://investmentpolicy.unctad.org/international-investment-agreements/countries/214/t-rkiye
- The UNCTAD treaty page 648 and the Canada country page could not be opened (Cloudflare 403 by curl; WebFetch permission not answered). Searches turned up no copy of a "Canada - Turkey BIT (2009)" record.
- The GAC list (saved in results.md) has no Canada-Türkiye FIPA in any status.
- The Canada Treaty Information search returned a server error.
- **Precise status:** no Canada-Türkiye investment treaty is in force. Neither UNCTAD's Türkiye list nor GAC records one as signed. Page 648 cannot be ruled out as a stray record (possibly linked to the 2009 tax treaty) until it is opened. Safe wording: "Canada and Türkiye have no investment protection treaty."

## 5. Imports by broad economic category (BEC): TurkStat official

Foreign Trade Statistics, December 2025 (53911, 2026-01-30), January-December 2025, general trade system:
- Intermediate goods **68.4%**, capital goods **15.0%**, consumption goods **16.2%** of total imports.
- Total imports were USD 365.370 bn and exports USD 273.361 bn.
- Leading import sources: China USD 49.576 bn, Russia 42.373 bn, Germany 30.110 bn.
- The three BEC shares sum to 99.6%. The remaining 0.4% is unclassified.
