from triage_engine import run_triage
from ai_extraction_groq import extract_symptoms   # switch to ai_extraction_gemini if needed

def process_emergency(text: str) -> dict:
    structured_data = extract_symptoms(text)
    result = run_triage(structured_data)
    result["extracted_data"] = structured_data
    return result
