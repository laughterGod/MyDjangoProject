#!/usr/bin/env python3
#coding=utf-8
"""
Author:hanziguo(@kingsoft.com)
Created:2019/02/15 10:12:23
desc:eip EIP月流量
"""


import requests
from django.shortcuts import render
from django.http import HttpResponse


def eip_submit(request, views_name_eip):
    context = {
        'views_name_eip': views_name_eip,
    }
    return render(request, 'HiMyserver/eip_submit.html', context)


def eip_day_transfer(request):
    http_url = "http://10.4.27.9:9998/query/normal"
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    product_id = request.POST.get('product_id')
    bandwidth = request.POST.get('bandwidth')
    http_params = {'ver': '2.0.0',
                   'businessline': 'eip',
                   'start': start_time,
                   'end': end_time,
                   'filter': 'product_id in (\'' + product_id + '\') and product_info in (\'eip\')',
                   'calcFunc': 'sum(txb) down,sum(rxb) up',
                   'returnField': 'region,name,product_id,isp',
                   'timeInterval': '30s',
                   'minCount': '1',
                   'preference': '_primary'}
    if bandwidth == '':
        bandwidth = '200'
    response = requests.get(http_url, params=http_params)
    data_json = response.json()
    length = len(data_json.get('body'))
    if length == 0:
        return HttpResponse("您查询的参数无数据返回，请重新输入")
    num_data_down = []
    num_data_up = []
    result_list = []
    for i in range(0, length):
        temp_up = data_json.get('body')[i].get('up')
        temp_down = data_json.get('body')[i].get('down')
        temp2 = temp_down.split('E')
        temp3 = temp_up.split('E')
        if len(temp2) != 2:
            temp2.append(0)
        temp2[0] = float(temp2[0])
        temp2[1] = int(temp2[1])
        temp_sum_down = temp2[0] * (10**temp2[1])
        num_data_down.append(temp_sum_down)
        if len(temp3) != 2:
            temp3.append(0)
        temp3[0] = float(temp3[0])
        temp3[1] = int(temp3[1])
        temp_sum_up = temp3[0] * (10**temp3[1])
        num_data_up.append(temp_sum_up)
    num_byte_down = sum(num_data_down)
    num_byte_up = sum(num_data_up)
    num_GB_down = (num_byte_down)/((1024 ** 3))
    num_GB_up = (num_byte_up) / ((1024 ** 3))
    num_GB_final = num_GB_down
    if int(bandwidth) > 200 and num_GB_up > num_GB_down:
        num_GB_final = num_GB_up
    result = " eip流量（GB）: " + str(num_GB_final)
    result_list.append(result)

    context = {
        'result_list': result_list,
    }
    return render(request, 'HiMyserver/common.html', context)

