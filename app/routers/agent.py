from fastapi import APIRouter, HTTPException
from app.schemas.agent import AgentRequest, AgentResponse
# from app.providers.agents.agent_provider import create_langchain_agent
from app.providers.agents.agent_provider import agent
from app.services.logger import logger

router = APIRouter(prefix="/agent")

@router.post("/")
async def agent_talk(request: AgentRequest):
    """
    Endpoint to talk to an agent
    """
    try:
        # agent = create_langchain_agent()
        
        # result = agent.invoke(
        #     {"messages": [{"role": "user", "content": request.message}]}
        # )
        
        result = agent.invoke(request.message)

        final_message = result['messages'][-1]
        response_text = final_message.content
        
        usage = final_message.usage_metadata
        
        return AgentResponse(
            response=response_text,
            reasoning_tokens=usage.get('output_token_details', {}).get('reasoning', 0),
            total_tokens=usage.get('total_tokens', 0)
        )
    except Exception as e:
        logger.error(f"Erro ao processar requisição: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao processar: {str(e)}")
        
