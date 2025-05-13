from langchain_core.messages import AIMessage
from api.workday_api import get_workday_data

def workday_agent(state: dict) -> dict:
    """
    Reads the last user message, fetches mock Workday data,
    and returns an AIMessage with the requested info.
    """
    data = get_workday_data()
    last = state["messages"][-1].content.lower()

    if "leave" in last:
        reply = f"Upcoming leaves: {', '.join(data['leaves'])}"
    elif "goal" in last:
        reply = f"Current goals: {', '.join(data['goals'])}"
    elif "role" in last:
        reply = f"Your current role is: {data['role']}"
    else:
        reply = "Sorry, I couldn't understand your Workday query."

    return {"messages": [AIMessage(content=reply)]}
