from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.services import BookService
from app.core.database import get_db
from app.repository.schemas import BookCreateSchema, BookUpdateSchema
from app.utils import Response_503, Response

book_router = APIRouter()

@book_router.get('/health_check/')
async def health_check(db: AsyncSession = Depends(get_db)):
    if await db.scalar(select(1)) == 1:
        return Response('Service correctly work')
    return Response_503()


@book_router.get('/books/')
async def get_all_books(
    limit: Optional[int] = None,
    offset: Optional[int] = None,
    db: AsyncSession = Depends(get_db)
):
    service = BookService(db, ['author', 'category'])
    books = await service.get(limit, offset)
    return Response('Books successfully got', books)


@book_router.get('/books/{book_id}/')
async def get_book_by_id(book_id: int, db: AsyncSession = Depends(get_db)):
    service = BookService(db, ['author', 'category'])
    book = await service.get(book_id)
    return Response('Book successfully got', book)


@book_router.post('/books/', status_code=201)
async def create_book(
    book: BookCreateSchema,
    db: AsyncSession = Depends(get_db),
):
    service = BookService(db, ['author', 'category'])
    db_book = await service.create(book)
    return Response('Book created', db_book, status_code=201)


@book_router.patch('/books/{book_id}/')
async def update_book(
    book: BookUpdateSchema,
    book_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = BookService(db, ['author', 'category'])
    db_book = await service.update(book, book_id)
    return Response('Book updated', db_book)


@book_router.delete('/books/{book_id}/')
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)):
    service = BookService(db, ['author', 'category'])
    await service.delete(book_id)
    return Response()
    