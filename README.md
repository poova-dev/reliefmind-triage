# 🩺 ReliefMind Triage — Crisis Management, HealthTech & Emergency Response

ReliefMind Triage is an AI-powered bystander emergency triage assistant that helps people assess emergency severity and get critical first-aid guidance before an ambulance arrives.

---

## 🏆 Hackathon Submission Details
*   **Theme:** Crisis Management, HealthTech & Emergency Response
*   **Live Deployment Link:** [https://reliefmind-triage.vercel.app](https://reliefmind-triage.vercel.app)
*   **GitHub Repository Link:** [https://github.com/poova-dev/reliefmind-triage](https://github.com/poova-dev/reliefmind-triage)
*   **Demo Video Link:** *(Insert your 2-3 minute YouTube/Google Drive link here)*

---

## 📌 Problem Statement
*   **The Challenge:** In critical medical emergencies or mass-casualty disasters, bystanders are often panicked, unsure of how urgent the situation is, and do not know what first-aid actions to perform. Existing triage systems are expensive, proprietary, designed exclusively for hospital ER admission staff, and not accessible to the public.
*   **Who is Affected:** Bystanders, patients seeking urgent care, first responders, and emergency operators (e.g., 108 dispatchers).
*   **Why Solving It Matters:** Triage delay is a major contributor to preventable deaths. By empowering bystanders with an instant, structured emergency assessment tool, we can save lives during the critical "Golden Hour" before professional medical help arrives.

---

## 💡 Solution Description
ReliefMind Triage takes free-text description of symptoms (via text or voice), extracts structured physiological indicators using a Large Language Model with strict schema validation, and applies a deterministic START-based rule engine to output severity levels (RED, YELLOW, GREEN) along with immediate first-aid instructions.

### 🌟 Key Features
*   **Voice/Text Symptom Intake:** Allows patients or bystanders to describe the emergency in natural, conversational language.
*   **Strict JSON Schema Validation:** Symptom data is structured into clinical criteria (`can_walk`, `is_breathing`, `breathing_labored`, `pulse_present`, `can_follow_commands`) and strictly coerced on the backend.
*   **START Disaster Protocol Alignment:** Integrates a deterministic rules engine aligned with the Simple Triage and Rapid Treatment (START) protocol. Supports a **Disaster Mode Toggle** that prioritizes resources by marking ambulatory patients as Green to optimize triage throughput.
*   **Real-time Google Maps Integration:** Automatically displays nearby medical facilities using the Google Maps API.
*   **Automatic Radius Expansion (5km → 10km → 20km):** Recursively widens the search radius if 0 hospitals are found nearby to prevent dead-ends.
*   **One-Tap SOS Dialer:** Captures current coordinates, copies them to the clipboard, and triggers dialer to call `108` in a single tap.
*   **Safety Fallback UI:** Gracefully alerts the user and runs manual triage rules if AI extraction or remote map services fail.

---

## 🛠️ Tech Stack & AI Models
*   **Backend Framework:** Python 3.x, FastAPI, Jinja2 Templates, python-dotenv
*   **Frontend Technologies:** HTML5, Tailwind CSS, Google Maps JavaScript API, Leaflet (Map controls and layout styling)
*   **AI Models:** Groq API (Llama 3.3 70B) for structured symptom extraction and natural language processing
*   **APIs Used:** OpenStreetMap Nominatim API (Manual Location Geocoding), Overpass API (Multi-mirror hospital data fallback)
*   **Hosting & Deployment:** Vercel (Production)

---

## 💻 Local Setup & Installation

### Prerequisites
*   Python 3.9 or higher
*   Groq API Key (for symptom extraction)
*   Google Maps API Key (for maps rendering)

### Steps
1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/poova-dev/reliefmind-triage.git
    cd reliefmind-triage
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables:**
    Create a `.env` file in the root directory and add the following variables:
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
    ```

5.  **Run the Server Locally:**
    ```bash
    uvicorn main:app --reload
    ```
    Open `http://127.0.0.1:8000` in your web browser.

---

## 📈 Expected Impact
*   **Reduced Dispatch Times:** Instant translation of conversational reports into structured triage data.
*   **Empowered Bystanders:** Direct access to clear first-aid instructions based on the patient's severity.
*   **Resiliency during Disasters:** Optimized resource allocation in high-casualty events using the disaster triage engine.

---

## 🚀 Future Roadmap & Scalability
*   **Medical RAG (Retrieval-Augmented Generation):** Connect the AI symptom parser to a vector database containing official WHO (World Health Organization) and Red Cross clinical first-aid manuals to verify all guidelines and eliminate LLM hallucinations.
*   **Wearable & IoT Integration:** Allow the app to pull bio-telemetry feeds (e.g., heart rate, SpO2, ECG) directly from smartwatches and connected pulse oximeters to provide objective triage criteria.
*   **Trusted Clinical API Feeds:** Integrate with public databases like NIH's PubMed, MeSH, and RxNorm to cross-reference symptom profiles with real-time epidemiological feeds and drug safety databases.
