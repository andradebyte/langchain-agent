from fastapi import APIRouter, HTTPException, Form, Depends
from app.schemas.project import ProjectUpload, ProjectResponse
from app.services.logger import logger
from app.services.weaviate_service import weaviate_service

router = APIRouter(prefix="/weaviate")

@router.post("/index", response_model=ProjectResponse)
async def insert_single_project(project: ProjectUpload):
    """
    Injest a single project.
    """
    try:
        result = await weaviate_service.insert_project(project)
        return result
    except Exception as e:
        logger.error(f"Failed to insert project: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/projects", response_model=list[ProjectResponse])
async def list_projects(limit: int = 100):
    """
    List all projects from Weaviate.
    """
    try:
        results = await weaviate_service.list_all_projects(limit=limit)
        return results
    except Exception as e:
        logger.error(f"Failed to list projects: {e}")
        raise HTTPException(status_code=500, detail=str(e))