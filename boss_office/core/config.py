import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path(__file__) / '..' / '..' / '.env'

load_dotenv(dotenv_path=env_path)


class Setting:
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD', "postgres")
    POSTGRES_USER: str = os.getenv('POSTGRES_USER', "postgres")
    POSTGRES_HOST: str = os.getenv('POSTGRES_HOST', "localhost")
    POSTGRES_NAME: str = os.getenv('POSTGRES_NAME', "postgres")
    POSTGRES_PORT: int = os.getenv('POSTGRES_PORT', 5432)

    SQLALCHEMY_DATABASE_URL: str = (f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
                                    f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}")


setting = Setting()


