# 1.3 The ReAct Pattern 🔄

**ReAct** stands for **Re**asoning and **Act**ing. It is the fundamental pattern that allows agents to solve complex problems.

## The Loop
Instead of just answering, a ReAct agent enters a loop:
1.  **Thought**: The agent reasons about the problem.
2.  **Action**: The agent decides to take an action (e.g., search Wikipedia).
3.  **Observation**: The agent sees the result of the action.
4.  **Repeat**: The agent thinks again, using the new information.

## Why is this powerful?
It allows the agent to break down problems and gather information it doesn't have in its training data.

## Hands-On: A Manual ReAct Loop
In `react_agent.py`, we will build a "manual" ReAct loop where we simulate the agent stopping to ask for tool outputs.
