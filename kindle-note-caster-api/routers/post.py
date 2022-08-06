from fastapi import APIRouter, UploadFile,File, HTTPException

# a noter: il faudra faire une fonction pour la gestion de l'id

router = APIRouter(
    prefix="/file",
    tags=['File']
)

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    # pour trouver la bonne écriture du content, c'est à travers MIME types
    # example: image/jpeg
    if file.content_type not in ['text/csv']:
        raise HTTPException(status_code=406, detail="Please upload only .csv files")
    return {"filename": file.filename}

@router.get("/{id}")
def get_file():
    return {"message": "get_file "}