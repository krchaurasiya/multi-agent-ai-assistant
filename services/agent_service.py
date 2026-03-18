from crewai import Crew, Task
from agents.planner import create_planner
from agents.executor import create_executor
from agents.analyst import create_analyst

def run_agents(user_input):
    try:
        planner = create_planner()
        executor = create_executor()
        analyst = create_analyst()

        planning_task = Task(
            description=f"Break down this task: {user_input}",
            expected_output="Step-by-step plan",
            agent=planner
        )

        execution_task = Task(
            description="Execute the planned steps",
            expected_output="Execution results",
            agent=executor
        )

        analysis_task = Task(
            description="Analyze the results and provide insights",
            expected_output="Final summary and insights",
            agent=analyst
        )

        crew = Crew(
            agents=[planner, executor, analyst],
            tasks=[planning_task, execution_task, analysis_task],
            verbose=True
        )

        return str(crew.kickoff())

    except Exception as e:
        return f"Error: {str(e)}"