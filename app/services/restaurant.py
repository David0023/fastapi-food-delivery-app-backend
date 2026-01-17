"""Restaurant service layer for database operations."""
from sqlalchemy.orm import Session
from typing import List

from app.models.users.restaurant import Restaurant
from app.api.deps import RestaurantPaginationParams
from app.services.filters import apply_filters, apply_pagination, apply_sorting


def get_restaurants(
    db: Session,
    params: RestaurantPaginationParams,
    filters: dict | None = None
) -> List[Restaurant]:
    """
    Get list of restaurants with filtering, sorting, and pagination.

    Args:
        db: Database session
        params: Pagination and sort parameters
        filters: Optional dict of {field_name: value} for filtering

    Returns:
        List of Restaurant objects
    """
    query = db.query(Restaurant)

    if filters.name:
        query = query.filter(Restaurant.name.ilike(f"%{filters.name}%"))

    if filters.cuisine_styles:
        query = query.filter(Restaurant.cuisine_style.in_filters.cuisine_styles)

    if params.sort_by:
        query = apply_sorting(query, Restaurant, params.sort_by.value, params.order.value)

    query = apply_pagination(query, params.skip, params.limit)

    return query.all()


def get_restaurant_by_id(db: Session, restaurant_id: int) -> Restaurant | None:
    """Get a single restaurant by ID."""
    return db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
