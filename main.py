import asyncio
from io_client import auto_listening, transcribe, tts
from brain import call_gemini_api

if __name__ == "__main__":
    while True:
        audio = auto_listening()
        if audio is not None:
            # Speech-to-text
            text = transcribe(audio)
            print(f"User: \t{text}")
            
            # AI request
            resp = call_gemini_api(text)
            print(f"AI: \t{resp}")
            
            # Text-to-speech
            asyncio.run(tts(resp))
            