import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1972782.html').read()
soup = BeautifulSoup(html, 'html.parser')

lnum = []
sum = 0

tags = soup('span')
for tag in tags:
    stag = str(tag)
    num = re.findall('[0-9]+', stag)
    for itag in num:
        lnum.append(itag)

for val in lnum:
    fval = int(val)
    sum = sum + fval

print(sum)
