import datetime
import time
from log_str import log_str
import os
os.st


def while_print():
    cnt = 1000
    while cnt:
        print(datetime.datetime.now().strftime('%F %T'), cnt)
        cnt -= 1
        time.sleep(0.01)


def print_log():
    log = log_str

    log_list = log.split('2019')
    for l in log_list:
        print(l)
        time.sleep(0.001)


if __name__ == '__main__':
    print_log()


