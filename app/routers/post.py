from fastapi import APIRouter, UploadFile,File, HTTPException, Depends
from fastapi.responses import StreamingResponse
from .note_caster import process_csv_to_docx,extract_Title
#from ..main import logger
from .config import settings
import psycopg2
from psycopg2.extras import RealDictCursor

import datetime

from .database import compute_max_post_next
from . import oauth2

o_chemin_du_word = "The_Customer_Success_Professionals_Handbook.docx"

router = APIRouter(
    prefix="/file",
    tags=['File']
)

@router.post("/")
async def upload_file(file: UploadFile = File(...), current_user: int = Depends(oauth2.get_current_user)):

    def iterfile():
        with open(o_chemin_du_word, mode="rb") as file_like:
            yield from file_like

    # check the MIME type (example: image/jpeg)

    if file.content_type not in ['text/csv']:
        raise HTTPException(status_code=406, detail="Please upload only .csv files")

    with open(file.filename, "wb+") as file_object:
        file_object.write(file.file.read())

    # need a calibration with the o_chemin_du_word and

    process_csv_to_docx(file.filename,o_chemin_du_word)

    # upload a trace to the db

    create_post(current_user.user_id, str(extract_Title(file.filename)), compute_max_post_next())

    return StreamingResponse(iterfile(), media_type="application/msword")

def create_post(user_id :str , title:str, post_id:int):
    """
    this function is used by upload_file to add to the database the title of the book read by the user
    in order to give this information when asked (get_user)

    using psycopg2
    """

    try:
        conn = psycopg2.connect(host=settings.database_hostname, port=settings.database_port,
                                database=settings.database_name, user=settings.database_username,
                                password=settings.database_password, cursor_factory=RealDictCursor)

        cursor = conn.cursor()
        print("Database connection was succesfull!")
        #logger.info("Database connection was succesfull!")

        postgres_insert_query = " INSERT INTO posts (title, post_id, user_id,post_created_at) VALUES ( '"+title+"',"+str(post_id)+","+str(user_id)+",'"+str(datetime.datetime.now())+"')"
        #logger.info("postgres_insert_query",postgres_insert_query)
        print("postgres_insert_query",postgres_insert_query)
        cursor.execute(postgres_insert_query)

        conn.commit()
        count = cursor.rowcount
        #logger.info(count, "Record inserted successfully into table")
        print(count, "Record inserted successfully into table")

    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table", error)
        #logger.error("Failed to insert record into table", error)
    finally:
        # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            #logger.info("PostgreSQL connection is closed")
            print("PostgreSQL connection is closed")
