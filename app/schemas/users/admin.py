from pydantic import ConfigDict
from .user import UserBase, UserInDB, UserCreate, UserUpdate
class AdminBase(UserBase):
    model_config = ConfigDict(from_attributes=True)

class AdminCreate(UserCreate):
    pass

class AdminInDB(UserInDB):
    pass

class AdminUpdate(UserUpdate):
    pass