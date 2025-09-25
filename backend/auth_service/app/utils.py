from datetime import datetime, timedelta, timezone
from typing import Any, Optional
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.repository.schemas import TokenPair


def Response(
    message: str = '',
    content: Optional[dict[str | int, Any]] = None,
    status: str = 'success',
    status_code: int = 200,
):
    """Returns JSONResponse instance with standart message

    Args:
        message (str, optional): General message
        content (Optional[dict[str | int, Any]], optional): Dictionary with any content
        status (str, optional): Status (success, error, warning, etc.)
        status_code (int, optional): Status code (200, 400, 500, 301, etc.)

    Returns:
        JSONResponse: Formatted JSONResponse instance
    """
    return JSONResponse(
        content={'status': status, 'message': message, 'content': content},
        status_code=status_code,
    )


def CookiesResponse(token: TokenPair, message: str, is_created=False):
    response = Response(message, status_code=201 if is_created else 200)
    response.set_cookie(
        key='access_token',
        value=token.access_token,
        max_age=settings.ACCESS_TOKEN_EXPIRE * 60,
        expires=datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE),
        httponly=not settings.IS_DEBUG,
    )
    if token.refresh_token:
        response.set_cookie(
            key='refresh_token',
            value=token.refresh_token,
            max_age=settings.REFRESH_TOKEN_EXPIRE * 60 * 60 * 24,
            expires=datetime.now(timezone.utc) + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE),
            httponly=not settings.IS_DEBUG,
        )
    return response
