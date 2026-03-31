# Agentic + Generative AI Demo

## 📌 Overview
This project demonstrates how to build an **Agentic AI system** combined with **Generative AI features** using **FastAPI**.  
It integrates reasoning, memory, and tool orchestration (Agentic AI) with creative synthesis (Generative AI: text, code, image generation).

---

## 🚀 Features

### 🔹 Agentic AI
- **Ask Endpoint (`/ask`)**  
  - Handles queries like `search:`, `remember:`, `recall:`  
  - Demonstrates reasoning, memory, and tool orchestration.

### 🔹 AI (Analytical Features)
- **Summarization (`/summarize`)**  
  - Condenses long text into concise summaries.  
  - Example: Summarize research papers or articles.

- **Sentiment Analysis (`/sentiment`)**  
  - Detects emotions in text (positive, negative, neutral).  
  - Example: Analyze customer feedback.

### 🔹 Generative AI (Creative Features)
- **Text Generation (`/generate_text`)**  
  - Produces creative text from prompts.  
  - Example: Poems, essays, chatbot responses.

- **Code Generation (`/generate_code`)**  
  - Generates Python code snippets from natural language.  
  - Example: "Python function to calculate factorial."

- **Image Generation (`/generate_image`)**  
  - Creates images from text descriptions.  
  - Example: "AI robot teaching students in a classroom."

---

## 🛠️ Tech Stack
- **FastAPI** → Web framework for building APIs  
- **Pydantic** → Request validation  
- **Groq API / LLMs** → Generative AI backend  
- **Python** → Core language  
- **Uvicorn** → ASGI server  

---

## 📂 Project Structure
Demo1/
│── server.py        # FastAPI app with endpoints
│── agent.py         # Agent logic (reasoning + generative calls)
│── requirements.txt # Dependencies
│── README.md        # Documentation

Code

---

## ▶️ Running the Project

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
Set environment variables

Add your API key in .env:

Code
GROQ_API_KEY=your_api_key_here
Run the server

bash
uvicorn server:app --reload
Open Swagger UI

Code
http://127.0.0.1:8000/docs
📡 Example Usage
Summarization
json
POST /summarize
{
  "text": "Artificial Intelligence is a broad field that includes machine learning, natural language processing, robotics, and more."
}
Sentiment
json
POST /sentiment
{
  "text": "I love learning AI!"
}
Text Generation
json
POST /generate_text
{
  "query": "Write a short poem about AI"
}
Code Generation
json
POST /generate_code
{
  "query": "Python function to calculate factorial"
}
Image Generation
json
POST /generate_image
{
  "query": "AI robot teaching students in a classroom"
}
📖 Concepts Covered
Endpoint	Feature Type	Concept
/ask	Agentic AI	Reasoning, memory, tool orchestration
/summarize	AI	NLP → Text Summarization
/sentiment	AI	Classification → Sentiment Analysis
/generate_text	Generative AI	LLMs → Creative Text Generation
/generate_code	Generative AI	LLMs → Code Generation
/generate_image	Generative AI	Diffusion Models → Text-to-Image
🌟 Learning Roadmap
NLP Basics → Summarization, sentiment analysis

Machine Learning → Classification, predictions

LLMs (Generative AI) → Text & code generation

Diffusion Models → Image generation

Agentic AI → Combining tools, memory, reasoning

