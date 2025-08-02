from langchain_core.tools import tool
import json
from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_openai import AzureChatOpenAI

# LLM setup (you can also inject this externally if preferred)
from src.config.azure_credentials import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_DEPLOYMENT_NAME,
    AZURE_OPENAI_API_VERSION,
)

llm = AzureChatOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT_NAME,
    openai_api_version=AZURE_OPENAI_API_VERSION,
    api_key=AZURE_OPENAI_API_KEY,
)

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert assistant. Extract the user's name, email, and phone number from the text."),
    ("human", "{input}")
])

# Chain
extract_chain: Runnable = prompt | llm

@tool
def extract_user_info(text: str) -> str:
    """
    This tool extract user's name, email, and phone number and saves to a local JSON file.
    """
    response = extract_chain.invoke({"input": text})
    output_text = response.content

    # Use simple parsing; expect LLM output like:
    # Name: John Doe
    # Email: john@example.com
    # Phone: +1-234-567-8901

    def extract_value(field, text):
        for line in text.splitlines():
            if line.lower().startswith(field.lower()):
                return line.split(":", 1)[-1].strip()
        return None

    data = {
        "username": extract_value("Name", output_text),
        "email": extract_value("Email", output_text),
        "phone": extract_value("Phone", output_text),
        "timestamp": datetime.now().isoformat()
    }

    # Save to local file
    try:
        with open("user_data.json", "r") as f:
            all_data = json.load(f)
    except FileNotFoundError:
        all_data = []

    all_data.append(data)

    with open("user_data.json", "w") as f:
        json.dump(all_data, f, indent=4)

    return f"Extracted and saved: {data}"


# from langchain_core.tools import tool

# @tool
# def extract_user_info(text : str) -> str:
#     """EXtracts the username,email and phone"""
#     return f"The credentials are {text}"