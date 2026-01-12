from sqlalchemy import Column, String

from app.core.enums import UserRole
from . import User

class Customer(User):
    __tablename__ = "customers"

    phone_number = Column(String, nullable=False)

    __mapper_args__ = {"polymorphic_identity": UserRole.customer.value}