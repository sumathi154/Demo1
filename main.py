import os
from dotenv import load_dotenv
from agent import Agent

def main():
    load_dotenv()
    groq_key = os.getenv("GROQ_API_KEY")
    agent = Agent(api_key=groq_key)

    print("🤖 Agentic Generative AI Demo")

    # Knowledge Base Queries
    print("\nKB Query (AI):\n", agent.ask("Tell me about AI"))
    print("\nKB Query (Python):\n", agent.ask("Who created Python?"))
    print("\nKB Query (Reinforcement Learning):\n", agent.ask("What is Reinforcement Learning?"))

    # Fallback to LLM
    print("\nLLM Response:\n", agent.ask("Explain quantum computing."))

if __name__ == "__main__":
    main()
