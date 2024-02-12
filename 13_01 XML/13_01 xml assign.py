import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

sassign = 'http://py4e-data.dr-chuck.net/comments_42.xml'
assign = 'http://py4e-data.dr-chuck.net/comments_1972784.xml'
fhand = urllib.request.urlopen(assign).read()
tsum = 0

tree = ET.fromstring(fhand)
tlist = tree.findall('comments/comment')

for line in tlist:
    tint = int(line.find('count').text)
    tsum = tsum + tint

print(tsum)