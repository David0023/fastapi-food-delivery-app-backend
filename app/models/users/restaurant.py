from sqlalchemy import Column, String, Integer, Boolean
from . import User 

class Restaurant(User):
    __tablename__ = "restaurants"

    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)