import gradio as gr
from crewai import Agent, Task, Crew, LLM

# ✅ Use FREE HuggingFace model via LiteLLM
def get_llm():
    return LLM(
        model="huggingface/google/flan-t5-small"
    )

# -------- Agents --------
planner = Agent(
    role="Planner",
    goal="Break down tasks into steps",
    backstory="Expert planner",
    llm=get_llm()
)

executor = Agent(
    role="Executor",
    goal="Execute tasks",
    backstory="Expert executor",
    llm=get_llm()
)

analyst = Agent(
    role="Analyst",
    goal="Analyze results",
    backstory="Expert analyst",
    llm=get_llm()
)

# -------- Function --------
def run_ai(query):

    planning_task = Task(
        description=f"Break down this task: {query}",
        expected_output="Step-by-step plan",
        agent=planner
    )

    execution_task = Task(
        description="Execute the plan",
        expected_output="Execution result",
        agent=executor
    )

    analysis_task = Task(
        description="Analyze results",
        expected_output="Final insights",
        agent=analyst
    )

    crew = Crew(
        agents=[planner, executor, analyst],
        tasks=[planning_task, execution_task, analysis_task],
        verbose=False
    )

    result = crew.kickoff()
    return str(result)

# -------- UI --------
with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
    gr.Markdown("# 🤖 Multi-Agent AI Assistant (Free Version)")

    input_box = gr.Textbox(label="Enter your task")
    output_box = gr.Textbox(label="Output", lines=15)

    btn = gr.Button("🚀 Run")

    btn.click(fn=run_ai, inputs=input_box, outputs=output_box)

demo.launch()