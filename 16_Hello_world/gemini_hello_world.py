import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="""You are an expert in Maths and only and only ans maths related questions. and if any questions rather than maths Don't answer to the question.
    
    Question:
    what is a + b whole square
    """
)

print(response.text)