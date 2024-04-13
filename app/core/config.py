# -------------------------------- PYTHON IMPORTS --------------------------------#
import os
import pathlib
from pydantic_settings import BaseSettings


# Project Directories
ROOT = pathlib.Path(__file__).resolve().parent
print(ROOT)
os.chdir(ROOT)


print(os.getcwd())


class Config(BaseSettings):
    # kucoin
    KUCOIN_API_KEY: str
    KUCOIN_API_SECRET: str
    KUCOIN_PASSWORD: str

    # Database
    DATABASE_URL: str
    DB_ECHO: str

    class Config:
        case_sensitive = True
        env_file = ".env"


config = Config()
config.DB_ECHO = eval(config.DB_ECHO)
