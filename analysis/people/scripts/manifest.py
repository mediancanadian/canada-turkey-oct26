import os,hashlib,json
O='../people/'
src={
 'raw/wds_98100356_ethnic_turkish.json':'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810035601 (via WDS getDataFromCubePidCoordAndLatestNPeriods)',
 'raw/wds_98100302_pob_turkey.json':'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810030201 (via WDS)',
 'raw/wds_98100181_mt_turkish.json':'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810018101 (via WDS)',
 'raw/wds_98100201_home_turkish.json':'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=9810020101 (via WDS)',
 'raw/wds_24100050_turkiye.json':'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2410005001 (via WDS)',
 'raw/wds_24100080_turkiye.json':'https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=2410008001 (via WDS)',
 'raw/ircc/EN_ODP-PR-Citz.xlsx':'https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP-PR-Citz.xlsx',
 'raw/ircc/ODP-PR-Citz.csv':'https://www.ircc.canada.ca/opendata-donneesouvertes/data/ODP-PR-Citz.csv',
 'raw/ircc/ODP-PR-Citz_immcat.csv':'https://www.ircc.canada.ca/opendata-donneesouvertes/data/ODP-PR-Citz_immcat.csv',
 'raw/ircc/study_citz_effective.xlsx':'https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP-TR-Study-IS_CITZ_sign_date.xlsx',
 'raw/ircc/study_citz_dec31.xlsx':'https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP_annual-TR-Study-IS_CITZ_year_end.xlsx',
 'raw/ircc/imp_citz_effective.xlsx':'https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP-TR-Work-IMP%20CITZ.xlsx',
 'raw/ircc/tfwp_citz_effective.xlsx':'https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP-TR-Work-TFWP%20CITZ.xlsx',
 'raw/ircc/imp_citz_dec31_all.xlsx':'https://www.ircc.canada.ca/opendata-donneesouvertes/data/en_odp_annual-tr-work-imp_citz_year_end_all_purpose.xlsx',
 'raw/ircc/tfwp_citz_dec31.xlsx':'https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP_annual-TR-work-TFW_CITZ_year_end.xlsx',
 'raw/ircc/asylum_top25_lastyear.xlsx':'https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP-Asylum-Top_25_CITZ_Office_Type_last_year.xlsx',
 'raw/ircc/asylum_top25_lastmonth.xlsx':'https://www.ircc.canada.ca/opendata-donneesouvertes/data/EN_ODP-Asylum-Top_25_CITZ_Office_Type_last_month.xlsx',
 'raw/ircc/trv_v1_approved.xlsx':'https://www.ircc.canada.ca/opendata-donneesouvertes/data/Open%20Data%20-%20OPS%20TRV%20V-1%20Approved%20en.xlsx',
 'raw/ircc/new_citizens_cob.xlsx':'https://www.ircc.canada.ca/opendata-donneesouvertes/data/Open%20Data%20-%20New%20Citizens%20by%20COB%20en.xlsx',
}
for y,eid in [('2016','53123,sinir-istatistikleri-2016xlsx.xlsx'),('2017','67753,59424sinir-istatistikleri-2017xlsx-2xlsx.xlsx'),('2018','63274,sinir-istatistikleri-2018xlsx.xlsx'),('2019','72101,sinir-istatistikleri-2019xlsxxlsx.xlsx'),('2020','81888,30032020yilliksinirbulteni-xlsx-1xlsx.xlsx'),('2021','93664,2021yilliksinirbultenixlsx.xlsx'),('2022','111370,2022yilliksinirbultenixlsx.xlsx'),('2023','122231,2023yilliksinirbultenixlsx.xlsx'),('2024','131301,2024yilliksinirbultenixlsxxlsx.xlsx'),('2025','145395,2025yilliksinirbultenixlsx.xlsx')]:
    src[f'raw/turkiye/sinir_{y}.xlsx']=f'https://yigm.ktb.gov.tr/Eklenti/{eid}?0'
src['raw/turkiye/sinir_2026aug.xls']='https://yigm.ktb.gov.tr/Eklenti/151440,ag-stos-2026-bultenixls.xls?0'
for y in range(2015,2027): src[f'raw/irb/rpd_{y}.html']=f'https://www.irb-cisr.gc.ca/en/statistics/protection/Pages/RPDStat{y}.aspx'
files=[]
for root,_,fs in os.walk(O):
    for f in sorted(fs):
        p=os.path.join(root,f); rel=os.path.relpath(p,O)
        if rel=='manifest.json': continue
        files.append({'path':rel,'bytes':os.path.getsize(p),'sha256':hashlib.sha256(open(p,'rb').read()).hexdigest(),'source_url':src.get(rel),'accessed':'2026-10-23'})
web=[
 {'what':'Entry requirements by country (Türkiye visa-required)','url':'https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada/entry-requirements-country.html','page_modified':'2026-07-31'},
 {'what':'PM statement Carney-Erdogan, Oct 22 2026','url':'https://www.pm.gc.ca/en/news/statements/2026/10/22/statement-prime-minister-carney-and-president-recep-tayyip-erdogan'},
 {'what':'CTA agreement page Turkey','url':'https://otc-cta.gc.ca/eng/transport-agreement/turkey'},
 {'what':'CTA Determination A-2024-140','url':'https://otc-cta.gc.ca/eng/ruling/a-2024-140'},
 {'what':'Transport Canada release Dec 15 2023','url':'https://www.canada.ca/en/transport-canada/news/2023/12/canadians-to-benefit-from-expanded-air-transport-agreements-with-ethiopia-jordan-and-turkiye.html'},
 {'what':'2009 agreement release','url':'https://www.canada.ca/en/news/archive/2009/03/canada-turkey-successfully-conclude-air-transport-agreement.html'},
 {'what':'Air Transat release YUL-IST','url':'https://www.transat.com/en-CA/corporate/media/news-releases/124611'},
 {'what':'LEAD ONLY haber.aero citing SHGM 12->21','url':'https://haber.aero/en/Aero-Agenda/Frequency-increase-on-the-Turkey-Canada-route./'},
 {'what':'LEAD ONLY Travelweek TK frequencies','url':'https://www.travelweek.ca/?p=192957'},
 {'what':'LEAD ONLY AeroRoutes TK NW26','url':'https://www.aeroroutes.com/eng/260701-tknw26ca'},
 {'what':'LEAD ONLY ch-aviation CTA rejection 2025','url':'https://www.ch-aviation.com/news/151000-canada-rejects-turkish-airlines-request-for-more-summer-ops'},
 {'what':'Air Canada-Pegasus interline release (GlobeNewswire via barchart)','url':'https://www.barchart.com/story/news/305120/air-canada-expands-travel-options-to-turkiye-through-new-partnership-with-pegasus-airlines'},
]
json.dump({'thread':'people and travel links, Canada-Türkiye','created':'2026-10-23','files':files,'web_sources_via_webfetch':web,'blocked':['https://www.turkishairlines.com/en-ca/press-room/ (permission not granted)','thecanadianpressnews.ca article (client error)']},open(O+'manifest.json','w'),indent=1,ensure_ascii=False)
print(len(files))
