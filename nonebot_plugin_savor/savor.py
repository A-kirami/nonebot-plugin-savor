import base64
import json
import random
import string
from io import BytesIO
from typing import List, TypedDict

import httpx
import websockets
from httpx import NetworkError
from PIL import Image


def RandomString():
    characters = string.ascii_lowercase + string.digits
    return "".join(random.choices(characters, k=10))


class Confidence(TypedDict):
    label: str
    confidence: float


async def savor_image(img_url: str) -> List[Confidence]:
    async with httpx.AsyncClient() as client:
        res = await client.get(img_url)
    if res.is_error:
        raise NetworkError("无法获取此图像")

    image = Image.open(BytesIO(res.content)).convert("RGB")
    image.save(imageData := BytesIO(), format="jpeg")
    img_b64 = base64.b64encode(imageData.getvalue()).decode()

    session_hash = RandomString()
    data = (
        '{"data":["data:image/jpeg;base64,'
        + img_b64
        + '",0.5],"event_data":null,"fn_index":1,"session_hash":"'
        + session_hash
        + '"}'
    )
    try:
        async with websockets.connect(
            "wss://hysts-deepdanbooru.hf.space/queue/join"
        ) as websocket:
            greeting = await websocket.recv()
            await websocket.send('{"fn_index":1,"session_hash":"' + session_hash + '"}')
            greeting = await websocket.recv()
            greeting = await websocket.recv()
            await websocket.send(data)
            greeting = await websocket.recv()
            greeting = await websocket.recv()
            if "process_completed" in greeting:
                return json.loads(greeting)["output"]["data"][0]["confidences"]
            else:
                raise ValueError("分析出错")
    except Exception as e:
        raise NetworkError("网络出错") from e
