from crewai import Agent
from config.llm_config import get_llm
from tools.search_tool import search_tool

def create_executor():
    return Agent(
        role="Executor",
        goal="Execute tasks using tools and APIs",
        backstory="Expert in execution and tool usage",
        tools=[search_tool],
        llm=get_llm(),
        verbose=True
    )