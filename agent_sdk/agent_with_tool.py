from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": "You are a funny assistant who answers with emojis."
        },
        {
            "role": "user",
            "content": "What is the current weather in Mangaluru?"
        }
    ]
)

print(response.choices[0].message.content)