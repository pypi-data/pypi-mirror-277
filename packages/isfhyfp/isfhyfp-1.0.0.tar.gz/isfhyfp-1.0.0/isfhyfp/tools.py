# -*- coding: utf-8 -*-
# @Author  : isFhy
# @Email   : fhy.sdwh@gmail.com
# @File    : tools.py
# @Time    : 2024/6/7 15:45
# **********************************************

import requests
from datetime import datetime


# 时间格式化
def handle_datetime(timestamp=None, onlyDate=False):
    """

    :param timestamp: 默认None,如果提供时间戳,则由时间戳格式化时间,否则按照当前时间来格式化
    :param onlyDate: 默认False, 格式化为:年月日时分秒, True,则格式化为年月日
    :return:
    """
    if timestamp:
        if len(str(timestamp)) == 13:
            date = datetime.fromtimestamp(timestamp / 1000)
        else:
            date = datetime.fromtimestamp(timestamp)
    else:
        date = datetime.now()
    if onlyDate:
        formatted_date = date.strftime('%Y-%m-%d')
    else:
        formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_date


def translate_by_google(API_KEY, text: str):
    """

    :param API_KEY: Google翻译的API_KEY
    :param text: 需要进行翻译的英文文本
    :return:
    """
    if text == '' or text is None:
        return ''
    url = 'https://translation.googleapis.com/language/translate/v2'
    params = {
        'q': text,
        'target': 'zh-CN',
        'source': 'en',
        'format': 'text',
        'key': API_KEY
    }
    try:
        resp = requests.get(url=url, params=params, verify=False).json()
        if resp.get('data').get('translations'):
            translatedText = resp['data']['translations'][0].get('translatedText')
            if translatedText:
                return translatedText
            else:
                return '翻译API网络异常,请自行翻译!'
        else:
            return '翻译API网络异常,请自行翻译!'
    except Exception as e:
        return '翻译API网络异常,请自行翻译!'
