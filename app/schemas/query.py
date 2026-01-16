from pydantic import list, BaseModel
from .users.restaurant import RestaurantBase
from .users.driver import DriverBase
from .users.customer import CustomerBase

class RestaurantList(BaseModel):
    total: int
    restaurants: list[RestaurantBase]

class DriverList(BaseModel):
    total: int
    drivers: list[DriverBase]

class CustomerList(BaseModel):
    total: int
    customers: list[CustomerBase]