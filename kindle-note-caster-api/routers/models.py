'''
création d'un ORM
description de la bdd pour la regénérer automatiquement avec sqlachemy
'''

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base

# dans la bbd postgre, la string est un 'character varying'
# ------------------------timestamp ---- 'timestamp with time zone'
# -------------------------tserver_default=text('now()') ---- now()

# clic droit et 'Query Tool'> et lancer 'select * from users'
#nullable=False la valeur ne peut pas etre nulle

class Post(Base):
    # table post document , title of the kindle document, created at, user
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User") # a quoi sert cette ligne???


class User(Base):
    # table users , column id, email, password, created_at
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


