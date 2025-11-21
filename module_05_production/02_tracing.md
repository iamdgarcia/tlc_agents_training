# 5.2 Tracing & Debugging 🕵️‍♀️

When an agent fails, it fails silently. It just gives you a bad answer. To fix it, you need to see the **Trace**.

## What is a Trace?
A trace shows the full execution path of your agent:
1.  User Input
2.  Router Decision
3.  Tool Call (Input/Output)
4.  LLM Reasoning
5.  Final Output

## Tools of the Trade
*   **LangSmith**: Built by LangChain. Excellent visualization.
*   **Phoenix (Arize)**: Open-source, great for local debugging.
*   **Weights & Biases**: Good for tracking experiments.

## How to Trace
Most frameworks make this easy. In LangChain, you just set an environment variable.

```bash
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=...
```

Once enabled, every run of your agent is logged to the cloud dashboard, where you can inspect exactly what prompt was sent to the LLM and what the raw output was.
