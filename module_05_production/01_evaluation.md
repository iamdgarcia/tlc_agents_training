# 5.1 Evaluation & Metrics 📊

"It looks good to me" is not a metric. To ship an agent, you need numbers.

## The Challenge
Traditional metrics like accuracy or F1-score don't work well for generated text.
*   **Exact Match**: Fails if the agent says "The answer is 5" instead of just "5".
*   **BLEU/ROUGE**: Measures word overlap, not meaning.

## The Solution: LLM-as-a-Judge
We use a stronger LLM (like GPT-4) to evaluate the output of our agent.

### RAGAS (Retrieval Augmented Generation Assessment)
A popular framework for evaluating RAG pipelines. It measures:
1.  **Faithfulness**: Is the answer based on the retrieved context?
2.  **Answer Relevance**: Does the answer actually address the user's question?
3.  **Context Precision**: Did the retriever find relevant documents?

## Hands-On: Building a Simple Evaluator
In `eval_agent.py`, we will write a script that takes a question, an answer, and the "ground truth", and asks GPT-4 to score it.
