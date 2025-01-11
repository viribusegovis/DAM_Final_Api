import urllib.parse

from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from config import settings
from models import Base, User, Recipe
from schemas import (UserCreate, UserResponse, RecipeCreate, RecipeResponse)

# Database connection setup
connection_string = (
    f"Driver={settings.DRIVER};"
    f"Server=tcp:{settings.SERVER},1433;"
    f"Database={settings.DATABASE};"
    f"Uid={settings.DB_USERNAME};"
    f"Pwd={settings.DB_PASSWORD};"
    f"Encrypt=yes;"
    f"TrustServerCertificate=no;"
    f"Connection Timeout=30;"
)

params = urllib.parse.quote_plus(connection_string)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
