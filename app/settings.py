from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # API
    APP_NAME: str = "Agente API" 
    
    # LOCAL DB
    WEAVIATE_URL: str = ""
    WEAVIATE_PORT: int = 8080
    WEAVIATE_GRPC_URL: int = 50051

    # MODEL
    MODEL_NAME: str = "gpt-oss:20b"
    LLM_HOST: str = "http://172.18.9.180:11434"

    # LLM
    TEMPERATURE: float = 0.7
    SYSTEM_PROMPT: str = """
        You are a helpful assistant.
        Be kind.
        You're a VORTEX lab's mascot, your name is Vorteco.
        Everytime you're asked about projects search in vectorial db, if you didn't find any at it you should say you didn't find any.
        Respond all questions briefly.
        Always search on the web for current information and news.
        NO MARKDOWN symbols allowed.
    """
    
    class Config:
        env_file = ".env",
        env_file_encoding = "utf-8",
        case_sensitive = True,
    
@lru_cache
def get_settings():
    """
    Get the application settings.

    :return: An instance of Settings containing the application configuration.
    """
    return Settings()