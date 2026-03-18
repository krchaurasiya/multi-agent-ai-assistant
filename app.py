import streamlit as st
from crewai import Crew, Task

from agents.planner import create_planner
from agents.executor import create_executor
from agents.analyst import create_analyst
#from config.memory import get_memory

#memory = get_memory()
# UI
st.title("🤖 Multi-Agent AI Business Assistant")

user_input = st.text_input("Enter your business task:")

if st.button("Run AI System"):

    planner = create_planner()
    executor = create_executor()
    analyst = create_analyst()

    # Tasks
    planning_task = Task(
        description=f"Break down this task: {user_input}",
        agent=planner
    )

    execution_task = Task(
        description="Execute the planned steps",
        agent=executor
    )

    analysis_task = Task(
        description="Analyze results and summarize insights",
        agent=analyst
    )

    # Crew
    crew = Crew(
    agents=[planner, executor, analyst],
    tasks=[planning_task, execution_task, analysis_task],
    #memory=memory,
    verbose=True
)

    result = crew.kickoff()

    st.subheader("Final Output:")
    st.write(result)


# import requests

# # st.title("🤖 AI Business Assistant")

# # query = st.text_input("Enter your task:")

# if st.button("Run"):
#     response = requests.get(f"http://localhost:8000/run?query={query}")
#     st.write(response.json())