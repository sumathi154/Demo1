import requests
import json
from tools.search import web_search
from tools.memory import Memory
from tools.email import send_email

class Agent:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"
        self.memory = Memory()

        # Load knowledge base
        with open("data/knowledge_base.json", "r") as f:
            self.knowledge_base = json.load(f)

    def ask(self, query: str) -> str:
        # Tool triggers
        if query.startswith("search:"):
            return web_search(query.replace("search:", "").strip())
        elif query.startswith("remember:"):
            parts = query.replace("remember:", "").split("=")
            return self.memory.remember(parts[0].strip(), parts[1].strip())
        elif query.startswith("recall:"):
            return self.memory.recall(query.replace("recall:", "").strip())
        elif query.startswith("email:"):
            return send_email("demo@example.com", "Demo Subject", query.replace("email:", "").strip())

        # Knowledge base lookup
        for key, value in self.knowledge_base.items():
            if key.lower() in query.lower():
                return f"[Knowledge Base] {key}: {value}"

        # Otherwise, default to Groq LLM
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {
            "model": "llama-3.1-8b-instant",  # ✅ use one of your available models
            "messages": [{"role": "user", "content": query}],
            "temperature": 0.7
        }

        response = requests.post(self.base_url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.text}"
