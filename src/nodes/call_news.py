from src.tools.news import get_news
from src.models.state import ToolState

def call_news(state: ToolState):
    tool_result = get_news.invoke({"topic": state['user_input']})
    return {"tool_result": tool_result, "invoked_tool": "get_news"}