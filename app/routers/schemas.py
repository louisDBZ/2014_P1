from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

'''

pydantic => schéma qui sert à décrire à quoi un appel à l'API devrait ressembler
permet de gérer automatiquement les erreurs sur la donnée envoyée ( ou renvoyée???) par le client

'''

class UserIn(BaseModel):
    # LE MOdel userin sert pour la route create_model
    user_id: int
    email: EmailStr
    user_created_at: datetime

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
    #permet d'éviter que cela crash
    id: Optional[str] = None

