from langchain_core.messages import AIMessage
from api.skills_api import get_skills_data

def skill_gap_agent(state: dict) -> dict:
    """
    Ignores the user query context and always computes
    the gap between current_skills and goal_skills.
    """
    data = get_skills_data()
    current = set(data["current_skills"])
    goals = set(data["goal_skills"])
    gaps = list(goals - current)

    reply = f"Skill gaps identified: {', '.join(gaps)}"
    return {"messages": [AIMessage(content=reply)]}
