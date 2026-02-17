# Challenge 04: Secure Azure OpenAI Deployment

## Introduction

Your OpenAI service is deployed with a private endpoint, but it's not fully configured yet. In this challenge, you'll deploy GPT models, configure content filtering, test embeddings, and validate that everything works through the private network with managed identity authentication.

By the end, you'll have a fully operational, secure OpenAI service ready for your chat application!

## Prerequisites

- Completed Challenge 3 (Managed identity and RBAC configured)
- Azure OpenAI resource deployed with private endpoint
- Managed identity has "Cognitive Services OpenAI User" role
- Key Vault configured with OpenAI endpoint secret
- Connected to VM via Azure Bastion
- VS Code open with PowerShell terminal
- Azure CLI logged in (`az login` completed)

## Challenge Objectives

- Deploy GPT-4 (or GPT-3.5-Turbo) model for chat completions
- Deploy text-embedding model for semantic search
- Configure content filtering policies
- Test model deployments using managed identity
- Store model deployment names in Key Vault
- Validate private endpoint connectivity
- Benchmark model performance

## Steps to Complete

### Part 1: Review OpenAI Resource Configuration

1. **In Azure Portal**, navigate to your **openai-secureai-<inject key="DeploymentID" enableCopy="false"/>** resource.

1. Verify the resource is deployed:
   - Note the **Location/Region**
   - Click **Networking** in the left menu
   - Verify **Public network access** is restricted or disabled
   - Check that **Private endpoint connections** show as **Approved**

1. **Optional - Verify using VS Code PowerShell** (to get resource details):

```powershell
$openaiName = az cognitiveservices account list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[?kind=='OpenAI'].name" -o tsv

Write-Host "OpenAI Resource: $openaiName"

# Get endpoint
$endpoint = az cognitiveservices account show `
 --name $openaiName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query properties.endpoint -o tsv

Write-Host "Endpoint: $endpoint"

# Check public access status
$publicAccess = az cognitiveservices account show `
 --name $openaiName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query properties.publicNetworkAccess -o tsv

Write-Host "Public Network Access: $publicAccess"
```

Should show: `Public Network Access: Disabled` or `Enabled` (depending on your Challenge 2 configuration)

### Part 2: Check Available Models in Your Region

Before deploying, verify which models are available using Azure AI Foundry portal.

1. **In Azure Portal**, go to your **openai-secureai-<inject key="DeploymentID" enableCopy="false"/>** resource.

1. Click **Go to Azure AI Foundry portal** (or **Go to Foundry portal**).

1. In Azure AI Foundry:
   - Click **Models + endpoints** in the left navigation
   - Click **Model catalog** tab
   - Search for **gpt-4** to see if it's available in your region
   - Also search for **gpt-35-turbo** as a backup option

1. **Optional - Check via VS Code PowerShell**:

```powershell
# List available models
az cognitiveservices account list-models `
 --name $openaiName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[?model.lifecycleStatus=='GenerallyAvailable'].{Name:model.name, Version:model.version, Format:model.format}" `
 --output table

# Check GPT-4 availability
az cognitiveservices account list-models `
 --name $openaiName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[?contains(model.name, 'gpt-4')]" `
 --output table
```

If GPT-4 is not available, you'll use GPT-3.5-Turbo (which is fine for this lab!).

### Part 3: Deploy GPT Model for Chat (Using Azure Portal)

Deploy your primary chat model using Azure AI Foundry portal.

> **Note**: Model deployment is easier and more intuitive through the Azure Portal for hackathons!

1. **In Azure AI Foundry portal**, click **Models + endpoints** in the left navigation.

1. Click **+ Deploy model** ? **Deploy base model**.

1. Search for and select **gpt-4.1** (or **gpt-4**) in the model catalog.

1. Click **Confirm**.

1. Configure:
   - **Deployment name**: **gpt-4-chat**
   - **Deployment type**: **Global Standard**
   - **TPM**: **20K**

1. Click **Deploy** and wait (30-60 seconds).

**If GPT-4 unavailable**: Use **gpt-35-turbo-chat** instead (TPM: 50K).

### Part 4: Deploy Embedding Model (Using Azure Portal - Optional)

1. **In Azure AI Foundry**, click **+ Deploy model** ? **Deploy base model**.

1. Search for **text-embedding-ada-002** and deploy it:
   - **Deployment name**: **text-embedding-ada-002**
   - **TPM**: **50K**

1. Verify both models are deployed in Models + endpoints list.

### Part 5: Configure Content Filtering

Azure OpenAI includes responsible AI content filtering. Let's review and configure it.

1. **View current content filter**:

   In the Azure Portal:
   - Navigate to your Azure OpenAI resource
   - Click **Content filters** (left menu under Management)
   - You'll see the default filter policy

2. **Create a custom content filter** (optional, for learning):

   In the portal:
   - Click **+ Create content filter**
   - Name: `strict-filter`
   - Configure filters: **Hate**: Severity High - Block, **Sexual**: Severity Medium - Block, **Violence**: Severity High - Block, **Self-harm**: Severity Medium - Block
   - Click **Create**

3. **Apply filter to your deployment**:

   - Go back to **Deployments**
   - Click on your GPT deployment
   - Click **Edit**
   - Under **Content filter**, select `strict-filter`
   - Click **Save**

### Part 6: Store Model Configuration in Key Vault

Store deployment names securely for your app to retrieve.

1. **Get Key Vault name**:

```powershell
$kvName = az keyvault list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[?contains(name, 'kv')].name" -o tsv
```

2. **Store chat model deployment name**:

```powershell
# If you deployed GPT-4:
az keyvault secret set `
 --vault-name $kvName `
 --name "ChatModelDeployment" `
 --value "gpt-4-chat"

# OR if you deployed GPT-3.5-Turbo:
# az keyvault secret set --vault-name $kvName --name "ChatModelDeployment" --value "gpt-35-turbo-chat"
```

