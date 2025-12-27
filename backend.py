import requests
import json

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3.2:1b"

SYSTEM_PROMPT = """
You are an AI Code Assistant.
Rules:
- Explain code step by step
- Write clean and optimized Python
- Mention time and space complexity if relevant
- Help with debugging clearly
"""

def ask_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "stream": True
    }

    response = requests.post(OLLAMA_URL, json=payload, stream=True)

    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            if "message" in data:
                yield data["message"]["content"]
