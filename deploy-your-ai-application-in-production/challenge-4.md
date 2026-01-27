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

1. **Get your OpenAI resource details**:

```powershell
$openaiName = az cognitiveservices account list `
 --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
 --query "[?kind=='OpenAI'].name" -o tsv

Write-Host "OpenAI Resource: $openaiName"

# Get endpoint
$endpoint = az cognitiveservices account show `
 --name $openaiName `
 --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
 --query properties.endpoint -o tsv

Write-Host "Endpoint: $endpoint"

# Check public access status
$publicAccess = az cognitiveservices account show `
 --name $openaiName `
 --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
 --query properties.publicNetworkAccess -o tsv

Write-Host "Public Network Access: $publicAccess"
```

Should show: `Public Network Access: Disabled`

2. **View private endpoint connection**:

```powershell
az cognitiveservices account show `
 --name $openaiName `
 --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
 --query properties.privateEndpointConnections `
 --output table
```

Status should be: `Approved`

### Part 2: Check Available Models in Your Region

Before deploying, verify which models are available.

1. **List available models**:

```powershell
az cognitiveservices account list-models `
 --name $openaiName `
 --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
 --query "[?model.lifecycleStatus=='GenerallyAvailable'].{Name:model.name, Version:model.version, Format:model.format}" `
 --output table
```

2. **Check GPT-4 availability**:

```powershell
az cognitiveservices account list-models `
 --name $openaiName `
 --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
 --query "[?contains(model.name, 'gpt-4')]" `
 --output table
```

If GPT-4 is not available, you'll use GPT-3.5-Turbo (which is fine for this lab!).

### Part 3: Deploy GPT Model for Chat

Deploy your primary chat model.

1. **Deploy GPT-4** (if available in your region):

```powershell
az cognitiveservices account deployment create `
 --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
 --name $openaiName `
 --deployment-name "gpt-4-chat" `
 --model-name "gpt-4" `
 --model-version "turbo-2024-04-09" `
 --model-format "OpenAI" `
 --sku-name "Standard" `
 --sku-capacity 20
```

**OR**, if GPT-4 quota is unavailable, deploy GPT-3.5-Turbo:

```powershell
az cognitiveservices account deployment create `
 --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
 --name $openaiName `
 --deployment-name "gpt-35-turbo-chat" `
 --model-name "gpt-35-turbo" `
 --model-version "0613" `
 --model-format "OpenAI" `
 --sku-name "Standard" `
 --sku-capacity 50
```

2. **Wait for deployment to complete** (takes 2-3 minutes):

```powershell
Write-Host "Waiting for model deployment..."
Start-Sleep -Seconds 120
```

3. **Verify deployment**:

```powershell
az cognitiveservices account deployment list `
 --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
 --name $openaiName `
 --query "[].{Name:name, Model:properties.model.name, Status:properties.provisioningState}" `
 --output table
```

Status should be: `Succeeded`

### Part 4: Deploy Embedding Model (Optional but Recommended)

Embeddings enable semantic search and RAG patterns.

1. **Deploy text-embedding-ada-002**:

```powershell
az cognitiveservices account deployment create `
 --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
 --name $openaiName `
 --deployment-name "text-embedding-ada-002" `
 --model-name "text-embedding-ada-002" `
 --model-version "2" `
 --model-format "OpenAI" `
 --sku-name "Standard" `
 --sku-capacity 50
```

2. **Verify both deployments**:

```powershell
az cognitiveservices account deployment list `
 --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
 --name $openaiName `
 --output table
```

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
- Configure filters:
 - **Hate**: Severity High - Block
 - **Sexual**: Severity Medium - Block
 - **Violence**: Severity High - Block
 - **Self-harm**: Severity Medium - Block
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
 --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
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
print(" • Private endpoint connectivity")
print(" • Managed identity authentication (zero API keys)")
print(" • Secrets stored in Key Vault")
print(" • Chat completions working")
print(" • Streaming responses working")
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
- Latency: Check Azure Portal → Metrics
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

## Troubleshooting

### Issue: Model deployment fails with "Insufficient quota"

**Solution**:
- Check quota in Azure Portal: OpenAI resource → Quotas
- Use GPT-3.5-Turbo instead of GPT-4
- Reduce capacity (e.g., 10 instead of 20)
- Request quota increase: Portal → Quotas → Request increase

---

### Issue: "This model is not available in your region"

**Solution**:
- Check model availability by region: [Azure OpenAI Model Availability](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)
- Use an alternative model (e.g., gpt-35-turbo instead of gpt-4)
- Or redeploy OpenAI to a different region

---

### Issue: Chat completion fails with "401 Unauthorized"

**Solution**:
- Verify managed identity has "Cognitive Services OpenAI User" role:
 ```powershell
 az role assignment list --assignee $identityId --scope $openaiId -o table
 ```
- Wait 2-3 minutes for RBAC to propagate
- Ensure you're running the script ON THE VM (managed identity only works there)

---

### Issue: "Deployment not found" error

**Solution**:
- List all deployments to check the exact name:
 ```powershell
 az cognitiveservices account deployment list -n $openaiName -g "challenge-rg-<inject key="DeploymentID"></inject>" -o table
 ```
- Update the deployment name in Key Vault to match exactly

---

### Issue: Private endpoint DNS not resolving

**Solution**:
- Verify private DNS zone exists and is linked:
 ```powershell
 az network private-dns link vnet list -g "challenge-rg-<inject key="DeploymentID"></inject>" --zone-name "privatelink.openai.azure.com" -o table
 ```
- Flush DNS cache:
 ```powershell
 Clear-DnsClientCache
 ```
- Test resolution:
 ```powershell
 nslookup "$openaiName.openai.azure.com"
 ```
 Should return 10.0.x.x (private IP)

## Bonus Challenges

1. **Deploy GPT-4 Vision** (if available):
 ```powershell
 az cognitiveservices account deployment create ... --model-name "gpt-4-vision-preview"
 ```
 Test with image analysis

2. **Implement Token Usage Monitoring**:
 - Create a script that tracks token usage per request
 - Calculate cost estimates based on pricing
 - Set up budget alerts

3. **Test Content Filtering**:
 - Try to submit prompts with harmful content
 - Verify they're blocked by the content filter
 - Review filter logs

4. **Benchmark Different Models**:
 - Deploy both GPT-4 and GPT-3.5-Turbo
 - Compare latency, quality, cost
 - Document trade-offs

## What You Learned

In this challenge, you:

Deployed GPT models for chat completions 
Configured embedding models for semantic search 
Implemented responsible AI content filtering 
Stored configuration securely in Key Vault 
Tested completions via private endpoint with managed identity 
Validated streaming and multi-turn conversations 
Set up monitoring and alerts 
Achieved 100% passwordless, private network AI access 

Your Azure OpenAI service is now production-ready and fully secure!

## Next Steps

Azure OpenAI: Configured and tested!

In **Challenge 5**, you'll download and configure the pre-built secure chat application that uses everything you've set up: private endpoints, managed identity, Key Vault secrets, and your OpenAI models.

Head to **challenge-5.md** to deploy the app!

---

**Performance Tip**: Monitor your token usage in the Azure Portal Metrics. Set up alerts to avoid unexpected costs from runaway requests!
