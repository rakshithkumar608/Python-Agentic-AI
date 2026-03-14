
import json
import os
import requests
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel, Field
from typing import Optional

load_dotenv()

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    res = requests.get(url)
    
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    
    
    return "Something went wrong"

available_tools = {
    "get_weather": get_weather
}

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are an expert reasoning AI assistant.

You solve problems using the following reasoning steps:

START → Understand the user problem
PLAN → Think step-by-step (multiple times)
OUTPUT → Final answer
You Can also call a tool if required from the list of available tools.
for every tool call wait for the observe step which is the output from the called tool

Rules:
- Always respond in JSON format
- Only produce ONE step per response
- Do NOT jump directly to OUTPUT unless reasoning is complete


Output JSON Format:
{"step":"START | PLAN | OUTPUT" | "TOOL","content":"string", "tool":"string","input":"string"}

Available Tools:
- get_weather: Takes city name as an input string and return the weather info about the city.

Example:
START: What is the weather of Delhi?
PLAN: {"step":"PLAN":"content":"Seems like user is intrested in getting weather of Delhi in India"}
PLAN: {"step":"PLAN":"content":"Let's see if we have any available tool from the list of available tools"}
PLAN: {"step":"PLAN":"content":"Great, we have get_weather tool available for this query."}
PLAN: {"step":"PLAN":"content":"I need to call get_weather tool for delhi as input for city."}
PLAN: {"step":"TOOL":"tool":"get_weather", "input":"delhi"}
PLAN: {"step":"OBSERVE":"tool":"get_weather", "output":"The temp of delhi is cloudy with 20c"}
PLAN: {"step":"PLAN":"content":"Great, I got the weather info about delhi."}
OUTPUT: {"step":"OUTPUT":"content":"The current weather in delhi is 20 C with some cloudy sky"}
"""

print("\n")

class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step.Example: PLAN, OUTPUT, TOOL, etc")
    content: Optional[str] = Field(None, description="The optional string content for the step")
    tool: Optional[str] = Field(None, description="The ID of the tool to call.")
    input: Optional[str] = Field(None, description="The input for the tool")

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

  
    response = client.models.generate_content.parse(
            model="gemini-3.1-pro-preview",
            contents=prompt,
            config={
                "response_mime_type": "application/json"
            }
        )


    raw_result = response.choice[0].message.parsed

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
        print("🔥", parsed_result.content)
        continue
        
        if parsed_result.step == "TOOL":
            tool_to_call = parsed_result.tool
            tool_input = parsed_result.input
            print(f"🔨:{tool_to_call} ({tool_input})")
            
            tool_response = available_tools[tool_to_call](tool_input)
            message_history.append({"role":"developer", "content":json.dump(
                {"step":"OBSERVE", "tool":"tool_to_call", "input": tool_input, "output": tool_response}
            )})
            continue

    elif step == "PLAN":
        print("🔥", parsed_result.content)
        continue

    elif step == "OUTPUT":
        print("\🤖", parsed_result.content)
        break

