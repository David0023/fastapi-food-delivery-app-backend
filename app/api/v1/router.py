from fastapi import APIRouter
from .endpoints.customer import router as customer_router

v1_router = APIRouter(
    prefix="/v1",
    tags=["v1"]
)

v1_router.include_router(customer_router)