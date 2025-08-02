from src.models.state import ToolState
from typing import Literal

def intent_router(state: ToolState) -> Literal["user_info_node", "weather_node", "news_node"]:
    if state["intent"] == "extract_user_info":
        return "user_info_node"
    elif state["intent"] == "weather":
        return "weather_node"
    elif state["intent"] == "news":
        return "news_node"
    else:
        raise ValueError(f"Unknown intent: {state['intent']}")
