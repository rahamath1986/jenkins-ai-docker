import sys
import requests

logs = sys.stdin.read()

response = requests.post(
    "http://ollama:11434/api/generate",
    json={
        "model": "mistral",
        "prompt": f"""
You are a CI/CD AI agent.
Analyze these Jenkins logs.
Explain error and suggest fix.

Logs:
{logs}
""",
        "stream": False
    }
)

print(response.json()["response"])