# -*- coding: utf-8 -*-
"""
@Time : 2023/11/28 14:16 
@项目：PuDongSmartPro
@File : hikvision_operations.by
@PRODUCT_NAME :PyCharm
"""
# 海康威视 - 使用
import requests

from basic_type_operations.date_operation import DateOperation


class GETHikVision(object):
    # 获取直播连接
    def get_player_url(self, accessToken, deviceSerial, quality=1, channelNo=1, protocol=2, **kwargs):
        url = 'https://open.ys7.com/api/lapp/v2/live/address/get'
        data = {
            "accessToken": accessToken,
            "deviceSerial": deviceSerial,
            "quality": quality,
            "channelNo": channelNo,
            "protocol": protocol
        }
        res = requests.post(url, data).json()
        code = res.get("code")
        if code == "200":
            live_connection = res.get("data").get("url")
            expireTime = DateOperation.string_year_second(res.get("data").get("expireTime"))
            return live_connection, expireTime
        else:
            return None, None

    def get_accessToken(self, appKey, secret, **kwargs):
        accessToken_url = 'https://open.ys7.com/api/lapp/token/get'
        data = {
            'appKey': appKey,
            'appSecret': secret
        }
        res = requests.post(url=accessToken_url, data=data)
        result = res.json()
        code = result.get('code')
        accessToken = None
        if code == '200':
            accessToken = result.get('data').get('accessToken')
        return accessToken
