# control_client/control.py
import asyncio, websockets, tkinter as tk, base64, json
from PIL import Image, ImageTk
import io

class ControllerApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.send_click)
        self.image_id = None

    async def run(self):
        self.ws = await websockets.connect("ws://localhost:8000/ws/controller")
        await self.receive_loop()

    async def receive_loop(self):
        while True:
            data = json.loads(await self.ws.recv())
            if data["type"] == "image":
                raw = base64.b64decode(data["data"])
                img = Image.open(io.BytesIO(raw))
                self.tk_img = ImageTk.PhotoImage(img)
                if self.image_id:
                    self.canvas.itemconfig(self.image_id, image=self.tk_img)
                else:
                    self.image_id = self.canvas.create_image(0, 0, anchor="nw", image=self.tk_img)

    def send_click(self, event):
        asyncio.create_task(self.ws.send(json.dumps({
            "type": "click", "x": event.x, "y": event.y
        })))

root = tk.Tk()
app = ControllerApp(root)
asyncio.run(app.run())
