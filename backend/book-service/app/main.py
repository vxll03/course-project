from fastapi import FastAPI
from app.api.routes.book_routes import book_router
from app.api.routes.category_routes import category_router
from app.api.routes.author_routes import author_router
from app.middleware import register_exceptions_handler

app = FastAPI()
register_exceptions_handler(app)

app.include_router(book_router, prefix='/bookshop', tags=['Books'])
app.include_router(category_router, prefix='/bookshop', tags=['Categories'])
app.include_router(author_router, prefix='/bookshop', tags=['Authors'])