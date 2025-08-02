from langchain_core.tools import tool

@tool
def get_news(topic: str) -> str:
    """Returns the news of any topic."""
    return f"Here is the latest news about {topic}"