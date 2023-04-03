import sqlalchemy
from data.db_session import SqlAlchemyBase


class Renter(SqlAlchemyBase):
    __tablename__ = 'renters'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    phone_number = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    mail = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    wishes = sqlalchemy.Column(
        sqlalchemy.Text, nullable=False, default="например ставка, этаж, наличие лифта")
