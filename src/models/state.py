from typing import TypedDict, Literal, Optional, Dict
from pydantic import BaseModel, Field

class ToolState(TypedDict, total=False):
    user_input: str
    intent: Literal["weather", "news", "extract_user_info"]
    tool_result: str
    result: str
    invoked_tool: str
    extracted_user_info: Optional[Dict[str, str]]

class IntentSchema(BaseModel):
    intent: Literal["weather", "news", "extract_user_info"] = Field(description="User's intent based on the query")
