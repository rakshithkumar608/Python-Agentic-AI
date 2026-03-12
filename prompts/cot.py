# Chain of thought Prompting



import os
from dotenv import load_dotenv
from google import genai

import json

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are an expert AI Assistant in resolving user queries using chain of thought.
You work on START, PLAN and Output steps.
You need to first PLAN what needs to br done. The PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT

Rules:
- Strictly Follow the given JSON output format
- Only run one step at a time.
- The sequence of steps is START (Where user gives an input), PLAN (That can br multiple times) and finally OUTPUT (which is going to the displayed to the user).

Oupput JSON Format:
{"step": "START" | "PLAN" | "OUTPUT", "content" : "string"}

Example:
START: Hey, can you solve 2 + 3 * 5 /10
PLAN: {"step": "PLAN": "content": "Seems like user is intrested in math problem}
PLAN: {"step":"PLAN":"content": "Lookinh at the problem, we should solve this using BODMAS method"}
PLAN: {"step":"PLAN":"content": "Yes, The BODMAS is correct thing to be done here"}
PLAN: {"step":"PLAN":"content": "first we must multiply 3 * 5 which is 15"}
PLAN: {"step":"PLAN":"content": "Now the new question is 2 + 15 / 10"}
PLAN: {"step":"PLAN":"content": "We must perform divide that is 15 / 10 = 1.5"}
PLAN: {"step":"PLAN":"content": "Now the question is 2 + 1.5"}
PLAN: {"step":"PLAN":"content": "Now finally lets perform the add 3.5"}
PLAN: {"step":"PLAN":"content": "Great, we have solved and finally left with 3.5 as ans"}
OUTPUT: {"step":"OUTPUT":"content": "3.5"}
"""



USER_PROMPT = """
Hey write a code to add n numbers in js
{
    "role": "assistant", "content": json.dumps({"step": "START", "content" : "User wants a JavaScript code snippet to add 'n' numbers."})
}

{
    "role": "assistant", "content": json.dumps({"step": "PLAN", "content" : "I should create a JavaScript function that takes an array of numbers as an argument."})
}

{
    "role": "assistant", "content": json.dumps({"step": "PLAN", "content" : "I will implement a flexible function using the rest parameter syntax to handle any number of arguments or an array."})
}
"""



response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=f"""
{SYSTEM_PROMPT}

User Question:
{USER_PROMPT}
""",
config={
    "response_mime_type": "application/json",
    "response_schema": {
        "type": "object",
        "properties": {
            "step":{
                "type": "string",
            },
            "content": {
                "type":"string"
            }
        }
    }
}
)

print(response.text)