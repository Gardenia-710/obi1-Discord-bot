from discordwebhook import Discord
import NoticeTube
import os

def Notice_Pnuts():
    url = os.environ["DISCORD_WEBHOOK_URL"]
    discord = Discord(url=url)
    resp = NoticeTube.yt_check()
    if resp == True:
        discord.post(content="公開済み\nURL: https://www.youtube.com/watch?v=viZh-Y3Rz9o")
    elif resp == False:
        discord.post(content="非公開")
        return

Notice_Pnuts()