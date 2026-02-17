# 🔒 Secure Azure OpenAI Chat Application

A production-grade, enterprise-ready chat application built with Azure OpenAI, featuring complete security controls including Managed Identity authentication, Key Vault secret management, and private endpoint connectivity.

[![Azure](https://img.shields.io/badge/Azure-OpenAI-blue)](https://azure.microsoft.com/services/cognitive-services/openai-service/)
[![Python](https://img.shields.io/badge/Python-3.11+-green)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31+-red)](https://streamlit.io)
[![Security](https://img.shields.io/badge/Security-Enterprise%20Grade-gold)](https://docs.microsoft.com/azure/security/)

---

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Security Model](#-security-model)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [Usage](#-usage)
- [Troubleshooting](#-troubleshooting)
- [Development](#-development)
- [Contributing](#-contributing)

---

## ✨ Features

### Security Features
- 🔐 **Managed Identity** - Zero API keys in code or configuration
- 🔑 **Key Vault Integration** - All secrets centralized and secured
- 🌐 **Private Endpoints** - No public internet exposure
- 🛡️ **RBAC Access Control** - Fine-grained permissions

### Application Features
- 💬 **Streaming Responses** - Real-time AI response generation
- 🔄 **Multi-turn Conversations** - Context-aware chat with history
- 💾 **Session Persistence** - Chat history saved to Azure Blob Storage
- 📱 **Responsive UI** - Professional enterprise-grade interface
- 📥 **Export Capability** - Download chat history as JSON

### Enterprise Readiness
- 📊 **Logging** - Comprehensive application logging
- ⚡ **Error Handling** - Graceful error recovery
- ✅ **Input Validation** - Security-first input processing
- 🔒 **Content Filtering** - Azure AI content moderation

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User's Browser                           │
│                  http://localhost:8501                      │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│              Azure VM (Application Subnet)                  │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │         Streamlit Application (app.py)                │  │
│  │                                                       │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐  │  │
│  │  │   Config    │  │  Services   │  │    Utils     │  │  │
│  │  │  Settings   │  │ - KeyVault  │  │  - Logger    │  │  │
│  │  │             │  │ - OpenAI    │  │  - Validator │  │  │
│  │  │             │  │ - Storage   │  │              │  │  │
│  │  └─────────────┘  └─────────────┘  └──────────────┘  │  │
│  │                                                       │  │
│  │            DefaultAzureCredential                     │  │
│  │           (Managed Identity Auth)                     │  │
│  └─────────────────────┬─────────────────────────────────┘  │
│                        │                                    │
└────────────────────────┼────────────────────────────────────┘
                         │ Private Endpoints
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│  Key Vault  │  │ Azure OpenAI│  │   Storage   │
│  (Secrets)  │  │ (Chat/GPT)  │  │  (Sessions) │
│  10.0.2.x   │  │  10.0.1.x   │  │  10.0.2.x   │
└─────────────┘  └─────────────┘  └─────────────┘
```

---

## 🔒 Security Model

### Zero Trust Architecture

| Component | Security Control |
|-----------|-----------------|
| **Authentication** | Managed Identity (DefaultAzureCredential) |
| **Secrets** | Azure Key Vault with RBAC |
| **Network** | Private endpoints, no public IPs |
| **Data** | Encrypted at rest and in transit |
| **Content** | Azure AI content filtering |

### What We DON'T Store

- ❌ API keys
- ❌ Connection strings
- ❌ Passwords
- ❌ Certificates
- ❌ Any credentials

### Required RBAC Roles

| Role | Resource | Purpose |
|------|----------|---------|
| Key Vault Secrets User | Key Vault | Read secrets |
| Cognitive Services OpenAI User | Azure OpenAI | Chat completions |
| Storage Blob Data Contributor | Storage Account | Session history |

---

## 📦 Prerequisites

### Azure Resources

1. **Azure VM** with System-assigned Managed Identity enabled
2. **Azure Key Vault** with secrets configured
3. **Azure OpenAI** with GPT model deployed
4. **Azure Storage Account** (optional, for session history)
5. **Private endpoints** for all services

### Key Vault Secrets Required

| Secret Name | Description | Example |
|-------------|-------------|---------|
| `OpenAIEndpoint` | Azure OpenAI endpoint URL | `https://openai-xxx.openai.azure.com/` |
| `ChatModelDeployment` | GPT model deployment name | `gpt-4` or `secure-chat` |
| `OpenAIApiVersion` | API version | `2024-08-01-preview` |
| `StorageAccountName` | Storage account name (optional) | `storsecureai123` |

### Local Requirements

- Python 3.11 or higher
- pip (Python package manager)
- Azure CLI (for local development)

---

## 🚀 Quick Start

### 1. Clone/Download the Project

```bash
cd C:\Code\SecureAI
# Project files should be in chat-app directory
```

### 2. Create Virtual Environment

```powershell
# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
# Copy example configuration
cp .env.example .env

# Edit .env and set your Key Vault name
# Only KEY_VAULT_NAME is required!
```

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

---

## ⚙️ Configuration

### Environment Variables (`.env`)

```env
# REQUIRED - Your Key Vault name
KEY_VAULT_NAME=kv-secureai-XXXXXXX

# OPTIONAL - Application settings
APP_NAME=Secure Enterprise Chat
DEBUG=false
MAX_TOKENS=1000
TEMPERATURE=0.7
LOG_LEVEL=INFO
```

### Key Vault Setup

Create the required secrets in Azure Key Vault:

```powershell
# Using Azure CLI
$kvName = "kv-secureai-XXXXXXX"

az keyvault secret set --vault-name $kvName --name "OpenAIEndpoint" --value "https://your-openai.openai.azure.com/"
az keyvault secret set --vault-name $kvName --name "ChatModelDeployment" --value "gpt-4"
az keyvault secret set --vault-name $kvName --name "OpenAIApiVersion" --value "2024-08-01-preview"
az keyvault secret set --vault-name $kvName --name "StorageAccountName" --value "yourstorageaccount"
```

---

## 📁 Project Structure

```
codefiles/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment template
├── .env                  # Your configuration (create from .env.example)
├── README.md             # This file
│
├── config/               # Configuration management
│   ├── __init__.py
│   └── settings.py       # Settings dataclass and loading
│
├── services/             # Azure service integrations
│   ├── __init__.py
│   ├── azure_auth.py     # Managed Identity authentication
│   ├── keyvault_service.py  # Key Vault secret retrieval
│   ├── openai_service.py    # Azure OpenAI chat client
│   └── storage_service.py   # Blob storage for sessions
│
└── utils/                # Utility functions
    ├── __init__.py
    ├── logger.py         # Logging configuration
    └── validators.py     # Input validation
```

---

## 💻 Usage

### Starting a Chat

1. Open the application in your browser
2. Verify the sidebar shows green status indicators
3. Type your message in the chat input
4. Press Enter to send

### Chat Commands

| Action | How To |
|--------|--------|
| Send message | Type and press Enter |
| Clear chat | Click "🗑️ Clear Chat" in sidebar |
| New session | Click "🔄 New Session" in sidebar |
| Export chat | Click "📥 Export Chat" in sidebar |

### Example Prompts

```
What is the principle of least privilege?
How do I configure private endpoints in Azure?
Explain the difference between service endpoints and private endpoints.
What are best practices for Azure Key Vault?
```

---

## 🔧 Troubleshooting

### Common Issues

#### "KEY_VAULT_NAME not set"

**Cause:** Missing or empty `.env` file

**Solution:**
```powershell
cp .env.example .env
# Edit .env and set KEY_VAULT_NAME=your-keyvault-name
```

#### "Authentication failed"

**Cause:** Not running on Azure VM or Azure CLI not authenticated

**Solutions:**
- On Azure VM: Ensure System-assigned Managed Identity is enabled
- Local development: Run `az login` first

#### "Secret not found"

**Cause:** Required secrets not in Key Vault

**Solution:**
```powershell
az keyvault secret list --vault-name YOUR_KV_NAME
# Create any missing secrets
```

#### "Connection error to OpenAI"

**Cause:** Private endpoint or DNS issues

**Solutions:**
1. Verify private endpoint exists for OpenAI
2. Test DNS resolution: `nslookup your-openai.openai.azure.com`
3. Check NSG rules allow traffic

#### "Custom subdomain required"

**Cause:** OpenAI resource doesn't have custom domain configured

**Solution:**
```powershell
az cognitiveservices account update \
  --name your-openai-name \
  --resource-group your-rg \
  --custom-domain your-openai-name
```

### Debug Mode

Enable debug logging for more details:

```env
DEBUG=true
LOG_LEVEL=DEBUG
```

---

## 🛠️ Development

### Running Tests

```bash
# Syntax check
python -m py_compile app.py

# Import test
python -c "from config import get_settings; print(get_settings())"
```

### Code Style

The project follows:
- PEP 8 style guidelines
- Type hints for function signatures
- Docstrings for all public functions
- Meaningful variable names

### Adding New Features

1. Create feature branch
2. Add tests if applicable
3. Update README if needed
4. Submit pull request

---

## 📄 License

This project is part of the "Deploy Your AI Application in Production" hackathon challenge.

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📞 Support

If you encounter issues:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Review Azure service health status
3. Verify all prerequisites are met
4. Enable debug mode for detailed logs

---

**Built with ❤️ using Azure AI and Streamlit**

Test from Cloud Shell (if you need to verify):
```powershell
# Get your deployment ID and set variables
$deploymentId = "<your-deployment-id>"
$kvName = "kv-secureai-$deploymentId"
$openaiName = "openai-secureai-$deploymentId"

# Check managed identity
$identityId = az vm identity show `
 --resource-group "challenge-rg-$deploymentId" `
 --name "vm-$deploymentId" `
 --query principalId -o tsv

# Check role assignments
az role assignment list --assignee $identityId --output table
```

## ️ Troubleshooting

### Error: "DefaultAzureCredential failed to retrieve a token"
- Make sure you're running on the VM with managed identity
- VM must have system-assigned managed identity enabled

### Error: "Connection is not an approved private link"
- Key Vault public access is disabled
- Temporarily enable: `az keyvault update --name kv-xxx --public-network-access Enabled`
- Or run from VM inside VNet (preferred)

### Error: "Forbidden" when calling OpenAI
- Check managed identity has "Cognitive Services OpenAI User" role
- Verify role assignment: `az role assignment list --assignee <identity-id>`

### Model not found
- Verify deployment name matches Key Vault secret "OpenAIDeployment"
- Check deployment exists: `az cognitiveservices account deployment list`

## Notes
- This app uses **managed identity only** - no API keys!
- All configuration comes from **Key Vault**
- Conversation history is maintained in memory only
- Type 'exit' or 'quit' to end the chat

---

**Security Best Practice**: Never hardcode API keys or secrets. Always use managed identity + Key Vault for production applications.
