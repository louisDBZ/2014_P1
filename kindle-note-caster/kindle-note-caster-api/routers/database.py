from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import psycopg2
from psycopg2.extras import RealDictCursor

import time
from ast import literal_eval
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

#méthode barbare pour la gestion des indexes
# ne s'incremente pas automatiquement et besoin de valeur par défault, ne pas passer par new_user.user_id
#https://docs.sqlalchemy.org/en/14/core/defaults.html
# a régler car à chaque fois repart de 1


with engine.connect() as con:
    quser = con.execute("""SELECT  max(user_id) FROM users """)
    qposts = con.execute("""select max(post_id) from posts""")

for row in quser:
    #<class 'sqlalchemy.engine.row.LegacyRow'>, conversion dégueue mais rapide car pas de get?
    if literal_eval(str(row))[0] is not None:
        id_user= literal_eval(str(row))[0]
    else:
        id_user=1

for row in qposts:
    if literal_eval(str(row))[0] is not None:
        id_post= literal_eval(str(row))[0]
    else:
        id_post=1


def mydefault_post():
    global id_post
    id_post += 1
    return id_post

def mydefault_user():
    global id_user
    id_user += 1
    return id_user




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