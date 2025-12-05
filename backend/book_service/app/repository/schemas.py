from datetime import date
from typing import Optional
from pydantic import BaseModel, field_serializer

# Author Schemas
class AuthorBaseSchema(BaseModel):
    last_name: str
    first_name: str
    second_name: str
    class Config:
        from_attributes = True

class AuthorReadSchema(AuthorBaseSchema):
    id: int

class AuthorCreateSchema(AuthorBaseSchema):
    pass

class AuthorUpdateSchema(AuthorBaseSchema):
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    second_name: Optional[str] = None



# Category Schemas
class CategoryBaseSchema(BaseModel):
    name: str
    description: str
    class Config:
        from_attributes = True

class CategoryReadSchema(CategoryBaseSchema):
    id: int

class CategoryCreateSchema(CategoryBaseSchema):
    pass

class CategoryUpdateSchema(CategoryBaseSchema):
    name: Optional[str] = None
    description: Optional[str] = None




# Book Schemas
class BookBaseSchema(BaseModel):
    title: str
    description: str
    created: date
    age_restriction: int
    class Config:
        from_attributes = True

class BookReadSchema(BookBaseSchema):
    id: int
    author: AuthorReadSchema
    category: CategoryReadSchema
    
    @field_serializer('created')
    def convert_date_8601(
        self,
        value: date,
    ) -> str:
        return value.isoformat()

    @field_serializer('age_restriction')
    def convert_restriction(self, value: int) -> str:
        return f'{value}+' if value else '0+'

class BookCreateSchema(BookBaseSchema):
    category_id: int
    author_id: int

class BookUpdateSchema(BookBaseSchema):
    title: Optional[str] = None
    description: Optional[str] = None
    created: Optional[date] = None
    age_restriction: Optional[int] = None
    category_id: Optional[int] = None
    author_id: Optional[int] = None
