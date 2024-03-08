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