3. **Store embedding model deployment name**:

```powershell
az keyvault secret set `
 --vault-name $kvName `
 --name "EmbeddingModelDeployment" `
 --value "text-embedding-ada-002"
```

4. **Store API version** (so app doesn't break when Azure updates):

```powershell
az keyvault secret set `
 --vault-name $kvName `
 --name "OpenAIApiVersion" `
 --value "2024-02-15-preview"
```

### Part 7: Test Chat Completions with Managed Identity

Validate everything works end-to-end.

1. **Create a comprehensive test script**:

```powershell
@'
"""
Test Azure OpenAI Chat Completions via Private Endpoint with Managed Identity
No API keys! Pure Entra ID authentication.
"""
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from openai import AzureOpenAI
import json

print("=" * 60)
print("SECURE AZURE OPENAI TEST")
print("=" * 60)

# Initialize managed identity
credential = DefaultAzureCredential()
print("\nManaged Identity authenticated")

# Connect to Key Vault
kv_name = "$kvName"
kv_url = f"https://{kv_name}.vault.azure.net"
secret_client = SecretClient(vault_url=kv_url, credential=credential)
print(f"Connected to Key Vault: {kv_name}")

# Retrieve configuration from Key Vault (zero hardcoded values!)
openai_endpoint = secret_client.get_secret("OpenAIEndpoint").value
chat_deployment = secret_client.get_secret("ChatModelDeployment").value
api_version = secret_client.get_secret("OpenAIApiVersion").value

print(f"\nOpenAI Endpoint: {openai_endpoint}")
print(f"Chat Deployment: {chat_deployment}")
print(f"API Version: {api_version}")

# Create OpenAI client with managed identity
print("\nCreating OpenAI client with managed identity token...")
client = AzureOpenAI(
 azure_endpoint=openai_endpoint,
 api_version=api_version,
 azure_ad_token_provider=lambda: credential.get_token(
 "https://cognitiveservices.azure.com/.default"
 ).token
)
print("OpenAI client initialized (no API key used!)")

# Test 1: Simple chat completion
print("\n" + "=" * 60)
print("TEST 1: Simple Chat Completion")
print("=" * 60)

messages = [
 {"role": "system", "content": "You are a helpful AI assistant specializing in cloud security."},
 {"role": "user", "content": "Explain the principle of least privilege in 2 sentences."}
]

print("\n Sending chat request...")
response = client.chat.completions.create(
 model=chat_deployment,
 messages=messages,
 max_tokens=150,
 temperature=0.7
)

print(f"\n AI Response:")
print(f"{response.choices[0].message.content}\n")
print(f" Tokens used: {response.usage.total_tokens}")
print(f" Finish reason: {response.choices[0].finish_reason}")

# Test 2: Multi-turn conversation
print("\n" + "=" * 60)
print("TEST 2: Multi-Turn Conversation")
print("=" * 60)

conversation = [
 {"role": "system", "content": "You are a security expert."},
 {"role": "user", "content": "What is a managed identity?"},
]

print("\n Turn 1: What is a managed identity?")
response = client.chat.completions.create(
 model=chat_deployment,
 messages=conversation,
 max_tokens=100
)
assistant_reply = response.choices[0].message.content
print(f" {assistant_reply}")

# Add to conversation
conversation.append({"role": "assistant", "content": assistant_reply})
conversation.append({"role": "user", "content": "How is it different from a service principal?"})

print("\n Turn 2: How is it different from a service principal?")
response = client.chat.completions.create(
 model=chat_deployment,
 messages=conversation,
 max_tokens=150
)
print(f" {response.choices[0].message.content}")

# Test 3: Streaming response
print("\n" + "=" * 60)
print("TEST 3: Streaming Response")
print("=" * 60)

print("\n Question: Write a haiku about cloud security")
print(" Streaming response:\n")

stream = client.chat.completions.create(
 model=chat_deployment,
 messages=[
 {"role": "system", "content": "You are a creative poet."},
 {"role": "user", "content": "Write a haiku about cloud security."}
 ],
 max_tokens=100,
 stream=True
)

for chunk in stream:
 if chunk.choices[0].delta.content:
 print(chunk.choices[0].delta.content, end='', flush=True)

print("\n")

# Final summary
print("\n" + "=" * 60)
print("ALL TESTS PASSED!")
print("=" * 60)
print("\nAzure OpenAI is fully operational with:")
print(" � Private endpoint connectivity")
print(" � Managed identity authentication (zero API keys)")
print(" � Secrets stored in Key Vault")
print(" � Chat completions working")
print(" � Streaming responses working")
print("\n100% secure, production-ready configuration!")
print("=" * 60)

'@ -replace '\$kvName', $kvName | Out-File -FilePath "C:\LabFiles\test_openai_complete.py" -Encoding UTF8

python "C:\LabFiles\test_openai_complete.py"
```

