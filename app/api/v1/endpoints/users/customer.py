from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db

from app.schemas.users.customer import CustomerCreate, CustomerBase
from app.models.users.customer import Customer
from app.utils.auth import hash_password_inside
from app.utils.validate import validate_user_registration

router = APIRouter(
    prefix="/customers",
    tags=["customers"]
)

@router.post("/register", response_model=CustomerBase)
def register_customer(user_data: CustomerCreate, db: Session = Depends(get_db)):
    try:
        validate_user_registration(user_data, db, Customer)

        data = hash_password_inside(user_data.model_dump(exclude_unset=True))
        new_customer = Customer(**data)
        db.add(new_customer)
        db.commit()
        db.refresh(new_customer)

        return new_customer
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