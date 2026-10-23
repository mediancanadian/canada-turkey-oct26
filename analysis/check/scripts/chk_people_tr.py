"""Rank Canadian nationals among foreign arrivals in Türkiye border bulletin 2025."""
import openpyxl
ws=openpyxl.load_workbook('../people/raw/turkiye/sinir_2025.xlsx',read_only=True,data_only=True)['C-Mil Göre G.Yabancı']
rows=[list(r[1:]) for r in ws.iter_rows(values_only=True)]
yrs=list(rows[2][1:])
data=[r for r in rows[3:] if r and isinstance(r[0],str) and r[0].strip()]
agg=[r[0] for r in data if any(k in r[0].upper() for k in ['TOPLAM','DİĞER','GENEL','TOTAL'])]
print('agg rows',agg)
data=[r for r in data if r[0] not in agg]
for y in range(2015,2026):
    j=yrs.index(y)+1
    vals={r[0].strip():(r[j] if isinstance(r[j],(int,float)) else 0) for r in data}
    print(y,'Kanada',vals.get('Kanada'),'rank',sorted(vals,key=lambda k:-vals[k]).index('Kanada')+1,'n',len(vals))
