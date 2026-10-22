import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    if not SECRET_KEY or not SQLALCHEMY_DATABASE_URI:
        raise RuntimeError("Defina SECRET_KEY e DATABASE_URL no .env")

class TestConfig:
    TESTING = True
    SECRET_KEY = "teste"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False