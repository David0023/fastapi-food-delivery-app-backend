"""Restaurant service layer for database operations."""
from sqlalchemy.orm import Session
from typing import List

from app.models.users.driver import Driver
from app.api.deps import DriverPaginationParams, DriverFilterParams
from app.services.filters import apply_filters, apply_pagination, apply_sorting


def get_drivers(
    db: Session,
    pagination: DriverFilterParams,
    filters: DriverFilterParams | None = None
) -> List[Driver]:
    """
    Get list of restaurants with filtering, sorting, and pagination.

    Args:
        db: Database session
        pagination: Pagination and sort parameters
        filters: Optional class for filtering

    Returns:
        List of Driver objects
    """
    query = db.query(Driver)

    if filters.is_available:
        query = query.filter(Driver.is_available == filters.is_available)

    if filters.vehicle_types:
        query = query.filter(Driver.vehicle_type.in_(filters.vehicle_types))

    if pagination.sort_by:
        query = apply_sorting(query, Driver, pagination.sort_by.value, pagination.order.value)

    query = apply_pagination(query, pagination.skip, pagination.limit)

    return query.all()


def get_driver_by_id(db: Session, restaurant_id: int) -> Driver | None:
    """Get a single driver by ID."""
    return db.query(Driver).filter(Driver.id == restaurant_id).first()
