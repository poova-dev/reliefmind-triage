import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pipeline import process_emergency

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/", response_class=HTMLResponse)
def landing(request: Request):
    return templates.TemplateResponse(request=request, name="landing.html", context={})

@app.get("/input", response_class=HTMLResponse)
def input_page(request: Request):
    return templates.TemplateResponse(request=request, name="input.html", context={})

@app.post("/result", response_class=HTMLResponse)
def result_page(request: Request, symptom_text: str = Form(...), disaster_mode: str = Form(None)):
    is_disaster = disaster_mode == "true"
    
    # 1. Enforce length limit to prevent abuse/spam
    if symptom_text and len(symptom_text) > 2000:
        symptom_text = symptom_text[:2000]
        
    try:
        result = process_emergency(symptom_text, disaster_mode=is_disaster)
        result["ai_failed"] = False
    except Exception as e:
        import sys
        import traceback
        print(f"CRITICAL ERROR in process_emergency: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        
        # Fallback safe values
        result = {
            "severity": "YELLOW",
            "reason": "AI Symptom Extraction is currently offline. Please call 108 immediately to report your emergency to the medical operator.",
            "ai_failed": True,
            "extracted_data": {
                "can_walk": False,
                "is_breathing": True,
                "breathing_labored": False,
                "pulse_present": True,
                "can_follow_commands": True,
                "disaster_mode": is_disaster
            }
        }
    return templates.TemplateResponse(request=request, name="result.html", context={"result": result})

@app.get("/hospitals", response_class=HTMLResponse)
def hospitals_page(request: Request):
    return templates.TemplateResponse(request=request, name="hospitals.html", context={
        "google_maps_api_key": os.environ.get("GOOGLE_MAPS_API_KEY", "")
    })
