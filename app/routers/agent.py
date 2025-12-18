from fastapi import APIRouter, HTTPException
from app.schemas.agent import AgentRequest, AgentResponse
from app.services.logger import logger
from app.services.agent_service import agent_service

router = APIRouter(prefix="/agent")

@router.post("/")
async def agent_talk(request: AgentRequest):
    """
    Endpoint to talk to an agent
    """
    try:
        result = await agent_service.process_message(request.message)
        return AgentResponse(**result)
    except Exception as e:
        logger.error(f"Erro ao processar requisição: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao processar: {str(e)}")