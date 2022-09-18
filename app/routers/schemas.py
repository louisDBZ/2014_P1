from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserIn(BaseModel):
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
    id: Optional[str] = None

