# 4.3 Ethics and Guardrails 🛡️

As agents become more powerful, they can also become more dangerous.
*   **Prompt Injection**: Users tricking the agent into revealing secrets.
*   **Hallucination**: The agent making up facts confidently.
*   **Harmful Actions**: The agent deleting files or sending offensive emails.

## Implementing Guardrails
A "Guardrail" is a check that runs *before* or *after* the LLM call.

1.  **Input Guardrail**: Checks if the user's query is safe.
2.  **Output Guardrail**: Checks if the agent's response is safe.

## Hands-On: A Safe Agent
In `guardrails_agent.py`, we will build an agent that refuses to answer questions about "hacking" or "violence".
