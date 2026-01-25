from pydantic import BaseModel, ConfigDict, Field

class ReviewBase(BaseModel):
    id: int
    customer_id: int
    restaurant_id: int
    rating: int
    content: str
    created_at: str
    updated_at: str

    model_config = ConfigDict(from_attributes=True)

class ReviewCreate(BaseModel):
    restaurant_id: int = Field(..., gt=0)
    rating: int = Field(..., ge=1, le=5)
    content: str

