from sqlalchemy import Column, String, Boolean, Integer, ForeignKey

from app.core.enums import UserRole
from .user import User

class Driver(User):
    __tablename__ = "drivers"

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    license_number = Column(String, unique=True, index=True)
    vehicle_type = Column(String, nullable=True)
    is_available = Column(Boolean, default=True, index=True)

    __mapper_args__ = {"polymorphic_identity": UserRole.driver.value}