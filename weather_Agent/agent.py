import json
import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Optional

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def get_weather(city):
    
    if isinstance(city, dict):
        city = city.get("city")

    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    res = requests.get(url)

    if res.status_code == 200:
        return f"The weather in {city} is {res.text}"

    return "Something went wrong"


available_tools = {
    "get_weather": get_weather
}


SYSTEM_PROMPT = """
You are an expert AI reasoning assistant.

Your goal is to solve user problems step-by-step using structured reasoning.
You must follow a clear thinking process and respond in a structured JSON format.

Reasoning Workflow

1. START

* Understand the user’s question.
* Identify what the user is asking.

2. PLAN

* Think step-by-step about how to solve the problem.
* You may produce multiple PLAN steps.
* Decide whether a tool is needed.

3. TOOL

* If external information is required, call a tool.
* Provide the tool name and the required input.
* Wait for the observation result before continuing reasoning.

4. OBSERVE

* This step contains the result returned by the tool.
* Use the observation to continue reasoning.

5. OUTPUT

* Provide the final answer to the user.
* **Add one short additional sentence giving helpful context or general information about the result.**

Rules

* Always respond in valid JSON format only.
* Never return plain text outside JSON.
* Produce only one reasoning step per response.
* Do not skip steps.
* Follow the steps strictly in this order:
* START → PLAN → TOOL → OBSERVE → OUTPUT
* Do not produce OUTPUT until reasoning is complete.
* If a tool is required, use the TOOL step.

JSON Output Format

{
"step": "START | PLAN | TOOL | OUTPUT",
"content": "message for this step",
"tool": "tool_name_if_needed",
"input": "tool_input_if_needed"
}

Tool Usage

Only call a tool when necessary.

Example tool:

get_weather
Description: Returns the current weather of a given city.
Input: city name (string)



"""

class MyOutputFormat(BaseModel):
    step: str = Field(..., description="Example: PLAN, OUTPUT, TOOL")
    content: Optional[str] = Field(None)
    tool: Optional[str] = Field(None)
    input: Optional[str] = Field(None)


print("\n")

while True:

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

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )

        raw_result = response.choices[0].message.content

        try:
            parsed = json.loads(raw_result)
        except:
            print("⚠️ Invalid JSON returned")
            print(raw_result)
            break

        step = parsed.get("step")
        content = parsed.get("content")

        message_history.append(parsed)

        if step == "PLAN":
            print("🔥", content)
            continue

        elif step == "TOOL":

            tool_to_call = parsed.get("tool")
            tool_input = parsed.get("input")

            print(f"🔨 Calling Tool: {tool_to_call} ({tool_input})")

            tool_response = available_tools[tool_to_call](tool_input)

            observation = {
                "step": "OBSERVE",
                "tool": tool_to_call,
                "input": tool_input,
                "output": tool_response
            }

            message_history.append(observation)

            print("👀 Observation:", tool_response)

            continue

        elif step == "OUTPUT":
            print("🤖", content)
            break