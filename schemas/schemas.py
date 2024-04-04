from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserBase(BaseModel):
    username:str
    email:str
    password:str
    
class UserDisplay(BaseModel):
    username:str
    email:str
    class Config():
        from_attributes=True
    
#for post display    
class User(BaseModel):
    username:str
    class Config():
        from_attributes=True
        
class Comment(BaseModel):
    id:int
    text:str
    username:str
    timestamp:datetime
    class Config():
        from_attributes=True
        

class LikeDisplay(BaseModel):
    id:int
    post_id:int
    total:int
    
    class Config():
        from_attributes=True
    
class PostBase(BaseModel):
    image_url:str
    image_url_type:str
    caption:str
    creator_id:int
    
class PostDisplay(BaseModel):
    id:int
    image_url:str
    image_url_type:str
    caption:str
    timestamp:datetime
    user:User
    # Display the comments
    comments:List[Comment]
    #Display the Likes
    like:List[LikeDisplay]
    class Config():
        from_attributes=True
        
#Data that will be pass to any method that requires authentication     
class UserAuth(BaseModel):
    id:int
    username:str
    email:str
    
class CommentBase(BaseModel):
    username:str
    text:str
    post_id:int
    
class LikeBase(BaseModel):
    total:int
    post_id:int
    