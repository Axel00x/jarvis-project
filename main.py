from io_client import auto_listening, transcribe
from brain import call_gemini_api

if __name__ == "__main__":
    while True:
        audio = auto_listening()
        if audio is not None:
            text = transcribe(audio)
            print(f"{text}")
            print(call_gemini_api(text))