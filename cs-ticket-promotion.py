# -*- coding:utf-8 -*-

import os
import requests
import json
import re

from flights import City, Region, Ticket, Airport

#from bs4 import BeautifulSoup

'''
url = 'http://www.csair.com/cn/favourable/discount_tickets_domestic/'
#url = 'http://www.csair.com/cn/index.shtml'

headers = {
    'Host': 'www.csair.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}

s = requests.Session()
s.headers.update(headers)
r = s.get(url)

# hack can't display Chinese charset issue
r.encoding = 'utf-8'

#print(r.text)

url = 'http://eunion.csair.com/E-UNION/data/avprice/getMinPrice.json?inter=N&jsoncallback=jQuery110208238446780323457_1464505830327&_=1464505830328'

r = s.get(url)
r.encoding = 'utf-8'

#print(r.text)

datafile = 'flights.txt'
if not os.path.isfile(datafile):
    with open(datafile, 'w') as fwrite:
        fwrite.write(r.text)

'''

datafile = 'flights.txt'
if os.path.isfile(datafile):
    with open(datafile, 'r') as fread:
        data = fread.read()

#print(data.strip())

pat = re.compile('\((.*?)\)')
res = pat.search(data)
if res:
    flights = res.group(1)
    j = json.loads(flights)
    #print(j['FROMOFLIGHTS'])
    x = j['FROMOFLIGHTS']
    for y in x:
        airport = Airport(**y)