# Local LangGraph Career Agent

A simple local AI agent built using LangGraph, LangChain, and Ollama.

## Architecture

```text
User Question
      |
      v
Question Classifier
      |
      +------ career ------> Career Advisor ---+
      |                                        |
      +------ general -----> General Advisor --+
                                               |
                                               v
                                             Answer
```

## Technology

- Python
- LangGraph
- LangChain
- Ollama
- Qwen/Llama local LLM
- Pytest
- VS Code

## Setup

Create virtual environment:

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Create your environment file, then set `OLLAMA_MODEL` and `OLLAMA_BASE_URL` if needed:

```bash
cp .env.example .env
```

## Ollama

Check Ollama:

```bash
ollama --version
```

Check models:

```bash
ollama list
```

Start Ollama if required:

```bash
ollama serve
```

## Run

```bash
python -m src.main
```

## Test

```bash
pytest -v
```

## Debug

1. Open VS Code Run and Debug.
2. Select **Debug LangGraph Agent**.
3. Press F5.

## LangGraph Concepts

### State

Shared information passed between nodes.

### Nodes

Functions that perform work.

### Edges

Connections between nodes.

### Conditional Edges

Determine which node executes next based on state.

## Future Improvements

- Add multiple specialized agents
- Add conversation memory
- Add tool calling
- Add web search
- Add RAG
- Add human approval
- Add LangGraph persistence
- Add FastAPI
- Add Streamlit UI
- Add tracing and observability
