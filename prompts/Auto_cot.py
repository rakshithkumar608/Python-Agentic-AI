# Auto Chain-of-Thought Reasoning Agent

import os
import json
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are an expert reasoning AI assistant.

You solve problems using the following reasoning steps:

START → Understand the user problem
PLAN → Think step-by-step (multiple times)
OUTPUT → Final answer

Rules:
- Always respond in JSON format
- Only produce ONE step per response
- Do NOT jump directly to OUTPUT unless reasoning is complete
- Math and derivation problems must contain multiple PLAN steps

JSON Format:
{"step":"START | PLAN | OUTPUT","content":"text explanation"}
"""

print("\n")

user_query = input("🚀 Enter the user input: ")

message_history = []

while True:

    prompt = f"""
{SYSTEM_PROMPT}

Previous Steps:
{message_history}

User Question:
{user_query}
"""

  
    response = client.models.generate_content(
            model="gemini-3.1-pro-preview",
            contents=prompt,
            config={
                "response_mime_type": "application/json"
            }
        )


    raw_result = response.text

    try:
        parsed = json.loads(raw_result)
    except:
        print("⚠️ Invalid JSON returned")
        print(raw_result)
        break

    step = parsed.get("step")
    content = parsed.get("content")

    message_history.append(parsed)

    if step == "START":
        print("\n🔥 START")
        print("Understanding:", content)

    elif step == "PLAN":
        print("\n🧠 PLAN")
        print("Reasoning:", content)

    elif step == "OUTPUT":
        print("\n🤖 FINAL OUTPUT")
        print("Answer:", content)
        break

