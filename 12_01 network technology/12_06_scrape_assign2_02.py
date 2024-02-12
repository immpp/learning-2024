import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

eurl = input('Enter URL ')
count = int(input('Enter Count: '))
position = int(input('Enter Position: ')) - 1
#eurl = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

print('Retrieving...', eurl)
uname = []

while count > 0:
    html = urllib.request.urlopen(eurl).read()
    soup = BeautifulSoup(html, 'html.parser')
    lname = []
    lurl = []
    tags = soup('a')
    for tag in tags:
        url = tag.get('href', None)
        lurl.append(url)
        names = re.findall('by_([a-zA-Z]+).', url)
        for name in names:
            lname.append(name)
    print('Retrieving...', lurl[position])
    eurl = lurl[position]
    uname.append(lname[position])
    count = count - 1

print(uname[-1])

