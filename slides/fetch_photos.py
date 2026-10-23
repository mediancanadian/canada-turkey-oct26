import json, re, subprocess, urllib.parse, sys
P = {p['slot']+'-'+p['letter']: p for p in json.load(open('../analysis/photos/photos.json'))}
PICK = {1:'01-cover-a',2:'02-trade-c',3:'06-tariffs-a',4:'04-imports-c',5:'03-lentils-c',6:'05-prairies-a',7:'07-energy-a',8:'09-trust-a',9:'08-flights-b'}
out = {}
for n, k in PICK.items():
    p = P[k]; u = p['original_url'].split('?')[0]
    m = re.match(r'https://upload.wikimedia.org/wikipedia/commons/(\w)/(\w\w)/(.+)$', u)
    w = p["width"]
    url = u if w == p['width'] else f"https://upload.wikimedia.org/wikipedia/commons/thumb/{m[1]}/{m[2]}/{m[3]}/{w}px-{m[3]}"
    f = f'photos/s{n}.jpg'
    r = subprocess.run(['curl','-sSfL','-A','TheMedianCanadianSlides/1.0 (https://github.com/sjvadrevu/the-median-canadian) curl','-o',f,url],capture_output=True,text=True)
    import time; time.sleep(8)
    print(n, k, r.returncode, r.stderr[:120])
    out[n] = dict(key=k, file=f, url=url, page=p['file_page'], author=p['author'], licence=p['licence'], licence_url=p['licence_url'], credit=p['credit_line'])
json.dump(out, open('photos_used.json','w'), indent=1)
