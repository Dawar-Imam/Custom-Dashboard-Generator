# 🚀 Custom Dashboard Generator App (AI Powered)
This project demonstrates generating and executing UI webpages at runtime using AI.

A user describes a web app (example: "modern todo list"), and the system:

1. Sends the request to a FastAPI backend
2. Uses Azure OpenAI (LLM) to generate full HTML + JavaScript
3. Saves it as app.html
4. Automatically opens the webpage in the browser

So the UI is created dynamically at runtime, not pre-coded.

## 🧠 Architecture Flow

```bash
User (Streamlit UI)
        ↓
FastAPI Backend
        ↓
Azure OpenAI LLM
        ↓
HTML + JS Code Generated
        ↓
Saved as app.html
        ↓
Browser Opens Web App
```

## Project Architecture

```bash
ROOT/
│
├── backend/
│   ├── api.py
│   ├── llm_logic.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── static/ap.html
│
└── README.md
```

## 📂 Project Files

| File      | Purpose                              |
|-----------|--------------------------------------|
| `app.py`  | Streamlit frontend (user input UI)   |
| `api.py`  | FastAPI backend + LLM integration    |
| `.env`    | Stores Azure OpenAI credentials      |
| `app.html`| Auto-generated webpage               |

## 📦 Installation
```bash
git clone https://github.com/Dawar-Imam/Custom-Dashboard-Generator.git
cd Custom-Dashboard-Generator
```
- Linux / Mac / Git Bash
```bash
chmod +x setup.sh
./setup.sh
```
- Windows PowerShell (alternative)
If .sh doesn't run:
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r backend\requirements.txt
pip install -r frontend\requirements.txt
```

## 🔑 Environment Setup

Create a .env file:
```bash
AZURE_OPENAI_API_KEY=your_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
AZURE_OPENAI_API_VERSION=2024-12-01-preview
```

## ▶️ Run the Project
Start backend:
```bash
cd backend
uvicorn api:app --reload
```
Start frontend:
```bash
cd frontend
streamlit run app.py
```

## 💡 How It Works
- User describes a webpage
- AI generates fully functional HTML + JavaScript
- Code is cleaned (removes markdown wrappers)
- File is saved and executed instantly

This enables:

✔ AI-driven UI prototyping
✔ Rapid app generation
✔ Dynamic interface creation

## 🧩 Example Prompts
- A modern todo list with animations
- A calculator with dark theme
- A quiz app with score tracking
- A drawing pad

## ⚡ Use Case
This system can be used for:

- AI UI prototyping tools
- No-code/low-code platforms
- Dynamic interface builders
- Research on generative UI systems
