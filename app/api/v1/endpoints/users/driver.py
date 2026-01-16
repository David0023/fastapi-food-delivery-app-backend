from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db

from app.schemas.users.driver import DriverCreate, DriverBase
from app.models.users.driver import Driver
from app.utils.auth import hash_password_inside
from app.utils.validate import validate_user_registration

router = APIRouter(
    prefix="/drivers",
    tags=["drivers"]
)

@router.post("/register", response_model=DriverBase)
def register_customer(user_data: DriverCreate, db: Session = Depends(get_db)):
    try:
        validate_user_registration(user_data, db, Driver)

        data = hash_password_inside(user_data.model_dump(exclude_unset=True))
        new_driver = Driver(**data)
        db.add(new_driver)
        db.commit()
        db.refresh(new_driver)

        return new_driver
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