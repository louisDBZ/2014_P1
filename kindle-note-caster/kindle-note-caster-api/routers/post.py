from fastapi import APIRouter, UploadFile,File, HTTPException
from fastapi.responses import FileResponse,StreamingResponse
from .note_caster import process_csv_to_docx

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
async def upload_file(file: UploadFile = File(...)):

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

    return StreamingResponse(iterfile(), media_type="application/msword")
