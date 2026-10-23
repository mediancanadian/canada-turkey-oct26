"""Post a search to Canada Treaty Information (treaty-accord.gc.ca). Usage: treaty_search.py <form.html> <text> <subjectValue|''> <out.html>"""
import sys, re, urllib.request, urllib.parse, http.cookiejar, html
form, text, subj, out = sys.argv[1:5]
s = open(form, encoding='utf-8', errors='ignore').read()
fields = {}
for n, v in re.findall(r'<input type="hidden" name="([^"]+)" id="[^"]*" value="([^"]*)"', s): fields[n] = html.unescape(v)
fields["ctl00$MainContent$txtSearchIndex"] = text
fields["ctl00$MainContent$ddlSubjects"] = subj
fields["ctl00$MainContent$ddlKeywords"] = ""
fields["ctl00$MainContent$btnSearchResults"] = "Search"
cj = http.cookiejar.CookieJar(); op = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
ua = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
r = op.open(urllib.request.Request("https://www.treaty-accord.gc.ca/search-recherche.aspx?lang=eng", data=urllib.parse.urlencode(fields).encode(), headers=ua), timeout=60)
b = r.read().decode('utf-8', 'ignore'); open(out, 'w').write(b); print(r.geturl(), len(b))
