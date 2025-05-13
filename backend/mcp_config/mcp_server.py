from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from mcp_config.config import GRAPH_MAP

app = FastAPI()

class ChatRequest(BaseModel):
    agent: str
    input: str

@app.post("/chat")
async def chat(req: ChatRequest):
    graph = GRAPH_MAP.get(req.agent)
    if not graph:
        raise HTTPException(status_code=400, detail="Invalid agent name")
    # Initialize state with the user's message
    init_state = {"messages": [HumanMessage(content=req.input)]}
    result = graph.invoke(init_state)
    # Return the last AI response
    return {"response": result["messages"][-1].content}

# If run as script:
# uvicorn main:app --reload --host 0.0.0.0 --port 8000
