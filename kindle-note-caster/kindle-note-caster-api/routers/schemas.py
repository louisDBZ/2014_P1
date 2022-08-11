from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint

# question: pourquoi le post a été enlevé???
'''

pydantic => schéma qui sert à décrire à quoi un post devrait ressembler
sert à décrire la donnée envoyée par le client

to do: faire celle du post que l'on envoie
'''
"""
class PostBase(BaseModel): # a modifier
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase): # a modifier
    pass

class PostOut(BaseModel): # a modifier
    Post: Post
    votes: int

    class Config:
        orm_mode = True

class Post(PostBase): # a modifier
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True
"""
# en dessous (a garder): les actions pour la gestion des users

class UserIn(BaseModel):
    # LE MOdel userin sert pour la route create_model
    user_id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    # LE MOdel userout sert pour la route get_user
    # a supprimer si en doublon
    user_id: int
    email: EmailStr
    created_at: datetime
    #title: str

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    # ce qui est interessant, c'est que l'on peut dire optional ou non
    id: Optional[str] = None

