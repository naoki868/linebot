import json
import os
from linebot import LineBotApi
from linebot.models import TextSendMessage
from dotenv import load_dotenv

import requests
from bs4 import BeautifulSoup

load_dotenv()

url = "https://kumamate.net/vip/"

# HTMLを取得
response = requests.get(url)
html = response.content

# BeautifulSoupで解析
soup = BeautifulSoup(html, "lxml")

# 記事本文を取得
border = soup.find("span", class_="vipborder").text

CHANNEL_ACCESS_TOKEN = os.environ["CHANNEL_ACCESS_TOKEN"]
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID = os.environ['USER_ID']
    messages = TextSendMessage(text='今日のスマブラのVIPボーダー→' + border)
    line_bot_api.push_message(USER_ID,messages=messages)


if __name__ == "__main__":
    main()
