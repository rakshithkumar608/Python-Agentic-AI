import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

chat_completion = client.chat.completions.create(
{
        "role": "system",
        "content": "You are an expert in Maths and only and only ans maths related questions"   
        },
    model="llama-3.1-8b-instant"
)

print(chat_completion.choices[0].message.content)