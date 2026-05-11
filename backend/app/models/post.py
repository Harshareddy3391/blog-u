from sqlalchemy import Column, String, Integer,ForeignKey
from .base import Base


class Post(Base):

    __tablename__="posts"

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(250),nullable=False)
    image=Column(String(240))
    author_id = Column(Integer,ForeignKey("users.id"))
