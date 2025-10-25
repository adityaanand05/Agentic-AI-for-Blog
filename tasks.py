from crewai import Task
from tools import yt_tool
from agent import video_researcher, web_scraper_agent, Documentation_writer

## Video Research Task
video_research_task = Task(
    description="Search for information about machine learning frameworks in the YouTube video at {youtube_video_url}",
    expected_output="A summary of the key machine learning frameworks mentioned in the video.",
    agent=video_researcher,
    output_file='video-research-output.txt'
)

## Web Scraping Task
scrape_task = Task(
    description="""
    Extract the following information from the news website at {website_url}:
    
    1. The headlines of all featured articles (CSS selector: '.headline')
    2. The main content of these articles (CSS selector: '.content')
   
    
    Compile this information into a structured format with each article's details grouped together.
    """,
    expected_output="A structured documentation of articles with their headlines and main content.",
    agent=web_scraper_agent,
    output_file='scraped-articles.txt'
)


# Writing task with language model configuration
write_task = Task(
  description=(
    "get the info from video-research-output.txt and scraped-articles.txt and topic:{topic}."
  ),
  expected_output='A well-structured and engaging Documentation on the research topic.',
  tools=[],
  agent=Documentation_writer,
  async_execution=False,
  output_file='new-doc.md'  # Example of output customization
)