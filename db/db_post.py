from sqlalchemy.orm.session import Session
from schemas.schemas import *
from db.models import DbPost
from datetime import datetime

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