from sqlalchemy import Column, DateTime
from datetime import datetime

from app.utils.database import Base

class TimestampMixin:
    created_at = Column(DateTime, default=datetime.now(datetime.UTC))
    updated_at = Column(DateTime, default=datetime.now(datetime.UTC))

class BaseModel(Base):
    __abstract__ = True

    def dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}