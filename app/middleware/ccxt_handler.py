# -------------------------------- PYTHON IMPORTS --------------------------------#
import asyncio
import json

# -------------------------------- CCXT IMPORTS --------------------------------#
import ccxt.async_support as ccxt

# -------------------------------- LOCAL IMPORTS --------------------------------#
from core.config import config

kucoin_exchange = ccxt.kucoin(
    {
        "apiKey": config.KUCOIN_API_KEY,
        "secret": config.KUCOIN_API_SECRET,
        "password": config.KUCOIN_PASSWORD,
    }
)


async def fetch_kucoin_currency_price(currency: str):
    """
    Fetch currency price from kucoin exchange

    Args:
        currency (str): currency to fetch price for

    Returns:
        dict: currency price, currency and date
    """
    # fetch price
    response = await kucoin_exchange.fetch_ticker(currency)

    return currency, response["last"], response["datetime"]
