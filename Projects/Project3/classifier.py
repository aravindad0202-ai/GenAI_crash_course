import os
from google import genai
from dotenv import load_dotenv

load_dotenv('.env')

client = genai.Client()

def AI_classifier(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )
    return response.text