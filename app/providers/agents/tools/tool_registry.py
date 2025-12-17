from functools import lru_cache
from app.providers.agents.tools.dateandtime import DateTimeTool
from app.providers.agents.tools.semantic_search import SemanticSearchTool

@lru_cache()
def get_tools():
    """Returns the agent functions"""
    return [DateTimeTool, SemanticSearchTool]