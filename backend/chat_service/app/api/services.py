from fastapi import WebSocket
from loguru import logger

from app.repository.repository import Repository
from app.repository.schemas import Message

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

    async def broadcast(self, chat_id: int, msg: Message):
        users_ws = active_connections.get(chat_id)
        if not users_ws:
            return
        for _, ws in users_ws.items():
            await ws.send_json(msg.model_dump_json())


class ChatService:
    def __init__(self, db) -> None:
        self.__db = db
        self.repo = Repository(self.__db)

    async def get_chat(self, chat_id) -> list[Message]:
        messages = await self.repo.get_chat_messages(chat_id)
        return [Message.model_validate(msg) for msg in messages]

    async def append_message(self, user_id, chat_id, text) -> Message:
        msg = await self.repo.append_message(user_id, chat_id, text)
        return Message.model_validate(msg)
