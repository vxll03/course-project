from fastapi import Request
from app.exceptions import NotFoundException
from app.utils import Response


def register_exceptions_handler(app):
    @app.exception_handler(NotFoundException)
    async def not_dound_excpetion_handler(request: Request, exc: NotFoundException):
        return Response(
            message='Something went wrong',
            status='error',
            status_code=404,
            content={'error': str(exc)},
        )
