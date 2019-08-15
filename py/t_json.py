# coding:utf-8
# !/usr/bin/env python
# Author: weiweicai@qudian.com
# Purpose:
# Create: 2019-08-05 13:23
import pymysql
import time
import logging

import datetime
import decimal
import json  # noqa
import uuid



class ComplexEncoder(json.JSONEncoder):
    """
        JSONEncoder subclass that knows how to encode date/time/timedelta,
        decimal types, generators and other basic python objects.
        """

    def default(self, obj):
        # For Date Time string spec, see ECMA 262
        # https://ecma-international.org/ecma-262/5.1/#sec-15.9.1.15
        print(type(obj))
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S---')
        elif isinstance(obj, int):
            return str(obj)
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')

        elif isinstance(obj, decimal.Decimal):
            # Serializers will coerce decimals to strings by default.
            return float(obj)
        elif hasattr(obj, '__getitem__'):
            try:
                return dict(obj)
            except Exception:
                pass
        elif hasattr(obj, '__iter__'):
            return tuple(item for item in obj)
        return super(ComplexEncoder, self).default(obj)

data = [
    {
        'a': 1,
        'date': datetime.datetime.now()
    }
]

# js 里面，大于 2的53次方（int的最大数据）的整数，后面是用0补齐，所以要转化成str保正准确
# 由于JSONEncoder.encode 不会处理int，所以，在序列化之前先转化类型
for x in data:
    for k, v in x.items():
        if isinstance(v, int):
            x[k] = str(x[k])  # 这里会直接修改到 data 内部的值

rd = json.dumps(data,cls=ComplexEncoder)
dd = json.loads(rd)
print(rd)
print(dd)
