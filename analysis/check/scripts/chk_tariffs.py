"""Recompute duty estimates and duty-free shares from tariffs outputs."""
import csv, collections
O='../tariffs/outputs/'
ca=list(csv.DictReader(open(O+'ca_imports_from_TR_2025_est_mfn_duty.csv')))
v=sum(float(r['value_cad']) for r in ca); d=sum(float(r['est_duty_cad'] or 0) for r in ca)
free=sum(float(r['value_cad']) for r in ca if r['mfn_rate'].strip().lower()=='free')
print('CA imports value %.1fM duty %.1fM rate %.2f%% free share %.1f%%'%(v/1e6,d/1e6,100*d/v,100*free/v))
dut=v-free; print('dutiable %.1fM, duty on dutiable %.1f%%'%(dut/1e6,100*d/dut))
ch=collections.defaultdict(float)
for r in ca: ch[r['hs10'][:2]]+=float(r['est_duty_cad'] or 0)
print('clothing 61+62 %.1fM carpets 57 %.1fM share %.1f%%'%((ch['61']+ch['62'])/1e6,ch['57']/1e6,100*(ch['61']+ch['62']+ch['57'])/d))
print('flags',collections.Counter(r['flag'] for r in ca))
tr=list(csv.DictReader(open(O+'ca_exports_to_TR_2025_est_tr_duty.csv')))
v=sum(float(r['value_cad']) for r in tr); d=sum(float(r['est_duty_cad'] or 0) for r in tr)
z=sum(float(r['value_cad']) for r in tr if r['total_pct'] not in ('',) and float(r['total_pct'])==0)
nr=sum(float(r['value_cad']) for r in tr if r['total_pct']=='')
print('TR on CA exports value %.1fM duty %.1fM rate %.2f%% zero share %.1f%% no-rate %.1fM'%(v/1e6,d/1e6,100*d/v,100*z/v,nr/1e6))
dur=sum(float(r['est_duty_cad'] or 0) for r in tr if r['hs8'].startswith('100119'))
print('durum duty %.1fM ex-durum %.1fM %.1f%%'%(dur/1e6,(d-dur)/1e6,100*(d-dur)/v))
len_=sum(float(r['est_duty_cad'] or 0) for r in tr if r['hs8'].startswith('071340'));chk=sum(float(r['est_duty_cad'] or 0) for r in tr if r['hs8'].startswith('071320'))
print('lentil duty %.1fM chickpea %.1fM'%(len_/1e6,chk/1e6))
igv=sum(float(r['value_cad'])*float(r['tr_igv_pct'] or 0)/100 for r in tr); print('IGV part %.1fM'%(igv/1e6))
for r in tr:
    if r['hs8'][:4] in ('0713','1001','8802'): print(r['hs8'],r['value_cad'],r['tr_gv_pct'],r['tr_igv_pct'],r['note'][:60])
# Values per line from raw check
print('dom exp total from hs8 file', sum(float(r['val']) for r in csv.DictReader(open(O+'domexports_to_TR_2025_hs8.csv')))/1e6)
print('imp total from hs10 file', sum(float(r['val']) for r in csv.DictReader(open(O+'imports_from_TR_2025_hs10.csv')))/1e6)
for f in ['tr_imports_2025_in_sima_listed_lines.csv','tr_imports_2025_in_steel_trq_classes.csv']:
    rs=list(csv.DictReader(open(O+f))); print(f, round(sum(float(r['val']) for r in rs)/1e6,1), [(r[list(r)[0]],round(float(r['val'])/1e6,1)) for r in rs][:6])
