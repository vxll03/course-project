from typing import Any
from fastapi.responses import JSONResponse

def Response(
message: str = '',
content = None,
status: str = 'success',
status_code: int = 200,
):
    """Returns JSONResponse instance with standart message

    Args:
        message (str, optional): General message
        content (Any): Dictionary with any content
        status (str, optional): Status (success, error, warning, etc.)
        status_code (int, optional): Status code (200, 400, 500, 301, etc.)

    Returns:
        JSONResponse: Formatted JSONResponse instance
    """
    return JSONResponse(
        content={'status': status, 'message': message, 'content': content},
        status_code=status_code,
    )

def Response_503():
    return Response('Database connection cannot be established')

