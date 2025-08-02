from src.models.state import ToolState, IntentSchema
from src.utils.llm import model
from langchain_core.prompts import ChatPromptTemplate

# First, structure the LLM output
structured_model = model.with_structured_output(IntentSchema)

# Then build a prompt chain
intent_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an intent classifier. Classify the user's input into one of: 'weather', 'news', 'extract_user_info'. "
               "If the user provides name, email, or phone number, classify it as 'extract_user_info'."),
    ("human", "{input}")
])

# Combine the prompt and model
intent_model = intent_prompt | structured_model

def determine_intent(state: ToolState):
    intent = intent_model.invoke({"input": state["user_input"]}).intent
    return {"intent": intent}
