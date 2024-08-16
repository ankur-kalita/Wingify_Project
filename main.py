import os
from PyPDF2 import PdfReader
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, WebsiteSearchTool
from langchain.llms import Ollama

# API keys
os.environ["SERPER_API_KEY"] = ""
os.environ["OPENAI_API_KEY"] = ""
ollama_openhermes = Ollama(model="openhermes")

pdf = 'blood_test_report.pdf'
pages_to_extract = [1]

text = ''
with open(pdf, 'rb') as file:
    reader = PdfReader(file)
    for page_num in pages_to_extract:
        page = reader.pages[page_num - 1] 
        content = page.extract_text()
        if content:
            text += content

print(text)

# Tools
search_tool = SerperDevTool()
web_search_tool = WebsiteSearchTool()

# Agents
blood_test_analyst = Agent(
    role='Blood Test Analyst',
    goal='Analyze the blood test report and summarize the findings.',
    backstory='You are a medical expert specializing in blood test analysis.',
    verbose=True,
    allow_delegation=False,
    llm=ollama_openhermes
)

article_researcher = Agent(
    role='Article Researcher',
    goal='Search for health articles based on blood test results.',
    backstory='Your are an expert researcher proficient in finding health-related articles.',
    tools=[search_tool, web_search_tool],
    verbose=True,
    allow_delegation = False,
    llm=ollama_openhermes
)

health_advisor = Agent(
    role='Health Advisor',
    goal='Provide health recommendations based on the articles found.',
    backstory='You are a health advisor with extensive knowledge in providing health advice.',
    verbose=True,
    allow_delegation = False,
    llm=ollama_openhermes
)

# Tasks
analyze_blood_test = Task(
    description= f'You have to analyze the blood test report from "{text}" blood report',
    expected_output='A summary of the blood test results.',
    agent=blood_test_analyst,
)

find_articles = Task(
    description='You have to search for health articles based on the blood test analysis.',
    expected_output='A list of relevant health articles with links.',
    agent=article_researcher,
    context=[analyze_blood_test]
)

provide_recommendations = Task(
    description='Your have to provide health recommendations based on the articles found.',
    expected_output='Health recommendations with links to the articles.',
    agent=health_advisor,
    context=[find_articles]
)

# Crew
crew = Crew(
    agents=[blood_test_analyst, article_researcher, health_advisor],
    tasks=[analyze_blood_test, find_articles, provide_recommendations],
    verbose=True,
    process=Process.sequential
)

# Execution
crew.kickoff()