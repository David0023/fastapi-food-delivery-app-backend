from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    email: str
    is_active: bool

class UserInDB(UserBase):
    hashed_password: str

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str | None = None
    email: str | None = None
    is_active: bool | None = None
    hashed_password: str | None = None