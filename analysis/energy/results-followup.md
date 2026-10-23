# Week 03 energy thread: follow-up checks

Accessed 2026-10-23. This file closes the gaps listed in results.md. Raw files are in raw/followup/ unless another folder is named. The CAD conversion table is in outputs/can_to_tur_energy_cad_2015_2025.json.

## Scorecard

| # | Claim | Result | Basis |
|---|---|---|---|
| 1 | Türkiye 2025 energy import bill USD 62.5B | **Confirmed: USD 62.47B** | UN Comtrade, reported by Türkiye |
| 2 | Canada list has 34 minerals, no boron | **Confirmed** | canada.ca (WebFetch) + OAG report |
| 3a | Canada 685 Mt (2024) | **Confirmed** | ECCC NIR 2026 |
| 3b | Türkiye 584.5 Mt (2024) | **Confirmed, excl. LULUCF** | Türkiye NIR 2026 |
| 3c | Per person 17 t vs 6.8 t | **Confirmed** (16.6 t and 6.83 t computed) | NIR texts + World Bank |
| 3d | Türkiye 2035 NDC 643 Mt | **Confirmed, but net (incl. LULUCF)** | NDC 3.0 text |
| 4 | Boron, chromium shares | Chromium: 17.6 to 18.8% of world mining. Boron: **no world share possible** | USGS MCS 2026 |
| 5 | Canada energy exports to Türkiye, CAD | Coal only; CAD 2.7M to 156M a year | Comtrade + Bank of Canada |
| 6 | Uranium 16.9 vs 14.3 kt | **Resolved: U3O8 vs U** | CER + NRCan |

---

## 1. Türkiye's energy import bill, 2025

UN Comtrade, reporter Türkiye (792), partner World, imports, annual:

| | 2024 | 2025 |
|---|---|---|
| HS 27 (mineral fuels) | USD 65,589,736,402 | **USD 62,465,580,162** |
| All goods | USD 344,010,273,095 | USD 365,369,912,607 |
| HS 27 share of imports | 19.1% | **17.1%** |

- 2025 vs 2024: -4.8%. This matches the TurkStat figures quoted by the news (USD 62.47B and 65.59B) to the dollar.
- Comtrade marks the chapter row "isAggregate: true". That means Comtrade summed Türkiye's own detailed lines into it. It is not a Comtrade estimate.
- The TurkStat bulletin portal (data.tuik.gov.tr, now veriportali.tuik.gov.tr) loads only as a JavaScript app. Its data API needs a login. So the bulletin PDF itself was not saved.
- Raw: comtrade_TUR_WORLD_M_HS27_2024.json, comtrade_TUR_WORLD_M_HS27_2025.json. URL pattern: https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=792&partnerCode=0&flowCode=M&cmdCode=27,TOTAL&period=2025

## 2. Canada's critical minerals list

- canada.ca still resets every connection from the shell (HTTP/2 and HTTP/1.1). web.archive.org is blocked too.
- WebFetch did read the official page: https://www.canada.ca/en/campaign/critical-minerals-in-canada/critical-minerals-an-opportunity-for-canada
  - It names "34 minerals and metals". The page was modified 2026-06-30, and the list was last revised in 2024.
  - The 34: aluminum, antimony, bismuth, cesium, chromium, cobalt, copper, fluorspar, gallium, germanium, graphite, helium, high-purity iron ore, indium, lithium, magnesium, manganese, molybdenum, nickel, niobium, phosphorus, platinum group metals, potash, rare earth elements, scandium, silicon metal, tantalum, tellurium, tin, titanium, tungsten, uranium, vanadium, zinc.
  - **Boron does not appear anywhere on the page.**
- Saved copy: canada_ca_critical_minerals_list_webfetch_transcript.txt. **This is a transcript made by a summarizing model, not the raw HTML.** Spot-check it in a browser before publishing.
- Independent official confirmation (saved as a PDF): Office of the Auditor General, CESD 2024 Report 6, para 6.3: "In June 2024, the Government of Canada released updated criteria along with an updated list of 34 critical minerals". The earlier 2021 list had 31. Raw: oag_cesd_2024_report6_critical_minerals.pdf
- NRCan consultation page (2021 list of 31; update due in 2024). Raw: nrcan_critical_minerals_list_consultation.html

## 3. Greenhouse gases

