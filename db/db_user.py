from fastapi import HTTPException,status
from schemas.schemas import UserBase
from sqlalchemy.orm.session import Session
from db.models import *
from hashing import Hash

def create_user(request:UserBase,db:Session):
    new_user= DbUser(
        username= request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


#Implementing the function to authenticate

def get_user_by_username(db:Session,username:str):
    user = db.query(DbUser).filter(DbUser.username==username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with username {username} Not Found"
        )
    return user
        