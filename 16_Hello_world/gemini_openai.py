from dotenv import load_dotenv
from openai import OpenAI
import os 

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role" : "user",
            "content" : "Hey there everyone, who are you?"
        }
    ]
)

print(response.choices[0].message.content)