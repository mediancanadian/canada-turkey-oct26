#!/bin/bash
# OCR the GTIP code column (top area) of a page of a Resmi Gazete scanned tariff annex; prints first code found
f=$1; p=$2
pdftoppm -r 300 -f $p -l $p -x 200 -y 250 -W 230 -H 900 -gray -png -singlefile $f ${TMPDIR:-/tmp}/pc_$p 2>/dev/null
tesseract ${TMPDIR:-/tmp}/pc_$p.png - --psm 6 -c tessedit_char_whitelist=0123456789. 2>/dev/null | grep -oE '[0-9]{4}\.[0-9]{2}\.[0-9]{2}' | head -1
