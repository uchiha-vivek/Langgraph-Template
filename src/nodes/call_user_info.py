from src.tools.user_info import extract_user_info
from src.models.state import ToolState
import json

def call_user_info(state: ToolState):
    tool_output = extract_user_info.invoke({"text": state['user_input']})
    
    # Optional: Parse tool_output back to dict if needed
    try:
        parsed_output = json.loads(tool_output)
    except Exception:
        parsed_output = {"raw": tool_output}
    
    return {
        "tool_result": tool_output,
        "invoked_tool": "extract_user_info",
        "extracted_user_info": parsed_output
    }
