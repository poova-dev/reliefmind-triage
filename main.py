from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok", "message": "ReliefMind Triage API is live"}
