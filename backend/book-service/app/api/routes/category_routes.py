from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.services import CategoryService
from app.core.database import get_db
from app.repository.schemas import CategoryCreateSchema, CategoryUpdateSchema
from app.utils import Response

category_router = APIRouter()

@category_router.get('/categories/')
async def get_all_categories(
    limit: int | None = None,
    offset: int | None = None,
    db: AsyncSession = Depends(get_db)
):
    service = CategoryService(db)
    categories = await service.get(limit, offset)
    return Response('categories successfully got', categories)


@category_router.get('/categories/{category_id}/')
async def get_category_by_id(category_id: int, db: AsyncSession = Depends(get_db)):
    service = CategoryService(db)
    categories = await service.get(category_id)
    return Response('category successfully got', categories)


@category_router.post('/categories/', status_code=201)
async def create_category(
    category: CategoryCreateSchema,
    db: AsyncSession = Depends(get_db),
):
    service = CategoryService(db)
    db_category = await service.create(category)
    return Response('category created', db_category, status_code=201)


@category_router.patch('/categories/{category_id}/')
async def update_category(
    category: CategoryUpdateSchema,
    category_id: int,
    db: AsyncSession = Depends(get_db),
):
    service = CategoryService(db)
    db_category = await service.update(category, category_id)
    return Response('category updated', db_category)


@category_router.delete('/categories/{category_id}/')
async def delete_category(category_id: int, db: AsyncSession = Depends(get_db)):
    service = CategoryService(db)
    await service.delete(category_id)
    return Response()
    