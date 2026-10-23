"""Independently parse GAC military export destination tables (2023-2025 HTML) and
2017-2022 text tables, rank Türkiye among non-US destinations."""
import re, html, sys
from html.parser import HTMLParser
D = '../defence/raw/reports/'

class T(HTMLParser):
    def __init__(s):
        super().__init__(); s.tables = []; s.cap = None; s.inT = 0; s.row = None; s.cell = None; s.incap = False
    def handle_starttag(s, t, a):
        if t == 'table': s.inT += 1; s.tables.append({'cap': '', 'rows': []})
        elif t == 'caption' and s.inT: s.incap = True
        elif t == 'tr' and s.inT: s.row = []
        elif t in ('td', 'th') and s.row is not None: s.cell = ''
    def handle_endtag(s, t):
        if t == 'table': s.inT -= 1
        elif t == 'caption': s.incap = False
        elif t == 'tr' and s.row is not None: s.tables[-1]['rows'].append(s.row); s.row = None
        elif t in ('td', 'th') and s.cell is not None: s.row.append(re.sub(r'\s+', ' ', s.cell).strip()); s.cell = None
    def handle_data(s, d):
        if s.incap: s.tables[-1]['cap'] += d
        elif s.cell is not None: s.cell += d

def money(x):
    x = x.replace('$', '').replace(',', '').replace('\xa0', '').strip()
    try: return float(x)
    except: return None

for yr in ['2023', '2024', '2025']:
    p = T(); p.feed(open(D + f'report_{yr}.html', errors='ignore').read())
    best = None
    for tb in p.tables:
        vals = [(r[0], money(r[-1])) for r in tb['rows'] if len(r) >= 2 and money(r[-1]) is not None]
        names = [n for n, _ in vals]
        if any('rkiye' in n for n in names) and len(vals) > 50:
            if best is None or len(vals) > len(best[1]): best = (tb['cap'], vals)
    cap, vals = best
    vals = [(n, v) for n, v in vals if not n.lower().startswith('total') and 'United States' != n]
    vals.sort(key=lambda x: -x[1])
    tot = sum(v for _, v in vals)
    tr = [(i + 1, n, v) for i, (n, v) in enumerate(vals) if 'rkiye' in n][0]
    ties = [n for n, v in vals if v == tr[2]]
    above = sum(1 for n, v in vals if v > tr[2])
    print(yr, cap.strip()[:80], '| n', len(vals), 'total %.0f' % tot, 'TR', tr, 'share %.2f%%' % (100 * tr[2] / tot), 'strictly above', above, 'ties', len(ties))
    if yr == '2025':
        print('  top 8', [(n, round(v / 1e6, 1)) for n, v in vals[:8]])
# 2017-2022 text: count destinations above Türkiye in the destination table
for yr, val in [('2017', 48269530.60), ('2018', 115743236.98), ('2019', 151428455.48), ('2020', 48049465.54), ('2021', 928441.50), ('2022', 60060.00)]:
    t = open(D + f'rep_{yr}.txt', errors='ignore').read()
    vals = {}
    for m in re.finditer(r'^\s*([A-Z][A-Za-zÀ-ÿ\'’ ,\.\(\)&-]+?)\s{2,}\$([\d,]+\.\d\d)', t, flags=re.M):
        n = m.group(1).strip(); v = float(m.group(2).replace(',', ''))
        if n.lower().startswith('total'): continue
        vals.setdefault(n, v)
    above = sorted([(n, v) for n, v in vals.items() if v > val and 'United States' not in n], key=lambda x: -x[1])
    print(yr, 'destinations parsed', len(vals), 'above TR:', len(above), [(n, round(v / 1e6, 1)) for n, v in above[:6]])
