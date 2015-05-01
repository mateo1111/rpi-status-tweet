#!/usr/bin/env python
import sys
from twython import Twython
import os
from datetime import datetime

degree = unichr(176)


CONSUMER_KEY = '***'
CONSUMER_SECRET = '***'
ACCESS_KEY = '***'
ACCESS_SECRET = '***'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

#api.update_status(status=sys.argv[1])


czas = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


cmd = '/opt/vc/bin/vcgencmd measure_temp'  
line = os.popen(cmd).readline().strip()  
Temp = line.split('=')[1].split("'")[0]  


cmd = 'cat /proc/meminfo | grep MemTotal'
line = os.popen(cmd).readline().strip()
line2 = line.split(':     ')[1].split(" kB")[0]
memtotal=int(line2)
MemTotalMB = memtotal / 1024
MemTotalMB = str(MemTotalMB)

cmd = 'cat /proc/meminfo | grep MemFree'
line = os.popen(cmd).readline().strip()
line2 = line.split(':     ')[1].split(" kB")[0]
memfree=int(line2)
MemFreeMB = memfree / 1024
MemFreeMB = str(MemFreeMB)



api.update_status(status='('+czas+') RPi2: Running, CPU temp: '+Temp+' '+degree+'C, Free RAM: '+MemFreeMB+'MB/'+MemTotalMB+'MB')
