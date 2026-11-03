from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.models.google import Gemini

from agno.tools.duckduckgo import DuckDuckGoTools
load_dotenv()  # loads GROQ_API_KEY and GOOGLE_API_KEY from .env

def build_agent(model):
    return Agent(
        model=model,
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are a helpful and expert travel agent.",
        add_datetime_to_context=True
    )

groq_agent = build_agent(Groq(id="openai/gpt-oss-20b"))
gemini_agent = build_agent(Gemini(id="gemini-3.8-flash"))

# groq_agent.print_response("My budget is 1L INR, suggest a 5-day trip.")
# gemini_agent.print_response("My budget is 1L INR, suggest a 5-day trip.")

# groq_agent.print_response("What is today's date?")
groq_agent.print_response("Is it safe to travel to UAE today?")