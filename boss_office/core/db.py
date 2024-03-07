from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import setting

print(f"-----------url db :{setting.SQLALCHEMY_DATABASE_URL}")
engine = create_engine(
    setting.SQLALCHEMY_DATABASE_URL, echo=True,
    pool_pre_ping=True,
    pool_size=100
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db_session():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


