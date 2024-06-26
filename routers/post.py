import random
import shutil
import string
from typing import List
from fastapi import APIRouter,Depends, File, HTTPException, UploadFile,status
from auth.oauth2 import get_current_user
from schemas.schemas import *
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_post


router= APIRouter(
    prefix="/post",
    tags=["post"]
)
image_url_types=['absolute','relative']

#For auth current_user:UserAuth = Depends(get_current_user)
@router.post('/',response_model=PostDisplay)
def create_post(request:PostBase,db:Session=Depends(get_db),current_user:UserAuth = Depends(get_current_user)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Parameter image_url_type can only take values 'absolute' or 'relative'"     
        )
    return db_post.create_post(request,db)

@router.get('/all',response_model=List[PostDisplay])
def get_all_post(db:Session=Depends(get_db)):
    return db_post.get_all_post(db)


# This allows us to upload images locally to access it
#Static image file store
@router.post('/image')
def upload_image(image:UploadFile=File(...),current_user:UserAuth = Depends(get_current_user)):
    letters=string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(5))
    new = f'_{rand_str}.'
    filename= new.join(image.filename.rsplit('.',1))
    path = f'images/{filename}'
    
    with open(path,"w+b") as buffer:
        shutil.copyfileobj(image.file,buffer)
    return {'filename': path}
    
@router.delete('/delete/{id}') 
def delete_post(id:int, db:Session=Depends(get_db),current_user:UserAuth = Depends(get_current_user)):
    return db_post.delete_post(db,id,current_user.id) 