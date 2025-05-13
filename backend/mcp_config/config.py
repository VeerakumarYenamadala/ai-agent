from langgraph.graph import StateGraph, MessagesState, START, END
from agents.workday_agent import workday_agent
from agents.skill_gap_agent import skill_gap_agent
from agents.pathway_agent import pathway_agent

# --- Workday Graph ---
graph_workday = StateGraph(state_schema=MessagesState)
graph_workday.add_node("workday", workday_agent)
graph_workday.add_edge(START, "workday")
graph_workday.add_edge("workday", END)
compiled_workday = graph_workday.compile()

# --- Skill Gap Graph ---
graph_skill_gap = StateGraph(state_schema=MessagesState)
graph_skill_gap.add_node("skill_gap", skill_gap_agent)
graph_skill_gap.add_edge(START, "skill_gap")
graph_skill_gap.add_edge("skill_gap", END)
compiled_skill_gap = graph_skill_gap.compile()

# --- Pathway Graph ---
graph_pathway = StateGraph(state_schema=MessagesState)
graph_pathway.add_node("pathway", pathway_agent)
graph_pathway.add_edge(START, "pathway")
graph_pathway.add_edge("pathway", END)
compiled_pathway = graph_pathway.compile()

# Expose a map for selecting which pipeline to run:
GRAPH_MAP = {
    "workday": compiled_workday,
    "skills": compiled_skill_gap,
    "pathway": compiled_pathway,
}
