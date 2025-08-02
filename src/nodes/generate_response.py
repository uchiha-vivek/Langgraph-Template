from src.utils.llm import model
from src.models.state import ToolState

def generate_response(state: ToolState):
    prompt = f"""You are an assistant. Based on the tool output below, generate a friendly and informative response to the user query.

User Query: {state['user_input']}
Tool Output: {state['tool_result']}

Response:"""
    result = model.invoke(prompt).content
    return {"result": result}