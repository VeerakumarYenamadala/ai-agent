from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from mcp_config.config import GRAPH_MAP
from datetime import datetime

app = FastAPI(
    title="Learning Assistant API",
    description="AI-powered learning assistant with multi-agent conversation protocol",
    version="1.0.0"
)

# Define allowed origins
origins = [
    "http://localhost:4200",     # Angular dev server
    "http://127.0.0.1:4200",    # Angular dev server (alternative localhost)
    "http://localhost:8080",     # Alternative Angular dev server
    "http://127.0.0.1:8080",    # Alternative Angular dev server (alternative localhost)
    "http://127.0.0.1:*",
]

# Add CORS middleware with enhanced configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
   # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=[
        "Content-Type",
        "Authorization",
        "Accept",
        "Origin",
        "X-Requested-With",
        "Access-Control-Request-Method",
        "Access-Control-Request-Headers"
    ],
    expose_headers=["Content-Type", "Authorization"],
    max_age=3600,  # Cache preflight requests for 1 hour
)

class AgentChatRequest(BaseModel):
    agent: str
    input: str

class AgentChatResponse(BaseModel):
    response: str

@app.post("/api/chat/agent", response_model=AgentChatResponse)
async def chat(req: AgentChatRequest):
    graph = GRAPH_MAP.get(req.agent)
    if not graph:
        raise HTTPException(status_code=400, detail="Invalid agent name")
    # Initialize state with the user's message
    init_state = {"messages": [HumanMessage(content=req.input)]}
    result = graph.invoke(init_state)
    # Return the last AI response
    return {"response": result["messages"][-1].content}

@app.get("/api/health")
async def health_check():
    """Health check endpoint to verify CORS and API functionality"""
    return {
        "status": "healthy",
        "cors_enabled": True,
        "allowed_origins": origins,
        "timestamp": datetime.utcnow().isoformat()
    }

# If run as script:
# uvicorn main:app --reload --host 0.0.0.0 --port 8000
