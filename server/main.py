from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.websocket("/ws/agent")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Halo dari server WebSocket!")
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Balasan: {data}")
