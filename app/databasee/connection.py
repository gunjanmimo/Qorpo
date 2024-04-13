# -------------------------------- SQL ALCHEMY IMPORTS --------------------------------#
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# -------------------------------- LOCAL IMPORTS --------------------------------#
from core.config import config

print("--------------------------------")
print("DATABASE CONNECTION")
print("--------------------------------")
# create database engine
engine = create_engine(
    config.DATABASE_URL,
    echo=False,
)


# database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
