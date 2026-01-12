from sqlalchemy import Column, DateTime
from datetime import datetime, timezone

from app.utils.database import Base

class TimestampMixin:
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

class BaseModel(Base):
    __abstract__ = True

    def dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}