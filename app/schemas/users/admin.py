from pydantic import ConfigDict
from . import UserBase, UserInDB, UserCreate, UserUpdate

class AdminBase(UserBase):
    model_config = ConfigDict(from_attributes=True)