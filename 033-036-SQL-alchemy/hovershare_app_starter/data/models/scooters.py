import sqlalchemy as sa
from data.sqlalchemybase import SqlAlchemyBase

class Scooter():
    __tablename__='scooters'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_at = sa.Column(sa.DateTime)
    vin = sa.Column(sa.String)
    model = sa.Column(sa.String)
    battery_level = sa.Column(sa.Integer)