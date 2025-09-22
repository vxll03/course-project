from fastapi import FastAPI

from app.middleware import register_exceptions_handler
from .api.routes import router

app = FastAPI()
register_exceptions_handler(app)

app.include_router(router, prefix='/api', tags=['User'])