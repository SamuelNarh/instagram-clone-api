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
    
    