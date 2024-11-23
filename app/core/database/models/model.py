from sqlalchemy.orm import DeclarativeBase


class Model(DeclarativeBase):
    __abstract__ = True
