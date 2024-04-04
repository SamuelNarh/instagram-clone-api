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
    
def update_like(post_id:int,request:LikeBase,db:Session):
    up_like=db.query(DbLike).filter(DbLike.post_id==post_id)
    up_like.update(
        {
            DbLike.total: request.total,
            DbLike.post_id: request.post_id,
        }
    )
    db.commit()
    return "ok"

def get_all(post_id:int,db:Session):
    Likes = db.query(DbLike).filter(DbLike.post_id==post_id).order_by(DbLike.id.desc()).first()
    return Likes