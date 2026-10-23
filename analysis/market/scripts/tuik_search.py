"""Search TurkStat veriportali press releases. Usage: tuik_search.py <lang> <text...>"""
import sys, json, urllib.request
lang=sys.argv[1]; text=" ".join(sys.argv[2:])
body=json.dumps({"text":text,"page":1,"typeIds":[],"categoryIds":[],"subCategoryIds":[],"years":[],"levels":[],"archive":True,"autoFilter":False}).encode()
req=urllib.request.Request(f"https://veriportali.tuik.gov.tr/api/{lang}/data/search",data=body,headers={
 "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
 "Accept":"application/json","Content-Type":"application/json","X-Requested-With":"XMLHttpRequest"})
d=json.load(urllib.request.urlopen(req,timeout=60))
s=json.dumps(d,ensure_ascii=False)
data=d.get("data")
items = data.get("items") or data.get("results") or data if isinstance(data,dict) else data
if isinstance(data,dict): print(list(data.keys()))
def walk(x):
    if isinstance(x,dict):
        if "title" in x or "name" in x: print({k:x.get(k) for k in ("id","title","name","period","date","url","type") if k in x})
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(data)
