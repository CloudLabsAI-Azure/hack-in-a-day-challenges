# Challenge 05: Deploy Secure Chat Application

## Introduction

All the infrastructure is ready! Now comes the fun part - deploying a secure, production-ready chat application that uses everything you've built:

- ✅ Private endpoints (no public access)
- ✅ Managed identity (no API keys)
- ✅ Key Vault secrets (zero hardcoded credentials)
- ✅ Azure OpenAI (chat models ready)

You'll download a pre-built Streamlit chat app, configure it using **only environment variables** (no code changes!), and run it on your VM.

Let's build a secure ChatGPT-like experience!

## Prerequisites

- Completed Challenge 4 (OpenAI models deployed and tested)
- All Key Vault secrets created (OpenAIEndpoint, ChatModelDeployment, etc.)
- Managed identity with proper RBAC roles
- Python 3.11 and VS Code installed on VM

## Challenge Objectives

- Download the pre-built secure chat application
- Create `.env` file with Key Vault-based configuration
- Install Python dependencies
- Run the chat app locally
- Test chat functionality with managed identity
- Validate security (no API keys, private endpoints only)
- Test session history with Storage Account

## Application Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     User's Browser                          │
│               http://localhost:8501                         │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ├─────> Streamlit Web UI
                             │
┌────────────────────────────▼────────────────────────────────┐
│                  VM (Application Subnet)                    │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │         Secure Chat Application (app.py)             │  │
│  │  - Streamlit UI                                      │  │
│  │  - Managed Identity auth                             │  │
│  │  - Key Vault integration                             │  │
│  │  - Session management                                │  │
│  └───────┬──────────────┬────────────────┬──────────────┘  │
│          │              │                │                 │
└──────────┼──────────────┼────────────────┼─────────────────┘
           │              │                │
      Private Endpoint    │                │
           │              │                │
┌──────────▼────────┐ ┌───▼──────────┐ ┌──▼────────────────┐
│  Azure Key Vault  │ │ Azure OpenAI │ │ Storage Account   │
│  (Secrets)        │ │ (Chat Model) │ │ (Session History) │
│  10.0.2.x         │ │ 10.0.1.x     │ │ 10.0.2.x          │
└───────────────────┘ └──────────────┘ └───────────────────┘

All connections via private endpoints - ZERO public internet traffic!
```

## Steps to Complete

### Part 1: Create Application Directory Structure

1. **Create the app directory**:

```powershell
New-Item -Path "C:\LabFiles\SecureAI\chat-app" -ItemType Directory -Force
Set-Location "C:\LabFiles\SecureAI\chat-app"

# Create subdirectories
New-Item -Path ".\pages" -ItemType Directory -Force
New-Item -Path ".\utils" -ItemType Directory -Force
```

2. **Verify directory structure**:

```powershell
Get-ChildItem -Path "C:\LabFiles\SecureAI\chat-app" -Recurse
```

Should show:
```
chat-app/
├── pages/
└── utils/
```

### Part 2: Download Application Files

We'll create the application files directly (simulating a download from your secure repository).

1. **Create the main application file** (`app.py`):

```powershell
@'
"""
Secure Azure OpenAI Chat Application
- Uses Managed Identity (no API keys!)
- Retrieves config from Key Vault
- All connections via private endpoints
- Session history stored in Azure Storage
"""
import streamlit as st
import os
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.storage.blob import BlobServiceClient
import json
from datetime import datetime
import uuid

