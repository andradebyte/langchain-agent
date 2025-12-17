from fastapi import FastAPI
from app.services.logger import logger
from app.api import api_router
from app.settings import get_settings

app = FastAPI(
    title="P3dia Agent",
    description="API with LangChain Agent"
)

# Routes
app.include_router(api_router)

@app.on_event("startup")
async def startup():
    logger.info("API started successfully")
    logger.info(get_settings().OPENAI_API_KEY)
    
@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutting down...")
