from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import PromptTemplate
import os
import webbrowser
from dotenv import load_dotenv
import os
import re


load_dotenv()  # reads .env file

app = FastAPI()

class Question(BaseModel):
    text: str

llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    temperature=0
)

prompt = PromptTemplate.from_template(
    "The user will ask for code for a webpage. **Just give html + javascript code no extra text please**. The code should be fully functional.\n Requirement: {question}"
)

@app.post("/ask")
def ask_llm(q: Question):
    # Step 1 — generate webpage code
    chain1 = prompt | llm
    response = chain1.invoke({"question": q.text})
    # Save to file and open in browser
    html_code = response.content
    html_code = re.sub(r"^```[a-zA-Z]*\n?", "", html_code.strip())
    html_code = re.sub(r"\n?```$", "", html_code).strip()
    with open("app.html", "w", encoding="utf-8") as f:
        f.write(html_code)
    file_path = os.path.join(os.getcwd(), "app.html")
    webbrowser.open(file_path)
    return {"answer": "App generated and opened in your browser!"}
