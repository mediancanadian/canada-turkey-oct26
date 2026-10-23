#!/bin/bash
# OCR Resmi Gazete scanned decision PDFs (Karar 10790 import regime, 10791 additional duty)
cd ../tariffs/raw/tr
mkdir -p ocr
for f in 20251231M3-2 20251231M3-1; do
  n=$(python3 -I -c "import pypdf;print(len(pypdf.PdfReader('$f.pdf').pages))")
  seq 1 $n | xargs -P 8 -I{} sh -c "[ -s ocr/$f-p{}.txt ] || (pdftoppm -r 200 -f {} -l {} -png -singlefile $f.pdf ocr/$f-p{} && tesseract ocr/$f-p{}.png ocr/$f-p{} --psm 6 >/dev/null 2>&1 && rm ocr/$f-p{}.png)"
done
echo done