2. **Expected output** - All tests should pass! 

### Part 8: Test Embeddings (If Deployed)

If you deployed the embedding model, test it:

```powershell
@'
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from openai import AzureOpenAI
import numpy as np

credential = DefaultAzureCredential()
kv_url = f"https://$kvName.vault.azure.net"
secret_client = SecretClient(vault_url=kv_url, credential=credential)

openai_endpoint = secret_client.get_secret("OpenAIEndpoint").value
embedding_deployment = secret_client.get_secret("EmbeddingModelDeployment").value
api_version = secret_client.get_secret("OpenAIApiVersion").value

client = AzureOpenAI(
 azure_endpoint=openai_endpoint,
 api_version=api_version,
 azure_ad_token_provider=lambda: credential.get_token("https://cognitiveservices.azure.com/.default").token
)

print(" Testing Embeddings...\n")

# Generate embeddings
texts = [
 "Azure OpenAI provides enterprise-ready AI models",
 "Managed identity eliminates the need for API keys",
 "What is the weather today?"
]

for text in texts:
 response = client.embeddings.create(
 model=embedding_deployment,
 input=text
 )
 embedding = response.data[0].embedding
 print(f"Text: {text}")
 print(f"Embedding dimension: {len(embedding)}")
 print(f"First 5 values: {embedding[:5]}\n")

print("Embeddings working! Dimension: 1536 (text-embedding-ada-002)")

'@ -replace '\$kvName', $kvName | Out-File -FilePath "C:\LabFiles\test_embeddings.py" -Encoding UTF8

python "C:\LabFiles\test_embeddings.py"
```

### Part 9: Monitor OpenAI Metrics

Check usage and performance.

1. **In Azure Portal**, go to your OpenAI resource

2. Click **Metrics** (left menu under Monitoring)

3. **Add metrics to track**:
   - **Total Calls**: Shows request volume
   - **Processed Inference Tokens**: Token consumption
   - **Time to Response**: Latency

4. **Set time range** to "Last hour" to see your test requests

5. **Create an alert** (optional):
   - Click **New alert rule**
   - Condition: `Total Calls > 1000` (or your threshold)
   - Action: Email notification
   - This helps monitor unexpected usage spikes

### Part 10: Document Your OpenAI Configuration

```powershell
@"
=== Azure OpenAI Configuration ===
Date: $(Get-Date)

Resource Details:
- Name: $openaiName
- Endpoint: $endpoint
- Public Access: Disabled
- Private Endpoint: Enabled & Approved

Model Deployments:
1. Chat Model: $(try { az keyvault secret show --vault-name $kvName --name "ChatModelDeployment" --query value -o tsv } catch { "gpt-4-chat or gpt-35-turbo-chat" })
 - Use: Chat completions
 - Capacity: 20-50 tokens/min
 
2. Embedding Model: text-embedding-ada-002
 - Use: Semantic search, RAG
 - Dimension: 1536
 - Capacity: 50 tokens/min

Content Filtering:
- Default: Azure content safety filters
- Custom: strict-filter (optional)
- Categories: Hate, Sexual, Violence, Self-harm

Key Vault Secrets:
- OpenAIEndpoint
- ChatModelDeployment
- EmbeddingModelDeployment
- OpenAIApiVersion

Authentication:
- Method: Managed Identity (Entra ID)
- Role: Cognitive Services OpenAI User
- API Keys: NEVER USED

Network Security:
- Public Access: DISABLED
- Access Method: Private endpoint only
- DNS Resolution: Private IP (10.0.x.x)

Performance Benchmarks:
- Latency: Check Azure Portal ? Metrics
- Token throughput: Monitor in Metrics
- Success rate: Should be >99%

Ready for Production: YES
"@ | Out-File -FilePath "C:\LabFiles\openai-config.txt"

notepad C:\LabFiles\openai-config.txt
```

## Success Criteria

Validate your OpenAI setup:

- [ ] GPT-4 or GPT-3.5-Turbo model deployed successfully
- [ ] Embedding model (text-embedding-ada-002) deployed (optional)
- [ ] Model deployment status is "Succeeded"
- [ ] Content filtering configured
- [ ] Model deployment names stored in Key Vault
- [ ] API version stored in Key Vault
- [ ] Test script successfully calls chat completions using managed identity
- [ ] Streaming responses work
- [ ] Multi-turn conversations work
- [ ] Embeddings work (if deployed)
- [ ] All authentication uses managed identity (zero API keys)
- [ ] Metrics visible in Azure Portal
- [ ] Configuration documented in `openai-config.txt`
