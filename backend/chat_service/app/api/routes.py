from uuid import UUID, uuid1
from fastapi import APIRouter, Depends, Query, WebSocket, WebSocketDisconnect
from loguru import logger
from sqlalchemy import select

from app.api.services import ChatService, ConnectionManager
from app.core.database import get_db
from app.utils import Response

router = APIRouter()


def get_connection_manager() -> ConnectionManager:
    return ConnectionManager()


def get_service(db=Depends(get_db)) -> ChatService:
    return ChatService(db)


@router.get('/health_check/')
async def health_check(db=Depends(get_db)):
    if await db.scalar(select(1)):
        return Response('Service correctly working')


@router.post('/initialize/')
async def test_chat(service: ChatService = Depends(get_service)):
    chat = await service.create_chat('general')
    return Response('Chat created', chat, status_code=201)

@router.post('/{chat_name}/')
async def create_chat(chat_name: str, service: ChatService = Depends(get_service)):
    chat = await service.create_chat(chat_name)
    return Response('Chat created', chat, status_code=201)

@router.get('/history/{chat_name}')
async def get_history(chat_name: str, service: ChatService = Depends(get_service)):
    chat = await service.get_chat(chat_name)
    return Response('Chat history successfully loaded', chat)


@router.websocket('/connect/{chat_id}/')
async def websocket(
    websocket: WebSocket,
    chat_id: int,
    user_id: int | None = Query(None),
):
    await websocket.accept()
    if not user_id:
        user_id = -1

    async for session in get_db():
        service: ChatService = get_service(session)
        await ConnectionManager.connect(websocket, chat_id, user_id)

    try:
        while True:
            msg = await websocket.receive_text()
            db_msg = await service.append_message(user_id, chat_id, msg)
            await ConnectionManager.broadcast(chat_id, db_msg)
    except WebSocketDisconnect:
        logger.info(f'Client {user_id} disconnected from {chat_id}')
    finally:
        await ConnectionManager.disconnect(chat_id, user_id)
