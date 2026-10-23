import re,html,sys
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
t=re.sub(r'(?s)<script.*?</script>|<style.*?</style>|<nav.*?</nav>','',t)
t=re.sub(r'<(br|p|li|tr|h\d|div)[^>]*>','\n',t)
s=html.unescape(re.sub(r'<[^>]+>',' ',t))
s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
print(s)
