from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.book_routes import book_router
from app.api.routes.category_routes import category_router
from app.api.routes.author_routes import author_router
from app.middleware import register_exceptions_handler

app = FastAPI()
register_exceptions_handler(app)

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book_router, prefix='/bookshop', tags=['Books'])
app.include_router(category_router, prefix='/bookshop', tags=['Categories'])
app.include_router(author_router, prefix='/bookshop', tags=['Authors'])
