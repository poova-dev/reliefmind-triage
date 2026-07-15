from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pipeline import process_emergency

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

MOCK_HOSPITALS = [
    {"name": "Government General Hospital", "distance": "1.2 km", "type": "Trauma Center", "maps_link": "https://maps.google.com"},
    {"name": "Apollo Hospital", "distance": "2.5 km", "type": "Multi-specialty", "maps_link": "https://maps.google.com"},
    {"name": "Primary Health Centre - Anna Nagar", "distance": "0.8 km", "type": "PHC", "maps_link": "https://maps.google.com"},
]

@app.get("/", response_class=HTMLResponse)
def landing(request: Request):
    return templates.TemplateResponse("landing.html", {"request": request})

@app.get("/input", response_class=HTMLResponse)
def input_page(request: Request):
    return templates.TemplateResponse("input.html", {"request": request})

@app.post("/result", response_class=HTMLResponse)
def result_page(request: Request, symptom_text: str = Form(...), disaster_mode: str = Form(None)):
    is_disaster = disaster_mode == "true"
    result = process_emergency(symptom_text, disaster_mode=is_disaster)
    return templates.TemplateResponse("result.html", {"request": request, "result": result})

@app.get("/hospitals", response_class=HTMLResponse)
def hospitals_page(request: Request):
    return templates.TemplateResponse("hospitals.html", {"request": request, "hospitals": MOCK_HOSPITALS})
