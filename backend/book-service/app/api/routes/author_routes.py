from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.services import AuthorService
from app.core.database import get_db
from app.repository.schemas import AuthorCreateSchema, AuthorUpdateSchema
from app.utils import Response

author_router = APIRouter()

@author_router.get('/authors/')
async def get_all_authors(
    limit: int | None = None,
    offset: int | None = None,
    db: AsyncSession = Depends(get_db)
):
    service = AuthorService(db)
    authors = await service.get(limit, offset)
    return Response('authors successfully got', authors)


@author_router.get('/authors/{author_id}/')
async def get_author_by_id(author_id: int, db: AsyncSession = Depends(get_db)):
    service = AuthorService(db)
    author = await service.get(author_id)
    return Response('author successfully got', author)


@author_router.post('/authors/', status_code=201)
async def create_author(
    author: AuthorCreateSchema,
    db: AsyncSession = Depends(get_db),
):
    service = AuthorService(db)
    db_author = await service.create(author)
    return Response('author created', db_author, status_code=201)


@author_router.patch('/authors/{author_id}/')
async def update_author(
    author: AuthorUpdateSchema,
    author_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = AuthorService(db)
    db_author = await service.update(author, author_id)
    return Response('author updated', db_author)


@author_router.delete('/authors/{author_id}/')
async def delete_author(author_id: int, db: AsyncSession = Depends(get_db)):
    service = AuthorService(db)
    await service.delete(author_id)
    return Response('author deleted')
    