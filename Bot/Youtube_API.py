# -*- coding: utf-8 -*-
from enum import Enum

from googleapiclient import discovery

api_service_name = "youtube"
api_version = "v3"
api_key = 'AIzaSyDbiOR0x93D1UC6uBdV2ZwTntj-vsAAdBk'

youtube = discovery.build(api_service_name, api_version, developerKey=api_key)


class Order(Enum):
    DATE = 'date'  # 依據影片上傳日期由最新開始排序
    VIEW_COUNT = 'viewCount'  # 依據觀看數由高至低排序
    RATING = 'rating'  # 依據評分由高至低排序
    RELEVANCE = 'relevance'  # 依據影片相關性排序
    TITLE = 'title'  # 依據標題字母 (英文) 順序排序
    VIDEO_COUNT = 'videoCount'  # 依據影片上傳數量由高至低排序


def get_videos(channelId, order, amount=5):
    if channelId is None:
        return "channelId is None"

    request = youtube.search().list(
        part="snippet",
        channelId=channelId,
        maxResults=amount,
        order=order.value,
        type="video"
    )
    response = request.execute()

    thumbnails_urls = []
    video_urls = []
    for item in response['items']:
        snippet = item['snippet']
        thumbnails = snippet['thumbnails']
        thumbnails_urls.append('' + (thumbnails['high'])['url'])
        video_urls.append('https://www.youtube.com/watch?v=' + (item['id'])['videoId'])
    return thumbnails_urls, video_urls


def get_broadcast():
    return ''
