from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.enums import UserRole
from app.utils.database import get_db
from app.utils.auth import Token, authenticate_user, create_access_token

auth_router = APIRouter(tags=['auth'])


@auth_router.post('/token', response_model=Token)
async def login_for_access_token(role: UserRole, db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    """
    End point for JWT Token generation
    """
    user = authenticate_user(form_data.username, form_data.password, role, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(username=user.username, role=role.name)
    return {"access_token": access_token, "token_type": "bearer"}