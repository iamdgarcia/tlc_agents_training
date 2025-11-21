# 3.2 Reflection and Self-Correction 🪞

Agents, like humans, make mistakes. A "Reflective" agent is one that checks its own work.

## The Reflection Loop
1.  **Draft**: The agent creates an initial response.
2.  **Critique**: The agent (or a separate "Critic" agent) reviews the draft for errors, style, or missing information.
3.  **Revise**: The agent generates a new response based on the critique.

## Why is this powerful?
It allows the agent to catch hallucinations or logic errors *before* showing them to the user.

## Hands-On: A Self-Correcting Code Generator
In `reflective_agent.py`, we will build an agent that writes Python code, "reviews" it for bugs (simulated), and then fixes it.
