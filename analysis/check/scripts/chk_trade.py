"""Independent recomputation of trade headline figures from saved raw files."""
import json, csv, collections
R = '../trade/raw/'

def load(f):
    return json.load(open(R + 'wds/' + f))

def annual(d, geo='1', est=None):
    out = collections.defaultdict(float)
    mon = collections.defaultdict(float)
    for k, series in d.items():
        p = k.split('.')
        if p[0] != geo:
            continue
        if est and p[3] != est:
            continue
        for ym, v in series:
            if v is None:
                continue
            out[ym[:4]] += v
            mon[ym] += v
    return out, mon

ex = load('hs2_exports_tur.json')
im = load('hs2_imports_tur.json')
exA, exM = annual(ex)
dom, domM = annual(ex, est='1')
rex, rexM = annual(ex, est='2')
imA, imM = annual(im)
print('Year exports dom reex imports twoway balance ratio (C$M)')
for y in range(2010, 2027):
    y = str(y)
    e, i = exA[y] / 1e3, imA[y] / 1e3
    print(y, round(e, 1), round(dom[y] / 1e3, 1), round(rex[y] / 1e3, 1), round(i, 1), round(e + i, 1), round(e - i, 1), round(i / e, 2))
# YTD Jan-Aug
def ytd(m, y):
    return sum(v for k, v in m.items() if k.startswith(y) and int(k[5:7]) <= 8) / 1e3
for y in ['2025', '2026']:
    print('JanAug', y, 'exp', round(ytd(exM, y), 1), 'dom', round(ytd(domM, y), 1), 'rex', round(ytd(rexM, y), 1), 'imp', round(ytd(imM, y), 1))
e25, e26 = ytd(exM, '2025'), ytd(exM, '2026')
i25, i26 = ytd(imM, '2025'), ytd(imM, '2026')
print('exp chg %.1f%% dom %.1f%% rex %.1f%% imp %.1f%% two-way %.1f%%' % (
    100 * (e26 / e25 - 1), 100 * (ytd(domM, '2026') / ytd(domM, '2025') - 1), 100 * (ytd(rexM, '2026') / ytd(rexM, '2025') - 1),
    100 * (i26 / i25 - 1), 100 * ((e26 + i26) / (e25 + i25) - 1)))
print('ratio ytd 2025 %.2f 2026 %.2f' % (i25 / e25, i26 / e26))
# 5-yr block ratios
for a in range(1991, 2026, 5):
    ys = [str(y) for y in range(a, a + 5)]
    print('block', a, a + 4, round(sum(imA[y] for y in ys) / sum(exA[y] for y in ys), 2))
for y in range(1988, 2026):
    pass
mx = max(range(1988, 2026), key=lambda y: imA[str(y)] / exA[str(y)] if exA[str(y)] else 0)
print('max ratio year', mx)
# CAGR
tw = {y: (exA[y] + imA[y]) / 1e3 for y in exA}
for a in [2020, 2015, 2010, 2000]:
    n = 2025 - a
    print('CAGR', a, 'total %.1f%%' % (100 * (tw['2025'] / tw[str(a)] - 1)), 'cagr %.1f%%' % (100 * ((tw['2025'] / tw[str(a)]) ** (1 / n) - 1)),
          'exp %.1f%%' % (100 * ((exA['2025'] / exA[str(a)]) ** (1 / n) - 1)), 'imp %.1f%%' % (100 * ((imA['2025'] / imA[str(a)]) ** (1 / n) - 1)))
print('2020-2024 two-way %.1f%%' % (100 * (tw['2024'] / tw['2020'] - 1)))
# CPI
cpi = {}
for r in csv.DictReader(open(R + 'x005/18100005.csv', encoding='utf-8-sig')):
    if r['GEO'] == 'Canada' and r['Products and product groups'] == 'All-items':
        cpi[r['REF_DATE']] = float(r['VALUE'])
for a in [2020, 2015, 2010, 2000]:
    n = 2025 - a
    real = (tw['2025'] / cpi['2025']) / (tw[str(a)] / cpi[str(a)])
    print('real CAGR', a, '%.1f%%' % (100 * (real ** (1 / n) - 1)), 'CPI rise %.1f%%' % (100 * (cpi['2025'] / cpi[str(a)] - 1)))

# Rank 2025 from 0171
tot = collections.defaultdict(lambda: collections.defaultdict(float))
for r in csv.DictReader(open(R + 'x171/12100171.csv', encoding='utf-8-sig')):
    if r['North American Product Classification System (NAPCS)'] != 'All sections':
        continue
    if r['VALUE'] == '':
        continue
    tot[r['REF_DATE']][(r['Trading partner'], r['Trade'])] = float(r['VALUE']) / 1e3
for yr in ['2015', '2020', '2024', '2025']:
    t = tot[yr]
    parts = set(p for p, _ in t) - {'All countries', 'Canada', 'High Seas'}
    for flow in ['two', 'Export', 'Import']:
        val = {p: (t.get((p, 'Export'), 0) + t.get((p, 'Import'), 0)) if flow == 'two' else t.get((p, flow), 0) for p in parts}
        allv = (t[('All countries', 'Export')] + t[('All countries', 'Import')]) if flow == 'two' else t[('All countries', flow)]
        order = sorted(val, key=lambda p: -val[p])
        rk = order.index('Türkiye') + 1
        print(yr, flow, 'rank', rk, 'of', len(parts), 'share %.3f%%' % (100 * val['Türkiye'] / allv), 'TR %.1f all %.1f' % (val['Türkiye'], allv))
        if yr == '2025' and flow == 'two':
            print('  neighbours', [(i + 1, p, round(val[p] / 1e3, 2)) for i, p in enumerate(order) if 23 <= i <= 29])
