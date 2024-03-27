from fastapi import FastAPI
from db import models
from db.database import engine
from routers import user,post,comment,like
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
app.include_router(like.router)

#Model Registration
models.Base.metadata.create_all(engine) 

app.mount('/images', StaticFiles(directory='images'), name='images')



#Middleware
origin =[
'http://localhost:3000',
"https://samuelnarh.github.io",
'http://172.20.10.5:3000'
]
app.add_middleware(
CORSMiddleware,
allow_origins=origin,
allow_credentials=True,
allow_methods=['*'],
allow_headers=['*']
)