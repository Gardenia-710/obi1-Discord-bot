#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json

from apiclient.discovery import build

def yt_check():
    API_KEY = os.environ["YOUTUBE_API_KEY"]
    print(API_KEY)
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'
    # CHANNEL_ID = 'UCybmNGptaQ6EhT9TWvqr3ZA'
    #↓ライブのやつ
    VIDEO_ID_LIST = ['viZh-Y3Rz9o']
    # VIDEO_ID_LIST = ['Po1l_ix2wSI']

    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=API_KEY
    )

    for video_id in VIDEO_ID_LIST:
        response = youtube.videos().list(
        part = 'snippet,statistics',
        id = video_id
        ).execute()

        for item in response.get("items", []):
            if item["kind"] != "youtube#video":
                continue
            with open("out.json","w") as fp:
                json.dump(item, fp, indent=4, ensure_ascii=False)

            # ↓printする場合
            # print('*' * 10)
            # print(json.dumps(item, indent=2, ensure_ascii=False))
            # print('*' * 10)

            # TorFで返す
            return True
        # ファイルのあるなしで判断してる。多分もうちょっといいやり方ある。
        # あ
        fl = os.path.exists("out.json")
        if fl==False:
            # print("非公開")
            return False
