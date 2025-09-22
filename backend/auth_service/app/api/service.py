from app.core.security import (
    create_token,
    decode_token,
    verify_password,
)
from app.exceptions import InvalidCredentialsException, UserDoesNotExistError
from app.repository.repository import Repository
from app.repository.schemas import TokenPair


class UserService:
    def __init__(self, db) -> None:
        self.db = db
        self.repo = Repository(db)

    async def generate_token(self, id, username, refresh=False) -> TokenPair:
        access_token = create_token({'id': id, 'username': username}, 'access')
        refresh_token = None
        if refresh:
            refresh_token = create_token({'id': id, 'username': username}, 'refresh')

        return TokenPair(
            access_token=access_token,
            refresh_token=refresh_token if refresh_token else None,
            token_type='bearer',
        )

    async def create_user(self, user) -> TokenPair:
        db_user = await self.repo.create_user(user)
        await self.repo.update_login_date(db_user)
        return await self.generate_token(db_user.id, db_user.username, True)

    async def login(self, user) -> TokenPair:
        db_user = await self.repo.get_user_by_username(user.username)
        if not db_user or db_user.is_active is False:
            raise UserDoesNotExistError(
                user.username, 'User does not exists or inactive'
            )
        if not verify_password(user.password, db_user.password):
            raise InvalidCredentialsException(user.username)

        await self.repo.update_login_date(db_user)
        return await self.generate_token(db_user.id, db_user.username, True)

    async def refresh(self, token) -> TokenPair:
        db_user = await self.validate_token(token, 'refresh')
        return await self.generate_token(db_user.id, db_user.username)

    async def validate_token(self, token, token_type: str):
        if not token:
            raise InvalidCredentialsException(message='Token not found')
        data = decode_token(token)
        if (
            not data.get('username')
            or not data.get('id')
            or data.get('type') != token_type
        ):
            raise InvalidCredentialsException()

        db_user = await self.repo.get_user_by_username(data.get('username'))
        if not db_user:
            raise InvalidCredentialsException(message='User not found')

        return db_user
