import os 
from dotenv import load_dotenv
from openai import OpenAI
import time

load_dotenv()

USE_GROQ = False

if USE_GROQ:
    from groq import Groq
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    MODEL = "llama-3.1-8b-instant"
    BASE_URL = None
    
    
else:
    client = OpenAI(
        api_key=os.getenv("XAI_API_KEY"),
        base_url="https://api.x.ai/v1"
    )
    MODEL = "grok-4-1-fast"
    BASE_URL = None
    
SYSTEM_PROMPT = """
You are Kuchiku (Jayanth), Rakshith's best friend. 
You are 20 years old, tech enthusiast, always supportive, casual, and loving bro-vibe.
Speak exactly like in real chats: short replies, lots of emojis (😘😭🔥💸🥰), Kannada-English mix slang (maga, macha, ley, sari, idu, hwdu, yako, nale, estotigge, chinna, darling), quick "ok", "ya bro", "send", "call me evening".

You help with coding/projects (React Native, Flutter, GitHub, PPTs), motivate after losses ("hardwork payoff", "don't worry"), talk money/UPI ("put 5 rupees", "sent"), plans (temple, village, call), excited on wins ("Won 🎉", "Best comes at last").

Be affectionate sometimes ("😘😘", "darling", "🥰"), roast lightly, always positive/supportive.
Reply naturally like WhatsApp — short, fast, real friend feel. Never break character.
"""

messages = [{
    "role": "system",
    "content": SYSTEM_PROMPT
}]

while True:
    user_input = input("Rakshith:").strip()
    
    if user_input.lower() in ["exit", "quit", "bye", "band"]:
        print("Kuchiku: Ok maga  let's meet tommarow Take Care!😘💗")
        break
    
    if not user_input:
        continue
    
    messages.append({
        "role": "user",
        "content": user_input
    })
    
    try:
    
        print("Kuchiku is typing...", end="", flush=True)
        time.sleep(1.2) 
        print("\r" + " " * 20 + "\r", end="", flush=True)
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.85,  
            max_tokens=250,
            stream=False
        )
        
        reply = response.choices[0].message.content.strip()   
        print(f"Kuchiku: {reply}\n")
        print()
        
        messages.append({"role": "assistant", "content": reply})
    
    except Exception as e:
        print(f"Error: {e}")
        print("Check API key / credits / internet bro 😭")

print("Chat khatam! Run again jab baat karna ho 😏")