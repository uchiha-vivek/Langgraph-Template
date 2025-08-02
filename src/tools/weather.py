from langchain_core.tools import tool

@tool
def get_weather(location: str) -> str:
    """Returns the weather of a location."""
    return f"The weather in {location} is "