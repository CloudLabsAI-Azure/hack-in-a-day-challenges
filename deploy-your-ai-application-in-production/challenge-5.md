# Challenge 05: Deploy Secure Chat Application

## Introduction

All the infrastructure is ready! Now comes the fun part - deploying a secure, production-ready chat application that uses everything you've built:

- Private endpoints (no public access)
- Managed identity (no API keys)
- Key Vault secrets (zero hardcoded credentials)
- Azure OpenAI (chat models ready)

You'll download a pre-built Streamlit chat app, configure it using **only environment variables** (no code changes!), and run it on your VM.

Let's build a secure ChatGPT-like experience!

## Prerequisites

- Completed Challenge 4 (OpenAI models deployed and tested)
- All Key Vault secrets created (OpenAIEndpoint, ChatModelDeployment, etc.)
- Managed identity configured on **vm-<inject key="DeploymentID" enableCopy="false"/>** with proper RBAC roles
- Python 3.11 and VS Code installed on **vm-<inject key="DeploymentID" enableCopy="false"/>**
- Connected to **vm-<inject key="DeploymentID" enableCopy="false"/>** via Azure Bastion

## Challenge Objectives

- Download the pre-built secure chat application
- Create `.env` file with Key Vault-based configuration
- Install Python dependencies
- Run the chat app locally
- Test chat functionality with managed identity
- Validate security (no API keys, private endpoints only)
- Test session history with Storage Account

## Steps to Complete

### Part 1: Create Application Directory Structure

1. **Connect to vm-<inject key="DeploymentID" enableCopy="false"/>** via Azure Bastion if not already connected.

