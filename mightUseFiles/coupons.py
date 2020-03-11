import requests
import re
import json

with open("coupon.json", 'w') as f:
    f.write('{\n')
    f.write('    "couponList":[\n')
    for i in range(1, 2):
        rq = requests.get(f"https://udemycoupon.learnviral.com/coupon-category/free100-discount/page/{i}/", headers={'User-Agent': 'Mozilla/5.0'})
        items = re.findall(r'href="(https://www.(udemy).com/course/.+)/\?couponCode=([^"]*)"', rq.text)
        for item in items:
            f.write('        ')
            f.write( json.dumps({'siteName':item[1],'siteURI':item[0], 'couponCode':item[2]}) )
            f.write(',\n')
    f.write('    ]\n')
    f.write('}\n')
