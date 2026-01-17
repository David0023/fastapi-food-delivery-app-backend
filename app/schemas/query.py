from pydantic import BaseModel
from typing import List
from .users.restaurant import RestaurantBase
from .users.driver import DriverBase
from .users.customer import CustomerBase

class RestaurantList(BaseModel):
    total: int
    restaurants: List[RestaurantBase]

class DriverList(BaseModel):
    total: int
    drivers: List[DriverBase]

class CustomerList(BaseModel):
    total: int
    customers: List[CustomerBase]