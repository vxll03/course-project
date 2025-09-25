from datetime import date
from typing import List
from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class IdMixin:
    id: Mapped[int] = mapped_column(Integer, primary_key=True)


class Author(Base, IdMixin):
    __tablename__ = 'author'

    last_name: Mapped[str] = mapped_column(String(100))
    first_name: Mapped[str] = mapped_column(String(100))
    second_name: Mapped[str] = mapped_column(String(100))
    
    books: Mapped[List['Book']] = relationship()


class Category(Base, IdMixin):
    __tablename__ = 'category'

    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000))

    books: Mapped[List['Book']] = relationship()


class Book(Base, IdMixin):
    __tablename__ = 'book'

    author: Mapped['Author'] = relationship(back_populates='books')
    author_id: Mapped[int] = mapped_column(ForeignKey('author.id'))
    
    category: Mapped['Category'] = relationship(back_populates='books')
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))
    
    title: Mapped[str] = mapped_column(String(300))
    created: Mapped[date] = mapped_column(Date)
    age_restriction: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(1000))
