import re,html,sys
t=open(sys.argv[1],encoding='utf8',errors='ignore').read()
t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
a=sys.argv[2] if len(sys.argv)>2 else None
if a:
  i=t.find(a); print(t[max(0,i-100):i+int(sys.argv[3]) if len(sys.argv)>3 else i+4000])
else: print(t)
