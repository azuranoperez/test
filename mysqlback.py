
# This script can be used to produce a dump of our DB if we want to upload it

import os
import time

user = 'root'
password = ''
db = 'im'
host='localhost'

os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s | gzip -c > %s.gz" % (user,password,host,db,db+"dump"))

