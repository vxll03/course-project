from fastapi import FastAPI
from app.api.routes import router
from app.middleware import register_exceptions_handler

app = FastAPI()
register_exceptions_handler(app)

app.include_router(router, prefix='/chat')
