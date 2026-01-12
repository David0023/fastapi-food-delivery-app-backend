from app.core.config import settings
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy starting point
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal will be the class of which its instance is db session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Opens up a session
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
