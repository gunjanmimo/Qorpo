# -------------------------------- PYTHON IMPORTS --------------------------------#
from datetime import datetime

# -------------------------------- LOCAL IMPORTS --------------------------------#
from models.price_models import Price
from middleware.ccxt_handler import fetch_kucoin_currency_price
from databasee.connection import get_db

# TODO: IMPLEMENT CCXT TO FETCH KUCOIN PRICE

db = get_db()


async def save_currency_price(currency: str, price: float, date_: datetime) -> bool:

    # save price to database
    price = Price(currency=currency, price=price, date_=date_)
    db.add(price)
    db.commit()
    return True


def get_all_price_history(
    page_no: int, page_limit: int = 10, currency: str = None
) -> dict:
    """
    FUNCTION TO FETCH PRICE HISTORY OF {CURRENCY} FROM DATABASE USING PAGINATION

    DEFAULT PAGINATION LIMIT IS 10

    Args:
        page_no (int): PAGE NUMBER
        page_limit (int, optional): PAGE LIMIT. Defaults to 10.
        currency (str, optional): CURRENCY FILTER. None means all currencies.
    """
    if currency:
        price_objs = (
            db.query(Price)
            .order_by(Price.date_.desc())
            .filter(Price.currency == currency)
            .offset(page_no * page_limit)  # Fix for proper pagination
            .limit(page_limit)
            .all()
        )
    else:
        price_objs = (
            db.query(Price)
            .order_by(Price.date_.desc())
            .offset(page_no * page_limit)
            .limit(page_limit)
            .all()
        )

    prices = []
    for price_obj in price_objs:
        currency = price_obj.currency
        price = price_obj.price
        date_ = price_obj.date_
        # format date
        date_ = date_.strftime("%Y-%m-%d %H:%M:%S")
        price_dict = {
            "currency": currency,
            "price": price,
            "date": date_,
        }
        prices.append(price_dict)
    return {"data": prices}


async def flash_price_history() -> bool:
    """
    FUNCTION TO DELETE PRICE HISTORY FROM DATABASE
    """
    db.query(Price).delete()
    return True
