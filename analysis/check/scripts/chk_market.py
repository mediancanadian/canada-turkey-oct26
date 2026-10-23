"""Recompute market-thread figures: Canada's share/rank in Türkiye imports, lira loss,
IMF ratios, FDI change, CPI chain."""
import json, csv, datetime
R = '../market/raw/'
# Comtrade partners 2025
ref = json.load(open(R + 'comtrade/partners_ref.json'))
refl = ref['results'] if isinstance(ref, dict) and 'results' in ref else ref
names = {r['id']: r['text'] for r in refl}
for yr in ['2024', '2025']:
    d = json.load(open(R + f'comtrade/tur_imports_{yr}_partners.json'))['data']
    vals = {r['partnerCode']: r['primaryValue'] for r in d}
    world = vals.get(0)
    excl = [c for c in vals if c == 0 or 'Special' in names.get(c, '') or names.get(c, '').endswith(' nes') or names.get(c, '').endswith(', nes') or 'World' in names.get(c, '')]
    ctry = {c: v for c, v in vals.items() if c not in excl}
    order = sorted(ctry, key=lambda c: -ctry[c])
    for c in [124, 842, 826, 36, 156, 643, 276]:
        if c in ctry:
            print(yr, names.get(c), 'US$%.2fbn' % (ctry[c] / 1e9), '%.2f%%' % (100 * ctry[c] / world), 'rank', order.index(c) + 1)
    print(yr, 'world %.1fbn' % (world / 1e9), 'excluded', [names.get(c) for c in excl])
# FX
fx = json.load(open(R + 'boc/FXCADTRY.json'))['observations']
s = {o['d']: float(o['FXCADTRY']['v']) for o in fx if o.get('FXCADTRY')}
def at(d):
    dd = datetime.date.fromisoformat(d)
    while dd.isoformat() not in s: dd -= datetime.timedelta(days=1)
    return dd.isoformat(), s[dd.isoformat()]
end = at('2026-10-22')
for st in ['2025-10-22', '2021-10-22', '2016-10-22']:
    if st < min(s):
        print('daily series starts', min(s), 'cannot do', st); continue
    a = at(st); print('lira loss from', a, 'to', end, '%.1f%%' % (100 * (1 - a[1] / end[1])), 'x%.2f' % (end[1] / a[1]))
leg = json.load(open(R + 'boc/legacy_noon_2015_2016.json'))
print('legacy keys', list(leg.keys())[:5])
# IMF ratios
imf = {}
for r in csv.DictReader(open('../market/outputs/imf_weo_oct2026_tur_can.csv')):
    imf[(r['indicator'], r['country'])] = r
print('GDPpc ratio nominal %.2f ppp %.2f' % (float(imf[('NGDPDPC', 'CAN')]['2025']) / float(imf[('NGDPDPC', 'TUR')]['2025']),
                                          float(imf[('PPPPC', 'CAN')]['2025']) / float(imf[('PPPPC', 'TUR')]['2025'])))
print('PPP GDPpc TR/CA %.2f' % (float(imf[('PPPPC', 'TUR')]['2025']) / float(imf[('PPPPC', 'CAN')]['2025'])))
raw = json.load(open(R + 'imf/NGDPDPC.json')); print('IMF raw TUR 2025', raw['values']['NGDPDPC']['TUR'].get('2025'))
print('cdia 3315/4126-1 = %.1f%%, 3315/992 = %.2f' % (100 * (3315 / 4126 - 1), 3315 / 992))
print('min wage 28075.5/33.127=%.0f; /35.3357=%.0f' % (28075.5 / 33.127, 28075.5 / 35.3357))
print('hh cons per cap TR %.0f CA %.0f' % (873.8e9 / 85.825e6, 1294.1e9 / 41.602e6))
print('ext debt/GDP 539/1818 = %.1f%%' % (100 * 539 / 1818))
# CPI chain
rows = list(csv.DictReader(open('../market/outputs/tur_cpi_monthly_tcmb.csv')))
print(rows[0].keys(), rows[:2])
