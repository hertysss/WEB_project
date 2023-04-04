import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Office(SqlAlchemyBase):
    __tablename__ = 'offices'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    area = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    floor = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    bet = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    status = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relationship('User')

    business_center_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("business_centers.id"))
    business_center = orm.relationship('Business_center')

    def __repr__(self):
        return f"Объект 'Офис' с id:{self.id}, создатель :{self.user.role} {self.user.name}"