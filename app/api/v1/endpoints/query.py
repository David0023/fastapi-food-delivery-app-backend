from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from enum import Enum

from app.schemas.query import RestaurantList, DriverList
from app.utils.database import get_db
from app.api.deps import RestaurantPaginationParams, RestaurantFilterParams, DriverPaginationParams, DriverFilterParams
from app.services.restaurant import get_restaurants
from app.services.driver import get_drivers

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

@router.get('/drivers', response_model=DriverList)
def query_drivers(
    filters: DriverFilterParams = Depends(),
    pagination: DriverPaginationParams = Depends(),
    db: Session = Depends(get_db)
):
    drivers = get_drivers(db, pagination, filters)

    return {
        'total': len(drivers),
        'drivers': drivers
    }