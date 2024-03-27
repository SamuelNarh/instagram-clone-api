from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship

class  DbUser(Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(64))
    email=Column(String(120),unique=True)
    password=Column(String)
    #Relationship
    items= relationship('DbPost',back_populates='user')
    
    
class DbPost(Base):
    __tablename__="post"
    id=Column(Integer,primary_key=True,index=True)
    image_url=Column(String)
    image_url_type=Column(String)
    caption=Column(String)
    timestamp=Column(DateTime)
    user_id= Column(Integer,ForeignKey("user.id"))
    #Relationship
    user= relationship('DbUser',back_populates='items')
    comments = relationship('DbComment',back_populates='post')
    like = relationship('DbLike',back_populates='post')
    

class DbComment(Base):
    __tablename__='comment'
    id=Column(Integer,primary_key=True,index=True)
    text=Column(String)
    username=Column(String)
    timestamp=Column(DateTime)
    post_id=Column(Integer,ForeignKey("post.id"))
    post = relationship("DbPost",back_populates='comments')
    
class DbLike(Base):
    __tablename__='like'
    id=Column(Integer,primary_key=True,index=True)
    total=Column(Integer)
    post_id=Column(Integer,ForeignKey("post.id"))
    post = relationship("DbPost",back_populates='like')
    