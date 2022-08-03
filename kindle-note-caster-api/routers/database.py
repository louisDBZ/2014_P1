from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import psycopg2
from psycopg2.extras import RealDictCursor

import time

from .config import settings

# tout ceci est du copier coller de la doc
#https://fastapi.tiangolo.com/tutorial/sql-databases/?h=sql+%28relational%29+databases

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# définition de cette fonction: à copier coller aussi de la doc pour la gestion des dépendances
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

'''
# connection la plus naturelle pour moi: passser par psycopg2 pour faire connect
while True:
    try:
        #conn = psycopg2.connect(host='localhost', port='5432',database='postgres', user='postgres', password='louis.debouzy', cursor_factory=RealDictCursor)
        conn = psycopg2.connect(host=settings.database_hostname, port=settings.database_port,database=settings.database_name, user=settings.database_username, password=settings.database_password, cursor_factory=RealDictCursor)
        #cursor factory: add an extra parameter pour lui dire d'aller chercher les colonnes car il ne le fait pas par lui meme
        #le database va matcher ce qui est en jaune
        cursor = conn.cursor() #curso sert à gérer les colonnes
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error:", error)
        time.sleep(2)
       # break



'''