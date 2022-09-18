from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

class Post(Base):
    # table post document , title of the kindle document, created at, user
    __tablename__ = "posts"
    post_id = Column(Integer, primary_key=True, nullable=False,default=text("(SELECT coalesce(max(post_id),0) + 1 FROM posts)"))
    title = Column(String, nullable=False)
    post_created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey(
        "users.user_id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")


class User(Base):
    # table users , column id, email, password, created_at
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, nullable=False,default=text("(SELECT coalesce(max(user_id),0) + 1 FROM users)"))
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    user_created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


