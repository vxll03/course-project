from fastapi import WebSocket
from loguru import logger

from app.repository.repository import Repository
from app.repository.schemas import Chat, GetChatSchema, Message

"""
{
    chat_id: {
        user_id: websocket
    }
}
"""
active_connections: dict[int, dict[int, WebSocket]] = {}


class ConnectionManager:
    async def connect(self, websocket: WebSocket, chat_id: int, user_id: int):
        chat_conn = active_connections.get(chat_id)
        if not chat_conn:
            active_connections[chat_id] = {}
            chat_conn = active_connections[chat_id]

        chat_conn[user_id] = websocket
        logger.info(f'Users in chat: {chat_conn}')

    async def disconnect(self, chat_id: int, user_id: int):
        chat_conn = active_connections.get(chat_id)
        if not chat_conn:
            return

        del chat_conn[user_id]

    async def broadcast(self, chat_id: int, msg: dict):
        users_ws = active_connections.get(chat_id)
        if not users_ws:
            return
        for _, ws in users_ws.items():
            await ws.send_json(msg)


class ChatService:
    def __init__(self, db) -> None:
        self.__db = db
        self.repo = Repository(self.__db)

    async def create_chat(self, name) -> dict:
        chat = await self.repo.create_chat(name)
        return Chat.model_validate(chat).model_dump()

    async def get_chat(self, chat_name: GetChatSchema) -> dict:
        chat = await self.repo.get_chat(chat_name.name)
        return Chat.model_validate(chat).model_dump()

    async def append_message(self, user_id, chat_id, text) -> dict:
        msg = await self.repo.append_message(user_id, chat_id, text)
        return Message.model_validate(msg).model_dump()
