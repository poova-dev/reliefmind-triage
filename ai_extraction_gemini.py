import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

EXTRACTION_SCHEMA = {
    "type": "object",
    "properties": {
        "can_walk": {"type": "boolean"},
        "is_breathing": {"type": "boolean"},
        "breathing_labored": {"type": "boolean"},
        "pulse_present": {"type": "boolean"},
        "can_follow_commands": {"type": "boolean"}
    },
    "required": ["can_walk", "is_breathing", "breathing_labored", "pulse_present", "can_follow_commands"]
}

def extract_symptoms(text: str) -> dict:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set in environment variables.")
        
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        "gemini-2.0-flash",
        generation_config={
            "response_mime_type": "application/json",
            "response_schema": EXTRACTION_SCHEMA
        }
    )
    
    prompt = f"""Read this patient description and determine each field.
The description might be in English, Tamil (தமிழ்), Hindi (हिंदी), or mixed languages. Translate internally if necessary.
Default to the safer (more urgent) assumption if something is unclear or ambiguous.

Patient description: {text}"""
    response = model.generate_content(prompt)
    return json.loads(response.text)
