import sqlalchemy
from data.db_session import SqlAlchemyBase


class LandLender(SqlAlchemyBase):
    __tablename__ = 'landlenders'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    phone_number = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    mail = sqlalchemy.Column(sqlalchemy.String, nullable=False)
