# lib
from sqlalchemy import Column, Integer, String

# pkg
from app.database.base import BASE


class User(BASE):
    __tablename__ = "user"

    num = Column( Integer, primary_key=True, autoincrement=True, unique=True, nullable=False )
    id = Column( String, unique=True, nullable=False )
    pw = Column( String, nullable=False )
