import openpyxl,sys,json
def load(path,label_cols=1):
    wb=openpyxl.load_workbook(path,read_only=True); ws=wb.worksheets[0]
    rows=[list(r) for r in ws.iter_rows(values_only=True)]
    return rows
def annual(path,keycol=0,header_row=None):
    rows=load(path)
    # find header row with 'Total' year labels
    hr=None
    for i,r in enumerate(rows[:12]):
        if any(isinstance(c,str) and c.strip().endswith(' Total') and c.strip()[:4].isdigit() for c in r): hr=i;break
    yearcols={str(c).strip()[:4]:j for j,c in enumerate(rows[hr]) if isinstance(c,str) and c.strip().endswith(' Total') and c.strip()[:4].isdigit()}
    # last year YTD: last numeric column if no 'YYYY Total'
    data={}
    for r in rows[hr+1:]:
        if not r: continue
        k=r[keycol]
        if not k or not isinstance(k,str): continue
        d={}
        for y,j in yearcols.items():
            v=r[j] if j<len(r) else None
            if v in (None,''): continue
            v=str(v).replace(',','')
            d[y]=None if v=='--' else float(v)
        data[k.strip()]=d
    return rows,hr,yearcols,data
if __name__=='__main__':
    rows,hr,yc,data=annual(sys.argv[1])
    print(rows[0][0]); print(yc)
    print(json.dumps({k:v for k,v in data.items() if 'Turk' in k or k=='Total'},indent=0))
