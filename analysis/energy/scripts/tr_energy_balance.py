import openpyxl,sys
wb=openpyxl.load_workbook(sys.argv[1],data_only=True,read_only=True)
ws=wb['BİN TEP 2024']; rows=list(ws.iter_rows(values_only=True))
hdr=rows[3]; idx={h:i for i,h in enumerate(hdr) if h}
def row(lbl): return next(r for r in rows if r[0] and str(r[0]).strip().startswith(lbl))
T=idx['TOPLAM']
prod=row('Yerli Üretim')[T]; imp=row('İthalat')[T]; exp=row('İhracat')[T]; bunk=row('İhrakiye')[T]; sup=row('ENERJİ ÜRÜNLERİ ARZI')[T]
print(f'2024 ktoe: production {prod:,.0f}; imports {imp:,.0f}; exports {exp:,.0f}; bunkers {bunk:,.0f}; total energy supply {sup:,.0f}')
print(f'net imports / supply = {(imp-exp)/sup*100:.1f}%')
print(f'gross imports / supply = {imp/sup*100:.1f}%')
print(f'domestic production / supply = {prod/sup*100:.1f}% -> 1 - that = {100-prod/sup*100:.1f}%')
for k in ('Taş Kömürü','Ham Petrol','Doğal Gaz3'):
    i=idx[k]; print(k,'imports',round(row('İthalat')[i] or 0),'supply',round(row('ENERJİ ÜRÜNLERİ ARZI')[i] or 0))
