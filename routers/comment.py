from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from auth.oauth2 import get_current_user
from db.database import get_db
from schemas.schemas import *
from db import db_comment


router = APIRouter(
    prefix='/comment',
    tags=['comment']
)

@router.post('/',)
def create(request:CommentBase,db:Session=Depends(get_db),current_user:UserAuth = Depends(get_current_user)):
    return db_comment.create(db,request)

@router.get('/all/{post_id}')
def comment (post_id:int,db:Session=Depends(get_db)):
    return db_comment.get_all_comments(db,post_id)