from datetime import datetime
from typing import List
from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class IdMixin:
    id: Mapped[int] = mapped_column(primary_key=True)


class Chat(Base, IdMixin):
    __tablename__ = 'chat'

    name: Mapped[str] = mapped_column(String(300))
    messages: Mapped[List['Message']] = relationship()


class Message(Base, IdMixin):
    __tablename__ = 'message'

    text: Mapped[str] = mapped_column(String(300))
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    author: Mapped[int] = mapped_column(Integer)

    chat_id: Mapped[int] = mapped_column(ForeignKey('chat.id'))
    chat: Mapped['Chat'] = relationship(back_populates='messages')