from fastapi import FastAPI
from services.agent_service import run_agents

app = FastAPI()

@app.get("/run")
def run(query: str):
    result = run_agents(query)
    return {"response": result}