from fastapi import FastAPI
from db import models
from db.database import engine
from routers import user

app = FastAPI()

@app.get('/')
def hello():
    return  {'message': 'Hello World'}


app.include_router(user.router)

#Model Registration
models.Base.metadata.create_all(engine) 
