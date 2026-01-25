from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.utils.database import get_db

from app.schemas.review import ReviewCreate, ReviewBase
from app.models.users.user import User
from app.models.users.customer import Customer
from app.models.users.restaurant import Restaurant
from app.models.review import Review
from app.utils.auth import get_current_user

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"]
)

@router.post('/customers/make', response_model=ReviewBase, tags=["customers"])
def make_review(
    review_data: ReviewCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    if user.role != 'customer':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only customers can make reviews"
        )
    customer = db.query(Customer).filter(Customer.id == user.id).first()
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer profile not found"
        )
    
    review_data = review_data.model_dump(exclude_unset=True)

    # Check if the customer has already reviewed this restaurant
    if db.query(Review).filter(
        Review.customer_id == customer.id,
        Review.restaurant_id == review_data['restaurant_id']
    ).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You have already reviewed this restaurant"
        )
    if db.query(Restaurant).filter(Restaurant.id == review_data['restaurant_id']).first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Restaurant not found"
        )
    
    try:
        new_review = Review(
            customer_id=customer.id,
            restaurant_id=review_data['restaurant_id'],
            rating=review_data['rating'],
            content=review_data['content']
        )
        db.add(new_review)
        db.commit()
        db.refresh(new_review)

        return new_review
    except Exception as e:
        db.rollback()
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while submitting the review"
        )

@router.get('/customers/my', response_model=list[ReviewBase], tags=["customers"])
def get_reviews_by_customer(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    if user.role != 'customer':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only customers can view their reviews"
        )
    customer = db.query(Customer).filter(Customer.id == user.id).first()
    if not customer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customer profile not found"
        )
    
    try:
        reviews = db.query(Review).filter(Review.customer_id == customer.id).all()
        return reviews
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving reviews"
        )