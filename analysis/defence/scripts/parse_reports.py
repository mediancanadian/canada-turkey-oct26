"""Parse GAC military exports reports (PDF text via pdftotext -layout, or HTML text) to get
Türkiye value, rank among non-US destinations, total, and ECL breakdown (Annex G / destination x ECL table)."""
import re,sys,json
D='../defence/raw/reports/'
# (file, value-table heading regex, value-table end regex, ecl-table heading regex)
CFG={
 '2014':('rep_2014.txt',r'Table 4: Exports of Military Goods and Technology by Destination - 201[45][ \d]*\n',r'Table 5',r'by Destination and Export Control List Item - 2014'),
 '2015':('rep_2015.txt',r'Table 4: Exports of Military Goods and Technology by Destination - 201[45][ \d]*\n',r'Table 5',r'by Destination and Export Control List Item - 2015'),
 '2016':('rep_2016.txt',r'Table 8: 2016 . Exports of Military Goods and Technology to All Destinations by Value',r'Table 9',r'Table 13: 2016 . Exports of Military Goods and Technology by Destination and ECL Item'),
 '2017':('rep_2017.txt',r'Table 6: 2017 . Export Value of Military Goods and Technology to All Destinations',r'Table 7',r'Table 10: 2017 . Exports of Military Goods and Technology by Destination and ECL Item'),
 '2018':('rep_2018.txt',r'Table 6: 2018 . Export Value of Military Goods and Technology to all non-U.S. Destinations',r'Table 7',r'Annex G'),
 '2019':('rep_2019.txt',r'Table 6: 2019 . Export Value of Military Goods and Technology to all non-U.S. Destinations',r'Table 7',r'Annex G'),
 '2020':('rep_2020.txt',r'Table 6: 2020 . Export Value of Military Goods and Technology to all non-U.S. Destinations',r'Table 7',r'Annex G'),
 '2021':('rep_2021.txt',r'Table 6: 2021 . Export Value of Military Goods and Technology to all non-U.S. Destinations',r'Table 7',r'Annex G'),
 '2022':('rep_2022.txt',r'Table 6: 2022 . Export value of military goods and technology to all non-U.S. destinations',r'Table 7',r'Annex G'),
 '2023':('report_2023.html.txt',r'Table 6: 2023 . Value of exports',r'Table 7',r'Annex G'),
 '2024':('report_2024.html.txt',r'Table 6:',r'Table 7',r'Annex G'),
 '2025':('report_2025.html.txt',r'Table 6:',r'Table 7',r'Annex G'),
}
money=r'\$\s?([\d,]+(?:\.\d+)?)'
def num(s): return float(s.replace(',',''))
out={}
for y,(f,h,e,eh) in CFG.items():
    t=open(D+f,encoding='utf-8',errors='ignore').read()
    ms=list(re.finditer(h,t,flags=re.I))
    if not ms: print(y,'no heading'); continue
    # choose the occurrence that yields most rows (skip table of contents)
    best=None
    for m in ms:
        i=m.end(); j=re.search(e,t[i:]); seg=t[i:i+(j.start() if j else 20000)]
        rows=[]
        for line in seg.split('\n'):
            mm=re.match(r'\s*([A-Z][A-Za-zÀ-ɏ\'’,\.\(\)\- &]+?)\s{1,}'+money,line)
            if mm and not re.search(r'(?i)total|destination|country|value',mm.group(1).strip()):
                rows.append((mm.group(1).strip(),num(mm.group(2))))
            # two-column layouts: catch second pair on same line
            for mm2 in re.finditer(r'\s{3,}([A-Z][A-Za-zÀ-ɏ\'’,\.\(\)\- &]+?)\s{1,}'+money,line[ (mm.end() if mm else 0):]):
                if not re.search(r'(?i)total|value',mm2.group(1).strip()): rows.append((mm2.group(1).strip(),num(mm2.group(2))))
        if best is None or len(rows)>len(best): best=rows
    rows=best
    seen={}; 
    for n,v in rows: seen.setdefault(n,v)
    rows=sorted(seen.items(),key=lambda r:-r[1])
    tk=[k for k,r in enumerate(rows) if re.search(r'rkiye|Turkey',r[0])]
    res={'file':f,'n_destinations_parsed':len(rows),'sum_parsed':round(sum(v for _,v in rows),2)}
    if tk: res.update(turkiye_value=rows[tk[0]][1],turkiye_rank=tk[0]+1)
    # ECL breakdown: find Türkiye block in last occurrence of ecl heading
    ems=list(re.finditer(eh,t,flags=re.I))
    if ems:
        seg=t[ems[-1].start():]
        m=re.search(r'\n\s*(Türkiye|Turkey)\s+(2-\d+)',seg)
        ecl={}
        if m:
            blk=seg[m.start():m.start()+3000].split('\n')[1:]
            for k,line in enumerate(blk):
                if re.search(r'(?i)continued|export destination|destination\s+ecl|value exported|^\s*-?\s*\d+\s*-?\s*$|annex g',line): continue
                if re.match(r'\s*[A-Z][a-z]',line) and not re.match(r'\s*(Türkiye|Turkey)',line): break
                for mm in re.finditer(r'(2-\d+)\.?\s+'+money,line): ecl[mm.group(1)]=num(mm.group(2))
        res['ecl']=ecl
    out[y]=res; print(y,res)
json.dump(out,open('../defence/outputs/exports_by_year_parsed.json','w'),indent=1,ensure_ascii=False)
