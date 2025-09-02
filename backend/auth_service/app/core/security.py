from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings
from app.exceptions import InvalidCredentialsException

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_token(data:dict, type: str):
    to_encode = data.copy()
    to_encode.update({'type': type})
    if type == 'access':
        to_encode.update({'exp': datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE)})
    else:
        to_encode.update({'exp': datetime.now(timezone.utc) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE)})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt

def decode_token(token):
    try:
        return jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise InvalidCredentialsException()