### Canada (ECCC NIR 2026, as submitted to UNFCCC)
- 2024 emissions: "685 megatonnes of carbon dioxide equivalent", excluding LULUCF.
  - That is -78 Mt (-10%) from 2005 and -2.2 Mt (-0.3%) from revised 2023.
- Per person: "from 24 t CO2 eq/capita [2005] to 17 t CO2 eq/capita in 2024".
- Targets: 40 to 45% below 2005 by 2030, and 45 to 50% by 2035.
- Raw: CAN_NIR_2026_partA_ec2d.pdf (643 pages, ECCC Cat. No. En81-4/4E-PDF), with text extract CAN_NIR_2026_p1-30.txt.
  - UNFCCC itself (unfccc.int/documents/656423) is behind an Incapsula block, so the file came from the Climate Policy Radar mirror of that UNFCCC document.

### Türkiye (NIR 2026, UNFCCC document 656426)
- 2024 emissions: **584.5 Mt CO2 eq excluding LULUCF.** That is +29.4 Mt (+5.3%) on 2023.
- Including LULUCF the total is **517.4 Mt** (LULUCF -67.1 Mt).
- By sector: energy 419.9, IPPU 75.7, agriculture 73.5 and waste 15.4 Mt.
- Raw: TUR_NIR_2026_unfccc_doc656426_via_CPR.pdf (507 pages), with text extract TUR_NIR_2026_p1-40.txt. Same mirror route as Canada.
- TurkStat's per-person figure of 6.8 t is in raw/ghg/eb2c2d.html (bulletin reproduction).

### Per person, using World Bank populations (SP.POP.TOTL, updated 2026-10-08)

| | Canada | Türkiye |
|---|---|---|
| Population 2024 | 41,262,329 | 85,518,661 |
| t CO2e per person (computed) | 16.6 | 6.83 |
| Official figure | 17 (ECCC) | 6.8 (TurkStat) |

- Ratio: **2.4 times** (computed). The 2.5 in results.md comes from dividing the rounded figures (17 / 6.8). Use 2.4.
- Raw: wb_population_CAN_TUR_2024.json
- StatCan is still unreachable, so the World Bank series stands in. It compiles from national sources.

### Türkiye NDC 3.0 (2035)
- Text: "limiting GHG emissions to 643 Mt CO2 eq. in 2035". It is a 466 Mt cut from BAU.
- **The reference indicator is "Net GHG emissions"**: 458.8 Mt incl. LULUCF in 2018. The target covers all IPCC sectors including LULUCF.
- **So compare 643 Mt with the net 517.4 Mt (2024), not with 584.5 Mt.** On that basis the target allows a rise of about 24% from 2024. Against the gross 584.5 Mt it would look like +10%, which mixes bases.
- Raw: TUR_NDC3_2035_faolex_tur240214.pdf (FAO FAOLEX copy of the NDC submission). The UNFCCC NDC registry was blocked. The UNEP LEAP record is unep_leap_tr_ndc3.html.

## 4. Boron and chromium (USGS MCS 2026, raw/minerals/)

| | Boron | Chromium |
|---|---|---|
| Türkiye production 2024 | 1,800 kt refined borates | 9,300 kt chromite (gross) |
| Türkiye production 2025e | 1,500 kt | 9,000 kt |
| World production 2025e | Not calculable | 51,000 kt |
| Türkiye share of production | Not calculable | **17.6%** (2025e), 18.8% (2024); 2nd after South Africa |
| Türkiye reserves | 950,000 kt (largest listed) | 27,000 kt ore (5,700 kt Cr2O3) |
| Share of world reserves | Not calculable | About 1% of Cr2O3 content (>540,000 kt) |
| US import reliance on Türkiye | 90% of boron imports | 3% of chromite ore |

- USGS on boron: "World totals cannot be calculated because production and reserves are not reported in a consistent manner by all countries". The countries report in different forms (refined borates, ulexite, B2O3 equivalent).
- **So no official world-share figure for boron exists in USGS. Do not use "73%".** Say instead "largest reserves of any country USGS lists".
- Eti Maden (etimaden.gov.tr): TLS certificate failure from the shell, and WebFetch was not approved. **Not reached.**
- Raw: raw/minerals/mcs2026-boron.pdf (sha256 a7606ad4...), mcs2026-chromium.pdf (sha256 c19e412f...), with .txt extracts.

