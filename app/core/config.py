import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./database.db")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"

settings = Settings()