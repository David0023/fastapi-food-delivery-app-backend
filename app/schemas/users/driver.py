from pydantic import ConfigDict
from . import UserBase, UserInDB, UserCreate, UserUpdate

class DriverBase(UserBase):
    model_config = ConfigDict(from_attributes=True)
    license_number: str
    vehicle_type: str | None = None
    is_available: bool

class DriverInDB(DriverBase):
    hashed_password: str

class DriverCreate(UserCreate):
    license_number: str
    vehicle_type: str | None = None
    is_available: bool

class DriverUpdate(UserUpdate):
    model_config = ConfigDict(from_attributes=True)
    license_number: str | None = None
    vehicle_type: str | None = None
    is_available: bool | None = None