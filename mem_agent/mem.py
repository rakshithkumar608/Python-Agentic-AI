from mem0 import Memory
import os
from dotenv import load_dotenv
from groq import Groq
import json

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq client
client = Groq(api_key=GROQ_API_KEY)

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "groq",
        "config": {
            "api_key": GROQ_API_KEY,
            "model": "text-embedding-3-small"
        }
    },
    "llm": {
        "provider": "groq",
        "config": {
            "api_key": GROQ_API_KEY,
            "model": "llama-3.1-8b-instant"
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333
        }
    }
}

# Initialize memory once
mem_client = Memory.from_config(config)

while True:

    user_query = input("> ")
    
    search_memory = mem_client.search(query= user_query)
    
    memories = [
        f"ID: {mem.get("id")}\nMemory: {mem.get("memory")}" for mem in search_memory.get("results")
    ]
    
    print("Found Memories", memories)
    
    SYSTEM_PROMPT = f"""
    Here is the context about the user:
    {json.dumps(memories)}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": user_query
            }
        ]
    )

    ai_response = response.choices[0].message.content

    print("AI:", ai_response)

    mem_client.add(
        user_id="rakshith",
        messages=[
            {
                "role": "user",
                "content": user_query
            },
            {
                "role": "assistant",
                "content": ai_response
            }
        ]
    )

    print("Memory has been saved...")