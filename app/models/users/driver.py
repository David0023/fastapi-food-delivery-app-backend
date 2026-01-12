from sqlalchemy import Column, String, Boolean
from . import User

class Driver(User):
    __tablename__ = "drivers"

    license_number = Column(String, unique=True, index=True)
    vehicle_type = Column(String, nullable=True)
    is_available = Column(Boolean, default=True, index=True)