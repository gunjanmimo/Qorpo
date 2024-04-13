# -------------------------------- PYTHON IMPORTS --------------------------------#
from aiohttp import web

# -------------------------------- LOCAL IMPORTS --------------------------------#
from service.kucoin_service import (
    save_currency_price,
    get_all_price_history,
    flash_price_history,
)
from middleware.ccxt_handler import fetch_kucoin_currency_price

# TODO: GET /price/{currency}
"""_summary_

1. STEP 1: FETCH PRICE OF {CURRENCY} FROM KUCOIN
2. STEP 2: SAVE THE PRICE DATA TO DATABASE
3. STEP 3: RETURN THE PRICE DATA TO THE USER
"""


async def get_price(request):
    currency = request.match_info["currency"]
    # STEP 1: FETCH PRICE OF {CURRENCY} FROM KUCOIN
    currency, price, timestamp = await fetch_kucoin_currency_price(currency)
    # STEP 2: SAVE THE PRICE DATA TO DATABASE
    await save_currency_price(currency=currency, price=price, date_=timestamp)
    # STEP 3: RETURN THE PRICE DATA TO THE USER
    return web.json_response({"currency": currency, "price": price, "date": timestamp})


# TODO: GET /price/history?page={page}
"""_summary_
DEFAULT PAGE : 10 
STEP 1: FETCH PRICE HISTORY DATA FROM DATABASE
STEP 2: RETURN THE PRICE HISTORY DATA TO THE USER
"""


async def get_price_history(request):
    page = request.query.get("page", 10)
    # STEP 1: FETCH PRICE HISTORY DATA FROM DATABASE
    price_history = get_all_price_history(page_no=page)
    # STEP 2: RETURN THE PRICE HISTORY DATA TO THE USER
    return web.json_response(price_history)


# TODO: DELETE price/history
"""_summary_

STEP 1: DELETE ALL PRICE HISTORY DATA FROM DATABASE
STEP 3: RETURN SUCCESS MESSAGE TO THE USER
"""


async def delete_price_history(request):
    # STEP 1: DELETE ALL PRICE HISTORY DATA FROM DATABASE
    await flash_price_history()
    # STEP 3: RETURN SUCCESS MESSAGE TO THE USER
    return web.json_response({"message": "Price history deleted successfully"})
