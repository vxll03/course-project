from typing import Generic, List, Sequence, TypeVar, Type, Optional
from venv import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.exceptions import NotFoundException
from app.repository.models import Author, Book, Category


T = TypeVar('T')  # Generic for ORM model


class GenericRepository(Generic[T]):
    def __init__(
        self,
        db: AsyncSession,
        model: Type[T],
        load_options: Optional[List[str]],
    ) -> None:
        self.db = db
        self.model = model
        self.load_options = load_options

    async def get(self, id: int) -> T:
        query = select(self.model).where(self.model.id == id)
        opts = [
            selectinload(getattr(self.model, opt)) for opt in (self.load_options or [])
        ]
        query = query.options(*opts)

        obj = await self.db.scalar(query)
        if not obj:
            raise NotFoundException(f'{self.model.__name__} with id {id} not found')
        return obj

    async def get_all(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Sequence[T]:
        query = select(self.model).offset(offset).limit(limit)
        opts = [
            selectinload(getattr(self.model, opt)) for opt in (self.load_options or [])
        ]
        query = query.options(*opts)

        objs = await self.db.scalars(query)
        if not objs:
            raise NotFoundException(f'{self.model.__name__} not found')
        return objs.all()

    async def create(self, obj: T) -> T:
        self.db.add(obj)
        await self.db.flush()
        await self.db.refresh(obj, attribute_names=self.load_options)
        return obj

    async def update(self, id: int, update_data: dict) -> T:
        obj = await self.get(id)
        for k, v in update_data.items():
            setattr(obj, k, v)
        await self.db.flush()
        await self.db.refresh(obj, attribute_names=self.load_options)
        return obj

    async def delete(self, id: int) -> None:
        obj = await self.get(id)
        await self.db.delete(obj)
        await self.db.flush()


# Initializing repos
class BookRepository(GenericRepository[Book]):
    def __init__(self, db: AsyncSession, load_options) -> None:
        super().__init__(db, Book, load_options)


class AuthorRepository(GenericRepository[Author]):
    def __init__(self, db: AsyncSession, load_options) -> None:
        super().__init__(db, Author, load_options)


class CategoryRepository(GenericRepository[Category]):
    def __init__(self, db: AsyncSession, load_options) -> None:
        super().__init__(db, Category, load_options)
