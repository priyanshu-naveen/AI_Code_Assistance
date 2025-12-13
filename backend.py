# backend.py (FAST STREAMING VERSION)
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3.2:1b"   # FASTEST for 8GB RAM

def ask_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}],
        "stream": True
    }

    response = requests.post(OLLAMA_URL, json=payload, stream=True)
    full_reply = ""

    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            if "message" in data:
                chunk = data["message"]["content"]
                full_reply += chunk
                yield chunk    # STREAM chunk by chunk (super fast)
