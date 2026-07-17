# ReliefMind Triage

AI-powered bystander emergency triage assistant. Helps people assess severity and get first-aid guidance before an ambulance arrives.

## Problem
During emergencies, bystanders don't know how urgent a situation is or what to do first. Existing triage tools (e.g., ERTRIAGE) are hospital-side, paid, and English-only.

## Solution
Takes a free-text description of symptoms, extracts structured data using an LLM, and applies a deterministic START/ESI-based rule engine to output RED/YELLOW/GREEN severity with first-aid guidance. Includes a disaster-mode toggle for mass-casualty scenarios.

## Tech Stack
- Backend: Python, FastAPI
- AI: Groq (Llama 3.3 70B) for structured symptom extraction
- Frontend: Jinja2 templates, Tailwind CSS
- Deployment: Railway / Cloud Hosting

## Setup
1. `python3 -m venv venv && source venv/bin/activate`
2. `pip install -r requirements.txt`
3. Add `.env` with `GROQ_API_KEY=your_key`
4. `uvicorn main:app --reload`

## Live Demo
- **Live Application:** [poova-dev-reliefmind-triage.vercel.app](https://poova-dev-reliefmind-triage.vercel.app)
- **Deployment Platform:** Vercel (Production)
