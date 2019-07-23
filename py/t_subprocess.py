import subprocess
import time

def test(cmd):
    p = subprocess.Popen(cmd, shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    while p.poll() is None:
        line = p.stdout.readline()
        time.sleep(1)
        print(line)
    left_lines = p.stdout.readlines()
    for x in left_lines:
        print(x)

    if p.returncode == 0:
        print('执行成功')
    else:
        print('执行失败')


if __name__ == '__main__':
    cmd = '/usr/local/bin/python3 /Users/qudian/code/private/practice/py/while.py'
    test(cmd)
