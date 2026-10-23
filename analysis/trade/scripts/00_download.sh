#!/bin/sh
# Download raw official files. Generic user agent only; no personal details sent.
# Usage: sh 00_download.sh ../trade/raw
set -e
R="$1"; UA="Mozilla/5.0"
cd "$R"
# StatCan WDS cube list + metadata
curl -sS -A "$UA" https://www150.statcan.gc.ca/t1/wds/rest/getAllCubesListLite -o allcubes.json
for p in 12100011 12100147 12100148 12100149 12100150 12100151 12100152 12100171 12100173 12100182; do
  curl -sS -A "$UA" -X POST -H 'Content-Type: application/json' -d "[{\"productId\":$p}]" \
    https://www150.statcan.gc.ca/t1/wds/rest/getCubeMetadata -o meta_$p.json
done
# Full-table CSVs (12-10-0173 is ~27 MB zipped, 456 MB unzipped; connection resets happen, retry)
for p in 12100171 12100173 12100011 18100005; do
  for i in 1 2 3; do curl -sS -L -A "$UA" -o $p-eng.zip https://www150.statcan.gc.ca/n1/tbl/csv/$p-eng.zip && break; done
  d=x$(echo $p | cut -c6-8); mkdir -p $d; unzip -o -q $p-eng.zip -d $d
done
# HS reference list (UN Comtrade)
curl -sS -A "$UA" https://comtradeapi.un.org/files/v1/app/reference/HS.json -o comtrade_HS_ref.json
# UN Comtrade public preview, annual totals, Canada<->Turkiye both reporters (1 period per call)
mkdir -p comtrade
for r in 792 124; do pt=$([ $r = 792 ] && echo 124 || echo 792)
  for y in 2015 2019 2020 2021 2022 2023 2024 2025; do
    curl -sS -A "$UA" "https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=$r&partnerCode=$pt&period=$y&cmdCode=TOTAL&flowCode=M,X&partner2Code=0&customsCode=C00&motCode=0" -o comtrade/total_r${r}_$y.json
    sleep 4
  done
done
# Bank of Canada annual average USD/CAD
curl -sS -A "$UA" https://www.bankofcanada.ca/valet/observations/FXAUSDCAD/json -o boc_FXAUSDCAD.json
# Government pages used to check stated figures
mkdir -p web
curl -sSL -A "$UA" "https://www.international.gc.ca/country-pays/turkiye/relations.aspx?lang=eng" -o web/2a1087a0.html
curl -sSL -A "$UA" "https://www.pm.gc.ca/en/node/54279" -o web/54d835a2.html
curl -sSL -A "$UA" "https://international.canada.ca/en/global-affairs/consultations/trade/2026-07-29-turkiye" -o web/93279161.html
# Then: python3 -I ../scripts/01_fetch_hs2.py wds ; python3 -I ../scripts/02_fetch_hs6.py .
