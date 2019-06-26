"""
试用inception
"""

import config

import requests
from rest_framework import status
from posixpath import join as url_join

notice_api = url_join('http://me:6061/', 'api/v2/dingtalk/notice/')

global_variables = globals()
ticket_id = 123
title = 'test'
content = 'content'
to = ['weiwencai']
print("\nticket_id: %s, to: %s, title: %s, ocntent: %s" % (
    ticket_id, to, title, content))


def main():
    data = {
        'ticket_id': ticket_id,
        'title': title,
        'content': content,
        'to': to
    }
    resp = requests.post(notice_api, json=data)
    if resp.status_code == status.HTTP_200_OK:
        print('通知发送成功')
    else:
        raise Exception('通知发送失败： code: %s, response: %s' % (
            resp.status_code, resp.text))


main()