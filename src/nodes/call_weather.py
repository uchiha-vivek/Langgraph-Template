from src.tools.weather import get_weather
from src.models.state import ToolState

def call_weather(state: ToolState):
    tool_result = get_weather.invoke({"location": state['user_input']})
    return {"tool_result": tool_result, "invoked_tool": "get_weather"}