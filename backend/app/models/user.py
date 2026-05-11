from sqlalchemy import column,Integer,String

from .base import Base

class User(Base):

    __tablename__="users"