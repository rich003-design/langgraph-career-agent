from langgraph.graph import StateGraph, START, END

from .state import AgentState
from .nodes import (
    classify_question,
    career_advisor,
    general_advisor,
)


def route_question(state: AgentState) -> str:
    """
    Decide which advisor should handle the question.
    """

    if state["category"] == "career":
        return "career"

    return "general"


def build_graph():
    """
    Build and compile the LangGraph workflow.
    """

    graph = StateGraph(AgentState)

    # Add nodes
    graph.add_node(
        "classify",
        classify_question,
    )

    graph.add_node(
        "career_advisor",
        career_advisor,
    )

    graph.add_node(
        "general_advisor",
        general_advisor,
    )

    # Start -> classifier
    graph.add_edge(
        START,
        "classify",
    )

    # Conditional routing
    graph.add_conditional_edges(
        "classify",
        route_question,
        {
            "career": "career_advisor",
            "general": "general_advisor",
        },
    )

    # Both advisors finish the graph
    graph.add_edge(
        "career_advisor",
        END,
    )

    graph.add_edge(
        "general_advisor",
        END,
    )

    return graph.compile()
