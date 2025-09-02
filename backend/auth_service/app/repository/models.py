from datetime import date
from enum import Enum as PyEnum
from sqlalchemy import Boolean, Date, Enum, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Role(PyEnum):
    USER = 'User'
    ADMIN = 'Admin'

class IdMixin:
    id: Mapped[int] = mapped_column(primary_key=True)

class User(Base, IdMixin):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(Text)
    role: Mapped[Role] = mapped_column(Enum(Role), default=Role.USER)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    latest_login: Mapped[date | None] = mapped_column(Date)
    latest_password_change: Mapped[date | None] = mapped_column(Date)
