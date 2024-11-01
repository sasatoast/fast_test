from fastapi import (
    APIRouter,
    Header, 
    Request
)
import os
from dotenv import load_dotenv #環境変数を.envから読み取り使用する
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from starlette.exceptions import HTTPException

load_dotenv()#.envから環境変数の読み込み
router = APIRouter()#ルートの集約？
 
handler = WebhookHandler(os.environ.get('CHANNEL_SECRET'))#lineからのリクエストが間違ってないか検証

@router.post('/api/callback')
async def callback(request: Request, x_line_signature=Header(None)):
    body = await request.body()#awaitは非同期処理を行うもので、よくわかってないので質問すること

    try:
		# リクエストがLINEプラットフォームからのものかを検証する
        handler.handle(body.decode("utf-8"), x_line_signature)

    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="InvalidSignatureError")

    return "OK"
#webhookとは特定のイベントが発生した時に作動する