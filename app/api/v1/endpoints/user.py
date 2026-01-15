from fastapi import APIRouter, Depends
from app.models.users.user import User
from app.models.users.customer import Customer
from app.core.enums import UserRole
from app.schemas.users.customer import CustomerBase
from app.schemas.users.admin import AdminBase
from app.schemas.users.restaurant import RestaurantBase
from app.schemas.users.driver import DriverBase
from app.utils.auth import get_current_user

router = APIRouter(
    tags=['users'],
    prefix='/users'
)

@router.get('/me')
def get_my_info(user: User = Depends(get_current_user)):
    if user.role == UserRole.admin:
        return AdminBase.model_validate(user)
    elif user.role == UserRole.customer:
        return CustomerBase.model_validate(user)
    elif user.role == UserRole.restaurant:
        return RestaurantBase.model_validate(user)
    elif user.role == UserRole.driver:
        return DriverBase.model_validate(user)