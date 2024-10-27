from database import engine, Base

async def init_db():
    async with engine.begin() as conn:
        # This will create all tables. Be careful with this in production!
        await conn.run_sync(Base.metadata.create_all)