import json
from time import perf_counter
from fastapi import FastAPI, WebSocket, Response as FastAPIResponse, WebSocketDisconnect
from websockets.exceptions import ConnectionClosed
from starlette.websockets import WebSocketDisconnect, WebSocketState
from listen.Wav2Vec.engine import Transcriber, Response, Error
from listen.Wav2Vec import utils
from listen.exception import NotAllowedToListenError
import uvicorn


CONFIG = utils.get_config_or_default()
is_allowed_to_listen = utils.is_allowed_to_listen(CONFIG)

if not is_allowed_to_listen:
    raise NotAllowedToListenError(utils.CONFIG_PATH)

models_path = utils.get_loc_model_path()

print("Loading transcription model...")
transcriber = Transcriber(models_path=models_path)

print("Starting server...")
app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def receive_audio(self, websocket: WebSocket):
        return await websocket.receive_bytes()

    async def send_reply(self, websocket: WebSocket, reply: dict):
        await websocket.send_json(json.dumps(reply))

    async def send_error(self, websocket: WebSocket, error: str):
        await self.send_reply(websocket, reply=Error(error).__dict__)

    async def send_transcript(self, websocket: WebSocket, text: str, inference_time: float):
        await self.send_reply(websocket, reply=Response(text, inference_time).__dict__)


manager = ConnectionManager()

@app.get("/")
async def healthcheck():
    """
    Health check endpoint
    """
    return FastAPIResponse(content="Welcome to listen.sock: Transcription as a Service!", status_code=200)

@app.websocket("/api/v2/transcribe")
async def transcribe(websocket: WebSocket):
    """
    Transcribe audio data received via WebSocket
    """
    await manager.connect(websocket)
    print("Received WebSocket request at /api/v2/transcribe")
    try:
        audio_data = await manager.receive_audio(websocket)
        inference_start = perf_counter()
        text, _ = transcriber.run(audio_data, transcriber.sample_rate)
        inference_end = perf_counter() - inference_start
        print(f"Completed WebSocket request at /api/v2/transcribe in {inference_end} seconds")
        await manager.send_transcript(websocket, text, inference_end)
    except Exception as e:
        if websocket.client_state == WebSocketState.CONNECTED:
            await manager.send_error(websocket, str(e))

if __name__ == "__main__":
    uvicorn.run('listen.Wav2Vec.as_service:app', host="127.0.0.1", port=5063, workers=1, lifespan="on", reload=True, limit_concurrency=True, timeout_keep_alive=None)