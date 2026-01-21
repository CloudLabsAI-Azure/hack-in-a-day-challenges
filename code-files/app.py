"""
B2B Account Intelligence AI Assistant
A RAG-based chat application for sales teams using Azure AI Search and Azure OpenAI.
"""

import os
import streamlit as st
from dotenv import load_dotenv
import requests
import json
from openai import AzureOpenAI

# Load environment variables
load_dotenv()

# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

# Azure AI Search Configuration
AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
AZURE_SEARCH_API_KEY = os.getenv("AZURE_SEARCH_API_KEY")
AZURE_SEARCH_INDEX_NAME = os.getenv("AZURE_SEARCH_INDEX_NAME")

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version="2024-02-01"
)


def search_account_intelligence(query: str, top_k: int = 5) -> list:
    """
    Retrieve relevant account intelligence from Azure AI Search.
    
    Args:
        query: User's search query
        top_k: Number of top results to return
        
    Returns:
        List of relevant documents with account intelligence
    """
    try:
        # Azure AI Search REST API endpoint
        search_url = f"{AZURE_SEARCH_ENDPOINT}/indexes/{AZURE_SEARCH_INDEX_NAME}/docs/search?api-version=2023-11-01"
        
        headers = {
            "Content-Type": "application/json",
            "api-key": AZURE_SEARCH_API_KEY
        }
        
        # Search request body
        search_body = {
            "search": query,
            "top": top_k,
            "queryType": "semantic",
            "select": "*",
            "searchFields": "content,account_name,industry,description"
        }
        
        # Execute search request
        response = requests.post(search_url, headers=headers, json=search_body)
        response.raise_for_status()
        
        results = response.json()
        documents = results.get("value", [])
        
        if documents:
            st.sidebar.success(f"✓ Retrieved {len(documents)} relevant documents")
        else:
            st.sidebar.warning("⚠ No documents found for this query")
        
        return documents
        
    except Exception as e:
        st.sidebar.error(f"❌ Search error: {str(e)}")
        return []


def build_rag_prompt(user_query: str, context_documents: list) -> str:
    """
    Build a RAG prompt with retrieved context for the LLM.
    
    Args:
        user_query: User's original question
        context_documents: Retrieved documents from Azure AI Search
        
    Returns:
        Formatted prompt with context and query
    """
    # Build context section from retrieved documents
    context_text = ""
    if context_documents:
        context_text = "=== ACCOUNT INTELLIGENCE CONTEXT ===\n\n"
        for idx, doc in enumerate(context_documents, 1):
            context_text += f"Document {idx}:\n"
            context_text += f"Account: {doc.get('account_name', 'N/A')}\n"
            context_text += f"Industry: {doc.get('industry', 'N/A')}\n"
            context_text += f"Content: {doc.get('content', doc.get('description', 'N/A'))}\n"
            context_text += f"Score: {doc.get('@search.score', 'N/A')}\n"
            context_text += "-" * 50 + "\n\n"
    else:
        context_text = "=== NO RELEVANT ACCOUNT DATA FOUND ===\n\n"
    
    # Construct the full RAG prompt
    rag_prompt = f"""You are an AI sales assistant providing account intelligence to B2B sales teams.

{context_text}

=== SALES USER QUESTION ===
{user_query}

=== INSTRUCTIONS ===
Based on the account intelligence context above, provide a concise, actionable response that:
1. Directly answers the sales user's question
2. Highlights key risks, opportunities, or changes
3. Suggests specific talking points or next actions
4. Uses business-friendly language (avoid technical jargon)
5. Structures information with bullet points or sections when appropriate

If no relevant context was found, acknowledge this and provide general guidance based on best practices.

Response:"""
    
    return rag_prompt


def generate_llm_response(prompt: str) -> str:
    """
    Generate a response using Azure OpenAI.
    
    Args:
        prompt: The complete RAG prompt with context
        
    Returns:
        Generated response from the LLM
    """
    try:
        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert B2B sales assistant specializing in account intelligence and strategic sales insights."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=800,
            top_p=0.95
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Error generating response: {str(e)}"


def validate_configuration() -> bool:
    """
    Validate that all required environment variables are set.
    
    Returns:
        True if configuration is valid, False otherwise
    """
    required_vars = [
        ("AZURE_OPENAI_ENDPOINT", AZURE_OPENAI_ENDPOINT),
        ("AZURE_OPENAI_API_KEY", AZURE_OPENAI_API_KEY),
        ("AZURE_OPENAI_DEPLOYMENT_NAME", AZURE_OPENAI_DEPLOYMENT_NAME),
        ("AZURE_SEARCH_ENDPOINT", AZURE_SEARCH_ENDPOINT),
        ("AZURE_SEARCH_API_KEY", AZURE_SEARCH_API_KEY),
        ("AZURE_SEARCH_INDEX_NAME", AZURE_SEARCH_INDEX_NAME)
    ]
    
    missing_vars = [name for name, value in required_vars if not value]
    
    if missing_vars:
        st.error(f"❌ Missing required environment variables: {', '.join(missing_vars)}")
        st.info("Please create a .env file with all required variables. See .env.example for reference.")
        return False
    
    return True


def main():
    """
    Main Streamlit application entry point.
    """
    # Page configuration
    st.set_page_config(
        page_title="B2B Account Intelligence Assistant",
        page_icon="💼",
        layout="wide"
    )
    
    # Header
    st.title("💼 B2B Account Intelligence Assistant")
    st.markdown("**AI-powered sales insights using Azure OpenAI and Azure AI Search**")
    st.divider()
    
    # Validate configuration
    if not validate_configuration():
        st.stop()
    
    # Sidebar with information
    with st.sidebar:
        st.header("ℹ️ About")
        st.markdown("""
        This assistant helps sales teams with:
        - Account summaries and updates
        - Risk and opportunity analysis
        - Meeting preparation and talking points
        - Strategic account intelligence
        """)
        
        st.divider()
        
        st.header("💡 Sample Queries")
        sample_queries = [
            "Summarize recent changes for this account",
            "What risks and opportunities exist for this customer?",
            "Give talking points for the next sales meeting",
            "What are the key decision makers at this account?",
            "How can we expand our footprint with this customer?"
        ]
        
        for query in sample_queries:
            if st.button(query, key=query, use_container_width=True):
                st.session_state.sample_query = query
        
        st.divider()
        st.caption("🔧 Powered by Azure OpenAI & Azure AI Search")
    
    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Handle sample query from sidebar
    user_input = None
    if "sample_query" in st.session_state:
        user_input = st.session_state.sample_query
        del st.session_state.sample_query
    
    # Chat input
    if prompt := (user_input or st.chat_input("Ask about your accounts...")):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate assistant response
        with st.chat_message("assistant"):
            with st.spinner("🔍 Searching account intelligence..."):
                # Step 1: Retrieve relevant documents from Azure AI Search
                retrieved_docs = search_account_intelligence(prompt)
                
            with st.spinner("🤖 Generating insights..."):
                # Step 2: Build RAG prompt with context
                rag_prompt = build_rag_prompt(prompt, retrieved_docs)
                
                # Step 3: Generate response using Azure OpenAI
                response = generate_llm_response(rag_prompt)
                
                # Display response
                st.markdown(response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Footer
    st.divider()
    st.caption("⚡ B2B Account Intelligence AI Hackathon | RAG-powered Sales Assistant")


if __name__ == "__main__":
    main()
