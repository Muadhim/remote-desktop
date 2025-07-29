# agent_client/agent.py
import asyncio, websockets, base64, mss, io, json
from PIL import Image
from pynput.mouse import Controller as Mouse
from pynput.keyboard import Controller as Keyboard

async def agent():
    ws = await websockets.connect("ws://localhost:8000/ws/agent")
    mouse = Mouse()
    keyboard = Keyboard()

    while True:
        with mss.mss() as sct:
            img = sct.grab(sct.monitors[1])
            buf = io.BytesIO()
            Image.frombytes("RGB", img.size, img.rgb).save(buf, format="JPEG")
            img_b64 = base64.b64encode(buf.getvalue()).decode()
            await ws.send(json.dumps({"type": "image", "data": img_b64}))
        
        try:
            msg = await asyncio.wait_for(ws.recv(), timeout=0.1)
            data = json.loads(msg)
            if data["type"] == "click":
                mouse.position = (data["x"], data["y"])
                mouse.click()
        except asyncio.TimeoutError:
            pass

asyncio.run(agent())
