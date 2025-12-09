"""
Manufacturing Data Analysis Chat Assistant - Azure AI Search + Azure OpenAI Integration

This application uses Azure AI Search to retrieve manufacturing data and Azure OpenAI 
to analyze machine logs and generate human-readable insights for operations teams.

Required Python Packages (install with: pip install -r requirements.txt):
- openai (Azure OpenAI SDK)
- azure-search-documents (Azure AI Search SDK)
- streamlit (Web UI framework)
- python-dotenv (Environment variable management)
- pandas (Data processing)

Setup Instructions:
1. Install dependencies: pip install -r requirements.txt
2. Copy .env.example to .env and fill in your Azure credentials
3. Run the app: streamlit run app.py

Azure Resources Required:
- Azure OpenAI resource (with deployed GPT-4.1-mini model and text-embedding-ada-002)
- Azure AI Search resource (with indexed manufacturing data)
"""

import os
import streamlit as st
from openai import AzureOpenAI
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# ===========================
# Configuration
# ===========================

# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4.1-mini")
AZURE_OPENAI_EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-ada-002")

# Azure AI Search Configuration
AZURE_SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
AZURE_SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")
AZURE_SEARCH_INDEX_NAME = os.getenv("AZURE_SEARCH_INDEX_NAME")

# ===========================
# Helper Functions
# ===========================

def validate_configuration():
    """Validate that all required environment variables are set."""
    required_vars = {
        "AZURE_OPENAI_ENDPOINT": AZURE_OPENAI_ENDPOINT,
        "AZURE_OPENAI_KEY": AZURE_OPENAI_KEY,
        "AZURE_SEARCH_ENDPOINT": AZURE_SEARCH_ENDPOINT,
        "AZURE_SEARCH_KEY": AZURE_SEARCH_KEY,
        "AZURE_SEARCH_INDEX_NAME": AZURE_SEARCH_INDEX_NAME,
    }
    
    missing_vars = [var for var, value in required_vars.items() if not value]
    
    if missing_vars:
        st.error(f"Missing required environment variables: {', '.join(missing_vars)}")
        st.info("Please create a .env file with all required configuration values. See .env.example for reference.")
        return False
    
    return True


def initialize_openai_client():
    """Initialize and return Azure OpenAI Client."""
    try:
        client = AzureOpenAI(
            api_key=AZURE_OPENAI_KEY,
            api_version="2024-10-21",
            azure_endpoint=AZURE_OPENAI_ENDPOINT
        )
        return client
    except Exception as e:
        st.error(f"Failed to initialize Azure OpenAI client: {str(e)}")
        return None


def initialize_search_client():
    """Initialize and return Azure AI Search Client."""
    try:
        search_client = SearchClient(
            endpoint=AZURE_SEARCH_ENDPOINT,
            index_name=AZURE_SEARCH_INDEX_NAME,
            credential=AzureKeyCredential(AZURE_SEARCH_KEY)
        )
        return search_client
    except Exception as e:
        st.error(f"Failed to initialize Azure AI Search client: {str(e)}")
        return None


def search_manufacturing_data(search_client, query, top_k=5):
    """
    Search manufacturing data using Azure AI Search.
    
    Args:
        search_client: Azure Search Client
        query: Search query string
        top_k: Number of results to return
        
    Returns:
        list: Search results
    """
    try:
        # Search without specifying field names to get all fields
        results = search_client.search(
            search_text=query,
            top=top_k
        )
        
        search_results = []
        for result in results:
            # Create a dictionary with all available fields from the result
            result_dict = {}
            
            # Iterate through all fields in the search result
            for key in result.keys():
                if key.startswith('@'):  # Skip metadata fields like @search.score
                    continue
                result_dict[key] = result.get(key, "N/A")
            
            search_results.append(result_dict)
        
        return search_results
        
    except Exception as e:
        st.error(f"Search error: {str(e)}")
        return []


