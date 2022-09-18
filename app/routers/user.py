from fastapi import  status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import get_db
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

class BadRequest(Exception):
    pass

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserIn)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db))-> models.User:

    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)

    try:
        db.commit()
        db.refresh(new_user)

    except IntegrityError as e:
        assert isinstance(e.orig, UniqueViolation)
        raise BadRequest from e

    return new_user


@router.get('/{id}')
def get_user(id: int, db: Session = Depends(get_db)) -> dict:
    """give the id of an user already created, and receive his history of books read

    I want a specific JSON model in output, I don't use a sql-alchelmy model.
    -> here is an example of the expected output:

    {
    "user_id": 3,
    "email": "sisterp3.123@gmail.fr",

    "user created_at": "2022-08-04T17:32:57.849154+02:00"

    "posts":
    [
    {"title":"La bible","created_at": "2022-08-04T17:32:57.849154+02:00" },
    {"title":"Le Coran","created_at": "2022-08-04T17:32:57.849154+02:00" }
    ]
    }

    """
    # table User

    user_profile = db.query(models.User).filter(models.User.user_id == id).first()

    if not user_profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    # table Post

    post_history = db.query(models.Post).filter(models.Post.user_id == id).all()

    def Json_caster(user_profile,post_history)-> dict:
        dico= {"user_id": user_profile.user_id,"email":user_profile.email, "user_created_at":user_profile.user_created_at,"history": []}
        for row in post_history:
            dico["history"].append({"title":row.title,"post_created_at":row.post_created_at})
        return dico

    return Json_caster(user_profile,post_history)
