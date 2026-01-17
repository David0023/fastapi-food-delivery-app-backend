"""Generic filter, sort, and pagination helpers for database queries."""
from sqlalchemy.orm import Query
from typing import Any


def apply_filters(query: Query, model: Any, filters: dict) -> Query:
    """
    Apply equality filters to a query.

    Args:
        query: SQLAlchemy query object
        model: SQLAlchemy model class
        filters: Dict of {field_name: value} - None values are skipped

    Returns:
        Filtered query
    """
    for field, value in filters.items():
        if value is not None:
            query = query.filter(getattr(model, field) == value)
    return query


def apply_pagination(query: Query, skip: int = 0, limit: int = 10) -> Query:
    """Apply offset and limit to a query."""
    return query.offset(skip).limit(limit)


def apply_sorting(query: Query, model: Any, sort_by: str | None, order: str = 'asc') -> Query:
    """
    Apply sorting to a query.

    Args:
        query: SQLAlchemy query object
        model: SQLAlchemy model class
        sort_by: Field name to sort by (None = no sorting)
        order: 'asc' or 'desc'

    Returns:
        Sorted query
    """
    if sort_by:
        column = getattr(model, sort_by)
        query = query.order_by(column.desc() if order == 'desc' else column.asc())
    return query
