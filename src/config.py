import os
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings


if load_dotenv(".env"):
    POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
    POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
    POSTGRES_DB = os.environ.get("POSTGRES_DB")
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_PATH = f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

class DbSettings(BaseModel):
    url: str = f"postgresql+asyncpg://{POSTGRES_PATH}"
    echo: bool = False

class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db_echo: bool = True
    db: DbSettings = DbSettings(echo=db_echo)


settings = Settings()
