from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db

from app.schemas.users.customer import CustomerCreate, CustomerBase
from app.models.users.customer import Customer
from app.core.enums import UserRole
from app.utils.auth import get_password_hash
from app.utils.validate import validate_user_registration

router = APIRouter(
    prefix="/customers",
    tags=["customers", "users"]
)

@router.post("/register", response_model=CustomerBase)
def register_customer(user_data: CustomerCreate, db: Session = Depends(get_db)):
    try:
        validate_user_registration(user_data, db, Customer)

        data = user_data.model_dump(exclude_unset=True)
        data["hashed_password"] = get_password_hash(data.pop("password"))
        data["role"] = UserRole.customer

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