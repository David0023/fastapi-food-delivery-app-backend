from pydantic import ConfigDict
from . import UserBase, UserCreate, UserUpdate

class RestaurantBase(UserBase):
    model_config = ConfigDict(from_attributes=True)
    name: str
    address: str
    phone_number: str

class RestaurantInDB(RestaurantBase):
    hashed_password: str

class RestaurantCreate(UserCreate):
    name: str
    address: str
    phone_number: str

class RestaurantUpdate(UserUpdate):
    model_config = ConfigDict(from_attributes=True)
    name: str | None = None
    address: str | None = None
    phone_number: str | None = None