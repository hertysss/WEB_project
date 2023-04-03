import sqlalchemy
from data.db_session import SqlAlchemyBase


class Object(SqlAlchemyBase):
    __tablename__ = 'objects'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    adress = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    region = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    metro = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    footage = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    floor = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    parking = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    obj_class = sqlalchemy.Column(
        sqlalchemy.String, nullable=True, default='B')
    photo = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    contacts = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
