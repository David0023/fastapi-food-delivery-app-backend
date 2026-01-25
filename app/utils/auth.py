import jwt
from pwdlib import PasswordHash
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, ValidationError
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import Dict

from app.core.config import settings
from app.utils.database import get_db
from app.models.users.user import User

pwd_context = PasswordHash.recommended()

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    # User identifier: username
    sub: str
    # User Type
    role: str
    iat: int
    exp: int

def create_access_token(
    username: str,
    role: str,
) -> str:
    exp = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {
        "sub": username,
        "role": role,
        "iat": int(datetime.now(timezone.utc).timestamp()),
        "exp": int(exp.timestamp()),
    }
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def decode_token(token: str) -> TokenData:
    if not token:
        raise credentials_exception

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return TokenData(
            sub=payload.get("sub"),
            role=payload.get("role"),
            iat=payload.get("iat"),
            exp=payload.get("exp"),
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired", headers={"WWW-Authenticate": "Bearer"})
    except jwt.PyJWTError:
        raise credentials_exception
    except ValidationError:
        raise credentials_exception

def authenticate_user(
    username: str,
    password: str,
    db: Session
) -> User:
    """
    Authenticate user by searching user table.
    """
    # This is fast because username is indexed in each table
    user = db.query(User).filter(User.username == username).first()

    if not user:
        return False

    if not pwd_context.verify(password, user.hashed_password):
        return False

    return user

def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth_scheme)
) -> User:
    token_data = decode_token(token)

    user = db.query(User).filter(and_(User.username == token_data.sub, User.role == token_data.role)).first()
    if user is None:
        raise credentials_exception
    return user

def hash_password_inside(data: Dict) -> Dict | None:
    if not 'password' in data:
        return None
    data["hashed_password"] = get_password_hash(data.pop("password"))
    return data