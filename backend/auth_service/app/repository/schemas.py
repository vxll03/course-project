from pydantic import BaseModel, Field, model_validator

# Authentication
class TokenPair(BaseModel):
    access_token: str
    refresh_token: str | None
    token_type: str

class UserCreate(BaseModel):
    username: str = Field(min_length=4, max_length=100)
    password: str = Field(min_length=8, max_length=100)
    password_repeat: str = Field(min_length=8, max_length=100)

    @model_validator(mode='after')
    def credentials_validate(self):
        if self.username == self.password:
            raise ValueError("Password and username can't match")
        return self
    
    @model_validator(mode='after')
    def validate_passworld(self):
        if self.password != self.password_repeat:
            raise ValueError("Passwords need to match")
        return self


class UserLogin(BaseModel):
    username: str
    password: str


class UserUpdatePassword(BaseModel):
    old_password: str
    new_password: str = Field(min_length=8, max_length=100)

    @model_validator(mode='after')
    def credentials_validate(self):
        if self.old_password == self.new_password:
            raise ValueError("Old and new password can't match")
        return self


class UserActivationChange(BaseModel):
    is_active: bool


class UserReadSchema(BaseModel):
    username: str

    class Config: 
        from_attributes = True

class CurrentUserReadSchema(UserReadSchema):
    id: int