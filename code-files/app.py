"""
Telecom Network Diagnostics AI Assistant
A RAG-based chat application for analyzing telecom network telemetry and incidents.
"""

import os
import streamlit as st
from openai import AzureOpenAI
import requests
from dotenv import load_dotenv
from typing import List, Dict, Any

# Load environment variables
load_dotenv()

# Configuration
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
AZURE_SEARCH_API_KEY = os.getenv("AZURE_SEARCH_API_KEY")
AZURE_SEARCH_INDEX_NAME = os.getenv("AZURE_SEARCH_INDEX_NAME")


def initialize_page():
    """Configure Streamlit page settings."""
    st.set_page_config(
        page_title="Telecom Network Diagnostics AI",
        page_icon="📡",
        layout="wide"
    )
    
    st.title("📡 Telecom Network Diagnostics AI Assistant")
    st.markdown("""
    Ask questions about network performance, incidents, and get AI-powered diagnostics.
    
    **Example queries:**
    - Why is network latency high in this region?
    - Which components are at risk of failure?
    - What remediation actions are recommended for recent outages?
    """)


def validate_configuration() -> bool:
    """Validate that all required environment variables are set."""
    required_vars = [
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_DEPLOYMENT_NAME",
        "AZURE_SEARCH_ENDPOINT",
        "AZURE_SEARCH_API_KEY",
        "AZURE_SEARCH_INDEX_NAME"
    ]
    
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        st.error(f"Missing required environment variables: {', '.join(missing_vars)}")
        st.info("Please create a `.env` file with all required variables. See `.env.example` for reference.")
        return False
    
    return True


def initialize_openai_client() -> AzureOpenAI:
    """Initialize Azure OpenAI client."""
    return AzureOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        api_version="2024-02-15-preview",
        azure_endpoint=AZURE_OPENAI_ENDPOINT
    )


