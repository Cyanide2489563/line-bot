# -*- coding: utf-8 -*-
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)

from Bot import Config
from Bot.Youtube_API import Order
from Bot.video import create_flex_template

app = Flask(__name__)

line_bot_api = LineBotApi(Config.get_channel_access_token())
handler = WebhookHandler(Config.get_channel_secret())
app.logger.info("Line Bot 初始化完成")


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "最新上傳":
        line_bot_api.reply_message(event.reply_token, create_flex_template(Order.DATE, 9))
    if event.message.text == "熱門影片":
        line_bot_api.reply_message(event.reply_token, create_flex_template(Order.VIEW_COUNT, 9))
    if event.message.text == "最多喜歡":
        line_bot_api.reply_message(event.reply_token, create_flex_template(Order.RATING, 9))

    if event.message.text == "直播":
        line_bot_api.reply_message(event.reply_token, TextSendMessage('目前沒有正在進行的直播'))


if __name__ == "__main__":
    app.debug = True
    app.run()
