"""Türkiye goods imports 2025 (and 2024) by partner and HS chapter, from UN Comtrade (reporter 792 = Türkiye, customs data reported by TurkStat).
Usage: python3 -I imports.py <base>"""
import json, csv, sys
base = sys.argv[1]
C = base + '/raw/comtrade/'
names = {p['id']: p['text'] for p in json.load(open(C + 'partners_ref.json'))['results']}
res = {}
for yr in ('2024', '2025'):
    rows = json.load(open(C + f'tur_imports_{yr}_partners.json'))['data']
    tot = [r for r in rows if r['partnerCode'] == 0][0]['primaryValue']
    ps = sorted([r for r in rows if r['partnerCode'] != 0], key=lambda r: -r['primaryValue'])
    # exclude non-country codes (areas nes, bunkers, free zones) only for ranking display
    rank = []
    for r in ps:
        rank.append((names.get(r['partnerCode'], r['partnerCode']), r['partnerCode'], r['primaryValue']))
    res[yr] = (tot, rank)
    with open(base + f'/outputs/tur_imports_{yr}_by_partner.csv', 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['rank', 'partner', 'code', 'usd', 'share_pct'])
        for i, (n, c, v) in enumerate(rank, 1): w.writerow([i, n, c, round(v), round(v / tot * 100, 2)])
    print(yr, 'TOTAL USD bn', round(tot / 1e9, 1))
    for i, (n, c, v) in enumerate(rank[:15], 1): print(' ', i, n, round(v / 1e9, 2), round(v / tot * 100, 1))
    for code in (124, 842, 826, 36):
        for i, (n, c, v) in enumerate(rank, 1):
            if c == code: print('  >>', i, n, round(v / 1e9, 3), round(v / tot * 100, 2))
for f, lab in (('tur_imports_2025_hs2.json', 'world'), ('tur_imports_2025_from_can_hs2.json', 'canada')):
    rows = [r for r in json.load(open(C + f))['data'] if r['cmdCode'] != 'TOTAL']
    tot = sum(r['primaryValue'] for r in rows)
    rows.sort(key=lambda r: -r['primaryValue'])
    with open(base + f'/outputs/tur_imports_2025_hs2_{lab}.csv', 'w', newline='') as fo:
        w = csv.writer(fo); w.writerow(['hs2', 'usd', 'share_pct'])
        for r in rows: w.writerow([r['cmdCode'], round(r['primaryValue']), round(r['primaryValue'] / tot * 100, 2)])
    print(lab, 'sum HS2 USD bn', round(tot / 1e9, 2))
    for r in rows[:10]: print('  HS', r['cmdCode'], round(r['primaryValue'] / 1e9, 3), round(r['primaryValue'] / tot * 100, 1))
