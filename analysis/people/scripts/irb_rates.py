import json
O='../people/'
d=json.load(open(O+'outputs/irb_turkiye.json'))
f=lambda s: float(str(s).replace('​','').replace(',',''))
out={}
for y,v in d.items():
    r=[x for x in v['row'] if ('Turkey' in x[0] or 'Türkiye' in x[0])][0]; t=v['total'][0]
    out[y]={'referred':f(r[1]),'accepted':f(r[2]),'rejected':f(r[3]),'finalized':f(r[6]),'pending_end':f(r[7]),'acc_pct_of_finalized':round(100*f(r[2])/f(r[6]),1),'all_countries_acc_pct':round(100*f(t[2])/f(t[6]),1),'all_referred':f(t[1])}
    print(y,out[y])
json.dump(out,open(O+'outputs/irb_turkiye_rates.json','w'),indent=1)
