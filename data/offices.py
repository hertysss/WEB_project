import sqlalchemy
from data.db_session import SqlAlchemyBase


class Office(SqlAlchemyBase):
    __tablename__ = 'offices'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    object = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('objects.id'), nullable=False)
    footage = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    building = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    floor = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    lift = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    rent = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    photo = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    status = sqlalchemy.Column(
        sqlalchemy.String, nullable=False, default='Сдан')
    client_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=True)
    broker_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False)
