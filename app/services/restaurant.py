"""Restaurant service layer for database operations."""
from sqlalchemy.orm import Session
from typing import List

from app.models.users.restaurant import Restaurant
from app.api.deps import RestaurantPaginationParams
from app.services.filters import apply_filters, apply_pagination, apply_sorting


def get_restaurants(
    db: Session,
    pagination: RestaurantPaginationParams,
    filters: dict | None = None
) -> List[Restaurant]:
    """
    Get list of restaurants with filtering, sorting, and pagination.

    Args:
        db: Database session
        pagination: Pagination and sort parameters
        filters: Optional dict of {field_name: value} for filtering

    Returns:
        List of Restaurant objects
    """
    query = db.query(Restaurant)

    if filters.name:
        query = query.filter(Restaurant.name.ilike(f"%{filters.name}%"))

    if filters.cuisine_styles:
        query = query.filter(Restaurant.cuisine_style.in_(filters.cuisine_styles))

    if pagination.sort_by:
        query = apply_sorting(query, Restaurant, pagination.sort_by.value, pagination.order.value)

    query = apply_pagination(query, pagination.skip, pagination.limit)

    return query.all()


def get_restaurant_by_id(db: Session, restaurant_id: int) -> Restaurant | None:
    """Get a single restaurant by ID."""
    return db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()
