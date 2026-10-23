"""Recompute HS6 top products, province figures and NAPCS sections from raw cubes."""
import json, csv, collections
R = '../trade/raw/'
def code(p):
    h2, h4, h6 = int(p[4]), int(p[5]), int(p[6])
    h4 = 0 if h4 == 100 else h4
    h6 = 0 if h6 == 100 else h6
    return '%02d%02d%02d' % (h2, h4, h6)
geo_names = {}
m = json.load(open(R + 'meta_12100148.json')); o = m[0]['object'] if isinstance(m, list) else m
for dim in o['dimension']:
    if dim['dimensionPositionId'] == 1:
        geo_names = {str(x['memberId']): x['memberNameEn'] for x in dim['member']}

def agg(f, ests):
    d = json.load(open(R + 'wds/' + f))
    out = collections.defaultdict(float)  # (geo, year, code)
    for k, s in d.items():
        p = k.split('.')
        if p[3] not in ests:
            continue
        c = code(p)
        for ym, v in s:
            if v is None:
                continue
            out[(p[0], ym[:4], c)] += v / 1e3
    return out
ex = agg('hs6_exp_tur.json', {'1', '2'})
dom = agg('hs6_exp_tur.json', {'1'})
im = agg('hs6_imp_tur.json', {'1'})
def top(d, geo, yr, n=15):
    items = [(c, v) for (g, y, c), v in d.items() if g == geo and y == yr]
    tot = sum(v for _, v in items)
    return tot, sorted(items, key=lambda x: -x[1])[:n]
for name, d in [('EXP', ex), ('IMP', im)]:
    for yr in ['2024', '2025']:
        tot, t = top(d, '1', yr)
        print(name, yr, 'HS6 sum %.1f' % tot, 'top15 share %.1f%%' % (100 * sum(v for _, v in t) / tot))
        print('  ', [(c, round(v, 1)) for c, v in t])
for c in ['071340']:
    print('lentils', [(y, round(ex[('1', y, c)], 1)) for y in ['2021', '2022', '2023', '2024', '2025']])
    print('SK lentils dom', [(y, round(dom[('47', y, c)], 1)) for y in ['2021', '2022', '2023', '2024', '2025']])
    print('AB lentils dom 2025', round(dom[('48', '2025', c)], 1))
print('SK chickpea', round(dom[('47', '2025', '071320')], 1), 'SK durum', round(dom[('47', '2025', '100119')], 1))
print('QC aircraft', round(dom[('24', '2025', '880240')] + dom[('24', '2025', '880230')], 1), 'QC scrap', round(dom[('24', '2025', '720429')], 1),
      'QC scrap 5y', round(sum(dom[('24', str(y), '720429')] for y in range(2021, 2026)) / 5, 1))
print('ON 901380', round(dom[('35', '2025', '901380')], 1), 'ON 870390', round(dom[('35', '2025', '870390')], 1))
print('BC 841121', round(dom[('59', '2025', '841121')], 1), 'BC coal', round(dom[('59', '2025', '270112')], 1),
      'BC coal 5y', round(sum(dom[('59', str(y), '270112')] for y in range(2021, 2026)) / 5, 1))
print('NL 890200 imp', round(im[('10', '2025', '890200')], 1))
print('ON 300215 imp', round(im[('35', '2025', '300215')], 1))
print('scrap 720429 total ex 2024/2025', round(ex[('1', '2024', '720429')], 1), round(ex[('1', '2025', '720429')], 1))
print('soy', round(ex[('1', '2024', '120190')], 1), round(ex[('1', '2025', '120190')], 1))
print('aircraft total', round(ex[('1', '2025', '880240')] + ex[('1', '2025', '880230')], 1))
# province totals from HS2 cube
d = json.load(open(R + 'wds/hs2_exports_tur.json'))
pe = collections.defaultdict(float)
for k, s in d.items():
    p = k.split('.')
    if p[3] != '1':
        continue
    for ym, v in s:
        if v is not None:
            pe[(p[0], ym[:4])] += v / 1e3
d = json.load(open(R + 'wds/hs2_imports_tur.json'))
pi = collections.defaultdict(float)
for k, s in d.items():
    p = k.split('.')
    for ym, v in s:
        if v is not None:
            pi[(p[0], ym[:4])] += v / 1e3
for g, n in geo_names.items():
    print(n, 'dom25 %.1f avg %.1f imp25 %.1f avg %.1f' % (pe[(g, '2025')], sum(pe[(g, str(y))] for y in range(2021, 2026)) / 5,
                                                      pi[(g, '2025')], sum(pi[(g, str(y))] for y in range(2021, 2026)) / 5))
print('ON+QC import share %.1f%%' % (100 * (pi[('35', '2025')] + pi[('24', '2025')]) / pi[('1', '2025')]))
# NAPCS
sec = collections.defaultdict(float)
for r in csv.DictReader(open(R + 'x171/12100171.csv', encoding='utf-8-sig')):
    if r['Trading partner'] == 'Türkiye' and r['REF_DATE'] in ('2024', '2025') and r['VALUE']:
        sec[(r['REF_DATE'], r['Trade'], r['North American Product Classification System (NAPCS)'])] = float(r['VALUE']) / 1e3
for k in sorted(sec):
    if sec[k] > 140:
        print(k, round(sec[k], 1))
fx = json.load(open(R + 'boc_FXAUSDCAD.json'))
obs = [float(o['FXAUSDCAD']['v']) for o in fx['observations'] if o['d'].startswith('2025')]
print('BoC 2025 annual', obs)