# Page config
st.set_page_config(
    page_title="Secure Azure OpenAI Chat",
    page_icon="🔒",
    layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Title and security badge
st.title("🔒 Secure Enterprise Chat")
st.caption("✅ 100% Private | ✅ Managed Identity | ✅ No API Keys | ✅ Enterprise-Grade Security")

# Sidebar for config info
with st.sidebar:
    st.header("🛡️ Security Status")
    
    # Initialize services with managed identity
    try:
        with st.spinner("🔐 Authenticating with Managed Identity..."):
            credential = DefaultAzureCredential()
            
            # Get Key Vault name from environment
            kv_name = os.getenv("KEY_VAULT_NAME")
            if not kv_name:
                st.error("❌ KEY_VAULT_NAME not set in .env file")
                st.stop()
            
            kv_url = f"https://{kv_name}.vault.azure.net"
            secret_client = SecretClient(vault_url=kv_url, credential=credential)
            
            # Retrieve all configuration from Key Vault
            openai_endpoint = secret_client.get_secret("OpenAIEndpoint").value
            chat_deployment = secret_client.get_secret("ChatModelDeployment").value
            api_version = secret_client.get_secret("OpenAIApiVersion").value
            
            # Storage account for session history (optional)
            try:
                storage_account = secret_client.get_secret("StorageAccountName").value
                storage_url = f"https://{storage_account}.blob.core.windows.net"
                blob_client = BlobServiceClient(account_url=storage_url, credential=credential)
                storage_enabled = True
            except:
                storage_enabled = False
            
            # Initialize OpenAI client
            openai_client = AzureOpenAI(
                azure_endpoint=openai_endpoint,
                api_version=api_version,
                azure_ad_token_provider=lambda: credential.get_token(
                    "https://cognitiveservices.azure.com/.default"
                ).token
            )
            
            st.success("✅ Authenticated")
            st.info(f"🤖 Model: {chat_deployment}")
            st.info(f"🔑 Auth: Managed Identity")
            st.info(f"🌐 Network: Private Only")
            if storage_enabled:
                st.info(f"💾 Storage: Enabled")
            
    except Exception as e:
        st.error(f"❌ Authentication failed: {str(e)}")
        st.error("Please check:")
        st.error("1. Managed Identity is enabled on VM")
        st.error("2. RBAC roles assigned correctly")
        st.error("3. KEY_VAULT_NAME in .env file")
        st.stop()
    
    # Session info
    st.divider()
    st.caption(f"Session ID: {st.session_state.session_id[:8]}...")
    st.caption(f"Messages: {len(st.session_state.messages)}")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.session_id = str(uuid.uuid4())
        st.rerun()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything about cloud security..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("🤔 Thinking..."):
            try:
                # Prepare messages for API
                api_messages = [
                    {"role": "system", "content": "You are a helpful AI assistant specializing in cloud security, Azure, and enterprise architecture. Provide clear, accurate, and secure guidance."}
                ]
                api_messages.extend(st.session_state.messages)
                
                # Call Azure OpenAI via private endpoint with managed identity
                response = openai_client.chat.completions.create(
                    model=chat_deployment,
                    messages=api_messages,
                    max_tokens=1000,
                    temperature=0.7,
                    stream=True  # Streaming for better UX
                )
                
                # Stream response
                response_placeholder = st.empty()
                full_response = ""
                
                for chunk in response:
                    if chunk.choices[0].delta.content:
                        full_response += chunk.choices[0].delta.content
                        response_placeholder.markdown(full_response + "▌")
                
                response_placeholder.markdown(full_response)
                
                # Save assistant message
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
                # Save to storage (optional)
                if storage_enabled:
                    try:
                        container_name = "chat-sessions"
                        blob_name = f"{st.session_state.session_id}.json"
                        
                        # Get or create container
                        try:
                            container_client = blob_client.get_container_client(container_name)
                            if not container_client.exists():
                                container_client.create_container()
                        except:
                            pass
                        
                        # Save session
                        session_data = {
                            "session_id": st.session_state.session_id,
                            "timestamp": datetime.now().isoformat(),
                            "messages": st.session_state.messages
                        }
                        
                        blob_client.get_blob_client(
                            container=container_name,
                            blob=blob_name
                        ).upload_blob(
                            json.dumps(session_data, indent=2),
                            overwrite=True
                        )
                        
                    except Exception as e:
                        # Don't fail the app if storage fails
                        st.sidebar.warning(f"⚠️ Could not save session: {str(e)[:50]}")
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.error("Check that OpenAI model is deployed and accessible via private endpoint.")

# Footer
st.divider()
st.caption("🔒 Enterprise Security: All connections encrypted and routed through private endpoints. Zero public internet exposure. Managed identity authentication only.")
'@ | Out-File -FilePath "app.py" -Encoding UTF8

Write-Host "✅ Created app.py"
```

2. **Create requirements.txt**:

```powershell
@'
streamlit==1.31.0
openai==1.12.0
azure-identity==1.15.0
azure-keyvault-secrets==4.7.0
azure-storage-blob==12.19.0
python-dotenv==1.0.0
'@ | Out-File -FilePath "requirements.txt" -Encoding UTF8

Write-Host "✅ Created requirements.txt"
```

3. **Create README**:

```powershell
@'
# Secure Azure OpenAI Chat Application

## Security Features
- ✅ Managed Identity authentication (zero API keys)
- ✅ Key Vault for all secrets
- ✅ Private endpoints only (no public internet)
- ✅ Session history in secure storage
- ✅ Content filtering enabled
- ✅ Enterprise-grade encryption

## Configuration
All configuration via environment variables in `.env` file.
NO hardcoded credentials ANYWHERE!

## Running the App
```
streamlit run app.py
```

## Architecture
- **Frontend**: Streamlit web UI
- **Backend**: Azure OpenAI (private endpoint)
- **Auth**: Managed Identity (Entra ID)
- **Secrets**: Azure Key Vault
- **Storage**: Azure Blob Storage (session history)
- **Network**: 100% private, zero public access

## Security Validation
1. No API keys in code ✅
2. No credentials in .env ✅
3. All secrets in Key Vault ✅
4. Private endpoints only ✅
5. Managed identity auth ✅
'@ | Out-File -FilePath "README.md" -Encoding UTF8

Write-Host "✅ Created README.md"
```

### Part 3: Create Environment Configuration

1. **Get your Key Vault name**:

```powershell
$kvName = az keyvault list `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --query "[0].name" -o tsv

Write-Host "Key Vault Name: $kvName"
```

2. **Get Storage Account name** (for session history):

```powershell
$storageName = az storage account list `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --query "[0].name" -o tsv

Write-Host "Storage Account Name: $storageName"
```

3. **Create `.env` file** (ONLY Key Vault name - all other config from KV!):

```powershell
@"
# Secure Chat Application Configuration
# Only the Key Vault name is needed - everything else retrieved from Key Vault!

# Key Vault Name (the ONLY thing you need to configure!)
KEY_VAULT_NAME=$kvName

# Optional: Enable debug mode
# DEBUG=false

# That's it! The app retrieves these from Key Vault:
#  - OpenAIEndpoint
#  - ChatModelDeployment  
#  - OpenAIApiVersion
#  - StorageAccountName (optional)

# NO API KEYS! NO CREDENTIALS! Everything via Managed Identity ✅
"@ | Out-File -FilePath ".env" -Encoding UTF8

Write-Host "✅ Created .env file"
```

4. **Store Storage Account name in Key Vault** (so app can retrieve it):

```powershell
az keyvault secret set `
  --vault-name $kvName `
  --name "StorageAccountName" `
  --value $storageName

Write-Host "✅ Stored storage account name in Key Vault"
```

5. **Create `.env.example`** (template for others):

```powershell
@'
# Secure Chat Application Configuration Template

# Key Vault Name (replace with your actual Key Vault name)
KEY_VAULT_NAME=your-keyvault-name

# Optional: Enable debug logging
# DEBUG=false

# ============================================
# SECURITY NOTE:
# ============================================
# This is the ONLY thing you configure!
# The app retrieves all other settings from Key Vault:
#  - OpenAIEndpoint
#  - ChatModelDeployment
#  - OpenAIApiVersion
#  - StorageAccountName
#
# NO API KEYS OR CREDENTIALS SHOULD EVER BE IN THIS FILE!
# Authentication uses Managed Identity only.
# ============================================
'@ | Out-File -FilePath ".env.example" -Encoding UTF8

Write-Host "✅ Created .env.example"
```

### Part 4: Install Dependencies

1. **Create a virtual environment** (best practice):

```powershell
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1
```

2. **Upgrade pip**:

```powershell
python -m pip install --upgrade pip
```

3. **Install requirements**:

```powershell
pip install -r requirements.txt
```

This will take 2-3 minutes. You should see:
```
Successfully installed streamlit-1.31.0 openai-1.12.0 azure-identity-1.15.0 ...
```

### Part 5: Configure Storage Account Access

The app saves session history to Blob Storage. Let's ensure managed identity can access it.

1. **Get VM's managed identity**:

```powershell
$identityId = az vm show `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --name "vm-<inject key="DeploymentID"></inject>" `
  --query identity.principalId -o tsv
```

2. **Verify Storage Blob Data Contributor role** (should be assigned in Challenge 3):

```powershell
$storageId = az storage account show `
  --name $storageName `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --query id -o tsv

az role assignment list `
  --assignee $identityId `
  --scope $storageId `
  --query "[?roleDefinitionName=='Storage Blob Data Contributor']" `
  --output table
```

If not assigned, assign it:

```powershell
az role assignment create `
  --assignee $identityId `
  --role "Storage Blob Data Contributor" `
  --scope $storageId
```

### Part 6: Run the Chat Application

🎉 Moment of truth!

1. **Start the app**:

```powershell
streamlit run app.py
```

2. **Expected output**:

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://10.0.3.4:8501
```

3. **Open browser**:
   - The browser should open automatically
   - If not, manually navigate to: `http://localhost:8501`

4. **You should see**:
   - ✅ Title: "🔒 Secure Enterprise Chat"
   - ✅ Sidebar showing: "✅ Authenticated"
   - ✅ Model name displayed
   - ✅ "Auth: Managed Identity"
   - ✅ "Network: Private Only"
   - ✅ Chat input box ready

### Part 7: Test the Chat Application

Let's validate everything works!

1. **Test 1: Simple question**

In the chat input, type:
```
What is the principle of least privilege?
```

Expected:
- ✅ Response appears (streaming effect!)
- ✅ No errors
- ✅ Professional security advice

2. **Test 2: Multi-turn conversation**

Continue the conversation:
```
How does that apply to Azure managed identities?
```

Expected:
- ✅ Contextual response (remembers previous question)
- ✅ Mentions managed identities specifically
- ✅ Message count increments in sidebar

3. **Test 3: Technical question**

Ask:
```
Explain the difference between private endpoints and service endpoints.
```

Expected:
- ✅ Detailed technical response
- ✅ Mentions Azure networking concepts
- ✅ Streaming works smoothly

4. **Test 4: Session history**

Check if session is saved to storage:

```powershell
# In a NEW PowerShell window (keep app running!)
az storage blob list `
  --account-name $storageName `
  --container-name "chat-sessions" `
  --auth-mode login `
  --query "[].name" `
  --output table
```

Expected:
- ✅ See a `.json` file with your session ID
- ✅ File name matches session ID from sidebar

5. **Download and view session**:

```powershell
$sessionId = (az storage blob list --account-name $storageName --container-name "chat-sessions" --auth-mode login --query "[0].name" -o tsv)

az storage blob download `
  --account-name $storageName `
  --container-name "chat-sessions" `
  --name $sessionId `
  --file "C:\LabFiles\session-backup.json" `
  --auth-mode login

notepad C:\LabFiles\session-backup.json
```

Expected:
- ✅ JSON file with all your messages
- ✅ Timestamps
- ✅ Full conversation history

### Part 8: Security Validation

Let's verify the security configuration!

1. **Check for API keys in code** (should be NONE!):

```powershell
Select-String -Path "app.py" -Pattern "api[_-]?key" -CaseSensitive

# Should return: NO MATCHES FOUND
```

2. **Check .env file** (should have ONLY Key Vault name):

```powershell
Get-Content ".env"
```

Expected:
- ✅ Only `KEY_VAULT_NAME=...`
- ❌ NO API keys
- ❌ NO passwords
- ❌ NO connection strings

3. **Verify all authentication is managed identity**:

```powershell
Select-String -Path "app.py" -Pattern "DefaultAzureCredential"
```

Expected:
- ✅ Found! (This proves managed identity is used)

4. **Check that all secrets come from Key Vault**:

```powershell
Select-String -Path "app.py" -Pattern "secret_client.get_secret"
```

Expected:
- ✅ Multiple matches (OpenAIEndpoint, ChatModelDeployment, etc.)

### Part 9: Test Error Handling

Let's verify the app handles errors gracefully.

1. **Test invalid input**:

In the chat, try an extremely long prompt (copy-paste lorem ipsum 5 times).

Expected:
- ✅ App should handle it
- ✅ May truncate or return a sensible error
- ✅ App doesn't crash

2. **Test rapid requests**:

Send 3-4 messages quickly in succession.

Expected:
- ✅ All process correctly
- ✅ No rate limit errors (capacity set appropriately)
- ✅ Responses in correct order

### Part 10: Document Your Deployment

```powershell
@"
=== Secure Chat Application Deployment ===
Date: $(Get-Date)

Application Details:
- Name: Secure Azure OpenAI Chat
- Framework: Streamlit
- Location: C:\LabFiles\SecureAI\chat-app
- URL: http://localhost:8501

Security Configuration:
- Authentication: Managed Identity (DefaultAzureCredential)
- API Keys in Code: NONE ✅
- API Keys in .env: NONE ✅
- Secrets Storage: Azure Key Vault
- Network Access: Private Endpoints Only
- Public Internet: BLOCKED ✅

Key Vault Secrets Retrieved:
- OpenAIEndpoint
- ChatModelDeployment
- OpenAIApiVersion
- StorageAccountName

Azure Services Used:
1. Azure OpenAI (private endpoint)
   - Chat completions via managed identity
   
2. Azure Key Vault (private endpoint)
   - All configuration stored as secrets
   
3. Azure Storage (private endpoint)
   - Session history in 'chat-sessions' container
   
Features Working:
- ✅ Chat completions
- ✅ Streaming responses
- ✅ Multi-turn conversations
- ✅ Session history
- ✅ Managed identity auth
- ✅ Private endpoint connectivity
- ✅ Error handling

Performance:
- Latency: ~1-3 seconds per response
- Streaming: Real-time token display
- Session persistence: Automatic to blob storage

Test Results:
- Simple questions: PASSED ✅
- Multi-turn conversations: PASSED ✅
- Technical questions: PASSED ✅
- Session history: PASSED ✅
- Security validation: PASSED ✅

Ready for Testing via Bastion: ✅

Next Steps:
- Test access via Azure Bastion (Challenge 6)
- Validate WAF compliance (Challenge 7)
- Consider adding authentication/authorization
- Deploy to App Service with private endpoint
"@ | Out-File -FilePath "C:\LabFiles\app-deployment.txt"

notepad C:\LabFiles\app-deployment.txt
```

## Success Criteria

Validate your app deployment:

- [ ] Application directory created with proper structure
- [ ] All Python files created (`app.py`, `requirements.txt`, `README.md`)
- [ ] `.env` file created with ONLY Key Vault name (no secrets!)
- [ ] Virtual environment created and activated
- [ ] All dependencies installed successfully
- [ ] Storage Account name added to Key Vault
- [ ] Managed identity has Storage Blob Data Contributor role
- [ ] App starts without errors (`streamlit run app.py`)
- [ ] Browser opens to `http://localhost:8501`
- [ ] Sidebar shows "✅ Authenticated"
- [ ] Chat completions work (receive AI responses)
- [ ] Streaming responses work
- [ ] Multi-turn conversations work (context maintained)
- [ ] Session history saved to Blob Storage
- [ ] Security validation passed (no API keys, all managed identity)
- [ ] Error handling works (no crashes)
- [ ] Deployment documented in `app-deployment.txt`

## Troubleshooting

### Issue: "KEY_VAULT_NAME not set in .env file"

**Solution**:
- Verify `.env` file exists in `C:\LabFiles\SecureAI\chat-app\`
- Check the content:
  ```powershell
  Get-Content .env
  ```
- Should have: `KEY_VAULT_NAME=your-kv-name`
- Restart the app after editing

---

### Issue: "Authentication failed" or "DefaultAzureCredential failed"

**Solution**:
- Ensure you're running the app ON THE VM (managed identity only works there)
- Verify managed identity is enabled:
  ```powershell
  az vm show -n "vm-<inject key="DeploymentID"></inject>" -g "challenge-rg-<inject key="DeploymentID"></inject>" --query identity
  ```
- Wait 2-3 minutes after enabling managed identity
- Restart VS Code and try again

---

### Issue: "Secret not found: OpenAIEndpoint"

**Solution**:
- List all secrets in Key Vault:
  ```powershell
  az keyvault secret list --vault-name $kvName -o table
  ```
- Re-create missing secrets from Challenge 3 & 4
- Ensure exact names match (case-sensitive!)

---

### Issue: Streamlit won't start or shows "ModuleNotFoundError"

**Solution**:
- Ensure virtual environment is activated:
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
  Prompt should show `(venv)` prefix
- Reinstall dependencies:
  ```powershell
  pip install -r requirements.txt --force-reinstall
  ```

---

### Issue: Chat works but session history not saving

**Solution**:
- Check Storage Blob Data Contributor role:
  ```powershell
  az role assignment list --assignee $identityId --scope $storageId -o table
  ```
- Verify container exists:
  ```powershell
  az storage container list --account-name $storageName --auth-mode login -o table
  ```
- Check app sidebar for warning messages

---

### Issue: "Access denied" when accessing storage

**Solution**:
- Ensure Storage Account has public access disabled
- Verify private endpoint exists and is approved
- Check NSG allows traffic from application subnet to storage subnet
- Wait 5 minutes for RBAC to propagate

## Bonus Challenges

1. **Add User Authentication**:
   - Integrate Entra ID login
   - Show username in sidebar
   - Filter session history by user

2. **Implement RAG (Retrieval Augmented Generation)**:
   - Upload documents to Blob Storage
   - Generate embeddings with text-embedding-ada-002
   - Store in Azure AI Search
   - Enhance chat with document context

3. **Add Conversation Export**:
   - Button to download chat history as PDF or JSON
   - Include timestamp and metadata
   - Store exports in Blob Storage

4. **Deploy to Azure App Service**:
   - Create App Service with VNET integration
   - Configure managed identity for App Service
   - Deploy via Azure CLI or GitHub Actions
   - Access via private endpoint only

## What You Learned

In this challenge, you:

✅ Deployed a production-ready chat application  
✅ Configured managed identity authentication (zero API keys!)  
✅ Integrated Key Vault for all secrets  
✅ Enabled session history with Blob Storage  
✅ Validated private endpoint connectivity  
✅ Implemented secure enterprise chat patterns  
✅ Achieved 100% zero-trust architecture  

Your secure chat app is fully operational and production-ready!

## Next Steps

Application deployed: ✅ Working locally!

In **Challenge 6**, you'll test secure access to your VM and application using Azure Bastion. This validates that everything works through the secure network you built!

Head to **challenge-6.md** to test connectivity! 🔐

---

**Pro Tip**: This same architecture pattern can be used for ANY AI application - not just chat! Swap Streamlit for a REST API, add Azure API Management, and you have an enterprise-grade AI service!
