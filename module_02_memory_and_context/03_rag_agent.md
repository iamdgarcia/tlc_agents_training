# 2.3 RAG for Agents 🕵️‍♂️

Now we will combine **Agents** + **RAG**.

## The "Retriever" Tool
To an agent, a Vector Database is just another tool.
*   **Tool Name**: `search_knowledge_base`
*   **Input**: A search query (string).
*   **Output**: Relevant text chunks from the documents.

## The Workflow
1.  **User**: "How do I reset my password?"
2.  **Agent**: "I need to check the knowledge base." -> Calls `search_knowledge_base("reset password")`.
3.  **Tool**: Returns 3 chunks from `manual.txt`.
4.  **Agent**: Reads chunks -> Generates answer.

## Hands-On: Chat with Your Docs
We will build `rag_agent.py`.
1.  **Load**: A sample text file (`knowledge.txt`).
2.  **Index**: Create a local vector store (using `Chroma` and `OpenAIEmbeddings`).
3.  **Agent**: Give the agent a tool to query this store.

### Prerequisites
You need to install `langchain-chroma`:
```bash
pip install langchain-chroma
```
