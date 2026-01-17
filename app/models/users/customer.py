from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.enums import UserRole
from .user import User

class Customer(User):
    __tablename__ = "customers"

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    phone_number = Column(String, nullable=False)

    reviews = relationship('Review', back_populates='customer')

    __mapper_args__ = {"polymorphic_identity": UserRole.customer.value}