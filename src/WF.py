from discordwebhook import Discord
import NoticeTube
import os
import logging
import schedule
import time

logging.basicConfig(filename='test.log', level=logging.DEBUG)

def Notice_Pnuts():
    url = os.environ["DISCORD_WEBHOOK_URL"]
    discord = Discord(url=url)
    resp = NoticeTube.yt_check()
    if resp == True:
        discord.post(content="@かぎしっぽ\n公開済み\nURL: https://www.youtube.com/watch?v=viZh-Y3Rz9o")
        logging.info("公開済み")
    elif resp == False:
        # discord.post(content="非公開")
        logging.info("非公開")
        return
# 1時間ごとに実行
schedule.every().hour.do(Notice_Pnuts)
# Notice_Pnuts()

while True:
    schedule.run_pending()
    time.sleep(1)