# lib
from fastapi import APIRouter

# pkg
from app.api.endpoints import navigation_api, login_api


ROUTERS = APIRouter()
ROUTERS.include_router( navigation_api.router )
ROUTERS.include_router( login_api.router )