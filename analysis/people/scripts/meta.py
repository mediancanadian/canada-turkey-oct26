import json,sys
d=json.load(open(sys.argv[1]))[0]['object']
print(d['productId'],d['cubeTitleEn'])
for dim in d['dimension']:
    ms=dim['member']
    print(' DIM',dim['dimensionPositionId'],dim['dimensionNameEn'],len(ms))
    for m in ms[:6]: print('    ',m['memberId'],m['memberNameEn'])
    for m in ms:
        n=m['memberNameEn'].lower()
        if any(k in n for k in ['turk','total','toronto','montr','vancouver','ottawa','calgary','edmonton']) and m not in ms[:6]: print('    *',m['memberId'],m['memberNameEn'])
