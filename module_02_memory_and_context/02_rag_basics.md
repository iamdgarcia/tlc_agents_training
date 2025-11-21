# 2.2 Retrieval-Augmented Generation (RAG) 📚

**RAG** is the bridge between the LLM's frozen training data and your dynamic, private data.

## How RAG Works (The Pipeline)

1.  **Ingestion**: You take your documents (PDFs, TXT, Notion).
2.  **Splitting**: You break them into small "chunks" (e.g., 500 characters).
3.  **Embedding**: You turn each chunk into a **Vector** (a list of numbers) using an Embedding Model (e.g., OpenAI `text-embedding-3-small`).
    *   *Concept*: Vectors that are close together in space represent text that is semantically similar.
4.  **Storage**: You save these vectors in a **Vector Database** (Chroma, Pinecone).
5.  **Retrieval**: When a user asks a question, you:
    *   Embed the question.
    *   Find the top $K$ most similar chunks in the DB.
6.  **Generation**: You feed those chunks + the question to the LLM.

## Why Embeddings?
Embeddings capture *meaning*, not just keywords.
*   "The canine barked" and "The dog made a noise" will have very similar vectors, even though they share few words.

## Hands-On: RAG Agent
In the next section, we will build an agent that can read a text file and answer questions about it.
