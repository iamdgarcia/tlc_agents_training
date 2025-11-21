# 1.2 Agent Reasoning & Prompt Engineering 🧠

To make an agent "smart", we need to guide its reasoning. We do this through **Prompt Engineering**.

## Zero-Shot vs. Few-Shot

*   **Zero-Shot**: Asking the model to do something without examples.
    *   *Example*: "Translate this to Spanish: Hello."
*   **Few-Shot**: Providing examples to guide the model.
    *   *Example*:
        *   "English: Good morning -> Spanish: Buenos días"
        *   "English: How are you? -> Spanish: ¿Cómo estás?"
        *   "English: Hello -> Spanish: "

## Chain of Thought (CoT)

For agents, the most powerful technique is **Chain of Thought**. We ask the model to "think step-by-step".

### The Prompt Template

In `langchain`, we use templates to structure these prompts.

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a math tutor. Solve the problem step-by-step."),
    ("user", "{input}")
])

chain = prompt | llm

response = chain.invoke({"input": "If I have 5 apples and eat 2, then buy 3 more, how many do I have?"})
```

## Hands-On: Prompt Engineering

Check out `prompt_engineering.py` to see how changing the prompt changes the agent's "brain".
