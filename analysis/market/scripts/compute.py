"""Derived numbers: FDI series, Canada age structure, min wage conversions, consumption per person, IMF table.
Usage: python3 -I compute.py <base>"""
import csv, json, sys
base = sys.argv[1]
R, O = base + '/raw/', base + '/outputs/'
out = {}
# FDI
fdi = {}
for r in csv.DictReader(open(R + 'statcan/36100008.csv', encoding='utf-8-sig')):
    if r['Countries or regions'] == 'Türkiye' and 'total book value' in r['Canadian and foreign direct investment'] and '2010' <= r['REF_DATE'] <= '2025':
        k = 'CDIA_in_Turkiye' if r['Canadian and foreign direct investment'].startswith('Canadian') else 'FDI_from_Turkiye_in_Canada'
        fdi.setdefault(r['REF_DATE'], {})[k] = r['VALUE'] if r['VALUE'] else r['STATUS']
with open(O + 'fdi_canada_turkiye_2010_2025.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['year', 'canadian_direct_investment_in_turkiye_CADm', 'turkish_direct_investment_in_canada_CADm'])
    for y in sorted(fdi): w.writerow([y, fdi[y].get('CDIA_in_Turkiye'), fdi[y].get('FDI_from_Turkiye_in_Canada')])
c24, c25, c22 = float(fdi['2024']['CDIA_in_Turkiye']), float(fdi['2025']['CDIA_in_Turkiye']), float(fdi['2022']['CDIA_in_Turkiye'])
out['cdia_2025_vs_2024_pct'] = round((c25 / c24 - 1) * 100, 1)
out['cdia_2025_vs_2022_x'] = round(c25 / c22, 2)
# Canada age structure
ca = {}
for r in csv.DictReader(open(R + 'statcan/17100005.csv', encoding='utf-8-sig')):
    if r['GEO'] == 'Canada' and r['REF_DATE'] in ('2025', '2026') and r['Gender'] == 'Total - gender' and r['Age group'] in ('All ages', '0 to 14 years', '15 to 64 years', '65 years and older', 'Median age'):
        ca.setdefault(r['REF_DATE'], {})[r['Age group']] = float(r['VALUE'])
for y, d in ca.items():
    t = d['All ages']
    out[f'canada_{y}'] = {'pop': t, 'median_age': d['Median age'], 'pct_0_14': round(d['0 to 14 years'] / t * 100, 1),
                          'pct_15_64': round(d['15 to 64 years'] / t * 100, 1), 'pct_65plus': round(d['65 years and older'] / t * 100, 1)}
out['canada_growth_jul2025_jul2026_pct'] = round((ca['2026']['All ages'] / ca['2025']['All ages'] - 1) * 100, 2)
# min wage conversion
try_cad = {o['d']: float(o['FXCADTRY']['v']) for o in json.load(open(R + 'boc/FXCADTRY.json'))['observations'] if o.get('FXCADTRY')}
usd_cad = {o['d']: float(o['FXUSDCAD']['v']) for o in json.load(open(R + 'boc/FXUSDCAD.json'))['observations'] if o.get('FXUSDCAD')}
y26 = [v for d, v in try_cad.items() if d.startswith('2026')]
avg26 = sum(y26) / len(y26)
u26 = [v for d, v in usd_cad.items() if d.startswith('2026')]
uavg26 = sum(u26) / len(u26)
last = max(try_cad); ulast = max(usd_cad)
mw = {'net': 28075.50, 'gross': 33030.00}
out['min_wage'] = {k: {'TRY': v, 'CAD_at_2026_avg': round(v / avg26), 'USD_at_2026_avg': round(v / avg26 / uavg26),
                       'CAD_at_latest': round(v / try_cad[last]), 'USD_at_latest': round(v / try_cad[last] / usd_cad[ulast])} for k, v in mw.items()}
out['fx_used'] = {'TRY_per_CAD_2026_avg': round(avg26, 3), 'CAD_per_USD_2026_avg': round(uavg26, 4), 'latest_TRY_date': last,
                  'TRY_per_CAD_latest': try_cad[last], 'latest_USD_date': ulast, 'CAD_per_USD_latest': usd_cad[ulast]}
# consumption per person (World Bank, current USD) / population (IMF LP 2025)
wb = json.load(open(R + 'wb/NE.CON.PRVT.CD.json'))[1]
lp = json.load(open(R + 'imf/LP.json'))['values']['LP']
for c, iso in (('TR', 'TUR'), ('CA', 'CAN')):
    v = [x['value'] for x in wb if x['country']['id'] == c and x['date'] == '2025'][0]
    out[f'hh_consumption_2025_{iso}'] = {'usd_bn': round(v / 1e9, 1), 'per_person_usd': round(v / (lp[iso]['2025'] * 1e6))}
# IMF table
rows = []
for ind in ['NGDPD', 'NGDPDPC', 'PPPGDP', 'PPPPC', 'LP', 'NGDP_RPCH', 'PCPIPCH', 'BCA_NGDPD', 'BCA', 'LUR']:
    d = json.load(open(R + f'imf/{ind}.json'))['values'][ind]
    for c in ('TUR', 'CAN'):
        rows.append([ind, c] + [d[c].get(y) for y in ('2024', '2025', '2026')])
with open(O + 'imf_weo_oct2026_tur_can.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['indicator', 'country', '2024', '2025', '2026']); w.writerows(rows)
d = json.load(open(R + 'imf/NGDPDPC.json'))['values']['NGDPDPC']; p = json.load(open(R + 'imf/PPPPC.json'))['values']['PPPPC']
out['gdp_pc_ratio_can_over_tur_2025'] = {'nominal': round(d['CAN']['2025'] / d['TUR']['2025'], 2), 'ppp': round(p['CAN']['2025'] / p['TUR']['2025'], 2)}
# Eldorado share
out['eldorado_turkiye_share_2025_pct'] = round((168701 + 72482) / 488268 * 100, 1)
json.dump(out, open(O + 'derived.json', 'w'), indent=1, ensure_ascii=False)
print(json.dumps(out, indent=1, ensure_ascii=False))

# Cumulative price rise from monthly m/m changes (TCMB table, rounded to 2 dp, so approximate)
rows = list(csv.DictReader(open(O + 'tur_cpi_monthly_tcmb.csv')))
idx = 1.0
for r in rows:
    if '2018-01' <= r['month'] <= '2026-09':
        idx *= 1 + float(r['cpi_mom_pct']) / 100
out['cpi_cumulative_factor_dec2017_to_sep2026'] = round(idx, 1)
json.dump(out, open(O + 'derived.json', 'w'), indent=1, ensure_ascii=False)
print('cpi factor', round(idx, 1))
