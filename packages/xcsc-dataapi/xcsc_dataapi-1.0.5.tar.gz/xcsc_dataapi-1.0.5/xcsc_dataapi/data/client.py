# -*- coding:utf-8 -*-
"""
Created on 2024/3/28
@author: pei jian
"""
import time
import requests
import pandas as pd
import json

from functools import partial
from xcsc_dataapi.util.unsafe_renegotiation_adapter import UnsafeRenegotiationAdapter


class DataApi:
    __token = ''
    __http_url = 'https://dataapi.xcsc.com/data-api'

    def __init__(self, token, timeout=10):
        self.__token = token
        self.__timeout = timeout

    def query(self, api_url='', fields='', current_page='', data_type='', **kwargs):
        """
                    查询dataframe_json以及json格式数据并返回dataframe格式数据
                    支持json格式以及dataframe_json格式的api返回dataframe数据格式的数据
                    :param api_url:接口地址，不包含域名及上下文
                    :param current_page: 当前页数，不传默认是 1
                    :param fields: 上送字段列表，不传默认返回全部
                    :param data_type: 默认是dataframe，可以上送json/dataframe
                    :return: api data
                    """
        if self.__token == '':
            raise Exception('token为空')
        api_headers = {
            'Content-Type': 'application/json',  # 自定义Content-Type头
            'Authorization': self.__token  # init 接口获取到的access_token
        }
        data_dict = kwargs
        # 向字典中添加新的键值对
        if current_page == '' or current_page is None:
            current_page = 1
        data_dict["currentPage"] = current_page  # 当前页数，1 代表第一页，2 代表第二页
        data_dict["fieldList"] = fields  # 自定义返回相应参数，不传或者为空默认都是返回全部，传参内容以逗号【,】分割
        api_data = {
            'requestId': time.time_ns(),
            'data': data_dict
        }
        session = requests.Session()
        # 将自定义的适配器挂载到 'https://' 协议
        session.mount("https://", UnsafeRenegotiationAdapter())
        res = session.post(self.__http_url + api_url, json=api_data, headers=api_headers, verify=False)
        # res = requests.post(self.__http_url + api_url, json=api_data, headers=api_headers, verify=False)
        if res.status_code == 200:
            if data_type == '' or data_type is None or data_type == 'dataframe':
                result_df_json = json.loads(res.text)
                if result_df_json['code'] != '0':
                    raise Exception('获取资讯数据失败:' + result_df_json['msg'])
                data = result_df_json['data']
                if 'fields' in data and 'items' in data:
                    columns = data['fields']
                    items = data['items']
                    return pd.DataFrame(items, columns=columns)
                else:
                    return pd.DataFrame(data)

            elif data_type == 'json':
                return res.text
            else:
                raise Exception('不支持的data_type类型')

        else:
            raise Exception('api数据请求失败:' + res.text)

    def __getattr__(self, name):
        return partial(self.query, name)
