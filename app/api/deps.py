"""Pagination and Sort Dependency"""
from enum import Enum
from fastapi import Query
from typing import List
from app.core.enums import CuisineStyle


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
            name: str = Query(None),
            cusine_styles: List[CuisineStyle] = Query([])
    ):
        self.name = name
        self.cuisine_styles = cusine_styles