from linebot.v3.messaging import ApiClient
from linebot.v3.webhooks import MessageEvent
# オウム返しサンプル

def match(event: MessageEvent, message: str) -> bool:
    return event.source.type == "user"

def action(event: MessageEvent, api_client: ApiClient, message: str):
    return "グループに招待して使ってね！"
