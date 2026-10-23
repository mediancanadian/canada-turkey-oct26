"""Fetch a TurkStat press release via the public veriportali API and dump plain text.
Usage: python3 -I tuik_press.py <id> <lang> <outdir>"""
import sys, json, re, html, urllib.request
pid, lang, out = sys.argv[1], sys.argv[2], sys.argv[3]
url = f"https://veriportali.tuik.gov.tr/api/{lang}/press/{pid}"
req = urllib.request.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*", "X-Requested-With": "XMLHttpRequest"})
d = json.load(urllib.request.urlopen(req, timeout=60))["data"]
json.dump(d, open(f"{out}/press_{pid}_{lang}.json", "w"), ensure_ascii=False)
c = re.sub(r'<img[^>]*>', '[IMG]', d.get("content") or "")
c = re.sub(r'</(td|th)>', ' | ', c); c = re.sub(r'</(tr|div|p|br)>|<br\s*/?>', '\n', c)
t = html.unescape(re.sub(r'<[^>]+>', '', c))
t = "\n".join(l.strip() for l in t.split("\n") if l.strip())
meta = {k: v for k, v in d.items() if k != "content"}
open(f"{out}/press_{pid}_{lang}.txt", "w").write(json.dumps(meta, ensure_ascii=False)[:3000] + "\n\n" + t)
print(d.get("title"), d.get("period"), d.get("date"))
