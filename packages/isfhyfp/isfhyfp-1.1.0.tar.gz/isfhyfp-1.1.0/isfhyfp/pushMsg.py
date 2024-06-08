# -*- coding: utf-8 -*-
# @Author  : isFhy
# @Email   : fhy.sdwh@gmail.com
# @File    : pushMsg.py
# @Time    : 2024/6/7 22:39
# **********************************************

import time
import requests
import telebot
import urllib3

urllib3.disable_warnings()


# Vocechat推送 - 通过Vocechat机器人API,推送消息到指定群组
def vocechat_push(message, vc_url, vc_token, gid):
    """

    :param message: 要推送的消息文本
    :param vc_url: Vocechat服务器URL 格式: http(s)://域名(IP):端口
    :param vc_token: Vocechat机器人API
    :param gid: 群组ID
    :return:
    """
    url = f'{vc_url}/api/bot/send_to_group/{gid}'
    headers = {
        'x-api-key': vc_token,
        'Content-Type': 'text/plain',
    }
    payload = message.encode('utf-8')
    try:
        resp = requests.post(url, headers=headers, data=payload)
        return resp
    except Exception as e:
        return None


# Telegram推送
def telegram_push(message, bot_token, chat_id):
    telegram_bot = telebot.TeleBot(token=bot_token)
    telegram_bot.send_message(chat_id, message)


# WxPusher推送
def wxpusher_push(message, title, app_token, topic_id=None, uid=None):
    """

    :param title: 推送消息的标题
    :param message: 要推送的消息正文
    :param app_token:
    :param topic_id: 推送到群组的ID  该参数和UID同时只能传递一个!
    :param uid: 推送到个人的UID
    :return:
    """
    url = 'https://wxpusher.zjiecode.com/api/send/message'
    payload = {}
    if topic_id and uid is None:
        payload = {
            "appToken": app_token,
            "content": message,
            "summary": title,
            "contentType": 1,
            "topicIds": [topic_id],
        }
    elif uid and topic_id is None:
        payload = {
            "appToken": app_token,
            "content": message,
            "summary": title,
            "contentType": 1,
            "uids": [uid],
        }

    try:
        resp = requests.post(url=url, json=payload, verify=False).json()
        if resp.get('msg') == '处理成功':
            return True, resp
    except Exception as e:
        return False, e


# 喵提醒推送
def miao_push(message, miao_id, product_id):
    url = "https://miaotixing.com/trigger"
    payload = {
        "id": miao_id,
        'text': message,
        'type': 'json',
        'ts': int(time.time()),
        'product': product_id
    }
    try:
        resp = requests.post(url=url, json=payload, verify=False).json()
        if resp.get('code') == 0:
            data = resp.get('data')
            users = data['users']
            mptext_success = data['success_sent']['mptext']
            phonecall_success = data['success_sent']['phonecall']
            return True, f"|- 喵提醒推送成功: 成功推送给{users}个人,成功推送公众号提醒{mptext_success}次,成功推送语音电话提醒{phonecall_success}次!"
        else:
            return False, f"|- 喵提醒推送失败: {resp.get('msg')}"
    except Exception as e:
        return False, f"|- 喵提醒推送失败: {e}"


# 推送消息文本处理
def handle_message(message_dict: dict):
    """
    提供字典格式的消息,{'title': '【交易所】公告监控', '发布时间': '2024年1月1日 10:10'}
    格式化成以下格式:
        *********【交易所】公告监控*********
        【发布时间】2024年1月1日 10:10
        ...

    :param message_dict: 提供待推送消息的字典格式, 第一个键值对必须是 标题内容
    :return:
    """
    title = message_dict['title']
    message = f'*********{title}*********\n\n'
    for k, v in message_dict.items():
        if k != 'title':
            message += f'【{k}】{v}\n'


    message += '*********************************\n'
    return message


