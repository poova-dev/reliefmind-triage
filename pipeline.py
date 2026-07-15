from triage_engine import run_triage
from ai_extraction_groq import extract_symptoms

def process_emergency(text: str, disaster_mode: bool = False) -> dict:
    structured_data = extract_symptoms(text)
    structured_data["disaster_mode"] = disaster_mode
    result = run_triage(structured_data)
    result["extracted_data"] = structured_data
    return result
