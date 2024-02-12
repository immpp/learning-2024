#<span class="comments">97</span>
import re

x = '<span class="comments">97</span>'

y = re.findall('[0-9]+', x)

print(y)