from crewai_tools import  SeleniumScrapingTool, YoutubeVideoSearchTool , FileReadTool , FileWriterTool

youtube_search_tool = YoutubeVideoSearchTool(use_chroma=False)

selenium_tool = SeleniumScrapingTool()

file_read_tool = FileReadTool()

file_write_tool = FileWriterTool()