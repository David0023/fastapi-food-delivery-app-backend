from sqlalchemy import Column, String
from . import User

class Customer(User):
    __tablename__ = "customers"

    phone_number = Column(String, nullable=False)