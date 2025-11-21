# 2.1 Types of Agent Memory 🧠

One of the biggest limitations of raw LLMs is that they are **stateless**. They don't remember what you said 5 seconds ago. To build a coherent agent, we need to engineer **Memory**.

## The Context Window Problem
LLMs have a fixed "Context Window" (e.g., 128k tokens for GPT-4o). You cannot fit infinite history into it.
*   **Short-Term Memory**: Stores the recent conversation history.
*   **Long-Term Memory**: Stores vast amounts of information in a database (Vector DB), retrieving only what is relevant.

## Types of Short-Term Memory

1.  **Buffer Memory**: Keeps the last $N$ messages. Simple, but can lose context.
2.  **Summary Memory**: Asks the LLM to summarize the conversation so far and keeps that summary. Good for long talks.
3.  **Entity Memory**: Extracts and remembers specific facts about entities (e.g., "User's name is Alice", "Alice likes Python").

## Hands-On: Adding Memory to an Agent
In `memory_agent.py`, we will build an agent that uses `RunnableWithMessageHistory` from LangChain to maintain a conversation state across multiple turns.
