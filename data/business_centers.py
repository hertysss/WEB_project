import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Business_center(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'business_centers'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    building = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    district = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    metro = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    total_area = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    klass = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    floors = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    lift = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    parking = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    contact = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relationship('User')

    offices = orm.relationship("Office", back_populates='business_center')

    def __repr__(self):
        return f"Объект 'Бизнес-центр' с id:{self.id}, создатель :{self.user.role} {self.user.name}"

