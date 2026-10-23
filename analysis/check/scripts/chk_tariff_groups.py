"""Recompute 1b product-group values and duty from tariffs output CSV."""
import csv
ca=list(csv.DictReader(open('../tariffs/outputs/ca_imports_from_TR_2025_est_mfn_duty.csv')))
G={'pharma':('3002','3004'),'clothing':('61','62'),'ch73':('73',),'ch72':('72',),'ch76':('76',),'8708':('8708',),
   'nuts':('0802','0804','0806','0813'),'carpets':('5701','5702','5703','5704','5705'),'ch89':('89',),'8411':('8411',),
   '7113':('7113',),'4411':('4411',),'8418':('8418',),'1806':('1806',),'6907':('6907',),'2523':('2523',),'1902':('1902',),'ch63':('63',),'8450':('8450',)}
for g,p in G.items():
    rs=[r for r in ca if r['hs10'].startswith(p)]
    v=sum(float(r['value_cad']) for r in rs); f=sum(float(r['value_cad']) for r in rs if r['mfn_rate'].strip().lower()=='free'); d=sum(float(r['est_duty_cad'] or 0) for r in rs)
    print('%-9s value %.1fM free %.0f%% duty %.2fM'%(g,v/1e6,100*f/v if v else 0,d/1e6))
print('dairy 0404+0406 %.2fM'%(sum(float(r['value_cad']) for r in ca if r['hs10'].startswith(('0404','0406')))/1e6))
print('tugs 890400 %.2fM'%(sum(float(r['value_cad']) for r in ca if r['hs10'].startswith('8904'))/1e6))
