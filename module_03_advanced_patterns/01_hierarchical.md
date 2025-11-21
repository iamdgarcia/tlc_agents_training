# 3.1 Hierarchical Planning 🗺️

Complex tasks cannot be solved in one step. If you ask an agent to "Write a book about AI," it will fail if it tries to generate the whole text at once.

## The Planner-Executor Pattern
To solve this, we separate the **Planning** from the **Execution**.

1.  **The Planner**: An LLM call that breaks the user's request into a list of sub-tasks.
2.  **The Executor**: An agent loop that takes one sub-task at a time and completes it.

## Why is this better?
*   **Focus**: The executor only has to worry about one small thing at a time.
*   **Reliability**: If one step fails, you can retry just that step, not the whole process.
*   **Context Management**: You don't need to feed the entire history of step 1 into step 10.

## Hands-On: Building a Planner
In `planning_agent.py`, we will build a system that:
1.  Takes a complex query.
2.  Generates a JSON plan.
3.  Executes each step sequentially.
