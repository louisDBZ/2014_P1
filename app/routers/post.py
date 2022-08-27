from fastapi import APIRouter, UploadFile,File, HTTPException, Depends
from fastapi.responses import FileResponse,StreamingResponse
from .note_caster import process_csv_to_docx,extract_Title
#from ..main import logger
from .config import settings
import psycopg2
from psycopg2.extras import RealDictCursor

import datetime

from .database import compute_max_post_next
from . import oauth2
"""
grosse question de design qui se pose ici:

l'api reçoit un fichier csv et peut renvoyer un fichier (chiffré) dans le body de la réponse ou un JSON

différents choix s'offrent à nous:
-on creuse l'idée d'un docx
-on refactor et passe par un échange sftp
-on renvoie un JSON ou un text

finalement, mon choix: 
sur postman faire save response>save to a file et choisir un fichier doc


questionnement que je me suis posé: faire un appel get avec gestion de l'id pour le document

time.sleep(3) # pour tester l'async ->ok ça marche, se poser la question est ce que c'est le bon moyen de tester l'async

"""


i_chemin_du_csv = "D.csv"
o_chemin_du_word = "The_Customer_Success_Professionals_Handbook.docx"



router = APIRouter(
    prefix="/file",
    tags=['File']
)

@router.post("/")
async def upload_file(file: UploadFile = File(...), current_user: int = Depends(oauth2.get_current_user)):
    """
    rappel il faut mettre le token dans le post

    """
    # a noter la syntaxe est différente selon la version de python

    def iterfile():
        with open(o_chemin_du_word, mode="rb") as file_like:
            yield from file_like

    # pour trouver la bonne écriture du content, c'est à travers MIME types
    # example: image/jpeg

    if file.content_type not in ['text/csv']:
        raise HTTPException(status_code=406, detail="Please upload only .csv files")

    # pour accéder au fichier, il faut l'enregistrer à un endroit puis l'afficher

    with open(file.filename, "wb+") as file_object:
        file_object.write(file.file.read())

    process_csv_to_docx(file.filename,o_chemin_du_word)

    # upload a trace to the db

    create_post(current_user.user_id, str(extract_Title(file.filename)), compute_max_post_next())

    return StreamingResponse(iterfile(), media_type="application/msword")

def create_post(user_id :str , title:str, post_id:int):
    """
    comme ici on ne veut pas utiliser une route fast APi alors le Depends de fastapi est inutilisable
    https://github.com/tiangolo/fastapi/issues/1693#issuecomment-665833384

    passage par psycopg2
    https://pynative.com/python-postgresql-insert-update-delete-table-data-to-perform-crud-operations/
    """

    try:
        conn = psycopg2.connect(host=settings.database_hostname, port=settings.database_port,
                                database=settings.database_name, user=settings.database_username,
                                password=settings.database_password, cursor_factory=RealDictCursor)

        cursor = conn.cursor()
        print("Database connection was succesfull!")
        #logger.info("Database connection was succesfull!")
        #INSERT INTO posts (title, post_id, user_id,post_created_at) VALUES ('indien',50,4,'2022-08-04 17:33:03.097168+02')

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
