from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import relationship
from app.models.base import BaseModel, TimestampMixin

class Review(BaseModel, TimestampMixin):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), index=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'), index=True)
    content = Column(String, nullable=False)
    rating = Column(Integer)

    customer = relationship("Customer", back_populates='reviews', foreign_keys=[customer_id])
    restaurant = relationship("Restaurant", back_populates='reviews', foreign_keys=[restaurant_id])

    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='rating_range'),
        UniqueConstraint('customer_id', 'restaurant_id', name='unique_customer_restaurant_review'),
    )   