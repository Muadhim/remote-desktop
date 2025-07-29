import uvicorn
import asyncio
from fastapi import FastAPI
from config import SERVER_HOST, SERVER_PORT
import sys
from ws_agent import ws_agent_router
from database import get_db, Base, engine  
from contextlib import asynccontextmanager

app = FastAPI()
app.include_router(ws_agent_router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Auto-create table (jika development)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("✅ Server started and DB initialized")
    yield
    # Shutdown
    print("🛑 Server shutting down")

# Buat instance app dengan lifespan
app = FastAPI(lifespan=lifespan)

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
