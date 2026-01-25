"""Pagination and Sort Dependency"""
from enum import Enum
from fastapi import Query
from typing import List
from app.core.enums import CuisineStyle, VehicleType


class SortOrder(str, Enum):
    asc = 'asc'
    desc = 'desc'


class BasePaginationParams:
    def __init__(
        self,
        skip: int = Query(0, ge=0),
        limit: int = Query(10, ge=0, le=100),
        order: SortOrder = Query(SortOrder.asc)
    ):
        self.skip = skip
        self.limit = limit
        self.order = order


#------------------------------------- Restaurant Specific -------------------------------------#
class RestaurantSortOption(str, Enum):
    name = 'name'
    rating = 'rating'

class RestaurantPaginationParams(BasePaginationParams):
    def __init__(
        self,
        skip: int = Query(0, ge=0),
        limit: int = Query(10, ge=0, le=100),
        sort_by: RestaurantSortOption | None = Query(None),
        order: SortOrder = Query(SortOrder.asc)
    ):
        super().__init__(skip, limit, order)
        self.sort_by = sort_by

class RestaurantFilterParams:
    def __init__(
            self,
            name: str | None = Query(None),
            cuisine_styles: List[CuisineStyle] | None = Query(None)
    ):
        self.name = name
        self.cuisine_styles = cuisine_styles or []

#------------------------------------- Driver Specific -------------------------------------#
class DriverSortOption(str, Enum):
    name = 'name'
    vehicle_type = 'vehicle_type'

class DriverPaginationParams(BasePaginationParams):
    def __init__(
        self,
        skip: int = Query(0, ge=0),
        limit: int = Query(10, ge=0, le=100),
        sort_by: DriverSortOption | None = Query(None),
        order: SortOrder = Query(SortOrder.asc)
    ):
        super().__init__(skip, limit, order)
        self.sort_by = sort_by

class DriverFilterParams:
    def __init__(
        self,
        is_available: bool = True,
        vehicle_types: List[VehicleType] | None = Query(None)
    ):
        self.is_available = is_available
        self.vehicle_types = vehicle_types or []