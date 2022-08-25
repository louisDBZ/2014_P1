from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .models import  User,Column
from . import models, schemas, utils
from .database import get_db
import psycopg2
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from psycopg2.errors import UniqueViolation

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

class BadRequest(Exception):
    pass

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserIn)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # pydantic est capable de savoir si l'email créé est un vrai ou non
    # hash the password - user.password
    """
    Exception A gérer:

    sqlalchemy.exc.IntegrityError: (psycopg2.errors.UniqueViolation) ERREUR:  la valeur d'une clé dupliquée rompt la c
    ontrainte unique « users_email_key »
    DETAIL:  La clé « (email)=(noemipe@gmail.fr) » existe déjà.
    """

    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    # mettre un try catch si le user existe déjà
    db.add(new_user)

    try:
        # pour que les changements ai bel et bien lieu: besoin de commit et de refresh ( sinon fait à la main)
        db.commit()
        db.refresh(new_user)

    except IntegrityError as e:
        # a corriger: crash quand une adresse email déjà existante est  donnée
        assert isinstance(e.orig, UniqueViolation)
        raise BadRequest from e

    return new_user


@router.get('/{id}')
def get_user(id: int, db: Session = Depends(get_db)):
    """comme je veux un modèle spécifique en sortie, je n'utilise pas de modèle ( response_model=schemas.UserOut),
    c'est surement possible mais je n'ai pas regardé comment faire
    je construis moi meme mon JSON de sortie:

    retour attendu:
    {


    "user_id": 3,
    "email": "sisterp3.debouzy@gmail.fr",

    "user created_at": "2022-08-04T17:32:57.849154+02:00"

    "posts":
    [
    {"title":"La bible","created_at": "2022-08-04T17:32:57.849154+02:00" },
    {"title":"Le Coran","created_at": "2022-08-04T17:32:57.849154+02:00" }
    ]
    }

    je voulais utiliser  SQLAlchemy et utiliser le join des
     2 tables pour essayer de retrouver la requete suivante:
    a noter: pas besoin de faire le on (models.Post.user_id==models.User.user_id), sql alchemy se sert de la foreignkey

    select  post_created_at, title,email,user_created_at,  C.user_id
    from posts as A
    join users as C
    ON
    A.user_id=C.user_id

    """
    # table User

    user_profile = db.query(models.User).filter(models.User.user_id == id).first()

    if not user_profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    # table Post

    post_history = db.query(models.Post).filter(models.Post.user_id == id).all()
    # all = des "first" dans un tableau

    def Json_caster(user_profile,post_history):
        dico= {"user_id": user_profile.user_id,"email":user_profile.email, "user_created_at":user_profile.user_created_at,"history": []}
        for row in post_history:
            dico["history"].append({"title":row.title,"post_created_at":row.post_created_at})
        return dico

    return Json_caster(user_profile,post_history)
