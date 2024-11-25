import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_USER :str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD :str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOSTNAME :str = os.getenv("POSTGRES_HOSTNAME")
    POSTGRES_PORT :int = 5432
    POSTGRES_DB :str = os.getenv("POSTGRES_DB")

    @property
    def get_sync_db_url(self):
        return (f"postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
                f"{self.POSTGRES_HOSTNAME}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}")
    
    print(f"postgresql+psycopg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
                f"{POSTGRES_HOSTNAME}:{POSTGRES_PORT}/{POSTGRES_DB}")

    @property
    def get_async_db_url(self):
        return (f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
                f"{self.POSTGRES_HOSTNAME}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}")

        
settings = Settings()