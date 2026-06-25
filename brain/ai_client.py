from google import genai
from google.genai import types

client = genai.Client()

def call_gemini_api(prompt):
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="You are Jarvis, a helpful voice assistant. You will answer the user's questions very concisely, in a friendly yet formal tone"
        )
    )
            
    return response.text