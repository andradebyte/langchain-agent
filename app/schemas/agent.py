"""
Data schemas for AgentRequests and Responses.
"""

from pydantic import BaseModel, Field
from typing import Optional, List

class AgentRequest(BaseModel):
    """
    Schema for INPUT an answer to the Agent.
    """
    message: str
    
class AgentResponse(BaseModel):
    """
    Schema for OUTPUT of an Agent.
    """
    response: str
    tools_usage: Optional[List[str]] = Field(
        default=[], description="Ferramentas que foram usadas"
    )
    reasoning_tokens: int
    total_tokens: int