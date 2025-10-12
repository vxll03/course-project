from typing import Generic, Optional, Type, TypeVar
import httpx
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.repository.repository import (
    AuthorRepository,
    BookRepository,
    CategoryRepository,
    GenericRepository,
)
from app.repository.schemas import (
    AuthorReadSchema,
    BookReadSchema,
    CategoryReadSchema,
)
from app.repository.models import Author, Book, Category
from app.core.config import settings

T = TypeVar('T')


class GenericService(Generic[T]):
    def __init__(self, repo: 'GenericRepository[T]', model: Type[T]) -> None:
        self.__repo = repo
        self.__model = model

    def get_serializer(self, method: Optional[str] = None) -> Type[BaseModel]: ...

    async def get(self, id=None, limit=None, offset=None):
        if id:
            obj = await self.__repo.get(id)
            serialized_obj = self.get_serializer().model_validate(obj)
            return serialized_obj.model_dump()

        objs = await self.__repo.get_all(limit, offset)
        return [self.get_serializer().model_validate(obj).model_dump() for obj in objs]

    async def create(self, obj_schema: BaseModel):
        model_obj = self.__model(**obj_schema.model_dump())
        db_obj = await self.__repo.create(model_obj)
        return self.get_serializer().model_validate(db_obj).model_dump()

    async def update(self, obj_schema: BaseModel, id: int):
        db_schema = await self.__repo.update(
            id, obj_schema.model_dump(exclude_unset=True)
        )
        return self.get_serializer().model_validate(db_schema).model_dump()

    async def delete(self, id: int):
        await self.__repo.delete(id)


class BookService(GenericService[Book]):
    def __init__(self, db: AsyncSession, load_options=None) -> None:
        super().__init__(BookRepository(db, load_options), Book)

    def get_serializer(self, method: str | None = None) -> Type[BaseModel]:
        return BookReadSchema
    
    async def create(self, obj_schema: BaseModel):
        db_book = await super().create(obj_schema)
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(f'{settings.CHAT_URL}/chat/{db_book.get('title')}/')
                response.raise_for_status()
            except httpx.HTTPError as e:
                print(f"Ошибка HTTP: {e}")
        return db_book



class AuthorService(GenericService[Author]):
    def __init__(self, db: AsyncSession, load_options=None) -> None:
        super().__init__(AuthorRepository(db, load_options), Author)

    def get_serializer(self, method: str | None = None) -> Type[BaseModel]:
        return AuthorReadSchema


class CategoryService(GenericService[Category]):
    def __init__(self, db: AsyncSession, load_options=None) -> None:
        super().__init__(CategoryRepository(db, load_options), Category)

    def get_serializer(self, method: str | None = None) -> Type[BaseModel]:
        return CategoryReadSchema
