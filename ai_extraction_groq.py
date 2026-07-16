import os
import json
from groq import Groq
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
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set in environment variables.")
        
    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": f"You extract triage fields from patient descriptions. The description might be in English, Tamil (தமிழ்), Hindi (हिंदी), or mixed languages. Understand the context and translate if necessary. Respond ONLY with valid JSON matching this schema: {json.dumps(EXTRACTION_SCHEMA)}. Default to the safer (more urgent) assumption if something is unclear."
            },
            {
                "role": "user",
                "content": f"Patient description: {text}"
            }
        ]
    )
    return json.loads(response.choices[0].message.content)
