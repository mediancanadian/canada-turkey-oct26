"""Recompute PR counts, ranks, 2026 months, categories, visa and citizen ranks for Türkiye."""
import csv, collections, openpyxl
R = '../people/raw/ircc/'
def num(x):
    x = (x or '').replace(',', '').strip()
    return float(x) if x and x != '--' else 0.0
pr = collections.defaultdict(lambda: collections.defaultdict(float)); mon = collections.defaultdict(float)
for r in csv.DictReader(open(R + 'ODP-PR-Citz.csv', encoding='utf-8-sig', errors='ignore'), delimiter='\t'):
    pr[r['EN_YEAR']][r['EN_COUNTRY_OF_CITIZENSHIP']] += num(r['TOTAL'])
    if r['EN_COUNTRY_OF_CITIZENSHIP'] == 'Turkey' and r['EN_YEAR'] == '2026': mon[r['EN_MONTH']] += num(r['TOTAL'])
for y in sorted(pr):
    d = {k: v for k, v in pr[y].items() if k not in ('Not stated', 'Total', '')}
    tot = sum(d.values()); rk = sorted(d, key=lambda k: -d[k]).index('Turkey') + 1
    print(y, 'TR', d['Turkey'], 'rank', rk, 'of', len(d), 'share %.2f%%' % (100 * d['Turkey'] / tot))
print('2026 months', dict(mon))
cat = collections.defaultdict(float)
for r in csv.DictReader(open(R + 'ODP-PR-Citz_immcat.csv', encoding='utf-8-sig', errors='ignore'), delimiter='\t'):
    if r['EN_COUNTRY_OF_CITIZENSHIP'] != 'Turkey': continue
    g = r['EN_IMMIGRATION_CATEGORY-GROUP']; m = r['EN_IMMIGRATION_CATEGORY-MAIN_CATEGORY']
    key = 'protected_in_canada' if 'Protected Persons in Canada' in g or 'Protected Person' in g else ('economic' if m == 'Economic' else ('family' if 'Sponsored' in m or 'Family' in m else None))
    if key: cat[(r['EN_YEAR'], key)] += num(r['TOTAL'])
for y in ['2019', '2021', '2023', '2024', '2025', '2026']:
    print('cat', y, {k: cat[(y, k)] for k in ['protected_in_canada', 'economic', 'family']})
groups = set()
for r in csv.DictReader(open(R + 'ODP-PR-Citz_immcat.csv', encoding='utf-8-sig', errors='ignore'), delimiter='\t'):
    groups.add((r['EN_IMMIGRATION_CATEGORY-MAIN_CATEGORY'], r['EN_IMMIGRATION_CATEGORY-GROUP']))
print(sorted(groups))
# visitor visas and new citizens rank
for f, col in [('trv_v1_approved.xlsx', None), ('new_citizens_cob.xlsx', None)]:
    ws = openpyxl.load_workbook(R + f, read_only=True, data_only=True).worksheets[0]
    rows = [list(r) for r in ws.iter_rows(values_only=True)]
    hdr = [i for i, r in enumerate(rows) if r and any(isinstance(c, str) and 'Total' in c for c in r[1:])][0]
    h = rows[hdr]
    tcols = [i for i, c in enumerate(h) if isinstance(c, str) and 'Total' in c]
    data = [r for r in rows[hdr + 1:] if r and isinstance(r[0], str) and r[0].strip() and r[0].strip() != 'Total']
    for ti, ci in enumerate(tcols):
        vals = {r[0].strip(): (r[ci] if isinstance(r[ci], (int, float)) else 0) for r in data}
        rk = sorted(vals, key=lambda k: -vals[k]).index('Turkey') + 1
        print(f, h[ci], 'TR', vals['Turkey'], 'rank', rk)
    if f == 'trv_v1_approved.xlsx':
        tr = [r for r in data if r[0].strip() == 'Turkey'][0]
        print('  2026 Jan-Aug sum', sum(c for c in tr[40:48] if isinstance(c, (int, float))), tr[40:49])
