from schemas.schemas import *
from sqlalchemy.orm.session import Session
from db.models import DbLike


def add_like(request:LikeBase,db:Session):
    liked= DbLike(
        total = request.total,
        post_id=request.post_id
    )
    db.add(liked)
    db.commit()
    db.refresh(liked)
    return liked
    

def get_all(post_id:int,db:Session):
    Likes = db.query(DbLike).filter(DbLike.post_id==post_id).first()
    return Likes