## 5. Canadian energy exports to Türkiye, 2015 to 2025

- ISED Trade Data Online still resets connections, and so does StatCan. The table below therefore uses UN Comtrade (Canada-reported exports, USD), converted to CAD at Bank of Canada annual average rates.
  - 2017 to 2025: series FXAUSDCAD.
  - 2015 and 2016: mean of daily noon rates, IEXE0101.
- **This is a conversion, not StatCan's own CAD figure.**

| Year | HS 27, CAD M | Coal 2701, CAD M | Coal, kt | HS 2844, CAD M | All goods, CAD M |
|---|---|---|---|---|---|
| 2015 | 86.6 | 86.2 | 834 | 5.4 | 1,127 |
| 2016 | 133.3 | 132.8 | 1,039 | 8.6 | 1,152 |
| 2017 | 118.6 | 118.0 | 659 | 6.8 | 1,266 |
| 2018 | 123.6 | 123.3 | 531 | 3.6 | 1,330 |
| 2019 | 127.9 | 127.8 | 668 | 5.9 | 1,616 |
| 2020 | 145.6 | 145.5 | 1,155 | 5.3 | 1,223 |
| 2021 | 138.9 | 138.9 | 520 | 4.3 | 1,151 |
| 2022 | 156.1 | 155.5 | 338 | 3.0 | 1,282 |
| 2023 | 60.7 | 58.4 | 162 | 2.9 | 1,231 |
| 2024 | 2.7 | none reported | none reported | 2.8 | 1,255 |
| 2025 | 39.7 | 37.4 | 166 | 3.6 | 1,139 |

- **Uranium ores (HS 2612): no exports recorded in any year.**
- HS 2844, at the 6-digit level: only 284440 (radioactive isotopes other than U-235, Pu or U-233) appears, in 2015 and 2018 to 2021. **No natural uranium (284410) or enriched uranium (284420) was exported to Türkiye in any year.**
- Coal is 97 to 100% of HS 27 in every year except 2024.
- Mirror check: Türkiye-reported imports from Canada (HS 27) run higher in most years, e.g. USD 205.3M in 2022 vs Canada's USD 120.0M. That is normal for CIF/FOB valuation and timing. Türkiye's 2025 data is not yet in Comtrade.
- The CAD 1.14B all-goods 2025 total fits the PMO's "CAD 1.1 billion".
- Raw: comtrade_CAN_TUR_X_{year}.json, comtrade_CAN_TUR_X_HS6_{year}.json, comtrade_TUR_CAN_M_{year}.json, boc_FXAUSDCAD_annual.json, boc_IEXE0101_annual_2015-2016.json.

## 6. Uranium: 16.9 kt vs 14.3 kt (2024)

- The 16.9 kt figure is from the **Canada Energy Regulator** (Market Snapshot, modified 2026-02-18), **not CNSC**. The CER wording is "Canada's uranium production, which was 16.9 kilotonnes (kt) in 2024". It gives no unit basis. Raw: raw/cer/market-snapshot-canadian-uranium-exports-help-fuel-nuclear-generation-around-the-world.html
- NRCan: "In 2024, Canada produced 14.3 kilotonnes of uranium" (14,327 tonnes), on an elemental uranium (tU) basis, the same basis as its resource figures. Raw: nrcan_uranium_nuclear_power_facts.html
- **Conversion:** U3O8 has 1.1792 times the mass of the uranium it contains (molar mass 842.08 / 714.09).
  - 14,327 t U x 1.1792 = **16,895 t U3O8, or 16.9 kt.**
  - **So CER's figure is the same production expressed as U3O8 concentrate (yellowcake).**
  - CER does not state this itself, but its own footnote describes production as "yellowcake".
- **Use 14.3 kt U (NRCan) and say "tonnes of uranium".** If CER is quoted, call it U3O8.

## Still blocked
- unfccc.int: Incapsula block (WebFetch to the NIR index was not approved). NIR files came through the Climate Policy Radar mirror, which states the UNFCCC document IDs.
- canada.ca and web.archive.org: connection resets.
- data.tuik.gov.tr: JavaScript app only; its API needs a login.
- etimaden.gov.tr: TLS error.
- ISED TDO and www150.statcan.gc.ca: connection resets.
