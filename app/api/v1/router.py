from fastapi import APIRouter

from .endpoints.user import router as user_router
from .endpoints.admin import router as admin_router
from .endpoints.customer import router as customer_router
from .endpoints.driver import router as driver_router
from .endpoints.restaurant import router as restaurant_router


v1_router = APIRouter(
    prefix="/v1",
    tags=["v1"]
)

v1_router.include_router(user_router)
v1_router.include_router(admin_router)
v1_router.include_router(customer_router)
v1_router.include_router(driver_router)
v1_router.include_router(restaurant_router)