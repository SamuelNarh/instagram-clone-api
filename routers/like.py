from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from auth.oauth2 import get_current_user
from db.database import get_db
from schemas.schemas import LikeBase,LikeDisplay,UserAuth
from db import db_like

router=APIRouter(
    prefix='/like',
    tags=['like']
)

@router.post('/')
def add_like(request:LikeBase,db:Session=Depends(get_db),current_user:UserAuth = Depends(get_current_user)):
    return db_like.add_like(request,db)


#Get all likes
@router.get('/all/{post_id}')
def all_likes(post_id:int,db:Session=Depends(get_db)):
    return db_like.get_all(post_id,db)