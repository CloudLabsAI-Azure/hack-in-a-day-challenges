"""
Healthcare AI RAG Chatbot
A clinical research assistant powered by Azure OpenAI and Azure AI Search.
This application retrieves relevant medical literature and generates grounded clinical answers.
"""

import os
import streamlit as st
from openai import AzureOpenAI
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# =============================================================================
# Configuration: Load Azure credentials from environment variables
# =============================================================================
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01")

AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
AZURE_SEARCH_API_KEY = os.getenv("AZURE_SEARCH_API_KEY")
AZURE_SEARCH_INDEX_NAME = os.getenv("AZURE_SEARCH_INDEX_NAME")

# =============================================================================
# Initialize Azure OpenAI Client (singleton pattern for connection reuse)
# =============================================================================
@st.cache_resource
def get_openai_client():
    """
    Initialize and cache the Azure OpenAI client for reuse across requests.
    This follows best practices by avoiding repeated client instantiation.
    """
    return AzureOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
        azure_endpoint=AZURE_OPENAI_ENDPOINT
    )

# =============================================================================
# Azure AI Search: Retrieve relevant documents
# =============================================================================
def search_documents(query: str, top_k: int = 5) -> list[dict]:
    """
    Query Azure AI Search to retrieve relevant medical documents.
    
    Args:
        query: User's clinical research question
        top_k: Number of top documents to retrieve
        
    Returns:
        List of document dictionaries containing content and metadata
    """
    search_url = f"{AZURE_SEARCH_ENDPOINT}/indexes/{AZURE_SEARCH_INDEX_NAME}/docs/search?api-version=2023-11-01"
    
    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_SEARCH_API_KEY
    }
    
    # Construct search payload with semantic ranking for better relevance
    payload = {
        "search": query,
        "top": top_k,
        "queryType": "semantic",
        "semanticConfiguration": "default",
        "select": "content,title,metadata",
        "queryLanguage": "en-us"
    }
    
    try:
        response = requests.post(search_url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        results = response.json()
        documents = results.get("value", [])
        
        # Extract relevant fields from search results
        retrieved_docs = []
        for doc in documents:
            retrieved_docs.append({
                "content": doc.get("content", ""),
                "title": doc.get("title", "Untitled"),
                "score": doc.get("@search.score", 0.0)
            })
        
        return retrieved_docs
    
    except requests.exceptions.RequestException as e:
        st.error(f"Error querying Azure AI Search: {str(e)}")
        return []

# =============================================================================
# Azure OpenAI: Generate grounded clinical answer
# =============================================================================
def generate_answer(user_question: str, context_documents: list[dict]) -> str:
    """
    Generate a clinical research answer grounded in retrieved documents.
    
    Args:
        user_question: The user's clinical question
        context_documents: Retrieved documents from Azure AI Search
        
    Returns:
        Generated answer string from the LLM
    """
    # If no documents found, return early with clear message
    if not context_documents:
        return "I couldn't find relevant medical literature to answer your question. Please try rephrasing or ask about a different clinical topic."
    
    # Build context string from retrieved documents
    context = "\n\n---\n\n".join([
        f"**{doc['title']}**\n{doc['content'][:1000]}"  # Limit each doc to 1000 chars
        for doc in context_documents
    ])
    
    # Construct RAG prompt with clear instructions
    system_prompt = """You are a clinical research assistant. Your role is to provide accurate, evidence-based answers to medical and clinical research questions.

Guidelines:
- Base your answers ONLY on the provided medical literature context
- Be factual, neutral, and research-oriented
- Cite relevant information from the sources when possible
- If the context doesn't contain sufficient information, clearly state that
- Use clear, professional medical terminology
- Do not provide medical advice or diagnoses
- Focus on research findings, treatment options, and clinical evidence"""

    user_prompt = f"""Based on the following medical literature, answer this clinical research question:

**Question:** {user_question}

**Medical Literature Context:**
{context}

**Answer:**"""

    try:
        client = get_openai_client()
        
        # Call Azure OpenAI with chat completion API
        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3,  # Lower temperature for more factual responses
            max_tokens=800,
            top_p=0.95
        )
        
        answer = response.choices[0].message.content
        return answer
    
    except Exception as e:
        st.error(f"Error generating answer: {str(e)}")
        return "An error occurred while generating the answer. Please try again."

# =============================================================================
# Streamlit UI: Chat Interface
# =============================================================================
def main():
    """
    Main Streamlit application entry point.
    Renders the chat UI and handles user interactions.
    """
    # Page configuration
    st.set_page_config(
        page_title="Healthcare AI Research Assistant",
        page_icon="🏥",
        layout="wide"
    )
    
    # Header
    st.title("🏥 Healthcare AI Research Assistant")
    st.markdown("""
    Ask clinical research questions and get evidence-based answers grounded in medical literature.
    Powered by Azure OpenAI and Azure AI Search.
    """)
    
    # Sidebar with information and sample questions
    with st.sidebar:
        st.header("ℹ️ About")
        st.info("""
        This RAG chatbot retrieves relevant medical literature from Azure AI Search 
        and generates grounded clinical research answers using Azure OpenAI.
        """)
        
        st.header("💡 Sample Questions")
        st.markdown("""
        - What are the latest treatments for glioblastoma in patients over 60?
        - Compare chemotherapy and immunotherapy outcomes
        - Which treatments are FDA approved for melanoma?
        - What are the side effects of checkpoint inhibitors?
        """)
        
        # Configuration status
        st.header("⚙️ Configuration")
        config_ok = all([
            AZURE_OPENAI_ENDPOINT,
            AZURE_OPENAI_API_KEY,
            AZURE_OPENAI_DEPLOYMENT_NAME,
            AZURE_SEARCH_ENDPOINT,
            AZURE_SEARCH_API_KEY,
            AZURE_SEARCH_INDEX_NAME
        ])
        
        if config_ok:
            st.success("✅ All credentials configured")
        else:
            st.error("❌ Missing credentials. Check your .env file")
    
    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display existing chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask a clinical research question..."):
        # Validate configuration before processing
        if not config_ok:
            st.error("⚠️ Please configure your Azure credentials in the .env file")
            return
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate assistant response
        with st.chat_message("assistant"):
            with st.spinner("🔍 Searching medical literature..."):
                # Step 1: Retrieve relevant documents from Azure AI Search
                documents = search_documents(prompt, top_k=5)
                
                if documents:
                    st.caption(f"Found {len(documents)} relevant documents")
                
                # Step 2: Generate answer using Azure OpenAI with retrieved context
                with st.spinner("🤖 Generating evidence-based answer..."):
                    answer = generate_answer(prompt, documents)
                
                # Display the answer
                st.markdown(answer)
                
                # Optionally show sources in an expander
                if documents:
                    with st.expander("📚 View Sources"):
                        for i, doc in enumerate(documents, 1):
                            st.markdown(f"**Source {i}: {doc['title']}**")
                            st.caption(f"Relevance Score: {doc['score']:.2f}")
                            st.text(doc['content'][:300] + "...")
                            st.divider()
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": answer})
    
    # Clear chat button
    if st.sidebar.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

if __name__ == "__main__":
    main()
