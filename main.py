import os
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pipeline import process_emergency

from pathlib import Path

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
    try:
        result = process_emergency(symptom_text, disaster_mode=is_disaster)
    except Exception as e:
        print(f"Error processing triage logic: {e}")
        result = {
            "severity": "YELLOW",
            "reason": "We couldn't fully analyze the description. Please call 108 immediately to report the emergency to the medical operator.",
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
