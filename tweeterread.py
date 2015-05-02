#!/usr/bin/env python
import time
time.sleep(120)
import sys
from twython import Twython
import os
from datetime import datetime

import csv





degree = unichr(176)



PATH1='/var/www/rpi1.csv'
PATH2='/var/www/rpi2.csv'

CONSUMER_KEY = '***'
CONSUMER_SECRET = '***'
ACCESS_KEY = '***'
ACCESS_SECRET = '***'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

czas = datetime.now().strftime('%Y-%m-%d %H')




output = api.get_user_timeline(screen_name="NaScotchMe", count="2")


textlist=[]
when=[]


for text in output:
    textlist.append(text['text'])

textA=textlist[0]
textB=textlist[1]


textA1 = textA.split('(')[1].split(":")[0]
textA2 = textA.split(') ')[1].split(": Running")[0]
textA3 = textA.split('temp: ')[1].split(" C,")[0]
textA4 = textA.split('RAM: ')[1].split("MB/")[0]


textB1 = textB.split('(')[1].split(":")[0]
textB2 = textB.split(') ')[1].split(": Running")[0]
textB3 = textB.split('temp: ')[1].split(" C,")[0]
textB4 = textB.split('RAM: ')[1].split("MB/")[0]


textlist0=[["Data", "Model", "Temperatura", "Wolny RAM"]]
textlistA=[[textA1+":00", textA2, textA3, textA4]]
textlistB=[[textB1+":00", textB2, textB3, textB4]]



if os.path.isfile(PATH1):
    print "file1 exist"
else:
    with open(PATH1, 'a') as f:
      csv_writer = csv.writer(f)
      for row in textlist0:
          csv_writer.writerow(row)

		  

if os.path.isfile(PATH2):
    print "file2 exist"
else:
    with open(PATH2, 'a') as f:
      csv_writer = csv.writer(f)
      for row in textlist0:
          csv_writer.writerow(row)




if czas == textA1:
  
  if textA2 == 'RPi1':
    with open(PATH1, 'a') as f:
      csv_writer = csv.writer(f)
      for row in textlistA:
          csv_writer.writerow(row)

  if textA2 == 'RPi2':
    with open(PATH2, 'a') as f:
      csv_writer = csv.writer(f)
      for row in textlistA:
          csv_writer.writerow(row)
  
  
if czas == textB1:

  if textB2 == 'RPi1':
    with open(PATH1, 'a') as f:
      csv_writer = csv.writer(f)
      for row in textlistB:
          csv_writer.writerow(row)

  if textB2 == 'RPi2':
    with open(PATH2, 'a') as f:
      csv_writer = csv.writer(f)
      for row in textlistB:
          csv_writer.writerow(row)


