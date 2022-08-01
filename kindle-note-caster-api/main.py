from fastapi import FastAPI

from routers import post
#from routers import auth#, user  # revoir les relatives import pour ces 2

#ajouter le database.py et le config.py au commit

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel

from config import settings

from datetime import datetime
import time
app = FastAPI()

# pourquoi utiliser un router?: to split pour une meilleure organisation?
app.include_router(post.router)
#app.include_router(user.router)
#app.include_router(auth.router)

'''class Post(BaseModel):
    id: int
    created_at: datetime
    owner_id: int
    title: str'''

@app.get("/")
def root():
    return {"message": "Hello World"}

# connection la plus naturelle pour moi: passser par psycopg2 pour faire connect
while True:
    try:
        #conn = psycopg2.connect(host='localhost', port='5432',database='postgres', user='postgres', password='louis.debouzy', cursor_factory=RealDictCursor)
        conn = psycopg2.connect(host=settings.database_hostname, port=settings.database_port,database=settings.database_name, user=settings.database_username, password=settings.database_password, cursor_factory=RealDictCursor)
        #cursor factory: add an extra parameter pour lui dire d'aller chercher les colonnes car il ne le fait pas par lui meme
        #le database va matcher ce qui est en jaune
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error:", error)
        time.sleep(2)
       # break


