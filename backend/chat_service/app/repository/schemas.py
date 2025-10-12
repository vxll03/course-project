from datetime import datetime
from pydantic import BaseModel, Field, field_serializer

class Message(BaseModel):
    id: int
    text: str
    timestamp: datetime
    author: int
    type: str = Field('user_message')

    @field_serializer('timestamp')
    def convert_datetime_8601(self, value: datetime, _info):
        return value.strftime('%Y.%m.%d %H:%M')

    class Config:
        from_attributes = True

class Chat(BaseModel):
    id: int
    name: str
    messages: list['Message']

    class Config:
        from_attributes = True