from fastapi import APIRouter, Depends, Request
from loguru import logger
from sqlalchemy import select

from app.api.service import UserService
from app.core.database import get_db
from app.repository.schemas import UserCreate, UserLogin
from app.utils import CookiesResponse, Response

router = APIRouter()


def get_service(db=Depends(get_db)) -> UserService:
    return UserService(db)


# user=Depends(authenticate)
async def authenticate(request: Request, db=Depends(get_db)):
    return await UserService(db).validate_token(
        request.cookies.get('access_token'), 'access'
    )


@router.get('/health_check/')
async def health_check(db=Depends(get_db)):
    if await db.scalar(select(1)):
        return Response(message='Service correctly working')


@router.get('/users/me/')
async def get_current_user(request: Request, service: UserService = Depends(get_service)):
    user = await service.get_current_user(request.cookies.get('access_token'))
    return Response('Current user successfully gotten', user)


@router.get('/users/{id}')
async def get_user_by_id(id: int, service: UserService = Depends(get_service)):
    user = await service.get_user(id)
    return Response('User sucessfully gotten', user)


@router.post('/register/', status_code=201)
async def register(user: UserCreate, service: UserService = Depends(get_service)):
    """Регистрация пользователя"""
    token = await service.create_user(user)
    return CookiesResponse(token, 'Registered successfully', True)


@router.post('/token/create/')
async def login(user: UserLogin, service: UserService = Depends(get_service)):
    """Аутентификация пользователя"""
    token = await service.login(user)
    return CookiesResponse(token, 'Logged in successfully')


@router.post('/token/refresh/')
async def refresh(request: Request, service: UserService = Depends(get_service)):
    """Обновление Access токена в куках по Refresh валидному токену"""
    refresh_token = request.cookies.get('refresh_token')
    logger.info(refresh_token)
    token = await service.refresh(refresh_token)
    return CookiesResponse(token, 'Access token refreshed successfully')


@router.post('/token/delete/')
async def logout():
    """Выход пользователя => Удаление токенов из кук"""
    response = Response(message='Logged out successfully')
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    return response
