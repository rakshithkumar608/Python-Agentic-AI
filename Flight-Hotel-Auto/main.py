import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from tools import available_tools
from prompt import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

print("\n✈️ AI Travel Agent Started\n")

while True:

    user_query = input("Enter your request: ")

    if user_query.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )

    content = response.choices[0].message.content

    try:
        data = json.loads(content)
    except:
        print("\n⚠️ Invalid response from AI")
        print(content)
        continue

    tool_name = data.get("tool")
    tool_input = data.get("input", {})

    # Fix common AI parameter mistakes
    if "from" in tool_input:
        tool_input["origin"] = tool_input.pop("from")

    if "to" in tool_input:
        tool_input["destination"] = tool_input.pop("to")

    if "class" in tool_input:
        tool_input["cabin_class"] = tool_input.pop("class")

    # Only add cabin_class for flights
    if tool_name == "search_flights":
        tool_input.setdefault("cabin_class", "economy")

    tool_function = available_tools.get(tool_name)

    if not tool_function:
        print("❌ Tool not found")
        continue

    try:
        result = tool_function(**tool_input)
    except TypeError as e:
        print("⚠️ Tool input error:", e)
        print("Tool input received:", tool_input)
        continue

    print("\n✅ Results:\n")
    print(result)