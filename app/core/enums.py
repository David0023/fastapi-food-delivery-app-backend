from enum import Enum

class UserRole(str, Enum):
    user = "user"
    admin = "admin"
    customer = "customer"
    driver = "driver"
    restaurant = "restaurant"