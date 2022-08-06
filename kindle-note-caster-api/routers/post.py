from fastapi import APIRouter

# a noter: il faudra faire une focntion pour la gestion de l'id

router = APIRouter(
    prefix="/file",
    tags=['File']
)

@router.post("/")
def upload_file():
    return {"message": "upload_file "}

@router.get("/{id}")
def get_file():
    return {"message": "get_file "}