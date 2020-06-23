import asyncio
import pydig
import datetime
from concurrent.futures import ThreadPoolExecutor
import asyncio
import threading
import time


# async def ping_server(ip):
# 	r = pydig.query('vpc-r-bp1d644a7ec56294.redis.rds.aliyuncs.com', 'A')
#     print(r)
#     return r

# async def ping_local():
#     return await ping_server('192.168.1.1')


import time
import asyncio
from aiohttp import ClientSession

import asyncio

import time

now = lambda: time.time()

async def do_some_work1(x):
    print('----')
    # time.sleep(1)
    await asyncio.sleep(x)
    pydig.query('www.baidu.com', 'A')


async def do_some_work(x):
    print('Waiting: ', x)
    # time.sleep(1)
    # await asyncio.sleep(x)
    await do_some_work1(1)


    return 'Done after {}s'.format(x)

start = now()

coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

tasks = []
for x in range(4):
    tasks.append(
        asyncio.ensure_future(do_some_work(1)),
    )

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print('Task ret: ', task.result())

print('TIME: ', now() - start)

# # 定义一个协程

# async def do_some_work(x):
#     print('start', x)
#     pydig.query('www.baidu.com', 'A')
#     # time.sleep(1)
#     await asyncio.sleep(1)
#     print('end', x)

    
# start = now()

# # 获取协程对象
# # coroutine = do_some_work(2)

# # 获取时间循环对象
# loop = asyncio.get_event_loop()
# # 注册协程到时间循环
# for x in range(5):
#     task = loop.create_task(do_some_work(x))
#     loop.run_until_complete(task)
#     # loop.run_until_complete(do_some_work(x))

# print('TIME: ', now() - start)


# tasks = []
# url = "https://www.baidu.com/{}"
# async def hello(url):
#     async with ClientSession() as session:
#         async with session.get(url) as response:
# #            print(response)
#             print('Hello World:%s' % time.time())
#             return await response.read()

# def run():

#     for i in range(5):
#         task = asyncio.ensure_future(hello(url.format(i)))
#         tasks.append(task)
#     result = loop.run_until_complete(asyncio.gather(*tasks))
#     print(result)

# if __name__ == '__main__':
#     t = datetime.datetime.now()
#     loop = asyncio.get_event_loop()
#     run()
#     print(t)
#     print(datetime.datetime.now())

# # -*- coding:utf-8 -*-
# import asyncio
# import time
# ioloop = asyncio.get_event_loop()


# async def get_url_title(url, i):
#     print('开始访问网站:{}'.format(url), i)
#     pydig.query(url, 'A')
#     time.sleep(2)

#     print('网站访问成功', i)

# if __name__ == '__main__':
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     # 创造一个事件循环
#     tasks = [ioloop.create_task(get_url_title('http://www.langzi.fun', i)) for i in range(50)]
#     # 这个列表代表总任务量，即执行10次get_url_title()函数
#     loop.run_until_complete(asyncio.wait(tasks))
#     # asyncio.wait后面接上非空可迭代对象,一般来说是功能函数列表
#     # 功能是一次性提交多个任务，等待完成
#     # loop.run_until_complete(asyncio.gather(*tasks))
#     # 和上面代码功能一致，但是gather更加高级，如果是列表就需要加上*
#     # 这里会等到全部的任务执行完后才会执行后面的代码
#     end_time = time.time()
#     print('消耗时间:{}'.format(end_time-start_time))

# import asyncio

# async def speak_async():
#     print('OMG asynchronicity!')

# loop = asyncio.get_event_loop()
# loop.run_until_complete(speak_async())
# loop.close()


# import signal
# import sys
# import asyncio
# import aiohttp
# import json

# loop = asyncio.get_event_loop()
# client = aiohttp.ClientSession(loop=loop)

# async def get_json(client, url):
#     async with client.get(url) as response:
#         assert response.status == 200
#         return await response.read()

# async def get_reddit_top(subreddit, client):
#     print(datetime.datetime.now())
#     data1 = await get_json(client, 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')

#     j = json.loads(data1.decode('utf-8'))
#     for i in j['data']['children']:
#         score = i['data']['score']
#         title = i['data']['title']
#         link = i['data']['url']
#         print(str(score) + ': ' + title + ' (' + link + ')')

#     print('DONE:', subreddit + '\n')

# def signal_handler(signal, frame):
#     loop.stop()
#     client.close()
#     sys.exit(0)

# signal.signal(signal.SIGINT, signal_handler)

# asyncio.ensure_future(get_reddit_top('python', client))
# asyncio.ensure_future(get_reddit_top('programming', client))
# asyncio.ensure_future(get_reddit_top('compsci', client))
# loop.run_forever()



# L = []
# def work():
# 	# print('---', datetime.datetime.now())
# 	# time.sleep(3)
# 	r = pydig.query('vpc-r-bp1d644a7ec56294.redis.rds.aliyuncs.com', 'A')
# 	L.append(datetime.datetime.now().strftime('%F %T'))
# 	print(datetime.datetime.now())


# async def main(loop):
#   executor = ThreadPoolExecutor()
#   await loop.run_in_executor(executor, work)

# loop = asyncio.get_event_loop()
# print(datetime.datetime.now())
# for x in range(500):
# 	loop.run_until_complete(main(loop))
# print(datetime.datetime.now())
# loop.close()


# print(datetime.datetime.now())
# t_list = []
# for x in range(100):
# 	t = threading.Thread(target=work)
# 	t.start()
# 	t_list.append(t)
# for x in t_list:
# 	x.join()
# print(L)
# print(datetime.datetime.now())


# print(datetime.datetime.now())
# for i in range(100):
# 	pydig.query('vpc-r-bp1d644a7ec56294.redis.rds.aliyuncs.com', 'A')
# print(datetime.datetime.now())



