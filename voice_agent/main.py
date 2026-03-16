import os
import asyncio
import speech_recognition as sr
import pyttsx3
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def main():

    r = sr.Recognizer()

    SYSTEM_PROMPT = """
    You're an expert voice agent.
    Respond like a helpful voice assistant.
    """

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    while True:

        try:
            with sr.Microphone() as source:

                r.adjust_for_ambient_noise(source)
                r.pause_threshold = 2

                print("🎤 Speak Something...")
                audio = r.listen(source)

            print("Processing audio... (STT)")
            stt = r.recognize_google(audio)

            print("You Said:", stt)

            messages.append({
                "role": "user",
                "content": stt
            })

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=messages
            )

            ai_reply = response.choices[0].message.content

            print("🤖 AI:", ai_reply)

            speak(ai_reply)

            messages.append({
                "role": "assistant",
                "content": ai_reply
            })

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError:
            print("Speech service error")


if __name__ == "__main__":
    main()