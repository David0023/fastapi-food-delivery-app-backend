from sqlalchemy import Column, Integer, ForeignKey
from app.core.enums import UserRole
from .user import User

class Admin(User):
    __tablename__ = "admins"

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": UserRole.admin.value}