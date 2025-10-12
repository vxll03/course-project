from datetime import datetime, timezone

from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import get_password_hash
from app.exceptions import UserAlreadyExistsError
from app.repository.models import User
from app.repository.schemas import UserCreate


class Repository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def create_user(self, user: UserCreate):
        try:
            new_user = User(
                username=user.username,
                password=get_password_hash(user.password),
                latest_password_change=datetime.now(timezone.utc),
            )
            self.db.add(new_user)
            await self.db.flush()
            return new_user
        except IntegrityError:
            raise UserAlreadyExistsError(user.username)

    async def update_login_date(self, user):
        await self.db.execute(
            update(User)
            .where(User == user)
            .values(latest_password_change=datetime.now(timezone.utc))
        )

    async def get_user_by_username(self, username):
        return await self.db.scalar(select(User).where(User.username == username))

    async def get_users(self, offset: int):
        return await self.db.scalars(select(User).offset(offset).limit(50))

    async def get_user_by_id(self, id: int):
        return await self.db.scalar(select(User).where(User.id == id))