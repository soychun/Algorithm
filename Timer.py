import time
import winsound as alarm
# import tqdm

def beepsound():
  freq = 1000
  duration = 1000
  alarm.Beep(freq,duration)
sec = int(0)
mint = int(0)
hour = int(0)
sec_total = int(0)


limit = 30

try:
  print('start')
  while 1:

    if sec_total==limit:
      beepsound()
      print(format(hour, '02') + ':' + format(mint, '02') + ':' + format(sec, '02'))

    sec+=1
    sec_total+=1
    time.sleep(1)
    if sec == 60:
      mint+=1
      sec = 0
      if mint ==60:
        hour +=1
        mint = 0
except KeyboardInterrupt:
  print(format(hour, '02') + ':' + format(mint, '02') + ':' + format(sec, '02'))



