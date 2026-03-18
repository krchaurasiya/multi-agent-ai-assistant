from crewai import Agent
from config.llm_config import get_llm

def create_analyst():
    return Agent(
        role="Analyst",
        goal="Analyze results and provide insights",
        backstory="Expert in business analysis and reporting",
        llm=get_llm(),
        verbose=True
    )