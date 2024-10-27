from datetime import timedelta, datetime, UTC
from typing import Optional

from jose import JWTError, jwt
from dns.dnssecalgs import algorithms
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from src.server.datasource.serializers import serialize_datetime

SECRET_KEY: str = "our_secret_key" # TODO(MANAGE AN ACTUAL KEY)
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 20

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") #   serverUrl/token

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)) -> Optional[str]:
    to_encode = data.copy()
    expire = serialize_datetime(datetime.now(UTC) + expires_delta)
    to_encode.update({"expires": expire})
    try:
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    except JWTError:
        return # TODO()
    return encoded_jwt