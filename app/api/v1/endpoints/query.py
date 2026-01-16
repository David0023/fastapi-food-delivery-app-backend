from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from enum import Enum

from app.schemas.query import RestaurantList
from app.utils.database import get_db
from app.api.deps import RestaurantPaginationParams

router = APIRouter(
    prefix='/queries',
    tags=['queries']
)





@router.get('/restaurants', response_model=RestaurantList)
def query_restaurants(params: RestaurantPaginationParams = Depends(), db: Session = Depends(get_db)):
    return