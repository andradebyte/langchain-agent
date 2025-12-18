from functools import lru_cache
from app.providers.agents.tools.dateandtime import DateAndTimeTool
from app.providers.agents.tools.semantic_search import ProjectsSearchTool
from app.providers.agents.tools.web_search import WebSearchTool

@lru_cache()
def get_tools():
    """Returns the agent functions"""
    return [DateAndTimeTool(), ProjectsSearchTool(), WebSearchTool()]