from sqlalchemy.orm.session import Session
from schemas.schemas import *
from db.models import DbPost
from datetime import datetime

def create_post(db:Session,request:PostBase):
    new_post=DbPost(
    image_url=request.image_url,
    image_url_type=request.image_url_type,
    caption=request.caption,
    creation=request.creation_id,
    timestamp= datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)