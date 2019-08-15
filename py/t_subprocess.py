import subprocess
import time

"""
调用shell，并且冲shell获取返回值
"""


def test(cmd):
    p = subprocess.Popen(cmd, shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    log_list = []
    log_list_dict = {
        'log_list': log_list
    }
    while p.poll() is None:
        line = p.stdout.readline()
        handle_log_line(line, log_list_dict)
        time.sleep(1)

    left_lines = p.stdout.readlines()
    for x in left_lines:
        handle_log_line(x, log_list_dict)

    print(''.join(log_list_dict['log_list']))
    if p.returncode == 0:
        print('执行成功')
    else:
        print('执行失败')


def handle_log_line(log_line, log_list_dict):
    line = log_line.decode()
    if line:
        log_list_dict['log_list'] = log_list_dict['log_list'][-5:]
        log_list_dict['log_list'].append(line)
        print('list', log_list_dict['log_list'])


def test_reg_for_gh_ost_log():
    import re
    pattern = r'Copy:\s\d+/\d+\s\d+\.\d+%; '


    s = 'Copy: 466000/940897 49.5%; Applied: 0; Backlog: 0/1000; Time: 36s(total), 36s(copy); streamer: mysql-bin.001748:104482329; State: migrating; ETA: 36s\n'
    m = re.search(pattern, s)
    if m:
        res = m.group()
        s = r'\s\d+'
        print(s)
        m = re.search(s, res)
        print(m)
        r = m.group()
        print(r)
        print(int(r[:-1]))


import shlex
import re
def execute_gh_ost():
    shell_cmd = f'''./gh-ost -host 172.16.6.35 -port 3307 -user ljh 
    -password "123456" --initially-drop-ghost-table --allow-on-master 
    --database ljh --table test
     --alter " ADD column cc varchar(20)" -chunk-size 2000 
     -max-load Threads_running=30 -critical-load Threads_running=50 
     -dml-batch-size 50  --verbose  --assume-rbr 
     --assume-master-host=172.16.6.35:3307    
     -serve-socket-file=/tmp/ghost_pay_trade.sock  --execute'''

    # shell_cmd = '/usr/local/bin/python3 /Users/qudian/code/private/practice/py/while.py'
    cmd = shlex.split(shell_cmd)
    print('开始执行ghost')
    p = subprocess.Popen(cmd, shell=False,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    log_list = []
    log_list_dict = {
        'log_list': log_list
    }
    log_line_num = 4
    execute_log = {}
    print('开始等待执行结果')
    while p.poll() is None:
        line = p.stdout.readline()
        handle_gh_ost_log_line(line, log_list_dict, execute_log,
                                    log_line_num)

    print(f'执行完成, 开始处理剩余日志:')
    left_lines = p.stdout.readlines()
    print(f'行数：{len(left_lines)}')
    for line in left_lines:
        print(line)
        handle_gh_ost_log_line(line, log_list_dict, log_line_num)
    print('日志处理完成')
    if p.returncode == 0:
        print('执行成功')
    else:
        print('执行失败')


def execute_gh_ost2():

    log_list = []
    log_list_dict = {
        'log_list': log_list
    }
    log_line_num = 4
    execute_log = {}
    from log_str import log_str

    left_lines = log_str.split('2019')
    for line in left_lines:
        handle_gh_ost_log_line(line, log_list_dict, log_line_num)

def handle_gh_ost_log_line(log_line, log_list_dict, execute_log,
                           log_line_num=5):
    """

    :param log_line:
    :param log_list_dict: 为字典，里面有log_list，为list，是引用的方式
    :param execute_log:
    :param log_line_num:
    :return:
    """
    # print(log_line)
    line = log_line
    pattern = r'Copy:\s\d+/\d+\s\d+\.\d+%;'
    if line:
        m = re.search(pattern, line)
        if m:
            print(line)
            line_num_pattern = r'\d+'
            execute_progress = m.group()
            print('进度', execute_progress)
            line_num_m = re.search(line_num_pattern, execute_progress)
            print('行数：', int(line_num_m.group()))
        else:
            # continue
            # print('不是进度行', line)
            pass


if __name__ == '__main__':
    cmd = '/usr/local/bin/python3 /Users/qudian/code/private/practice/py/while.py'
    # cmd = 'ls'
    # test(cmd)
    # test_reg_for_gh_ost_log()
    execute_gh_ost()