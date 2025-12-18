from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type, Optional
from app.services.logger import logger
from app.services.weaviate_service import weaviate_service

class ProjectsSearchInput(BaseModel):
    """Input schema for semantic search."""
    query: str = Field(description="A pergunta ou termo de busca para encontrar projetos relevantes")
    limit: int = Field(default=5, description="Número máximo de resultados a retornar")
    
class ProjectsSearchTool(BaseTool):
    name: str = "busca_semantica_projetos"
    description: str = """
    Ferramenta para buscar projetos usando busca semântica.
    Use esta ferramenta quando o usuário perguntar sobre projetos, procurar exemplos,
    ou quiser encontrar projetos relacionados a um tema específico.
    
    Exemplos de uso:
    - "Encontre projetos sobre e-commerce"
    - "Quais projetos usam microserviços?"
    - "Me mostre projetos de IA"
    - "Busque projetos relacionados a pagamentos"
    """
    
    args_schema: Type[BaseModel] = ProjectsSearchInput
    def _run(self, query: str, limit: int = 5) -> str:
        """Execute semantic search synchronously"""
        try:
            projects = weaviate_service.client.collections.get("Project")
            
            response = projects.query.near_text(
                query=query,
                limit=limit,
                return_metadata=["distance"]
            )    
            
            if not response.objects:
                return f"Nenhum projeto encontrado para a busca: '{query}'"

            results = []
            
            for i, obj in enumerate(response.objects, 1):
                distance = obj.metadata.distance if obj.metadata else "N/A"
                title = obj.properties.get("title", "Sem título")
                description = obj.properties.get("description", "Sem descrição")
                tags = obj.properties.get("tags", [])
                
                results.append(
                    f"{i}. **{title}**\n"
                    f"   - Descrição: {description}\n"
                    f"   - Tags: {', '.join(tags) if tags else 'Nenhuma'}\n"
                    f"   - Relevância: {1 - float(distance):.2%}\n"
                )
                
            return (
                f"Encontrei {len(results)} projeto(s) para '{query}':\n\n" +
                "\n".join(results)
            )
        except Exception as e:
            logger.error(f"Error in semantic search: {e}")
            return f"Erro ao buscar projetos: {str(e)}"
        
    async def _arun(self, query: str, limit: int = 5) -> str:
        """Execute semantic search asynchronously"""
        return self._run(query, limit)