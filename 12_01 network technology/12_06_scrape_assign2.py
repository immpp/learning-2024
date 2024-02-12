import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Fikret.html').read()
soup = BeautifulSoup(html, 'html.parser')

#input()
lname = []
lurl = []
dname = dict()
sum = 0

tags = soup('a')
for tag in tags:
    url = tag.get('href', None)
    lurl.append(url)
    names = re.findall('by_([a-zA-Z]+).', url)
    print(url)
    for name in names:
        #dname[name] = url
        lname.append(name)
#print('Retrieving...',lurl[3])
#print(dname[3])
#print(lname[3])
