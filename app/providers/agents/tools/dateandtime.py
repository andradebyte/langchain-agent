from datetime import datetime
from zoneinfo import ZoneInfo
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type, Optional

class DateTimeInput(BaseModel):
    """Input schema - vazio pois não precisa de parâmetros."""
    timezone: str = Field(default="UTC", description="Timezone")

class DateTimeTool(BaseTool):
    name: str = "data_hora_atual"
    description: str = "Retorna a data e hora atual. Use quando o usuário perguntar que dia é hoje ou que horas são."
    args_schema: Type[BaseModel] = DateTimeInput
    
    def _run(self, timezone: str = "UTC") -> str:
        """Retorna data e hora atual."""
        now = datetime.now(ZoneInfo(timezone))
        return f"A data e hora atual é: {now.strftime('%d/%m/%Y às %H:%M:%S')}, ({timezone})"
    
    async def _arun(self) -> str:
        """Versão assíncrona."""
        return self._run()