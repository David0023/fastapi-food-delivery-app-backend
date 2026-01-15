from sqlalchemy import Column, String, Integer, ForeignKey

from app.core.enums import UserRole
from .user import User

class Restaurant(User):
    __tablename__ = "restaurants"

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)

    __mapper_args__ = {"polymorphic_identity": UserRole.restaurant.value}