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
So if the question is about to write the code so write the code
"""

USER_PROMPT = """
1.What is syntax for exception handling in Java
2.Write a Python code to find out the even or odd number
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