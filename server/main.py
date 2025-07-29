import uvicorn
import asyncio
from fastapi import FastAPI
from config import SERVER_HOST, SERVER_PORT
import sys
from ws_agent import ws_agent_router

app = FastAPI()
app.include_router(ws_agent_router)

@app.get("/")
async def index():
    return {"message": "Hello, World"}

async def run_direct():
    config = uvicorn.Config(app, host=SERVER_HOST, port=SERVER_PORT, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

def run_with_reload():
    uvicorn.run("main:app", host=SERVER_HOST, port=SERVER_PORT, reload=True)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--reload":
        run_with_reload()
    else:
        asyncio.run(run_direct())
