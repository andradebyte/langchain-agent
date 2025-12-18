from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from app.services.logger import logger


class WebSearchInput(BaseModel):
    """Input para busca web."""
    query: str = Field(description="Consulta de busca na web")

class WebSearchTool(BaseTool):
    name: str = "buscar_web"
    description: str = """
    Busca informações atualizadas na web usando DuckDuckGo. 
    Use quando precisar de informações recentes, notícias, ou dados que não estão 
    na base de conhecimento interna.
    """
    args_schema: Type[BaseModel] = WebSearchInput
    
    def _run(self, query: str) -> str:
        """Executa busca na web."""
        try:
            search = DuckDuckGoSearchRun()
            results = search.run(query)
            return results
        except Exception as e:
            logger.error(f"Error in web search: {e}")
            return f"Erro ao buscar na web: {str(e)}"
    
    async def _arun(self, query: str) -> str:
        """Versão assíncrona."""
        return self._run(query)
