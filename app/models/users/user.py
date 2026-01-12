from sqlalchemy import Column, Integer, String, Boolean, Enum as SAEnum
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, TimestampMixin
from app.core.enums import UserRole

class User(BaseModel, TimestampMixin):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(SAEnum(UserRole), nullable=False, default=UserRole.user)

    _mapper_args__ = {"polymorphic_on": role, "polymorphic_identity": UserRole.user.value}

    # TODO: Add profile image