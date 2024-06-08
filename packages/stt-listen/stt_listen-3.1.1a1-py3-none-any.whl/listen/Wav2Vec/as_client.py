import json
# import websockets # not websocket!!!
import aiohttp
import asyncio
from listen.Wav2Vec.utils import get_config_or_default

HOST, PORT = "0.0.0.0", "5063"
CONFIG = get_config_or_default()

if CONFIG.get('service'):
    HOST = CONFIG['service'].get('host', None)
    PORT = CONFIG['service'].get('port', None)

async def stt(audio_bin: bytes, host=HOST, port=PORT):
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(f"ws://{host}:{port}/api/v2/transcribe", timeout=60, receive_timeout=120) as ws:
            # await ws.send(audio_bin)
            await ws.send_bytes(audio_bin)
            response = await ws.receive_json()
            r = json.loads(response)
            if r.get('message'):
                return r.get('message')
            elif r.get('text'):
                return r.get('text')
