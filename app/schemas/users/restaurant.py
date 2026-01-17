from pydantic import ConfigDict
from .user import UserBase, UserCreate, UserUpdate
from app.core.enums import CuisineStyle

class RestaurantBase(UserBase):
    model_config = ConfigDict(from_attributes=True)
    name: str
    address: str
    phone_number: str
    cuisine_style: CuisineStyle

class RestaurantInDB(RestaurantBase):
    hashed_password: str

class RestaurantCreate(UserCreate):
    name: str
    address: str
    phone_number: str
    cuisine_style: CuisineStyle = None

class RestaurantUpdate(UserUpdate):
    model_config = ConfigDict(from_attributes=True)
    name: str | None = None
    address: str | None = None
    phone_number: str | None = None