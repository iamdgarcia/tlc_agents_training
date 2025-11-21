# 0.2 Core Building Blocks 🧱

To build agents, we need a few key components.

## 1. Large Language Models (LLMs) 🧠
The LLM is the reasoning engine of the agent. It decides what to do next based on the input it receives.
*   **Proprietary Models**: GPT-4o (OpenAI), Claude 3.5 Sonnet (Anthropic), Gemini 1.5 Pro (Google).
*   **Open Source Models**: Llama 3 (Meta), Mistral.

## 2. Orchestration Frameworks 🎻
While you *can* build agents with raw API calls, frameworks make it much easier to manage memory, tools, and planning.
*   **LangChain**: The most popular framework, great for building custom chains and agents.
*   **CrewAI**: Excellent for multi-agent orchestration and role-based agents.
*   **AutoGen**: Microsoft's framework for conversational multi-agent systems.

## 3. Vector Databases 🗄️
For Long-term memory and RAG (Retrieval Augmented Generation).
*   **ChromaDB**, **FAISS**, **Pinecone**.

## 💻 Hands-On: Installation

Let's install the core libraries we'll use in this course. We'll focus on `langchain` and `crewai` for their ease of use.

### Step 1: Create a Virtual Environment
It's best practice to use a virtual environment to keep your dependencies isolated.

```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 2: Install Libraries
Create a `requirements.txt` file with the following:

```text
langchain
langchain-openai
langchain-community
crewai
python-dotenv
```

Then run:

```bash
pip install -r requirements.txt
```

Now you're ready to code!
