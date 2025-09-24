from datetime import datetime
from pydantic import BaseModel, Field, field_serializer

class Message(BaseModel):
    text: str
    timestamp: datetime
    author: int
    type: str = Field('user_message')

    @field_serializer('timestamp')
    def convert_datetime_8601(self, value: datetime, _info):
        return value.strftime('%Y-%m-%dT%H:%M:%SZ')

    class Config:
        from_attributes = True