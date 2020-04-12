# -*- coding: utf-8 -*-
import configparser

from linebot import LineBotApi

config = configparser.ConfigParser()
config.read('resource/config.ini')

channel_token = LineBotApi("").issue_channel_token(
    config.get('line-bot', 'channel_id'), config.get('line-bot', 'channel_secret'))


def get_channel_access_token():
    """
    回傳 Line Bot token
    """
    return channel_token.access_token


def get_channel_secret():
    """
    回傳 Line Bot secret
    """
    return config.get('line-bot', 'channel_secret')
