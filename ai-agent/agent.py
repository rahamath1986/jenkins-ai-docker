import sys
import requests

logs = sys.stdin.read()

response = requests.post(
    "http://ollama:11434/api/generate",
    json={
        "model": "mistral",
        "prompt": f"Analyze CI logs and suggest a fix:\n{logs}",
        "stream": False
    }
)

print(response.json()["response"])
