import configparser

from linebot import LineBotApi

config = configparser.ConfigParser()
config.read('config.ini')


LineBotApi("").issue_channel_token(
    config.get('line-bot', 'channel_id'), config.get('line-bot', 'channel_secret'))
