from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.repository.models import Chat, Message


class Repository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def create_chat(self, chat_name):
        try:
            chat = Chat(name=chat_name)
            self.db.add(chat)
            await self.db.flush()
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
    
    async def get_chat_messages(self, chat_id):
        chat = await self.db.scalars(select(Chat))
        print([ch.id for ch in chat.all()])

        messages = await self.db.scalars(select(Message).where(Message.chat_id==chat_id))   
        return messages.all()
