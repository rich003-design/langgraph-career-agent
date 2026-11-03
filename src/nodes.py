import os

from dotenv import load_dotenv
from langchain_ollama import ChatOllama

from .state import AgentState


load_dotenv()


MODEL_NAME = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2:3b",
)

BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434",
)


llm = ChatOllama(
    model=MODEL_NAME,
    base_url=BASE_URL,
    temperature=0,
)


def classify_question(state: AgentState) -> AgentState:
    """
    Classify the user's question as either
    career or general.
    """

    question = state["question"]

    prompt = f"""
Classify the following question into exactly one category:

career
general

Question:
{question}

Return only one word:
career
or
general
"""

    response = llm.invoke(prompt)

    category = response.content.strip().lower()

    if "career" in category:
        category = "career"
    else:
        category = "general"

    return {
        **state,
        "category": category,
    }


def career_advisor(state: AgentState) -> AgentState:
    """
    Answer career-related questions.
    """

    question = state["question"]

    prompt = f"""
You are a helpful career advisor.

Answer the following career question clearly
and practically.

Question:
{question}

Give:
1. A direct answer
2. Practical recommendations
3. A short action plan
"""

    response = llm.invoke(prompt)

    return {
        **state,
        "answer": response.content,
    }


def general_advisor(state: AgentState) -> AgentState:
    """
    Answer general questions.
    """

    question = state["question"]

    prompt = f"""
You are a helpful assistant.

Answer the following question clearly and
concisely.

Question:
{question}
"""

    response = llm.invoke(prompt)

    return {
        **state,
        "answer": response.content,
    }
