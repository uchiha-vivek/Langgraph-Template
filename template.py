import os
from pathlib import Path

project_name = "src"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/azure_credentials.py",
    f"{project_name}/graph/__init__.py",
    f"{project_name}/graph/workflow.py",
    f"{project_name}/models/__init__.py",
    f"{project_name}/models/state.py",
    f"{project_name}/nodes/__init__.py",
    f"{project_name}/nodes/call_news.py",
    f"{project_name}/nodes/call_weather.py",
    f"{project_name}/nodes/determine_intent.py",
    f"{project_name}/nodes/generate_response.py",
    f"{project_name}/tools/__init__.py",
    f"{project_name}/tools/news.py",
    f"{project_name}/tools/weather.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/llm.py",
    "main.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "setup.py",
    ".gitignore"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    os.makedirs(filepath.parent, exist_ok=True)
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass
    else:
        print(f"File is already present at: {filepath}")
