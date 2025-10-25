from crewai import Crew, Process
from agent import video_researcher, Documentation_writer ,web_scraper_agent
from tasks import video_research_task,write_task ,scrape_task



Video_crew = Crew(agents=[video_researcher], 
                  tasks=[video_research_task], 
                  verbose=True, 
                  process=Process.sequential
)
result = Video_crew.kickoff(inputs={"youtube_video_url": "https://youtu.be/k9TUPpGqYTo?si=SECbK8w_HIG3qU-l"})
print(result)

crew = Crew(
    agents=[web_scraper_agent],
    tasks=[scrape_task],
    verbose=True,
    process=Process.sequential,
)
result1 = crew.kickoff(inputs={"website_url": "https://www.w3schools.com/python/python_strings.asp"})
print(result1)

final_crew = Crew(
    agents=[Documentation_writer],
    tasks=[write_task],
    verbose=True,
    process=Process.sequential
)
result2 = final_crew.kickoff(inputs={"file1": "video-research-output.txt", "file2": "scraped-articles.txt", "topic": "Machine Learning Frameworks"})
print(result2)