def search_telemetry_and_incidents(query: str, top_k: int = 5) -> List[Dict[str, Any]]:
    """
    Retrieve relevant telemetry and incident data from Azure AI Search.
    
    Args:
        query: User's search query
        top_k: Number of top results to retrieve
        
    Returns:
        List of search results with content and metadata
    """
    if not AZURE_SEARCH_ENDPOINT or not AZURE_SEARCH_API_KEY:
        st.warning("Azure AI Search is not configured. Using mock data.")
        return []
    
    search_url = f"{AZURE_SEARCH_ENDPOINT}/indexes/{AZURE_SEARCH_INDEX_NAME}/docs/search?api-version=2023-11-01"
    
    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_SEARCH_API_KEY
    }
    
    payload = {
        "search": query,
        "top": top_k,
        "select": "*",
        "queryType": "semantic",
        "semanticConfiguration": "default",
        "captions": "extractive",
        "answers": "extractive|count-3"
    }
    
    try:
        response = requests.post(search_url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        results = response.json().get("value", [])
        return results
    except requests.exceptions.RequestException as e:
        st.warning(f"Azure AI Search request failed: {str(e)}. Proceeding without retrieval.")
        return []


def format_search_results(results: List[Dict[str, Any]]) -> str:
    """
    Format search results into context string for the LLM.
    
    Args:
        results: List of search results from Azure AI Search
        
    Returns:
        Formatted context string
    """
    if not results:
        return "No relevant telemetry or incident data found."
    
    context_parts = []
    for idx, result in enumerate(results, 1):
        # Extract relevant fields (adjust based on your index schema)
        title = result.get("title", result.get("id", f"Document {idx}"))
        content = result.get("content", result.get("description", "No content available"))
        timestamp = result.get("timestamp", "")
        severity = result.get("severity", "")
        component = result.get("component", "")
        
        context_part = f"### Document {idx}: {title}\n"
        if timestamp:
            context_part += f"**Timestamp:** {timestamp}\n"
        if severity:
            context_part += f"**Severity:** {severity}\n"
        if component:
            context_part += f"**Component:** {component}\n"
        context_part += f"**Content:** {content}\n"
        
        context_parts.append(context_part)
    
    return "\n---\n".join(context_parts)


def create_rag_prompt(user_query: str, retrieved_context: str) -> str:
    """
    Create a RAG-enhanced prompt for the LLM focused on telecom diagnostics.
    
    Args:
        user_query: Original user question
        retrieved_context: Context retrieved from Azure AI Search
        
    Returns:
        Complete prompt for the LLM
    """
    system_message = """You are an expert telecom network diagnostics AI assistant. 
Your role is to analyze network telemetry and incident data to provide:
1. Root cause explanations
2. Risk assessments
3. Recommended remediation actions

Base your responses on the retrieved telemetry and incident data provided.
Be specific, technical, and actionable. Always explain your reasoning."""

    prompt = f"""{system_message}

## Retrieved Telemetry and Incident Data:
{retrieved_context}

## User Query:
{user_query}

## Your Response:
Please provide a comprehensive analysis that includes:
- **Root Cause Analysis:** What is causing the issue?
- **Risk Assessment:** What are the potential impacts and risks?
- **Recommended Actions:** What specific steps should be taken to remediate?

Ensure your response is clear, actionable, and based on the data provided above."""

    return prompt


def get_ai_response(client: AzureOpenAI, prompt: str, chat_history: List[Dict[str, str]]) -> str:
    """
    Get response from Azure OpenAI with RAG-enhanced prompt.
    
    Args:
        client: Azure OpenAI client
        prompt: RAG-enhanced prompt
        chat_history: Previous conversation history
        
    Returns:
        AI-generated response
    """
    # Build messages with system context and history
    messages = [
        {"role": "system", "content": "You are a telecom network diagnostics expert assistant."}
    ]
    
    # Add chat history (limit to last 10 messages for context window management)
    messages.extend(chat_history[-10:])
    
    # Add current RAG-enhanced prompt
    messages.append({"role": "user", "content": prompt})
    
    try:
        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT_NAME,
            messages=messages,
            temperature=0.7,
            max_tokens=1000,
            top_p=0.95
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        st.error(f"Error calling Azure OpenAI: {str(e)}")
        return "I apologize, but I encountered an error processing your request. Please try again."


def initialize_session_state():
    """Initialize Streamlit session state for chat history."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "openai_client" not in st.session_state:
        st.session_state.openai_client = initialize_openai_client()


def display_chat_history():
    """Display chat message history."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
            # Display sources if available
            if message["role"] == "assistant" and "sources" in message:
                with st.expander("📚 Retrieved Sources"):
                    st.markdown(message["sources"])


def main():
    """Main application logic."""
    initialize_page()
    
    # Validate configuration
    if not validate_configuration():
        st.stop()
    
    # Initialize session state
    initialize_session_state()
    
    # Display chat history
    display_chat_history()
    
    # Chat input
    if user_query := st.chat_input("Ask about network diagnostics, incidents, or telemetry..."):
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_query)
        
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": user_query})
        
        # Show assistant thinking
        with st.chat_message("assistant"):
            with st.spinner("Analyzing telemetry and incidents..."):
                # Step 1: Retrieve relevant context from Azure AI Search
                search_results = search_telemetry_and_incidents(user_query, top_k=5)
                
                # Step 2: Format search results
                retrieved_context = format_search_results(search_results)
                
                # Step 3: Create RAG-enhanced prompt
                rag_prompt = create_rag_prompt(user_query, retrieved_context)
                
                # Step 4: Get AI response
                response = get_ai_response(
                    st.session_state.openai_client,
                    rag_prompt,
                    st.session_state.messages[:-1]  # Exclude the just-added user message
                )
                
                # Display response
                st.markdown(response)
                
                # Display retrieved sources
                if search_results:
                    with st.expander("📚 Retrieved Sources"):
                        st.markdown(retrieved_context)
        
        # Add assistant response to history
        assistant_message = {
            "role": "assistant",
            "content": response
        }
        
        if search_results:
            assistant_message["sources"] = retrieved_context
        
        st.session_state.messages.append(assistant_message)


if __name__ == "__main__":
    main()
