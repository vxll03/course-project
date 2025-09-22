from pydantic import Field, PositiveInt
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SECRET_KEY: str = Field(min_length=32)
    ACCESS_TOKEN_EXPIRE: PositiveInt = Field(default=15)
    REFRESH_TOKEN_EXPIRE: PositiveInt = Field(default=7)
    ALGORITHM: str = Field(default='HS256')

    IS_DEBUG: bool = Field(default=False)

    DB_HOST: str = Field(default='127.0.0.1')
    DB_PORT: int = Field(default=5432)
    DB_USER: str = Field(default='postgres')
    DB_PASS: str = Field(default='postgres')
    DB_NAME: str = Field(default='auth')

    @property
    def DATABASE_URL(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @property
    def SYNC_DATABASE_URL(self):
        return f'postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


settings = Settings()  # type: ignore
