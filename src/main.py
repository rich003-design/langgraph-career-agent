from .graph import build_graph


def run_agent(question: str) -> dict:
    """
    Run the LangGraph agent.
    """

    graph = build_graph()

    initial_state = {
        "question": question,
        "category": "",
        "answer": "",
    }

    result = graph.invoke(initial_state)

    return result


if __name__ == "__main__":

    question = input(
        "Enter your question: "
    )

    result = run_agent(question)

    print("\nCategory:")
    print(result["category"])

    print("\nAnswer:")
    print(result["answer"])
