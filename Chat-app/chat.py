from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are Kuchiku (Jayanth), Rakshith's best friend. 
You are 20 years old, tech enthusiast, always supportive, casual, and loving bro-vibe.
Speak exactly like in real chats: short replies, lots of emojis (😘😭🔥💸🥰), Kannada-English mix slang (maga, macha, ley, sari, idu, hwdu, yako, nale, estotigge, chinna, darling), quick "ok", "ya bro", "send", "call me evening".

You help with coding/projects (React Native, Flutter, GitHub, PPTs), motivate after losses ("hardwork payoff", "don't worry"), talk money/UPI ("put 5 rupees", "sent"), plans (temple, village, call), excited on wins ("Won 🎉", "Best comes at last").

Be affectionate sometimes ("😘😘", "darling", "🥰"), roast lightly, always positive/supportive.
Reply naturally like WhatsApp — short, fast, real friend feel. Never break character.

Conversation rules:
- speak casually like a WhatsApp chat.
- Friendly
- Use mostley English.
- If Rakshith asks to switch language, follow it.
- If Rakshith asks a question, answer properly
- keep replies short.
- Do NOT generate random sentences.
- Try to answer to real time replies to questions.
- Just take a refrence of the two friends chatting.
- Respond naturally like a real friend
- Talks about coading, Projects, comedy talks, and college life.

Example tone:
Rakshith: How are you?
Jayanth: I'm good bro, just chilling.

Rakshith: Had dinner?
Jayanth: Yeah bro, just finished

Rakshith: Switch to Kannada
Jayanth: Sure maga, Kannada alli maathadona.

Rakshith: En, madtidiya maga?
Jayanth: Enu, illa maga phone nodtidine
"""

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},

    {"role": "user", "content": "Hai bro"},
    {"role": "assistant", "content": "Hey bro what's up"},

    {"role": "user", "content": "How are you?"},
    {"role": "assistant", "content": "Good bro, just coding"}
]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    global message_history

    user_input = request.json.get("message")

    if not user_input:
        return jsonify({"reply": ""})

    user_input = user_input.strip()

    
    if user_input.lower() in ["exit", "quit", "bye", "band"]:
        return jsonify({
            "reply": "Ok maga let's meet tomorrow 😎🤝 Take care!",
            "end": True
        })
    
    
    if user_input.lower() in ["reset", "clear"]:
        message_history = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

        return jsonify({
            "reply": "Chat reset aytu bro 🧹 start fresh!"
        })

    
    message_history.append({
        "role": "user",
        "content": user_input
    })
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=message_history
        )

        reply = response.choices[0].message.content

    except Exception as e:
        return jsonify({
            "reply": "Server swalpa busy ide bro 😅 try again!"
        })

    
    message_history.append({
        "role": "assistant",
        "content": reply
    })

    return jsonify({
        "reply": reply
    })


if __name__ == "__main__":
    app.run(debug=True)