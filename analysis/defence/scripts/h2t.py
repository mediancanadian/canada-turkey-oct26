import re,sys,html
for f in sys.argv[1:]:
    t=open(f,encoding='utf-8',errors='ignore').read()
    t=re.sub(r'(?s)<script.*?</script>|<style.*?</style>','',t)
    t=re.sub(r'(?i)<(p|li|h\d|br|tr|div)[^>]*>','\n',t)
    t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(f+'.txt','w').write(t)
