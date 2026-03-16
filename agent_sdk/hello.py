from dotenv import load_dotenv
from typing import Any
from agents import Agent, Runner
import os

load_dotenv()


os.environ["OPENAI_TRACING_DISABLED"] = "1"


os.environ["OPENAI_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_BASE_URL"] = "https://api.groq.com/openai/v1"

hello_agent = Agent[Any](
    name="hello world Agent",
    instructions="You're an agent which greets the user and helps them answer using emojis and in a funny way",
    model="llama-3.1-8b-instant"
)

result = Runner.run_sync(
    hello_agent,
    "Hey There, My name is Rakshith!"
)

print(result.final_output)