from fastapi import FastAPI
from db import models
from db.database import engine
from routers import user,post,comment
from fastapi.staticfiles import StaticFiles
from auth import authentication
#Midddleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get('/')
def hello():
    return  {'message': 'Hello World'}


app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(authentication.router)

#Model Registration
models.Base.metadata.create_all(engine) 

app.mount('/images', StaticFiles(directory='images'), name='images')



#Middleware
origin =[
'https://samuelnarh.github.io'
]
app.add_middleware(
CORSMiddleware,
allow_origins=origin,
allow_credentials=True,
allow_methods=['*'],
allow_headers=['*']
)