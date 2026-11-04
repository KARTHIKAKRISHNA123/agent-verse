from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.models.google import Gemini
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint


load_dotenv()  # loads GROQ_API_KEY and GOOGLE_API_KEY from .env

db = SqliteDb(db_file="tmp/agno.db")
#db.clear_memories()


def build_agent():
    return Agent(
        db=db,
        model=Groq(id="openai/gpt-oss-20b"),
        markdown=True,
        add_history_to_context=True,
        update_memory_on_run=True,
        add_memories_to_context=True,
    )

# groq_agent = build_agent(Groq(id="openai/gpt-oss-20b"))
# gemini_agent = build_agent(Gemini(id="gemini-3.8-flash"))

# # groq_agent.print_response("My budget is 1L INR, suggest a 5-day trip.")
# # gemini_agent.print_response("My budget is 1L INR, suggest a 5-day trip.")

# # groq_agent.print_response("What is today's date?")
# groq_agent.print_response("Is it safe to travel to UAE today?")

agent = build_agent()

user_id = "kk@gmail.com"

session_id = "intro"

agent.print_response("Iam Karthika Krishna M. I am an aspiring AI Engineer", user_id=user_id)

agent.print_response("Who am I?", user_id=user_id)

memories = db.get_user_memories(user_id=user_id)

pprint("Memories stored in the database:")
pprint(memories)

