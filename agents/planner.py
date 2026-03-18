from crewai import Agent
from config.llm_config import get_llm

def create_planner():
    return Agent(
        role="Planner",
        goal="Break down complex business tasks into actionable steps",
        backstory="Expert in strategic planning and task decomposition",
        llm=get_llm(),
        verbose=True
    )