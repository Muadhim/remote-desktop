import asyncio
from database import Base, engine
import database.models # Import semua model sebelum migrasi

async def migrate():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("✅ Migration complete: All tables created (if not exist).")

if __name__ == "__main__":
    asyncio.run(migrate())
