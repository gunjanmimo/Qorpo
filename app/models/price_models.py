# -------------------------------- SQL ALCHEMY IMPORTS --------------------------------#
from sqlalchemy import Column, String, Float, Integer, DateTime

# -------------------------------- LOCAL IMPORTS --------------------------------#
# from database import Base
from databasee.connection import Base
from models.utils import get_random_uuid_string

# TODO: PRICE MODEL
"""_summary_
id: int : primary key
currency: str : currency name
price: float : currency price
date_: datetime : timestamp
"""


class Price(Base):
    __tablename__ = "price"

    id = Column(
        String(50),
        primary_key=True,
        index=True,
        nullable=False,
        unique=True,
        default=get_random_uuid_string,
    )
    currency = Column(String, index=True)
    price = Column(Float)
    date_ = Column(DateTime)

    def __init__(self, currency: str, price: float, date_: str):
        self.currency = currency
        self.price = price
        self.date_ = date_

    def __repr__(self):
        return f"<Price {self.currency} {self.price} {self.date_}>"
