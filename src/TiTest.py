import schedule
import time

def job():
    print("I'm working...")

# 10分ごとに実行
schedule.every(1).minutes.do(job)

# １時間ごとに実行
schedule.every().hour.do(job)

# 毎日10時30分に実行
schedule.every().day.at("10:30").do(job)

# 毎日月曜日に実行
schedule.every().monday.do(job)

# 毎週水曜13時15分に実行
schedule.every().wednesday.at("13:15").do(job)

# 毎時17分に実行
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)