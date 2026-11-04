from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.youtube import YouTubeTools
from agno.models.groq import Groq

from youtube_transcript_api import YouTubeTranscriptApi

for t in YouTubeTranscriptApi().list("JkaxUblCGz0"):
    print(t.language_code, "| auto-generated" if t.is_generated else "| manual")

load_dotenv()

def build_youtube_agent():
    return Agent(
    name="YouTube Agent",
    model=Groq(id="openai/gpt-oss-20b"),   # or Groq(id="openai/gpt-oss-20b") if the transcript is short
tools=[YouTubeTools(languages=["en", "en-US", "en-GB"])],  description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
    instructions=[
        "Use the tools to fetch the video's captions and metadata before answering.",
        "Only use timestamps that appear in the tool output. If captions are unavailable, say so instead of guessing.",
        "The captions may be in another language. Always write your answer in English.",
    ],
    markdown=True,
)


print(Groq.__module__)

# if __name__ == "__main__":
#     agent.print_response("Summarize this video https://youtu.be/JkaxUblCGz0", stream=True)