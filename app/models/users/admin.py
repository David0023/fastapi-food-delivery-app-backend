from sqlalchemy import Column, String, Integer, Boolean
from . import User

class Admin(User):
    __tablename__ = "admins"