from app.core.enums import UserRole
from app.models.users.admin import Admin
from app.models.users.customer import Customer
from app.models.users.driver import Driver
from app.models.users.restaurant import Restaurant

def get_model_by_role(user_role: UserRole) -> Admin | Customer | Driver | Restaurant:
    if user_role == UserRole.admin:
        return Admin
    if user_role == UserRole.customer:
        return Customer
    if user_role == UserRole.driver:
        return Driver
    if user_role == UserRole.restaurant:
        return Restaurant
