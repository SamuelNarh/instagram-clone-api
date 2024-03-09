from fastapi.param_functions import Depends
from fastapi.security.oauth2 import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError
from sqlalchemy.orm import Session
from db.database import get_db
from fastapi import HTTPException, status
from db import db_user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = '843f0f26c9413f7ffcfb55e08d69d010455d4595705ac2a7f327dd8fa8a0b4b5'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
  credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Could not validate credentials',
    headers={"WWW-Authenticate": "Bearer"}
  )
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    #authenticate username
    username: str = payload.get("sub")
    if username is None:
      raise credentials_exception
  except JWTError:
    raise credentials_exception
  
  user = db_user.get_user_by_username(db, username=username)

  if user is None:
    raise credentials_exception

  return user
