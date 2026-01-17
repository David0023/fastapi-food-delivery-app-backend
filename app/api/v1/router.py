from fastapi import APIRouter

from .endpoints.users.user import router as user_router
from .endpoints.users.admin import router as admin_router
from .endpoints.users.customer import router as customer_router
from .endpoints.users.driver import router as driver_router
from .endpoints.users.restaurant import router as restaurant_router
from .endpoints.query import router as query_router


v1_router = APIRouter(
    prefix="/v1",
    tags=["v1"]
)

v1_router.include_router(user_router)
v1_router.include_router(admin_router)
v1_router.include_router(customer_router)
v1_router.include_router(driver_router)
v1_router.include_router(restaurant_router)
v1_router.include_router(query_router)