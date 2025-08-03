from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:078@localhost:5432/fastapi"


engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session





# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
# from sqlalchemy import create_engine  # sync version
# from sqlmodel import SQLModel
# from typing import AsyncGenerator

# DATABASE_URL_ASYNC = "postgresql+asyncpg://postgres:078@localhost:5432/fastapi"
# DATABASE_URL_SYNC = "postgresql+psycopg2://postgres:078@localhost:5432/fastapi"

# # Async engine for real usage
# async_engine = create_async_engine(DATABASE_URL_ASYNC, echo=True)

# # Sync engine just for creating tables
# def init_db():
#     sync_engine = create_engine(DATABASE_URL_SYNC, echo=True)
#     SQLModel.metadata.create_all(sync_engine)

# # Call once at startup
# init_db()

# # Session maker for async
# async_session_maker = async_sessionmaker(
#     bind=async_engine,
#     class_=AsyncSession,
#     expire_on_commit=False,
#     autoflush=False,
#     autocommit=False,
# )

# # Dependency
# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         try:
#             yield session
#         except Exception:
#             await session.rollback()
#             raise
#         finally:
#             await session.close()
