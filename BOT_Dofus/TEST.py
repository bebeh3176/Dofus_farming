import os
from datetime import datetime

now = datetime.today()
now = datetime(now.year,now.month,now.day,now.hour,now.minute)
ste = 'LOG/{}.txt'.format(str(now))
# year = date.today()
# day = date.day
# month = date.month

# print(now)

log = open(ste, 'a')
log.write('allo')
log.close
#
log = open(ste, 'a')
log.write('allo')
log.close
