from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.models.google import Gemini

load_dotenv()  # loads GROQ_API_KEY and GOOGLE_API_KEY from .env

def build_agent(model):
    return Agent(
        model=model,
        markdown=True,
        instructions="You are a helpful and expert travel agent.",
    )

groq_agent = build_agent(Groq(id="llama-3.3-70b-versatile"))
gemini_agent = build_agent(Gemini(id="gemini-2.0-flash"))

groq_agent.print_response("My budget is 1L INR, suggest a 5-day trip.")
gemini_agent.print_response("My budget is 1L INR, suggest a 5-day trip.")