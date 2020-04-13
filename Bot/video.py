# -*- coding: utf-8 -*-
from linebot.models import (
    CarouselTemplate, TemplateSendMessage, CarouselColumn,
    PostbackTemplateAction, MessageTemplateAction, URITemplateAction, BubbleContainer, BoxComponent, ButtonComponent,
    ImageComponent, MessageAction, URIAction, CarouselContainer, FlexSendMessage
)

from Bot.Youtube_API import get_videos, Order


def get_carousel_template_message(video_sort=Order, carousel_column_amount=5):
    if carousel_column_amount > 9:
        return "過多的 columns (必須小於10)"
    columns = []
    for video in get_videos("UC-sM_PLqzgktdUcW2LEKKkQ", video_sort, carousel_column_amount):
        columns.append(CarouselColumn(
            thumbnail_image_url=video,
            title='標題',
            text='敘述',
            actions=[
                PostbackTemplateAction(
                    label='postback1',
                    text='postback text1',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='message1',
                    text='message text1'
                ),
                URITemplateAction(
                    label='uri1',
                    uri='http://example.com/1'
                )
            ]
        ))
    columns.append(get_video_menu())

    return TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=columns
        )
    )


def get_video_menu():
    return BubbleContainer(
        direction='ltr',
        #hero=ImageComponent(
        #    url='https://previews.123rf.com/images/galinadarla/galinadarla1610/galinadarla161000124/67174940-web-site-menu-icon-flat-style-made-in-vector-black-and-white-icon.jpg',
        #    size='full',
        #    aspectRatio='16:9',
        #    aspectMode='cover'
        #),
        body=BoxComponent(
            layout='vertical',
            contents=[
                ButtonComponent(
                    action=MessageAction(label='最新上傳', text='最新上傳'),
                    style='primary',
                    color='#29D90C',
                    margin='lg'
                ),
                ButtonComponent(
                    action=MessageAction(label='熱門影片', text='熱門影片'),
                    style='primary',
                    color='#29D90C',
                    margin='lg'
                ),
                ButtonComponent(
                    action=MessageAction(label='最多喜歡', text='最多喜歡'),
                    style='primary',
                    color='#29D90C',
                    margin='lg'
                ),
                ButtonComponent(
                    action=MessageAction(label='相關影片', text='相關影片'),
                    style='primary',
                    color='#29D90C',
                    margin='lg'
                ),
                ButtonComponent(
                    action=MessageAction(label='標題順序', text='標題順序'),
                    style='primary',
                    color='#29D90C',
                    margin='lg'
                ),
                ButtonComponent(
                    action=MessageAction(label='影片上傳次數', text='影片上傳次數'),
                    style='primary',
                    color='#29D90C',
                    margin='lg'
                )
            ]
        )
    )


def create_flex_template(order=Order.DATE, amount=5):
    thumbnails_url, video_url = get_videos('UC-sM_PLqzgktdUcW2LEKKkQ', order, amount)
    bubble_containers = []
    for i in range(len(video_url)):
        bubble_containers.append(create_bubble_container(thumbnails_url[i], video_url[i]))
    bubble_containers.append(get_video_menu())
    return FlexSendMessage(
        alt_text='test',
        contents=CarouselContainer(
            contents=bubble_containers
        )
    )


def create_bubble_container(thumbnail_image_url, video_url):
    return BubbleContainer(
        direction='ltr',
        hero=ImageComponent(
            url=thumbnail_image_url,
            size='full',
            aspectRatio='16:9',
            aspectMode='cover'
        ),
        body=BoxComponent(
            layout='vertical',
            contents=[
                ButtonComponent(
                    action=URIAction(label='觀看影片', uri=video_url),
                    style='primary',
                    color='#29D90C',
                    margin='lg'
                ),
                ButtonComponent(
                    action=URIAction(label='分享影片', uri='https://line.me/R/msg/text/?' + video_url),
                    style='primary',
                    color='#29D90C',
                    margin='lg'
                )
            ]
        )
    )
