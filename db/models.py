from sqlalchemy import Column,String,Integer
from db.database import Base

class  DbUser(Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(64))
    email=Column(String(120),unique=True)
    password=Column(String)