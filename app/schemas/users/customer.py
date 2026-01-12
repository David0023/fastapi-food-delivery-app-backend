from pydantic import ConfigDict
from .user import UserBase, UserInDB, UserCreate, UserUpdate

class CustomerBase(UserBase):
    model_config = ConfigDict(from_attributes=True)
    phone_number: str

class CustomerInDB(UserInDB):
    phone_number: str

class CustomerCreate(UserCreate):
    phone_number: str

class CustomerUpdate(UserUpdate):
    model_config = ConfigDict(from_attributes=True)
    phone_number: str | None = None
