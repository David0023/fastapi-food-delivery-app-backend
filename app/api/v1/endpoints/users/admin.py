from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.models.users.admin import Admin
from app.schemas.users.admin import AdminCreate, AdminBase
from app.utils.auth import hash_password_inside
from app.utils.database import get_db
from app.utils.validate import validate_user_registration

router = APIRouter(
    prefix='/admins',
    tags=['admins']
)

@router.post('/register', response_model=AdminBase)
def create_new_admin(user_data: AdminCreate, db: Session = Depends(get_db)):
    try:
        validate_user_registration(user_data, db, Admin)

        data = hash_password_inside(user_data.model_dump(exclude_unset=True))
        new_admin = Admin(**data)
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)
        return new_admin
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