from fastapi import Request

from app.exceptions import (
    ChatDoesNotExistError
)
from app.utils import Response


def register_exceptions_handler(app):
    @app.exception_handler(ChatDoesNotExistError)
    async def user_does_not_exists_handler(
        request: Request, exc: ChatDoesNotExistError
    ):
        return Response(
            message='Something went wrong',
            status='error',
            status_code=404,
            content={'error': str(exc), 'data': {'username': exc.chat_id}},
        )