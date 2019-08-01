#!/usr/bin/env python3
# coding=utf-8
"""
Author:hanziguo(@kingsoft.com)
Created:2018/11/07 15:12:23
desc:ks3 存储量
"""

import requests
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


def ks3_storage(request):
    http_url = "http://10.4.27.9:9998/query/normal"
    http_params = {'ver':'2.0.0',
                   'businessline':'ks3',
                   'start':'201904250000',
                   'end':'201904270000',
                   'filter':'userid=2000085575 and storageclass not in (\'STANDARD_IA\',\'ARCHIVE\')',
                   'calcFunc':'sum(allSize) as size',
                   'returnField':'userid',
                   'timeInterval':'1d',
                   'minCount':'1',
                   'type':'store_of_day'}
    response = requests.get(http_url, params=http_params)
    data_json = response.json()
    length = len(data_json.get('body'))
    num_data = []
    num_data_time_day = []
    result_list = []
    for i in range(0,length):
        temp = data_json.get('body')[i].get('size')
        time_hour = data_json.get('body')[i].get('time')
        time_day = time_hour.split(' ')[0]
        num_data_time_day.append(time_day)
        num_data.append(temp)
    for j in range(0, length):
        num_times = eval(num_data[j])/(1024**3)
        num_times = str(num_times) + '\n'
        result = num_data_time_day[j] + "日存储storage量（GB）: " + num_times
        result_list.append(result)

    context = {
        'result_list': result_list,
    }

    return render(request, 'HiMyserver/common.html', context)




