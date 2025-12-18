"""
Data schemas for requests and responses.
"""

from pydantic import BaseModel, Field
from typing import Optional

class ProjectUpload(BaseModel):
    """
    Schema for uploading a single Project Document.
    """
    title: str = Field(..., description="Project Title.")
    description: str = Field(..., description="Project Descrirption.")
    tags: Optional[list[str]] = Field(None, description="Project TAGS.")
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Nome do projeto.",
                "description": "Descrição do projeto",
                "tags": ["TAG1","TAG2","TAG3"]
            }
        }
        
class ProjectResponse(BaseModel):
    """
    Schema for return a single Project Document.
    """
    title: str
    description: str
    tags: list[str]
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Nome do projeto.",
                "description": "Descrição do projeto",
                "tags": ["TAG1","TAG2","TAG3"]
            }
        }