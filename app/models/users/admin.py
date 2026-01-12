from app.core.enums import UserRole
from . import User

class Admin(User):
    __tablename__ = "admins"

    __mapper_args__ = {"polymorphic_identity": UserRole.admin.value}