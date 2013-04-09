from mortar_rdb import declarative_base
from sqlalchemy import Column, String, Enum

from .common import Common

Base = declarative_base()

roles = ('Poster','Administrator')

class User(Base,Common):

    username = Column(String(50), primary_key=True)
    role = Column(Enum(*roles))
