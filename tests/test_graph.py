from src.graph import build_graph


def test_career_question():

    graph = build_graph()

    result = graph.invoke(
        {
            "question": "How can I improve my software engineering career?",
            "category": "",
            "answer": "",
        }
    )

    assert result["category"] == "career"
    assert result["answer"] != ""


def test_general_question():

    graph = build_graph()

    result = graph.invoke(
        {
            "question": "What is the capital of Canada?",
            "category": "",
            "answer": "",
        }
    )

    assert result["category"] == "general"
    assert result["answer"] != ""
