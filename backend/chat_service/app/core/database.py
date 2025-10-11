from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from .config import settings

engine = create_async_engine(url=settings.DATABASE_URL)

async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    pass


async def get_db():
    """
    Function generator that yields async session
    """
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception as ex:
            await session.rollback()
            logger.error(f'Error in AsyncSession: {ex}')
            raise
        finally:
            await session.close()


# async def get_redis():
#     try:
#         session = redis.from_url(settings.REDIS_URL, encoding='utf-8', decode_responses=True)
#         yield session
#     except Exception as ex:
#         logger.warning(f'Error with redis occured: {ex}')
#         raise
#     finally:
#         await session.close()

