"""
LangChain Core Examples using Groq (Fast & Cheap) - 2026
"""

import os
from dotenv import load_dotenv

# === CHANGE: Import from langchain_groq instead of langchain_openai ===
from langchain_groq import ChatGroq

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

load_dotenv()

# ====================== CONFIG (Groq) ======================
llm = ChatGroq(
    model="llama-3.3-70b-versatile",   # Good balance of speed & quality
    # Other popular models:
    # "llama-3.1-8b-instant", "mixtral-8x7b-32768", "qwen/qwen3-32b", "gemma2-9b-it"
    temperature=0.7,
    max_tokens=1024,
    # streaming=True   # Uncomment if you want streaming
)

# In-memory session history
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


# ====================== 1. BASIC LLM CALL ======================
def basic_llm_call():
    print("\n=== 1. Basic LLM Call (Groq) ===")
    messages = [
        SystemMessage(content="You are a helpful AI assistant."),
        HumanMessage(content="What is LangChain in one sentence?")
    ]
    
    response = llm.invoke(messages)
    print(response.content)


# ====================== 2. PROMPT TEMPLATE ======================
def prompt_template_example():
    print("\n=== 2. PromptTemplate Usage ===")
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert {domain} teacher."),
        ("human", "Teach me about {topic} in a {style} style.")
    ])
    
    formatted = prompt.invoke({
        "domain": "AI Frameworks",
        "topic": "LangChain",
        "style": "simple and beginner-friendly"
    })
    
    print("Formatted Prompt created successfully!")


# ====================== 3. SIMPLE CHAIN ======================
def simple_chain_example():
    print("\n=== 3. Simple LCEL Chain ===")
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("human", "Explain {topic} briefly.")
    ])
    
    chain = prompt | llm | StrOutputParser()
    
    result = chain.invoke({"topic": "Retrieval Augmented Generation (RAG)"})
    print("Chain Output:", result)


# ====================== 4. AGENT WITH TOOL ======================
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    weather_data = {
        "Hyderabad": "28°C, Sunny",
        "Bangalore": "24°C, Cloudy",
        "Mumbai": "30°C, Rainy",
    }
    return weather_data.get(city, f"Weather in {city} is pleasant.")


def agent_with_tool_example():
    """
    NOTE: Agent API has changed in LangChain 1.2.15.
    This example is simplified. For full agent support, upgrade LangChain
    or use the newer langchain-experimental package.
    """
    print("\n=== 4. Tool Example (Groq) ===")
    print(f"Weather in Hyderabad: {get_weather('Hyderabad')}")
    print(f"Weather in Mumbai: {get_weather('Mumbai')}")


# ====================== 5. MEMORY EXAMPLE ======================
def memory_example():
    print("\n=== 5. Memory Example ===")
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a friendly assistant."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    
    chain = prompt | llm | StrOutputParser()
    
    chain_with_memory = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
    )
    
    # Turn 1
    print("AI:", chain_with_memory.invoke(
        {"input": "Hi, my name is Deepak."},
        config={"configurable": {"session_id": "user_001"}}
    ))
    
    # Turn 2 (Memory works)
    print("AI:", chain_with_memory.invoke(
        {"input": "What is my name?"},
        config={"configurable": {"session_id": "user_001"}}
    ))


# ====================== RUN ======================
if __name__ == "__main__":
    print(">>> Running LangChain Examples with Groq (Very Fast!)\n")
    
    basic_llm_call()
    prompt_template_example()
    simple_chain_example()
    agent_with_tool_example()
    memory_example()
    