1. **Open VS Code** on the VM and open a PowerShell terminal (Ctrl + `).

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
+-- pages/
+-- utils/
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
 page_icon="\N{lock}",
 layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
 st.session_state.messages = []
if "session_id" not in st.session_state:
 st.session_state.session_id = str(uuid.uuid4())

# Title and security badge
st.title("Secure Enterprise Chat")
st.caption("100% Private | Managed Identity | No API Keys | Enterprise-Grade Security")

# Sidebar for config info
with st.sidebar:
 st.header("Security Status")
 
 # Initialize services with managed identity
 try:
 with st.spinner("Authenticating with Managed Identity..."):
 credential = DefaultAzureCredential()
 
 # Get Key Vault name from environment
 kv_name = os.getenv("KEY_VAULT_NAME")
 if not kv_name:
 st.error("KEY_VAULT_NAME not set in .env file")
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
 
 st.success("Authenticated")
 st.info(f"Model: {chat_deployment}")
 st.info(f"Auth: Managed Identity")
 st.info(f"Network: Private Only")
 if storage_enabled:
 st.info(f"Storage: Enabled")
 
 except Exception as e:
 st.error(f"Authentication failed: {str(e)}")
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
 if st.button("Clear Chat"):
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
 with st.spinner("Thinking..."):
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
 stream=True # Streaming for better UX
 )
 
 # Stream response
 response_placeholder = st.empty()
 full_response = ""
 
 for chunk in response:
 if chunk.choices[0].delta.content:
 full_response += chunk.choices[0].delta.content
 response_placeholder.markdown(full_response + "�")
 
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
 st.sidebar.warning(f"Could not save session: {str(e)[:50]}")
 
 except Exception as e:
 st.error(f"Error: {str(e)}")
 st.error("Check that OpenAI model is deployed and accessible via private endpoint.")

# Footer
st.divider()
st.caption("Enterprise Security: All connections encrypted and routed through private endpoints. Zero public internet exposure. Managed identity authentication only.")
'@ | Out-File -FilePath "app.py" -Encoding UTF8

Write-Host "Created app.py"
```

2. **Create requirements.txt**:

```powershell
@'
streamlit==1.31.0
openai==2.15.0
azure-identity==1.15.0
azure-keyvault-secrets==4.7.0
azure-storage-blob==12.19.0
python-dotenv==1.0.0
'@ | Out-File -FilePath "requirements.txt" -Encoding UTF8

Write-Host "Created requirements.txt"
```

> **Critical**: We're using `openai==2.15.0` (or later). Versions earlier than 2.x will fail with errors like "Client.__init__() got an unexpected keyword argument 'proxies'". This is due to breaking changes in the OpenAI Python SDK and its compatibility with Azure SDK components.

3. **Create README**:

```powershell
@'
# Secure Azure OpenAI Chat Application

## Security Features
- Managed Identity authentication (zero API keys)
- Key Vault for all secrets
- Private endpoints only (no public internet)
- Session history in secure storage
- Content filtering enabled
- Enterprise-grade encryption

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
1. No API keys in code
2. No credentials in .env
3. All secrets in Key Vault
4. Private endpoints only
5. Managed identity auth
'@ | Out-File -FilePath "README.md" -Encoding UTF8

Write-Host "Created README.md"
```

### Part 3: Create Environment Configuration

1. **Get your Key Vault name and create `.env` file**:

```powershell
$kvName = az keyvault list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[0].name" -o tsv

Write-Host "Key Vault Name: $kvName"

# Create .env file (ONLY Key Vault name - all other config from KV!)
@"
# Secure Chat Application Configuration
# Only the Key Vault name is needed - everything else retrieved from Key Vault!
KEY_VAULT_NAME=$kvName
"@ | Out-File -FilePath ".env" -Encoding UTF8

Write-Host "Created .env file"
```

2. **Store Storage Account name in Key Vault** (if not already done in Challenge 3):

```powershell
$storageName = az storage account list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[0].name" -o tsv

# Temporarily enable Key Vault public access
az keyvault update `
 --name $kvName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --public-network-access Enabled

az keyvault secret set `
 --vault-name $kvName `
 --name "StorageAccountName" `
 --value $storageName

Write-Host "Stored StorageAccountName in Key Vault"

# Disable public access again
az keyvault update `
 --name $kvName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --public-network-access Disabled

Write-Host "Key Vault secured"
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

### Part 5: Verify Storage Account Access

The app saves session history to Blob Storage. Verify managed identity has access (should be assigned from Challenge 3).

```powershell
$identityId = az vm show `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --name "vm-<inject key="DeploymentID" enableCopy="false"/>" `
 --query identity.principalId -o tsv

$storageName = az storage account list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[0].name" -o tsv

$storageId = az storage account show `
 --name $storageName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query id -o tsv

# Check if role is already assigned
$existing = az role assignment list `
 --assignee $identityId `
 --scope $storageId `
 --query "[?roleDefinitionName=='Storage Blob Data Contributor']" -o tsv

if (-not $existing) {
 az role assignment create `
 --assignee $identityId `
 --role "Storage Blob Data Contributor" `
 --scope $storageId
 Write-Host "Assigned Storage Blob Data Contributor"
} else {
 Write-Host "Storage Blob Data Contributor already assigned"
}
```

### Part 6: Run the Chat Application

 Moment of truth!

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
   - Title: " Secure Enterprise Chat"
   - Sidebar showing: " Authenticated"
   - Model name displayed
   - "Auth: Managed Identity"
   - "Network: Private Only"
   - Chat input box ready

### Part 7: Test the Chat Application

1. **Send a test message** in the chat input:

```
What is the principle of least privilege?
```

   - You should receive an AI response with streaming effect
   - Sidebar shows **Authenticated**, **Managed Identity**, and **Private Only**

2. **Send a follow-up** to test multi-turn conversation:

```
How does that apply to Azure managed identities?
```

   - Response should reference the previous question (context maintained)

3. **Verify no API keys in code** (quick security check):

   Open a **new** PowerShell terminal (keep app running) and run:

```powershell
Select-String -Path "C:\LabFiles\SecureAI\chat-app\app.py" -Pattern "api[_-]?key"
# Should return NO MATCHES
```

## Success Criteria

Validate your app deployment:

- [ ] Application files created (`app.py`, `requirements.txt`)
- [ ] `.env` file created with ONLY Key Vault name (no secrets!)
- [ ] Virtual environment created and dependencies installed
- [ ] App starts without errors (`streamlit run app.py`)
- [ ] Sidebar shows "Authenticated" with Managed Identity
- [ ] Chat completions work (receive AI responses)
- [ ] Multi-turn conversations work (context maintained)
- [ ] No API keys in code or config files