def generate_insights_with_rag(openai_client, user_query, search_results):
    """
    Generate insights using RAG (Retrieval-Augmented Generation).
    
    Args:
        openai_client: Azure OpenAI Client
        user_query: User's question
        search_results: Retrieved data from Azure AI Search
        
    Returns:
        str: Generated insights
    """
    try:
        # Format search results as context
        context = "Here is the manufacturing data:\n\n"
        for idx, result in enumerate(search_results, 1):
            context += f"Record {idx}:\n"
            # Dynamically format all fields from the result
            for key, value in result.items():
                context += f"- {key}: {value}\n"
            context += "\n"
        
        # Create prompt with context
        system_prompt = """You are a manufacturing operations analyst. Analyze the provided manufacturing data 
and answer questions with clear, actionable insights. Include specific metrics, patterns, and recommendations 
based on the data. Keep your response concise but comprehensive."""

        user_prompt = f"""{context}

User Question: {user_query}

Please analyze the data and provide insights to answer the question. Include:
1. Direct answer with supporting data
2. Key patterns or trends observed
3. Recommendations for operations team (if applicable)"""

        # Call Azure OpenAI with retry logic for rate limiting
        max_retries = 3
        retry_delay = 5
        
        for attempt in range(max_retries):
            try:
                response = openai_client.chat.completions.create(
                    model=AZURE_OPENAI_DEPLOYMENT_NAME,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.5,
                    max_tokens=300
                )
                
                insights = response.choices[0].message.content.strip()
                return insights
                
            except Exception as api_error:
                error_str = str(api_error)
                if "429" in error_str or "RateLimitReached" in error_str:
                    if attempt < max_retries - 1:
                        import time
                        st.warning(f"Rate limit reached. Retrying in {retry_delay} seconds... (Attempt {attempt + 1}/{max_retries})")
                        time.sleep(retry_delay)
                        retry_delay *= 2  # Exponential backoff
                    else:
                        st.error("Rate limit exceeded. Please wait 60 seconds and try again, or increase your Azure OpenAI quota.")
                        return "Rate limit exceeded. Please try again in a moment."
                else:
                    raise api_error
        
    except Exception as e:
        st.error(f"Azure OpenAI generation error: {str(e)}")
        return "Unable to generate insights at this time."


# ===========================
# Streamlit UI
# ===========================

def main():
    """Main application entry point."""
    
    # Page configuration
    st.set_page_config(
        page_title="Manufacturing Data Analysis Assistant",
        page_icon="📊",
        layout="wide"
    )
    
    # Application header
    st.title("Manufacturing Data Analysis Assistant")
    st.markdown("""
    **AI-Powered Manufacturing Data Insights with RAG**
    
    Ask questions about your manufacturing data using natural language. 
    This assistant uses Azure AI Search to retrieve relevant data and Azure OpenAI to generate insights.
    """)
    
    st.divider()
    
    # Validate configuration
    if not validate_configuration():
        st.stop()
    
    # Initialize Azure services
    with st.spinner("Initializing Azure services..."):
        openai_client = initialize_openai_client()
        search_client = initialize_search_client()
    
    if not openai_client or not search_client:
        st.error("Failed to initialize Azure services. Please check your configuration.")
        st.stop()
    
    st.success("Azure services initialized successfully")
    
    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    st.subheader("Chat History")
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Sample questions
    st.sidebar.header("Sample Questions")
    st.sidebar.markdown("""
    Try asking:
    - Which machine had the most downtime this week?
    - Show me all machines with RUNNING status
    - What is the average temperature for MACHINE_001?
    - Find machines with high vibration levels
    - Which machines are currently in maintenance?
    - Analyze temperature trends across all machines
    """)
    
    # Configuration status
    with st.sidebar.expander("Configuration Status"):
        st.write("**Azure OpenAI:**")
        st.code(f"Endpoint: {AZURE_OPENAI_ENDPOINT[:40]}...")
        st.code(f"Deployment: {AZURE_OPENAI_DEPLOYMENT_NAME}")
        
        st.write("**Azure AI Search:**")
        st.code(f"Endpoint: {AZURE_SEARCH_ENDPOINT[:40]}...")
        st.code(f"Index: {AZURE_SEARCH_INDEX_NAME}")
    
    # Chat input
    if prompt := st.chat_input("Ask a question about manufacturing data..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Searching data and generating insights..."):
                # Search for relevant data (limited to 1 to avoid rate limits)
                search_results = search_manufacturing_data(search_client, prompt, top_k=1)
                
                if search_results:
                    # Generate insights using RAG
                    insights = generate_insights_with_rag(openai_client, prompt, search_results)
                    
                    # Display insights
                    st.markdown(insights)
                    
                    # Show retrieved data in expander
                    with st.expander("Retrieved Data"):
                        st.json(search_results)
                    
                    # Add assistant response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": insights})
                else:
                    error_msg = "No relevant data found for your query. Please try rephrasing your question."
                    st.warning(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
    
    # Clear chat button
    if st.sidebar.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()


if __name__ == "__main__":
    main()
