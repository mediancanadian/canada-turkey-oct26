#!/bin/sh
# Builds site/data/provinces.json, the province map on the page.
# Source: Natural Earth 1:10m admin-1 states and provinces with large lakes cut out (public domain),
# https://github.com/nvkelso/natural-earth-vector (geojson/ne_10m_admin_1_states_provinces_lakes.geojson).
# Projected to EPSG:3978 (Canada Atlas Lambert) and simplified as one topology, so neighbouring
# provinces share the same border points and no gaps open between them.
set -e
cd "$(dirname "$0")"
curl -sSfL -o "${TMPDIR:-/tmp}/ne10_lakes.geojson" https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_admin_1_states_provinces_lakes.geojson
npx -y mapshaper@0.6.102 -i "${TMPDIR:-/tmp}/ne10_lakes.geojson" -filter "adm0_a3=='CAN'" -each "p=postal" -filter-fields p \
  -proj EPSG:3978 -simplify 6% keep-shapes planar -filter-islands min-area=150km2 -rename-layers provs \
  -o format=topojson quantization=100000 data/provinces.json
