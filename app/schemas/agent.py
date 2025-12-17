"""
Data schemas for AgentRequests and Responses.
"""

from pydantic import BaseModel

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
    reasoning_tokens: int
    total_tokens: int