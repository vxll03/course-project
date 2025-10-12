from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.exceptions import ChatDoesNotExistError
from app.repository.models import Chat, Message


class Repository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def create_chat(self, chat_name):
        try:
            chat = Chat(name=chat_name)
            self.db.add(chat)
            await self.db.flush()
            await self.db.refresh(chat)
            return chat
        except Exception as e:
            logger.warning(f'Error occured while creating chat: {e}')
            raise

    async def append_message(self, user_id, chat_id, text):
        try:
            message = Message(text=text, author=user_id, chat_id=chat_id)
            self.db.add(message)
            await self.db.flush()
            await self.db.commit()
            return message
        except Exception as e:
            logger.warning(f'Error occured while appending message: {e}')
            raise

    async def get_chat(self, chat_name: str):
        query = await self.db.scalar(
            select(Chat)
            .where(Chat.name == chat_name)
            .options(joinedload(Chat.messages))
        )
        if not query:
            raise ChatDoesNotExistError(chat_name)
        return query
