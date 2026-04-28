import sys
import requests
import json
import os

JOB_NAME = os.getenv("JOB_NAME", "unknown")
BUILD_NUMBER = os.getenv("BUILD_NUMBER", "unknown")
BUILD_URL = os.getenv("BUILD_URL", "")
GIT_BRANCH = os.getenv("GIT_BRANCH", "unknown")

SLACK_WEBHOOK = os.environ.get("SLACK_WEBHOOK_URL")

logs = sys.stdin.read()


payload = {
    "model": "phi",  # stable, low‑memory model
    "prompt": f"""
You are an AI CI/CD failure analysis agent.

Given Jenkins build logs, respond in EXACTLY this format:

Exact error message:
<copy the exact error from the logs>

Root cause:
<one clear sentence explaining why it happened>

Suggested fix:
<one short actionable fix>

Do NOT add extra text.
Do NOT add explanations outside these sections.

Jenkins Metadata:
- Job: {JOB_NAME}
- Build: #{BUILD_NUMBER}
- Branch: {GIT_BRANCH}

Logs:
{logs}
""",
    "stream": False
}


# Step 1: Call Ollama
try:
    r = requests.post(
        "http://ollama:11434/api/generate",
        json=payload,
        timeout=60
    )
    data = r.json()
except Exception as e:
    result = f"AI error: {e}"
    data = {}

# Step 2: Extract AI summary
ai_summary = data.get("response", "AI could not generate summary.")

print("\n=== AI SUMMARY ===\n")
print(ai_summary)

# Step 3: Send to Slack
if SLACK_WEBHOOK:
    slack_payload = {
        "text": (
            "*🚨 Jenkins CI AI Summary*\n\n"
            f"```{ai_summary}```"
        )
    }
    try:
        requests.post(SLACK_WEBHOOK, json=slack_payload, timeout=10)
        print("\n✅ Slack notification sent")
    except Exception as e:
        print(f"\n⚠️ Slack failed: {e}")