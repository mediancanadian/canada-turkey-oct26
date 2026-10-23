"""Bank of Canada TRY/CAD: annual series 2015-2026 and 5- and 10-year lira loss vs CAD.
Inputs (raw/boc): FXCADTRY.json (daily avg, TRY per CAD, 2017-), FXATRYCAD.json (annual avg CAD per TRY, 2017-2025),
legacy_annual.json (IEXA5802 annual avg CAD per TRY, to 2016), legacy_noon_2015_2016.json (IEXE5802 noon CAD per TRY)."""
import json, csv, sys
base = sys.argv[1]
B = base + '/raw/boc/'
daily = {o['d']: float(o['FXCADTRY']['v']) for o in json.load(open(B + 'FXCADTRY.json'))['observations'] if o.get('FXCADTRY')}
noon = {o['d']: 1 / float(o['IEXE5802']['v']) for o in json.load(open(B + 'legacy_noon_2015_2016.json'))['observations'] if o.get('IEXE5802')}
ann = {}
for o in json.load(open(B + 'legacy_annual.json'))['observations']:
    if o.get('IEXA5802') and o['d'][:4] in ('2015', '2016'):
        ann[o['d'][:4]] = (1 / float(o['IEXA5802']['v']), 'BoC legacy annual avg (noon basis), IEXA5802')
for o in json.load(open(B + 'FXATRYCAD.json'))['observations']:
    ann[o['d'][:4]] = (1 / float(o['FXATRYCAD']['v']), 'BoC annual avg FXATRYCAD')
y26 = [v for d, v in daily.items() if d.startswith('2026')]
ann['2026 YTD (to Oct 22)'] = (sum(y26) / len(y26), 'mean of BoC daily FXCADTRY 2026-01-02 to 2026-10-22')

def near(series, date):
    ks = sorted(k for k in series if k <= date)
    return ks[-1], series[ks[-1]]

latest_d, latest = max(daily.items())
out = []
for label, src, date in [('5 years', daily, '2021-10-22'), ('10 years', noon, '2016-10-21'), ('1 year', daily, '2025-10-22')]:
    d0, v0 = near(src, date)
    loss = 1 - v0 / latest  # value of 1 lira in CAD fell by this share
    out.append((label, d0, round(v0, 4), latest_d, latest, round(loss * 100, 1), round(latest / v0, 2)))
with open(base + '/outputs/fx_try_per_cad_annual.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['year', 'TRY_per_CAD', 'source'])
    for k in sorted(ann): w.writerow([k, round(ann[k][0], 3), ann[k][1]])
with open(base + '/outputs/fx_lira_loss.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['horizon', 'start_date', 'TRY_per_CAD_start', 'end_date', 'TRY_per_CAD_end', 'lira_value_lost_pct', 'CAD_buys_x_times_more_lira'])
    w.writerows(out)
for k in sorted(ann): print(k, round(ann[k][0], 3))
for r in out: print(r)
