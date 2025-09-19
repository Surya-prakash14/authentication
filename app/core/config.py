from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:Surya%40123@1407localhost/auth_db"

settings = Settings()
