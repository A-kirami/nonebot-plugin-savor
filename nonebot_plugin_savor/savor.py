import base64
import time
from io import BytesIO
from random import choice, randint
from typing import List, TypedDict

import httpx
from httpx import NetworkError
from PIL import Image


class Confidence(TypedDict):
    label: str
    confidence: float


def random_code(length: int = 6) -> str:
    return "".join(chr(randint(*choice(((48, 57), (97, 122))))) for _ in range(length))


async def fetch_data(hash_: str) -> List[Confidence]:
    async def get_data():
        status_url = "https://hf.space/embed/hysts/DeepDanbooru/api/queue/status/"
        async with httpx.AsyncClient() as client:
            res = await client.post(status_url, json={"hash": hash_})
            if data := res.json()["data"]:
                return data

    timestamp = time.time()
    while not (data := await get_data()) and time.time() - timestamp <= 3:
        ...
    if not data:
        raise NetworkError("无法获取返回数据")
    return data["data"][0]["confidences"]


async def savor_image(img_url: str) -> List[Confidence]:
    async with httpx.AsyncClient() as client:
        res = await client.get(img_url)
    if res.is_error:
        raise NetworkError("无法获取此图像")

    image = Image.open(BytesIO(res.content))
    image.save(imageData := BytesIO(), format="jpeg")
    img_b64 = base64.b64encode(imageData.getvalue()).decode()

    url_push = "https://hf.space/embed/hysts/DeepDanbooru/api/queue/push/"
    data = {
        "fn_index": 0,
        "data": [f"data:image/jpeg;base64,{img_b64}", 0.5],
        "session_hash": random_code(11),
        "action": "predict",
    }

    async with httpx.AsyncClient() as client:
        res = await client.post(url_push, json=data, timeout=10)

    return await fetch_data(res.json()["hash"])
