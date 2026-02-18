"""
Secure Azure OpenAI Chat Application

A production-grade, enterprise-ready chat application using:
- Azure OpenAI for intelligent conversations
- Managed Identity for passwordless authentication
- Azure Key Vault for centralized secret management
- Azure Blob Storage for session persistence
- Private endpoints for network security

Author: Enterprise AI Team
Version: 1.0.0
Security: Zero API keys - 100% Managed Identity
"""

import streamlit as st
import uuid
from datetime import datetime

# Configure page immediately (must be first Streamlit command)
st.set_page_config(
    page_title="Secure Azure OpenAI Chat",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Now import other modules
from config.settings import get_settings
from services.keyvault_service import KeyVaultService
from services.openai_service import OpenAIService
from services.storage_service import StorageService
from utils.logger import setup_logging, get_logger
from utils.validators import validate_user_input, truncate_messages

# Setup logging
settings = get_settings()
setup_logging(level=settings.log_level)
logger = get_logger(__name__)


# ============================================================================
# Custom CSS Styling
# ============================================================================

def inject_custom_css():
    """Inject custom CSS for professional enterprise styling."""
    st.markdown("""
    <style>
    /* Main container styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Header styling */
    .security-banner {
        background: linear-gradient(135deg, #1a5276 0%, #2980b9 50%, #3498db 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .security-banner h1 {
        margin: 0;
        font-size: 1.8rem;
        font-weight: 600;
    }
    
    .security-banner p {
        margin: 0.5rem 0 0 0;
        font-size: 0.9rem;
        opacity: 0.9;
    }
    
    /* Status indicators */
    .status-success {
        color: #27ae60;
        font-weight: 600;
    }
    
    .status-error {
        color: #e74c3c;
        font-weight: 600;
    }
    
    .status-warning {
        color: #f39c12;
        font-weight: 600;
    }
    
    /* Security badge */
    .security-badge {
        display: inline-flex;
        align-items: center;
        background: rgba(39, 174, 96, 0.1);
        border: 1px solid #27ae60;
        border-radius: 20px;
        padding: 0.25rem 0.75rem;
        font-size: 0.75rem;
        color: #27ae60;
        font-weight: 600;
        margin: 0.25rem;
    }
    
    /* Chat message styling */
    .stChatMessage {
        border-radius: 12px;
        margin-bottom: 0.5rem;
    }
    
    /* Sidebar styling */
    .sidebar-section {
        background: rgba(0, 0, 0, 0.02);
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-left: 4px solid #3498db;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 0.5rem 0;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 1rem;
        color: #7f8c8d;
        font-size: 0.8rem;
        border-top: 1px solid #ecf0f1;
        margin-top: 2rem;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .security-banner h1 {
            font-size: 1.4rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


# ============================================================================
# Session State Initialization
# ============================================================================

def initialize_session_state():
    """Initialize all session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())
    
    if "services_initialized" not in st.session_state:
        st.session_state.services_initialized = False
    
    if "keyvault_service" not in st.session_state:
        st.session_state.keyvault_service = None
    
    if "openai_service" not in st.session_state:
        st.session_state.openai_service = None
    
    if "storage_service" not in st.session_state:
        st.session_state.storage_service = None
    
    if "initialization_errors" not in st.session_state:
        st.session_state.initialization_errors = []
    
    if "session_start_time" not in st.session_state:
        st.session_state.session_start_time = datetime.now()


# ============================================================================
# Service Initialization
# ============================================================================

@st.cache_resource(show_spinner=False)
def initialize_services(_settings):
    """
    Initialize all Azure services using Managed Identity.
    
    Uses Streamlit's caching to ensure services are only initialized once.
    
    Args:
        _settings: Application settings (prefixed with _ to prevent hashing)
        
    Returns:
        Tuple of (keyvault_service, openai_service, storage_service, errors)
    """
    errors = []
    kv_service = None
    openai_service = None
    storage_service = None
    
    # Validate settings
    is_valid, validation_errors = _settings.validate()
    if not is_valid:
        return None, None, None, validation_errors
    
    # Initialize Key Vault Service
    try:
        kv_service = KeyVaultService(_settings.key_vault_url)
        success, message = kv_service.initialize()
        if not success:
            errors.append(f"Key Vault: {message}")
            return None, None, None, errors
        logger.info("Key Vault service initialized")
    except Exception as e:
        errors.append(f"Key Vault initialization failed: {str(e)}")
        return None, None, None, errors
    
    # Initialize OpenAI Service
    try:
        openai_service = OpenAIService(kv_service)
        success, message = openai_service.initialize()
        if not success:
            errors.append(f"OpenAI: {message}")
        else:
            logger.info("OpenAI service initialized")
    except Exception as e:
        errors.append(f"OpenAI initialization failed: {str(e)}")
    
    # Initialize Storage Service (optional - don't fail if unavailable)
    try:
        storage_service = StorageService(
            kv_service,
            container_name=_settings.session_container_name
        )
        success, message = storage_service.initialize()
        logger.info(f"Storage service: {message}")
    except Exception as e:
        logger.warning(f"Storage service not available: {e}")
        storage_service = None
    
    return kv_service, openai_service, storage_service, errors


# ============================================================================
# UI Components
# ============================================================================

def render_header():
    """Render the main application header."""
    st.markdown("""
    <div class="security-banner">
        <h1>🔒 Secure Enterprise Chat</h1>
        <p>Powered by Azure OpenAI | Managed Identity Authentication | Private Endpoints Only</p>
    </div>
    """, unsafe_allow_html=True)


def render_security_badges():
    """Render security status badges."""
    st.markdown("""
    <div style="margin-bottom: 1rem;">
        <span class="security-badge">🔐 Managed Identity</span>
        <span class="security-badge">🔑 Key Vault Secured</span>
        <span class="security-badge">🌐 Private Network</span>
        <span class="security-badge">🚫 Zero API Keys</span>
    </div>
    """, unsafe_allow_html=True)


def render_sidebar(kv_service, openai_service, storage_service, errors):
    """Render the sidebar with status and controls."""
    with st.sidebar:
        st.header("🛡️ Security Status")
        
        # Authentication Status
        st.subheader("Authentication")
        if kv_service and kv_service.is_initialized:
            st.success("✅ Managed Identity Active")
        else:
            st.error("❌ Authentication Failed")
        
        # Service Status
        st.subheader("Services")
        
        # Key Vault
        if kv_service and kv_service.is_initialized:
            st.markdown("**Key Vault:** 🟢 Connected")
        else:
            st.markdown("**Key Vault:** 🔴 Disconnected")
        
        # OpenAI
        if openai_service and openai_service.is_initialized:
            st.markdown(f"**OpenAI:** 🟢 Ready")
            st.caption(f"Model: {openai_service.model_name}")
        else:
            st.markdown("**OpenAI:** 🔴 Unavailable")
        
        # Storage
        if storage_service and storage_service.is_enabled:
            st.markdown("**Storage:** 🟢 Session History On")
        else:
            st.markdown("**Storage:** 🟡 Session History Off")
        
        # Network Status
        st.subheader("Network")
        st.markdown("**Access:** Private Endpoints Only")
        st.markdown("**Public Internet:** Blocked")
        
        # Session Info
        st.divider()
        st.subheader("📊 Session Info")
        st.caption(f"ID: {st.session_state.session_id[:8]}...")
        st.caption(f"Messages: {len(st.session_state.messages)}")
        
        # Calculate session duration
        duration = datetime.now() - st.session_state.session_start_time
        minutes = int(duration.total_seconds() // 60)
        st.caption(f"Duration: {minutes} min")
        
        # Actions
        st.divider()
        st.subheader("🔧 Actions")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🗑️ Clear Chat", use_container_width=True):
                clear_chat()
        
        with col2:
            if st.button("🔄 New Session", use_container_width=True):
                new_session()
        
        # Export option
        if st.session_state.messages:
            if st.button("📥 Export Chat", use_container_width=True):
                export_chat()
        
        # Show errors if any
        if errors:
            st.divider()
            st.subheader("⚠️ Issues")
            for error in errors:
                st.error(error)
        
        # Footer
        st.divider()
        st.caption(f"Version {settings.app_version}")
        st.caption("Enterprise Security Enabled")


def clear_chat():
    """Clear the chat history."""
    st.session_state.messages = []
    st.toast("Chat cleared!", icon="🗑️")
    st.rerun()


def new_session():
    """Start a new chat session."""
    # Save current session if storage is available
    if (st.session_state.storage_service and 
        st.session_state.storage_service.is_enabled and
        st.session_state.messages):
        st.session_state.storage_service.save_session(
            st.session_state.session_id,
            st.session_state.messages
        )
    
    # Reset session
    st.session_state.session_id = str(uuid.uuid4())
    st.session_state.messages = []
    st.session_state.session_start_time = datetime.now()
    st.toast("New session started!", icon="🆕")
    st.rerun()


def export_chat():
    """Export chat history as JSON."""
    import json
    
    export_data = {
        "session_id": st.session_state.session_id,
        "exported_at": datetime.now().isoformat(),
        "message_count": len(st.session_state.messages),
        "messages": st.session_state.messages
    }
    
    st.download_button(
        label="💾 Download JSON",
        data=json.dumps(export_data, indent=2),
        file_name=f"chat_export_{st.session_state.session_id[:8]}.json",
        mime="application/json"
    )


def render_chat_history():
    """Render the chat message history."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def handle_user_input(openai_service, storage_service):
    """Handle user input and generate AI response."""
    if prompt := st.chat_input("Ask me anything about cloud security, Azure, or enterprise architecture..."):
        # Validate input
        is_valid, cleaned_input, error = validate_user_input(prompt)
        
        if not is_valid:
            st.error(f"Invalid input: {error}")
            return
        
        # Add user message to history
        st.session_state.messages.append({
            "role": "user",
            "content": cleaned_input
        })
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(cleaned_input)
        
        # Generate AI response
        with st.chat_message("assistant"):
            if not openai_service or not openai_service.is_initialized:
                st.error("OpenAI service not available. Please check configuration.")
                return
            
            try:
                # Truncate history if needed to prevent token overflow
                truncated_messages = truncate_messages(st.session_state.messages)
                
                # Create placeholder for streaming
                response_placeholder = st.empty()
                full_response = ""
                
                # Stream response
                with st.spinner("Thinking..."):
                    for chunk in openai_service.chat_completion(
                        messages=truncated_messages,
                        system_prompt=settings.system_prompt,
                        max_tokens=settings.max_tokens,
                        temperature=settings.temperature,
                        stream=True
                    ):
                        full_response += chunk
                        response_placeholder.markdown(full_response + "▌")
                
                # Final update without cursor
                response_placeholder.markdown(full_response)
                
                # Add to message history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": full_response
                })
                
                # Save to storage (non-blocking)
                if storage_service and storage_service.is_enabled:
                    try:
                        storage_service.save_session(
                            st.session_state.session_id,
                            st.session_state.messages
                        )
                    except Exception as e:
                        logger.warning(f"Failed to save session: {e}")
                
            except Exception as e:
                error_msg = str(e)
                logger.error(f"Chat completion error: {error_msg}")
                
                if "rate limit" in error_msg.lower():
                    st.error("Rate limit exceeded. Please wait a moment and try again.")
                elif "content filter" in error_msg.lower():
                    st.warning("Your message was filtered by content moderation. Please rephrase.")
                elif "token" in error_msg.lower():
                    st.error("Message too long. Please try a shorter message.")
                else:
                    st.error(f"An error occurred: {error_msg}")


def render_error_state(errors):
    """Render error state when services fail to initialize."""
    st.error("⚠️ Application Initialization Failed")
    
    st.markdown("""
    ### Troubleshooting Steps
    
    Please verify the following:
    
    1. **Environment Configuration**
       - `.env` file exists with `KEY_VAULT_NAME` set
       - Key Vault name is correct
    
    2. **Azure Authentication**
       - Running on Azure VM with Managed Identity enabled
       - Or locally with `az login` completed
    
    3. **RBAC Permissions**
       - Managed Identity has **Key Vault Secrets User** role on Key Vault
       - Managed Identity has **Cognitive Services OpenAI User** role on OpenAI
       - Managed Identity has **Storage Blob Data Contributor** role on Storage (optional)
    
    4. **Key Vault Secrets**
       - `OpenAIEndpoint` - Azure OpenAI endpoint URL
       - `ChatModelDeployment` - Model deployment name
       - `OpenAIApiVersion` - API version (e.g., 2024-08-01-preview)
    
    5. **Network Configuration**
       - Private endpoints configured for Key Vault and OpenAI
       - DNS resolution working for private endpoints
    """)
    
    st.subheader("Errors Encountered")
    for error in errors:
        st.error(f"• {error}")
    
    st.info("""
    **Quick Fix Commands:**
    ```bash
    # Check Azure CLI login
    az account show
    
    # Verify Key Vault access
    az keyvault secret list --vault-name YOUR_KV_NAME
    
    # Test DNS resolution (from Azure VM)
    nslookup YOUR_KV_NAME.vault.azure.net
    ```
    """)


def render_footer():
    """Render application footer."""
    st.markdown("""
    <div class="footer">
        <p>🔒 <strong>Enterprise Security Active</strong></p>
        <p>All connections encrypted via private endpoints | Zero public internet exposure | Managed Identity authentication only</p>
        <p>© 2024 Secure AI Platform | Built with Azure AI</p>
    </div>
    """, unsafe_allow_html=True)


# ============================================================================
# Main Application
# ============================================================================

def main():
    """Main application entry point."""
    # Initialize session state
    initialize_session_state()
    
    # Inject custom CSS
    inject_custom_css()
    
    # Render header
    render_header()
    render_security_badges()
    
    # Initialize services (cached)
    kv_service, openai_service, storage_service, errors = initialize_services(settings)
    
    # Store in session state for access in other functions
    st.session_state.keyvault_service = kv_service
    st.session_state.openai_service = openai_service
    st.session_state.storage_service = storage_service
    st.session_state.initialization_errors = errors
    
    # Render sidebar
    render_sidebar(kv_service, openai_service, storage_service, errors)
    
    # Check for critical errors
    if errors and not openai_service:
        render_error_state(errors)
        return
    
    # Main chat interface
    st.divider()
    
    # Render existing chat history
    render_chat_history()
    
    # Handle new user input
    handle_user_input(openai_service, storage_service)
    
    # Render footer
    render_footer()


if __name__ == "__main__":
    main()
