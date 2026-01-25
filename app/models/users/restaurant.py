from sqlalchemy import Column, String, Integer, ForeignKey, Float, Enum, func
from sqlalchemy.orm import relationship, Session
from app.core.enums import UserRole, CuisineStyle
from .user import User

class Restaurant(User):
    __tablename__ = "restaurants"

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    cuisine_style = Column(Enum(CuisineStyle), nullable=True)


    rating = Column(Float, default=None)
    review_count = Column(Integer, default=0)
    reviews = relationship("Review", back_populates="restaurant")

    __mapper_args__ = {"polymorphic_identity": UserRole.restaurant.value}

    def update_rating(self, db: Session):
        from app.models.review import Review
        
        count, avg = db.query(
            func.count(Review.id),
            func.avg(Review.rating)
        ).filter(Review.restaurant_id == self.id).first()
        
        self.review_count = count or 0
        self.rating = float(avg) if avg else None
