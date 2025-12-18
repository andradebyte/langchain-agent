from datetime import datetime
from zoneinfo import ZoneInfo
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type, Optional
from app.services.logger import logger

class DateAndTimeInput(BaseModel):
    """Input schema - vazio pois não precisa de parâmetros."""
    timezone: str = Field(default="UTC", description="Timezone")

class DateAndTimeTool(BaseTool):
    name: str = "data_hora_atual"
    description: str = "Retorna a data e hora atual. Use quando o usuário perguntar que dia é hoje ou que horas são."
    args_schema: Type[BaseModel] = DateAndTimeInput
    
    def _run(self, timezone: str = "UTC") -> str:
        """Retorna data e hora atual."""
        try:
            now = datetime.now(ZoneInfo(timezone))
            return f"A data e hora atual é: {now.strftime('%d/%m/%Y às %H:%M:%S')}, ({timezone})"
        except Exception as e:
            logger.error(f"Error in semantic search: {e}")
            return f"Erro ao buscar projetos: {str(e)}"
    
    async def _arun(self, timezone: str = "UTC") -> str:
        """Versão assíncrona."""
        return self._run(timezone)