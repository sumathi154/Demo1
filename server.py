from fastapi import FastAPI
from pydantic import BaseModel
from agent import Agent
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")

# Initialize agent
agent = Agent(api_key=groq_key)

# Create FastAPI app
app = FastAPI(title="Agentic + Generative AI Demo")

class QueryRequest(BaseModel):
    query: str
    text: str | None = None  # for summarization, sentiment, etc.

@app.get("/ask")
def ask(query: str):
    return {"response": agent.ask(query)}

@app.post("/ask")
def ask_post(request: QueryRequest):
    return {"response": agent.ask(request.query)}

# --- New AI Features ---

@app.post("/summarize")
def summarize(request: QueryRequest):
    """
    Summarize long text into concise form.
    """
    summary = agent.summarize(request.text)
    return {"summary": summary}

@app.post("/sentiment")
def sentiment(request: QueryRequest):
    """
    Analyze sentiment of text (positive/negative/neutral).
    """
    sentiment_result = agent.analyze_sentiment(request.text)
    return {"sentiment": sentiment_result}

@app.post("/generate_text")
def generate_text(request: QueryRequest):
    """
    Generate creative text from a prompt.
    """
    generated = agent.generate_text(request.query)
    return {"generated_text": generated}

@app.post("/generate_code")
def generate_code(request: QueryRequest):
    """
    Generate Python code snippets from a description.
    """
    code = agent.generate_code(request.query)
    return {"code": code}

@app.post("/generate_image")
def generate_image(request: QueryRequest):
    """
    Generate an image from a description.
    """
    image_url = agent.generate_image(request.query)
    return {"image_url": image_url}
