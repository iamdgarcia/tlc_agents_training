# 1.4 The Action Layer (Tools) 🛠️

The "Action Layer" is where the agent connects to the real world.

## What is a Tool?
A tool is simply a function that the agent can call. It has:
1.  **Name**: e.g., `calculator`
2.  **Description**: Tells the agent *when* to use it.
3.  **Arguments**: What inputs it needs (schema).

## Function Calling
Modern LLMs (like GPT-4) have been trained to output structured JSON to call functions. This is much more reliable than the text parsing we did in the previous ReAct example.

## Hands-On: LangChain Tools
In `agent_with_tools.py`, we will use LangChain's `@tool` decorator to create a real tool and bind it to an agent.
