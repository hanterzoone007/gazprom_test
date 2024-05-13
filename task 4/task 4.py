import datetime
import os
import time

path = 'directory'

n = int(input('Введите количество дней: '))
for i in os.listdir(path):
    f = os.path.join(path, i)
    print(datetime.timedelta(seconds=os.stat(f).st_mtime),datetime.timedelta(seconds=time.time() - n * 86400))
    if os.stat(f).st_mtime < time.time() - n * 86400:
        if os.path.isfile(f):
            os.remove(f)
    


