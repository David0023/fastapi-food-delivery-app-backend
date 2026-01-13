from email_validator import validate_email, EmailNotValidError
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import Type
import re

def is_valid_email(email: str) -> bool:
    """
    Validate the given email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False
    
def is_valid_phone(phone_number: str) -> bool:
    pattern = r'^[0-9-]+$'
    return re.fullmatch(pattern, phone_number)

def validate_user_registration(
    data: BaseModel,
    db: Session,
    user_model: Type = None
) -> None:
    """
    Raise error if username, email, password is correctly given.
    Raise error if username or email is not unique.
    """
    if not hasattr(data, 'username') or not data.username:
        raise ValueError('User Name must be provided')
    if not hasattr(data, 'email') or not data.email:
        raise ValueError('Email must be provided')
    if not hasattr(data, 'password') or not data.password:
        raise ValueError('Password must be provided')

    if not is_valid_email(data.email):
        raise ValueError('Wrong email format')

    if user_model:
        if db.query(user_model).filter(user_model.username == data.username).first():
            raise ValueError('Duplicate Username')
        if db.query(user_model).filter(user_model.email == data.email).first():
            raise ValueError('Duplicate Email')
    