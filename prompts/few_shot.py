# Zero Shot prompting

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are an expert in Coding.
Only answer coding related questions.
If the question is not about coding, politely refuse to answer.

Rule:
- Strictly follow the output in JSON formate

Output Formate:
{{
    "code": "string" or None,
    "isCoadingQuestion": boolean
}}

Example:
Q: Can you explain the a + b whole square?
A: {{ "code": null, "isCoadingQuestion": false }}

Q: Hey, write a code in python for adding two numbers.
A: def add(a,b):
        return a + b
"""

USER_PROMPT = """
Q: Hey, write a code to add n numbers in js.

"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
{SYSTEM_PROMPT}

User Question:
{USER_PROMPT}
"""
)

print(response.text)# Zero Shot prompting

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are an expert in Coding.
Only answer coding related questions.
If the question is not about coding, politely refuse to answer.

Rule:
- Strictly follow the output in JSON formate

Output Formate:
{{
    "code": "string" or None,
    "isCoadingQuestion": boolean
}}

Example:
Q: Can you explain the a + b whole square?
A: {{ "code": null, "isCoadingQuestion": false }}

Q: Hey, write a code in python for adding two numbers.
A: def add(a,b):
        return a + b
"""

USER_PROMPT = """
Q: Hey, write a code to add n numbers in js.

"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
{SYSTEM_PROMPT}

User Question:
{USER_PROMPT}
"""
)

print(response.text)