from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, Enum

from app.core.enums import UserRole, VehicleType
from .user import User

class Driver(User):
    __tablename__ = "drivers"

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    license_number = Column(String, unique=True, index=True)
    vehicle_type = Column(Enum(VehicleType), nullable=False)
    is_available = Column(Boolean, default=True, index=True)

    __mapper_args__ = {"polymorphic_identity": UserRole.driver.value}

    def update_availability(self, is_available: bool):
        self.is_available = is_available