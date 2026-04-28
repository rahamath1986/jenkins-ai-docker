import sys
import requests
import json

logs = sys.stdin.read()

payload = {
    "model": "mistral",
    "prompt": f"""
You are a CI/CD AI agent.
Analyze the following Jenkins build logs.
Explain the root cause and suggest a fix.

Logs:
{logs}
""",
    "stream": False
}

try:
    r = requests.post(
        "http://ollama:11434/api/generate",
        json=payload,
        timeout=60
    )
except Exception as e:
    print(f"[AI ERROR] Failed to contact Ollama: {e}")
    sys.exit(1)

# Parse JSON safely
try:
    data = r.json()
except json.JSONDecodeError:
    print("[AI ERROR] Ollama returned non‑JSON response")
    print(r.text)
    sys.exit(1)

# Handle different response formats
if "response" in data:
    print("\n=== AI ANALYSIS ===\n")
    print(data["response"])

elif "error" in data:
    print("\n=== AI ERROR ===\n")
    print(data["error"])
    sys.exit(1)

else:
    print("\n=== AI RAW RESPONSE (DEBUG) ===\n")
    print(json.dumps(data, indent=2))
