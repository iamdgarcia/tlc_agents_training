import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

# Initialize the LLM
# Ensure you have OPENAI_API_KEY set in your .env file
try:
    llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
except Exception as e:
    print(f"Error initializing LLM: {e}")
    exit(1)

def simple_agent(query):
    """
    A simple agent that takes a user query and returns a response
    with a 'thought process' included.
    """
    print(f"\n--- New Interaction ---")
    print(f"User: {query}")
    print("Agent: Thinking...")
    
    # The 'SystemMessage' sets the behavior or 'persona' of the agent.
    messages = [
        SystemMessage(content="You are a helpful assistant. Before answering, briefly explain your thought process in a [THOUGHT] block, then provide the [ANSWER]."),
        HumanMessage(content=query)
    ]
    
    try:
        response = llm.invoke(messages)
        print(f"Agent Response:\n{response.content}")
    except Exception as e:
        print(f"Error during invocation: {e}")

if __name__ == "__main__":
    # Test the agent
    simple_agent("What is the square root of 144?")
    simple_agent("Who wrote '1984'?")
