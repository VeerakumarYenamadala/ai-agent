import os
import json
import openai
from dotenv import load_dotenv
from pathlib import Path
from langchain_core.messages import AIMessage

# load .env (only once at import time)
load_dotenv()
key = os.getenv("OPENAI_API_KEY")
if not key:
    raise RuntimeError("OPENAI_API_KEY is not set — please add it to your environment or .env file")
openai.api_key = key

# Paths to our mock data
DATA_DIR       = Path(__file__).parent.parent / "data"
SKILLS_PATH    = DATA_DIR / "skills_data.json"
COURSES_PATH   = DATA_DIR / "courses_data.json"

def pathway_agent(state: dict) -> dict:
    """
    Takes the last AIMessage (which should list skill gaps),
    prompts OpenAI for a 4-week learning pathway, and returns it.
    """
    skill_gap_msg = state["messages"][-1].content

    # Load full skills profile and catalog of courses
    with open(SKILLS_PATH, "r") as f:
        skills_data = json.load(f)
    with open(COURSES_PATH, "r") as f:
        courses_data = json.load(f)

    prompt = f"""
    You are an expert learning advisor.

    User skill profile:
    {json.dumps(skills_data, indent=2)}

    Skill gaps to address:
    {skill_gap_msg}

    Available courses (each tied to a skill):
    {json.dumps(courses_data, indent=2)}

    Please generate a 4-week learning pathway. Each week, assign 1–2 courses from the above list
    that directly address the user’s skill gaps. Output strictly in this JSON format:

    "pathway":[
    {{
        "week": 1,
        "courses": [
        {{ "course_name": "...", "url": "..." }},
        ...
        ]
    }},
    ... (weeks 2–4)
    ]
    """

    resp = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        stream=False  # Streaming enabled
    )
    print(f"Response:{resp}")
    pathway = resp.choices[0].message.content
    return {"messages": [AIMessage(content=pathway)]}
