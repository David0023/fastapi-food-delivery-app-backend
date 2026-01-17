from fastapi import FastAPI
from app.utils.database import Base, engine
from app.api.v1.router import v1_router
from app.api.auth import auth_router
from app.models import *

app = FastAPI()
app.include_router(v1_router)
app.include_router(auth_router)


# Create all tables in DB
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "root page"}