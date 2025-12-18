from typing import List, Dict, Any
from app.providers.agents.agent_provider import agent
from app.services.remove_md import remove_md
from app.services.logger import logger

class AgentService:
    """
    Service layer for agent operations
    """
    
    @staticmethod
    async def process_message(message: str) -> Dict[str, Any]:
        """
        Process a message through the agent and extract response data
        
        Args:
            message: User message to process
            
        Returns:
            Dictionary containing response, tools_usage, reasoning_tokens, and total_tokens
        """
        try:
            # Invoke agent
            result = agent.invoke(message)
            messages = result['messages']
            final_message = messages[-1]
            
            # Extract tools used
            tools_used = AgentService._extract_tools_used(messages)
            
            # Clean markdown from response
            response_text = await remove_md(message=final_message.content)
            
            # Extract usage metadata
            usage = final_message.usage_metadata
            
            return {
                "response": response_text,
                "tools_usage": tools_used,
                "reasoning_tokens": usage.get('output_token_details', {}).get('reasoning', 0),
                "total_tokens": usage.get('total_tokens', 0)
            }
            
        except Exception as e:
            logger.error(f"Erro ao processar mensagem no AgentService: {str(e)}")
            raise
    
    @staticmethod
    def _extract_tools_used(messages: List[Any]) -> List[str]:
        """
        Extract unique tool names from agent messages
        
        Args:
            messages: List of agent messages
            
        Returns:
            List of unique tool names used
        """
        tools_used = []
        
        for msg in messages:
            if hasattr(msg, 'tool_calls') and msg.tool_calls:
                for tool_call in msg.tool_calls:
                    tools_used.append(tool_call['name'])
        
        return list(dict.fromkeys(tools_used))

agent_service = AgentService()
