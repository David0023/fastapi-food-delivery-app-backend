from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db

from app.schemas.users.restaurant import RestaurantCreate, RestaurantBase
from app.models.users.restaurant import Restaurant
from app.utils.auth import hash_password_inside
from app.utils.validate import validate_user_registration

router = APIRouter(
    prefix="/restaurants",
    tags=["restaurants"]
)

@router.post("/register", response_model=RestaurantBase)
def register_customer(user_data: RestaurantCreate, db: Session = Depends(get_db)):
    try:
        validate_user_registration(user_data, db, Restaurant)

        data = hash_password_inside(user_data.model_dump(exclude_unset=True))
        new_restaurant = Restaurant(**data)
        db.add(new_restaurant)
        db.commit()
        db.refresh(new_restaurant)

        return new_restaurant
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        db.rollback()
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during registration"
        )