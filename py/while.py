import datetime
cnt = 1000
import time
while cnt:
    print(datetime.datetime.now().strftime('%F %T'), cnt)
    cnt -= 1
    time.sleep(0.01)
