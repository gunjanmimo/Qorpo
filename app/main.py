# -------------------------------- PYTHON IMPORTS --------------------------------#
from aiohttp import web

# -------------------------------- LOCAL IMPORTS --------------------------------#
from api.endpoints.price_endpoint import (
    get_price,
    get_price_history,
    delete_price_history,
)
from databasee.connection import Base, engine


print("--------------------------------")
print("STARTING BACKEND SERVER")
print("--------------------------------")

# application instance
app = web.Application()


# routes
app.router.add_get("/price/history", get_price_history)
app.router.add_get("/price/{currency}", get_price)
app.router.add_delete("/price/history", delete_price_history)

# create tables
Base.metadata.create_all(engine)
