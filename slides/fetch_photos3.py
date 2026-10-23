import json, re, subprocess, time
P = {p['slot']+'-'+p['letter']: p for p in json.load(open('../analysis/photos/photos.json'))}
PICK = {'1':'10-market-b','1b':'01-cover-c','2':'02-trade-a','3':'02-trade-c','4':'03-lentils-c','5':'05-prairies-a',
        '6':'08-flights-b','7':'07-energy-a','8':'09-trust-a','9':'12-next-b'}
UA = 'TheMedianCanadianSlides/1.0 (https://github.com/sjvadrevu/the-median-canadian)'
out = {}
for n, k in PICK.items():
    p = P[k]; u = p['original_url'].split('?')[0]
    m = re.match(r'https://upload.wikimedia.org/wikipedia/commons/(\w)/(\w\w)/(.+)$', u)
    w = p['width']
    if w <= 3840:
        url = u
    else:
        url = f"https://upload.wikimedia.org/wikipedia/commons/thumb/{m[1]}/{m[2]}/{m[3]}/3840px-{m[3]}"
    f = f'photos/s{n}.jpg'
    r = subprocess.run(['curl','-sSfL','-A',UA,'-o',f,url],capture_output=True,text=True)
    print(n, k, r.returncode, r.stderr[:100]); time.sleep(3)
    out[n] = dict(key=k, url=url, page=p['file_page'], author=p['author'], licence=p['licence'], licence_url=p['licence_url'], credit=p['credit_line'],
                  description=p['description'], file_in_use=('full size' if r.returncode == 0 else 'FAILED'))
json.dump(out, open('photos_used.json','w'), indent=1, ensure_ascii=False)
