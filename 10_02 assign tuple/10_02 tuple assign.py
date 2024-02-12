#Write a program to read through the mbox-short.txt and figure out the distribution
# by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time
# and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

file = open('mbox-short.txt')
lfile = []
dtime = dict()

for line in file:
    if 'From ' in line:
        sline = line.split()
        stime = sline[5].split(':')
        lfile.append(stime[0])

for hour in lfile:
    dtime[hour] = dtime.get(hour, 0) + 1

hlist = []
for k,v in dtime.items():
    tup = (k, v)
    hlist.append(tup)

hlist = sorted(hlist)

for k,v in hlist:
    print(k,v)

