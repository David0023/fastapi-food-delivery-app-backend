from sqlalchemy import Column, String, Integer, Boolean

from app.core.enums import UserRole
from . import User 

class Restaurant(User):
    __tablename__ = "restaurants"

    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)

    __mapper_args__ = {"polymorphic_identity": UserRole.restaurant.value}