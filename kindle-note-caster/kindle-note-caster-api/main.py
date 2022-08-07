from fastapi import FastAPI
'''
from routers import post
from .routers import auth
from .routers import user  # revoir les relatives import pour ces 2
'''
#ajouter le database.py et le config.py au commit

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel

from routers.config import settings

from datetime import datetime
import time

from routers import post, user, auth

from routers.database import engine
from routers import models

models.Base.metadata.create_all(bind=engine) # cette ligne sert à gérer l'ORM de models et database

app = FastAPI()

# pourquoi utiliser un router?: to split pour une meilleure organisation?
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

'''class Post(BaseModel):
    id: int
    created_at: datetime
    owner_id: int
    title: str'''




# se poser la question du choix de la faire asynchrone ou non
@app.get("/")
def root():
    return {"message": "Hello World"}


