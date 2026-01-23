# Secure AI Chatbot - Testing App

## 🔒 Security Features
- **No API keys stored** - Uses Azure Managed Identity
- **Passwordless authentication** - Entra ID tokens only
- **Secrets in Key Vault** - No hardcoded configuration
- **Private network** - Connects via VNet (once private endpoints configured)

## 📋 Prerequisites
1. VM with managed identity enabled
2. Managed identity has these roles:
   - **Cognitive Services OpenAI User** (on OpenAI resource)
   - **Key Vault Secrets User** (on Key Vault)
3. Key Vault contains:
   - `OpenAIEndpoint`
   - `OpenAIDeployment`
   - `OpenAIApiVersion`

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Update Key Vault name
Edit `secure-chatbot.py` line 20:
```python
kv_name = "kv-secureai-2036950"  # Your Key Vault name
```

### 3. Run the chatbot
```bash
python secure-chatbot.py
```

### 4. Chat!
```
You: What is the capital of France?
AI: The capital of France is Paris.

You: Tell me a fun fact about AI
AI: ...

You: exit
👋 Goodbye!
```

## 🧪 Testing Commands

Test from Cloud Shell (if you need to verify):
```powershell
# Get variables
$kvName = "kv-secureai-2036950"
$openaiName = "openai-secureai-2036950"

# Check managed identity
az vm identity show `
  --resource-group "challenge-rg-2036950" `
  --name "labvm-2036950" `
  --query principalId -o tsv

# Check role assignments
$identityId = "74383812-fd6a-44e6-8f4b-69f95122e16b"
az role assignment list --assignee $identityId --output table
```

## 🛠️ Troubleshooting

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

## 📝 Notes
- This app uses **managed identity only** - no API keys!
- All configuration comes from **Key Vault**
- Conversation history is maintained in memory only
- Type 'exit' or 'quit' to end the chat

---

**Security Best Practice**: Never hardcode API keys or secrets. Always use managed identity + Key Vault for production applications.
