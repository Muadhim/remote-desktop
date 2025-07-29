from fastapi import FastAPI, WebSocket, APIRouter, WebSocketDisconnect
from fastapi.responses import HTMLResponse

ws_agent_router = APIRouter()

@ws_agent_router.websocket("/ws/agent")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Halo dari server WebSocket!")
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Balasan: {data}")
    except WebSocketDisconnect:
        print("client disconnected")
