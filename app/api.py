from fastapi import APIRouter
from app.routers.ping import router as ping_router
from app.routers.agent import router as agent_router
from app.routers.project import router as project_router

api_router = APIRouter(prefix="/api/v1", tags=["api"])
api_router.include_router(ping_router)
api_router.include_router(agent_router)
api_router.include_router(project_router)