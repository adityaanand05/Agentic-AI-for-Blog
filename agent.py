from crewai import Agent , LLM
from tools import selenium_tool , youtube_search_tool, file_read_tool , file_write_tool

from dotenv import load_dotenv

load_dotenv()

import os
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini LLM
llm_gemini = LLM(
    model="gemini-2.5-flash",  
    temperature=0.7,
    api_key=gemini_api_key
)

## Create a senior youtube video researcher agent
video_researcher = Agent(
    role="Video Researcher",
    goal="Extract relevant information from YouTube videos",
    backstory="An expert researcher who specializes in analyzing video content.",
    tools=[youtube_search_tool],
    verbose=True,
    llm=llm_gemini
)

## Create a senior website researcher agent
web_scraper_agent = Agent(
    role="Web Scraper",
    goal="Extract and analyze information from dynamic websites",
    backstory="""You are an expert web scraper who specializes in extracting 
    content from dynamic websites that require browser automation. You have 
    extensive knowledge of CSS selectors and can identify the right selectors 
    to target specific content on any website.""",
    tools=[selenium_tool],
    verbose=True,
    llm=llm_gemini
)
## creating a senior Documentation writer agent with YT tool

Documentation_writer=Agent(
    role='Documentation Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    backstory=(
         "Expert in writing detailed documentation posts on New Technology, Computer Science, Artificial Intelligence, Data Science, Machine Learning, and Generative AI topics"
    ),
    tools=[file_read_tool, file_write_tool],
    allow_delegation=False,
    llm=llm_gemini
)