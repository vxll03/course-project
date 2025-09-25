from fastapi import Request

from app.exceptions import (
    InvalidCredentialsException,
    UserAlreadyExistsError,
    UserDoesNotExistError,
)
from app.utils import Response


def register_exceptions_handler(app):
    @app.exception_handler(UserAlreadyExistsError)
    async def user_already_exists_handler(
        request: Request, exc: UserAlreadyExistsError
    ):
        return Response(
            message='Something went wrong',
            status='error',
            status_code=403,
            content={
                'error': str(exc),
                'data': {'username': exc.username},
            },
        )

    @app.exception_handler(UserDoesNotExistError)
    async def user_does_not_exists_handler(
        request: Request, exc: UserDoesNotExistError
    ):
        return Response(
            message='Something went wrong',
            status='error',
            status_code=404,
            content={'error': str(exc), 'data': {'username': exc.username}},
        )

    @app.exception_handler(InvalidCredentialsException)
    async def invalid_credentials_handler(request: Request, exc: UserDoesNotExistError):
        return Response(
            message='Something went wrong that raise InvalidCredentialsException',
            status='error',
            status_code=401,
            content={
                'error': str(exc),
                'data': {'username': exc.username} if exc.username else None,
            },
        )
