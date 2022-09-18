from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from ..main import logger
from .config import settings

# this is mainly a copy paste from the doc
# https://fastapi.tiangolo.com/tutorial/sql-databases/?h=sql+%28relational%29+databases

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def compute_max_post_next():
    try:
        with engine.connect() as con:
            result = con.execute("""select coalesce(max(post_id),0)+1 as o_id from posts""")
            for row in result:
                return int(row['o_id'])

    except Exception as error:
        #logger.error("Connecting to database failed")
        #logger.error("Error:", error)
        print("Connecting to database failed")
        print("Error:", error)


def compute_max_user_next():
    try:
        with engine.connect() as con:
            result = con.execute("""select coalesce(max(user_id),0)+1 as o_id from users""")
            for row in result:
                return int(row['o_id'])

    except Exception as error:
        #logger.error("Connecting to database failed")
        #logger.error("Error:", error)
        print("Connecting to database failed")
        print("Error:", error)

'''
while True:
    try:
        conn = psycopg2.connect(host=settings.database_hostname, port=settings.database_port,database=settings.database_name, user=settings.database_username, password=settings.database_password, cursor_factory=RealDictCursor)
        #cursor factory (extra parameter) :  to seak in the rows because it is not done naturally 
        #cursor to manage the rows 
        cursor = conn.cursor() 
        print("Database connection was succesfull!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error:", error)
        time.sleep(2)
       # break
'''