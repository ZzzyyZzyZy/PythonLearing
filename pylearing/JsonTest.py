#!/usr/bin/python3

import json
import datetime

# Python 字典类型转换为 JSON 对象

data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)
print(datetime.datetime.now())
