import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open("info.json","r")
info = json.load(file)
print(info)

CHANNEL_ACCESS_TOKEN = info["CHANNEL_ACCESS_TOKEN"]
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID = info["USER_ID"]
    messages = TextSendMessage(text="今日のVIPボーダーは〇〇です\nVPIに入れるよう頑張りましょう")
    line_bot_api.push_message(USER_ID,messages=messages)


if __name__ == "__main__":
    main()
