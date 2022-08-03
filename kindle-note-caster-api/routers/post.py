from fastapi import APIRouter

# a noter: il faudra faire une focntion pour la gestion de l'id

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.post("/")
def post_file():
    print("hello")
    return {"message": "Hello World 2 "}

