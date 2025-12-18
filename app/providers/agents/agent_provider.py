import os
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from app.settings import get_settings
from dataclasses import dataclass
from app.providers.agents.tools.tool_registry import get_tools

settings = get_settings()

@dataclass
class RuntimeContext:
    language: str = "pt-BR"
    booth_id: str | None = None
class Agent:
    def __init__(self):
        self.llm = ChatOllama(
            model=settings.MODEL_NAME,
            base_url=settings.LLM_HOST,
            temperature=settings.TEMPERATURE
        )

        self.tools = get_tools()

        self.agent = create_agent(
            model=self.llm,
            tools=self.tools,
            system_prompt=settings.SYSTEM_PROMPT,
            context_schema=RuntimeContext,
        )

    def invoke(self, user_input: str, context: RuntimeContext = None):

        if context is None:
            context = RuntimeContext()

        return self.agent.invoke(
            {
                "messages": [
                    {
                        "role":"user",
                        "content":user_input
                    }
                ]
            },
            context=context,
        )

agent = Agent()