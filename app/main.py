from fastapi import FastAPI
from app.api.meeting_api import router as meeting_router
from app.core.database import Base, engine
from app.api.auth_api import router as auth_router

# import models so SQLAlchemy sees them
from app.models import meeting, user

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(meeting_router, prefix="/api/v1")
app.include_router(auth_router)

