"""Rank Türkiye in Table 6 of the 2023-2025 GAC report text extracts."""
import re
D='../defence/raw/reports/'
for yr in ['2023','2024','2025']:
    t=open(D+f'report_{yr}.html.txt',errors='ignore').read().split('\n')
    i=[k for k,l in enumerate(t) if re.match(r'Table 6: '+yr,l)]
    if not i:
        i=[k for k,l in enumerate(t) if 'Value of exports of military goods and technology by destination' in l]
    i=i[-1]; rows=[]
    for l in t[i+1:]:
        if l.startswith('Table 7'): break
        m=re.match(r'\s*(.+?)\s+\$\s?([\d,]+\.\d\d)\s*$',l)
        if m and not m.group(1).lower().startswith('total'): rows.append((m.group(1).strip(),float(m.group(2).replace(',',''))))
    rows.sort(key=lambda x:-x[1]); tot=sum(v for _,v in rows)
    tv=[v for n,v in rows if 'rkiye' in n][0]
    above=sum(1 for _,v in rows if v>tv); same=sum(1 for _,v in rows if v==tv)
    print(yr,'n',len(rows),'total %.2f'%tot,'TR %.2f'%tv,'rank',above+1,'(ties %d)'%same,'share %.3f%%'%(100*tv/tot))
