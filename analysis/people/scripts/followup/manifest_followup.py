import os,hashlib,json
O='../people/'
C='https://otc-cta.gc.ca/eng/'; I='https://www.ircc.canada.ca/opendata-donneesouvertes/data/'
src={'raw/followup/a-2024-45.html':C+'ruling/a-2024-45','raw/followup/a-2025-25.html':C+'ruling/a-2025-25','raw/followup/a-2025-77.html':C+'ruling/a-2025-77','raw/followup/a-2025-81.html':C+'ruling/a-2025-81','raw/followup/a-2026-59.html':C+'ruling/a-2026-59','raw/followup/decision-33-a-2025.html':C+'ruling/decision-33-a-2025','raw/followup/cta_agreement_turkey.html':C+'transport-agreement/turkey','raw/followup/dd_list.html':C+'decisions-determinations',
'raw/followup/pmo_release_2026-10-23.html':'https://www.pm.gc.ca/en/news/news-releases/2026/10/23/prime-minister-carneys-historic-visit-turkiye-launches-new-strategic','raw/followup/pmo_remarks_2026-10-22.html':'https://www.pm.gc.ca/en/news/speeches/2026/10/22/prime-minister-carney-delivers-remarks-alongside-president-turkiye-recep','raw/followup/oic_2026-0976.html':'https://orders-in-council.canada.ca/results.php?pcNumber=2026-0976&lang=en','raw/followup/oic_post.html':'https://orders-in-council.canada.ca/results.php?lang=en (POST pcNumber=2026-0976; no rows returned)',
'raw/followup/ircc/imp_citz_dec31_workonly.xlsx':I+'en_odp_annual-tr-work-imp_citz_year_end.xlsx','raw/followup/ircc/hc_citz_effective.xlsx':I+'EN_ODP-TR-Work-HC_citizenship_sign.xlsx','raw/followup/ircc/hc_citz.csv':I+'ODP-TR-Work-HC_citizenship.csv','raw/followup/ircc/imp_citz.csv':I+'ODP-TR-Work-IMP-CITZ.csv','raw/followup/ircc/imp_pt_program_effective.xlsx':I+'EN_ODP-TR-Work-IMP_PT_program_sign.xlsx'}
for f in os.listdir(O+'raw/followup'):
    if f.startswith('dd_'): src.setdefault('raw/followup/'+f, C+'decisions-determinations (search: '+f+')')
files=[]
for root,_,fs in os.walk(O):
    for f in sorted(fs):
        p=os.path.join(root,f); rel=os.path.relpath(p,O)
        if not (rel.startswith(('raw/followup','scripts/followup')) or rel in ('results-followup.md','outputs/work_permit_split_turkey.json')): continue
        files.append({'path':rel,'bytes':os.path.getsize(p),'sha256':hashlib.sha256(open(p,'rb').read()).hexdigest(),'source_url':src.get(rel),'accessed':'2026-10-23'})
web=[
 {'what':'GAC media advisory, Minister Sidhu announcement on Canada-Türkiye ATA (issued 2026-08-14)','url':'https://www.canada.ca/en/global-affairs/news/2026/08/minister-sidhu-to-make-announcement-related-to-canadaturkiye-air-transport-agreement.html','via':'WebFetch'},
 {'what':'IRCC earthquake public policy (signed 2023-03-15)','url':'https://www.canada.ca/en/immigration-refugees-citizenship/corporate/mandate/policies-operational-instructions-agreements/public-policies/turkiye-syria-earthquake-2023.html','via':'WebFetch'},
 {'what':'IRCC earthquake public policy extension (signed 2023-09-28, expired 2024-01-03)','url':'https://www.canada.ca/en/immigration-refugees-citizenship/corporate/mandate/policies-operational-instructions-agreements/public-policies/turkiye-syria-earthquake-2023-extension.html','via':'WebFetch'},
 {'what':'IRCC earthquake measures program instructions','url':'https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/operational-bulletins-manuals/service-delivery/earthquake-turkiye-syria.html','via':'WebFetch'},
 {'what':'IRCC program delivery update, measures expired 2024-01-03','url':'https://www.canada.ca/en/immigration-refugees-citizenship/corporate/publications-manuals/operational-bulletins-manuals/updates/2024-earthquakes-turkiye-syria.html','via':'WebFetch'},
 {'what':'@CanadaTrade X post 12 to 21 (official account, social media)','url':'https://x.com/CanadaTrade/status/2089369612831887653','via':'search snippet only'},
 {'what':'LEAD ONLY Bloomberg Tax: OIC 2026-0976 dated 2026-10-09 authorizing signing','url':'https://news.bloombergtax.com/daily-tax-report-state/canada-issues-order-authorizing-signing-of-air-transport-agreement-with-turkey','via':'WebFetch'},
 {'what':'LEAD ONLY Turkville 2026-05-10, 12 to 21, unlimited cargo, fifth freedom','url':'https://turkville.ca/en/news/canada-turkey-aviation-agreement-revised-thy-flights-increasing-from-12-to-21','via':'WebFetch'},
 {'what':'LEAD ONLY Airlinehaber 2026-05-12 SHGM MoU','url':'https://www.airlinehaber.com/turkiye-ile-kanada-arasinda-sivil-havacilikta-yeni-donem-ucus-haklari-artirildi/','via':'WebFetch'},
 {'what':'LEAD ONLY CAPA 2026-05-13 Canada and Türkiye revise ATA (paywalled)','url':'https://centreforaviation.com/news/canada-and-turkiye-revise-air-transport-agreement-1359029','via':'WebFetch'},
 {'what':'LEAD ONLY Aviation A2Z 2026-05-16 TK Montréal 3 to 4 weekly from Jul 7 2026','url':'https://aviationa2z.com/index.php/2026/05/16/turkish-airlines-adds-more-flights-to-canada/','via':'WebFetch'},
 {'what':'LEAD ONLY Travel Extra 2025-03-05 (misstates objectors)','url':'https://www.travelextra.ie/canada-denies-turkish-airlines-request-for-five-additional-weekly-flights-between-turkiye-and-canada/','via':'WebFetch'},
 {'what':'LEAD ONLY aviation.direct 2025-03-05 (misstates objectors)','url':'https://aviation.direct/en/kanadische-behoerde-lehnt-mehr-turkish-airlines-fluege-ab','via':'WebFetch'},
]
blocked=['https://www.turkishairlines.com/en-ca/press-room/ (timeouts)','https://web.shgm.gov.tr/tr/haberler (timeouts)','https://portail-portal.otc-cta.gc.ca/en/wet-lease-applications/544908 (robots_disallowed; curl reset)','https://simpleflying.com/canada-rejects-this-long-haul-airlines-growth-plan-to-the-country/ (robots_disallowed)','orders-in-council.canada.ca search for 2026-0976 (no rows returned)']
json.dump({'thread':'follow-up: CTA rulings, new ATA, work permit split, Canada-Türkiye','created':'2026-10-23','files':files,'web_sources':web,'blocked':blocked},open(O+'manifest-followup.json','w'),indent=1,ensure_ascii=False)
print(len(files))
