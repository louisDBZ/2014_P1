from fastapi import APIRouter


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.post("/")
def post_file():
    return {"message": "Hello World 2 "}

