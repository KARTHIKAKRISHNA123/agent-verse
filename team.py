from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.models.google import Gemini
from agno.team import Team

load_dotenv()  # loads GROQ_API_KEY and GOOGLE_API_KEY from .env

eng_agent = Agent(
    name="English Agent",
    role="You are an English language expert that can help with grammar, vocabulary, and writing style.",
)

chi_agent = Agent(
    name="Chinese Agent",
    role="You are a Chinese language expert that can help with grammar, vocabulary, and writing style.",
)

hi_agent = Agent(
    name="Hindi Agent",
    role="You are a Hindi language expert that can help with grammar, vocabulary, and writing style.",
)

team_leader = Team(
    name="Linguistic Experts (Answer and Translate)",
    members=[eng_agent, chi_agent, hi_agent],
    model=Groq(id="openai/gpt-oss-20b"),
    markdown=True,
    show_members_responses=True,
    instructions="You are a team of linguistic experts that can help with grammar, vocabulary, and writing style in English, Chinese, and Hindi. Each member will provide their response in their respective language. Do not route to just one agent. Output the response of all agents",
)

# def build_agent(model):
#     return Agent(
#         model=model,
#         tools=[DuckDuckGoTools()],
#         markdown=True,
#         instructions="You are a helpful and expert travel agent.",
#         add_datetime_to_context=True
#     )

# groq_agent = build_agent(Groq(id="openai/gpt-oss-20b"))
# gemini_agent = build_agent(Gemini(id="gemini-3.8-flash"))

# groq_agent.print_response("My budget is 1L INR, suggest a 5-day trip.")
# gemini_agent.print_response("My budget is 1L INR, suggest a 5-day trip.")

# groq_agent.print_response("What is today's date?")
# groq_agent.print_response("Is it safe to travel to UAE today?")

team_leader.print_response("What is the capital of India?")