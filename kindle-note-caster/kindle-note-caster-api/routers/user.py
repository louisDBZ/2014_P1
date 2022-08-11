from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .models import  User,Column
from . import models, schemas, utils
from .database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserIn)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # pydantic est capable de savoir si l'email créé est un vrai ou non
    # hash the password - user.password

    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.dict())

    db.add(new_user)
    # pour que les changements ai bel et bien lieu: besoin de commit et de refresh ( sinon fait à la main)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db), ):
    '''
     requete à retravailler car on veut l'historique: on doit faire un join des
     2 tables avec un historique sous form json

    {
    "user_id": 3,
    "email": "sisterp3.debouzy@gmail.fr",

    "user created_at": "2022-08-04T17:32:57.849154+02:00"

    "history":
    [
    {"title":"La bible","created_at": "2022-08-04T17:32:57.849154+02:00" },
    {"title":"Le Coran","created_at": "2022-08-04T17:32:57.849154+02:00" }
    ]
    }

    select * from posts as A
    join users as C
    ON
    A.user_id=C.user_id

    result = session.query(Customer).join(Invoice).filter(Invoice.amount == 8500)
    '''

    user = db.query(models.User).filter(models.User.user_id == id).first()
    #user = db.query(models.User).join(models.Post,models.Post.owner_id==models.User.id).filter(models.User.id == id).first()
    print(user)

    # comme on va avoir plusieurs lignes, on va avoir un casting à faire en JSON : enlever le first


    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    return user
