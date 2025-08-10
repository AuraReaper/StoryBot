from logging import DEBUG
from typing import List
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )

    DATABASE_URL: str = None
    API_PREFIX: str = "/api"
    DEBUG: bool = True
    ALLOWED_ORIGINS: str = ""
    GEMINI_API_KEY: str

    def __init__(self, **values):
        super().__init__(**values)
        if not self.DEBUG:
            db_user = os.getenv("DB_USER")
            db_password = os.getenv("DB_PASSWORD")
            db_host = os.getenv("DB_HOST")
            db_port = os.getenv("DB_PORT")
            db_name = os.getenv("DB_NAME")
            self.DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, value) -> List[str]:
        return value.split(",") if value else []

settings = Settings()
