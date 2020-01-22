import urllib.request as req
import re
import json

with open("coupon.json", 'w') as f:
    f.write('{\n')
    f.write('    "couponList":[\n')
    for i in range(1, 20):
        rq = req.Request(f"https://udemycoupon.learnviral.com/coupon-category/free100-discount/page/{i}/", headers={'User-Agent': 'Mozilla/5.0'})
        r = req.urlopen(rq).read().decode('ISO-8859-1')
        items = re.findall(r'href="(https://www.(udemy).com/course/.+)/\?couponCode=([^"]*)', r)
        for item in items:
            f.write('        ')
            f.write( json.dumps({'siteName':item[1],'siteURI':item[0], 'couponCode':item[2]}) )
            f.write(',\n')
    f.write('    ]\n')
    f.write('}\n')
