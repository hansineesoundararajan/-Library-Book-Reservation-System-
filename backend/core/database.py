import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import StaticPool

BACKEND_DIR = os.path.dirname(os.path.dirname(__file__))
DEFAULT_DB_PATH = os.path.join(BACKEND_DIR, "library.db")
SQLALCHEMY_DATABASE_URL = os.getenv(
    "LIBRARY_DATABASE_URL",
    f"sqlite:///{DEFAULT_DB_PATH}",
)
engine_kwargs = {"connect_args": {"check_same_thread": False}}

if SQLALCHEMY_DATABASE_URL == "sqlite://":
    engine_kwargs["poolclass"] = StaticPool

engine = create_engine(SQLALCHEMY_DATABASE_URL, **engine_kwargs)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
