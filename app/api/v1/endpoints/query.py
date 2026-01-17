from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from enum import Enum

from app.schemas.query import RestaurantList
from app.utils.database import get_db
from app.api.deps import RestaurantPaginationParams, RestaurantFilterParams
from app.services.restaurant import get_restaurants

router = APIRouter(
    prefix='/queries',
    tags=['queries']
)

@router.get('/restaurants', response_model=RestaurantList)
def query_restaurants(
    filters: RestaurantFilterParams = Depends(),
    pagination: RestaurantPaginationParams = Depends(),
    db: Session = Depends(get_db)
):
    restaurants = get_restaurants(db, pagination, filters)

    return {
        'total': len(restaurants),
        'restaurants': restaurants
    }