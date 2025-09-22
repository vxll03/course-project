from typing import Generator
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
    def __str__(self) -> str:
        cols = {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }
        return f'{self.__name__}: {cols}'


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
