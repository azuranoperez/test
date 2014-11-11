
# This script converts the file cities (json) into a csv file 
#{"id":"1","country_id":"250","region_id":"388","name":"Abancourt","iso_code":"aco"}

from collections import OrderedDict
import json

f = open('cities','r')
g = open('cities.csv','wa')

for i in f:
    a = json.loads(i, object_pairs_hook=OrderedDict)
    print a
    if len(a.keys()) == 5:
       s=''
       for item in a.values():
           item=item.encode('utf-8')
           s=s+item+','
       s=s[:-1]+'\n'
       g.write(s)

g.close()
