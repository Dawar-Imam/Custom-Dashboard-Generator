# Custom Dashboard Generation

A full-stack application combining FastAPI backend and Streamlit frontend for custom dashboard generation.

## Project Structure

- **backend/**: FastAPI backend application with API routes, schemas, services, and database configuration
- **frontend/**: Streamlit frontend application with pages, components, and API client services

## Repo Structure

```bash
Custom Dashboard Generation/
│
├── .git/
├── .gitignore
├── LICENSE
├── README.md
├── setup.sh
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── dashboard_generation.py
│   │   │   ├── __init__.py
│   │   │   ├── router.py
│   │   │
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── config.py
│   │   │   ├── logging.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── schema.py
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── webpage_generation_pipeline.py
│   │   │
│   │   ├── database/
│   │   │   ├── __init__.py
│   │   │   └── db.py
│   │   │
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   └── save_generated_snippet.py
│   │   │
│   │   ├── prompts/
│   │   │   ├── __init__.py
│   │   │   ├── loader.py
│   │   │   ├── code_generation_prompt.txt
│   │   │
│   │   ├── __init__.py
│   │   ├── main.py
│   │
│   ├── .env
│   ├── requirements.txt
│   └── logs/ (auto-created)
│
├── frontend/
│   ├── app/
│   │   ├── pages/
│   │   │   ├── __init__.py
│   │   │   ├── home.py
│   │   │   └── analytics.py
│   │   │
│   │   ├── components/
│   │   │   └── __init__.py
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── api_client.py
│   │   │
│   │   ├── utils/
│   │   │   └── __init__.py
│   │   │
│   │   ├── __init__.py
│   │   └── main.py
│   │
│   ├── .env
│   ├── requirements.txt
│   └── generated_app.html (auto-generated)
│
└── README.md
```

## 🚀 Running the Project

### Prerequisites
- Python 3.8+
- Azure OpenAI API credentials

You would need to open 2 terminals for setting up and running backend and frontend respectively.

### Step 1: Backend Setup (Terminal 1)

```bash
cd backend
python -m venv venv
pip install -r requirements.txt
.\venv\Scripts\activate
```

### Step 2: Configure Backend Environment
Create/update `backend/.env` with your Azure OpenAI credentials:
```
AZURE_OPENAI_API_KEY=your_key_here
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4.1-mini
```

### Step 3: Start Backend (Terminal 1)
```bash
cd backend
uvicorn api:app --reload
```
✅ Backend will run at: `http://127.0.0.1:8000`

### Step 4: Frontend Setup (Terminal 2)

Now start a new terminal seperate from backend one and make sure no environment is activated in it.

```bash
cd frontend
python -m venv venv
pip install -r requirements.txt
.\venv\Scripts\activate
```

### Step 5: Start Frontend (Terminal 2)
```bash
cd frontend
streamlit run app/main.py
```
✅ Frontend will run at: `http://localhost:8501`

---

## 📋 Project Details

- **Backend**: FastAPI + Azure OpenAI LLM (generates HTML/JS code)
- **Frontend**: Streamlit UI (user interface for webpage generation)
- **Workflow**: User describes webpage → Frontend sends to Backend → LLM generates code → Webpage opens in browser
- **Logging**: Rotating logs available in `backend/logs/`
- **API Endpoint**: `POST /api/dashboard_generation` - Generates webpage from user input

