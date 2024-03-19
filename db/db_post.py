from fastapi import HTTPException,status
from sqlalchemy.orm.session import Session
from schemas.schemas import *
from db.models import DbPost
from datetime import datetime
from db.models import DbUser

def create_post(request:PostBase,db:Session):
    new_post=DbPost(
    image_url=request.image_url,
    image_url_type=request.image_url_type,
    caption=request.caption,
    timestamp= datetime.now(),
    user_id = request.creator_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all_post(db:Session):
    all_post=db.query(DbPost).all()
    return all_post

def delete_post(db:Session,id:int,user_id:int):
    # Gets all dbpost
    user_post= db.query(DbPost).filter(DbPost.id==id).first()
    if not user_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f'user with id {id} not found'
        )
    # Actual user that creates the post to delete #if (database.id) != auth_id
    if user_post.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail= "Only post creator can delete post"
        )
    db.delete(user_post)
    db.commit()
    return "ok"