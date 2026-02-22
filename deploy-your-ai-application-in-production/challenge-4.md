# Challenge 04: Secure Azure OpenAI Deployment

## Introduction

Your OpenAI service is deployed with a private endpoint, but it's not fully configured yet. In this challenge, you will deploy GPT models, configure content filtering, test embeddings, and validate that everything works through the private network with managed identity authentication.

By the end, you will have a fully operational, secure OpenAI service ready for your chat application.

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

### Task 1: Verify OpenAI Resource and Check Available Models

1. **Open VS Code PowerShell terminal** on **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>** and run:

   ```powershell
   $openaiName = az cognitiveservices account list `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query "[?kind=='AIServices'].name" -o tsv

   Write-Host "OpenAI Resource: $openaiName"

   # Get endpoint
   $endpoint = az cognitiveservices account show `
   --name $openaiName `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query properties.endpoint -o tsv

   Write-Host "Endpoint: $endpoint"

   # List existing deployments
   az cognitiveservices account deployment list `
   --name $openaiName `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query "[].{Name:name, Model:properties.model.name, Version:properties.model.version}" `
   --output table
   ```

   - You should see the **secure-chat** deployment from Challenge 1. This is your primary chat model.

### Task 2: Store Model Configuration in Key Vault

Store the deployment name and API version so your app can retrieve them securely.

```powershell
$kvName = az keyvault list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[?contains(name, 'kv')].name" -o tsv

# Temporarily enable Key Vault public access
az keyvault update `
 --name $kvName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --public-network-access Enabled

# Store chat model deployment name (use whichever model you deployed)
az keyvault secret set `
 --vault-name $kvName `
 --name "ChatModelDeployment" `
 --value "secure-chat"

# Store API version
az keyvault secret set `
 --vault-name $kvName `
 --name "OpenAIApiVersion" `
 --value "2024-12-01-preview"

Write-Host "Stored ChatModelDeployment and OpenAIApiVersion in Key Vault"

# Disable public access again
az keyvault update `
 --name $kvName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --public-network-access Disabled

Write-Host "Key Vault secured"
```

   > **Note**: If you deployed a different model, replace `"secure-chat"` with your deployment name.

### Task 3: Test Chat Completions with Managed Identity

Validate that Azure OpenAI works end to end with managed identity authentication.

1. **Install required Python packages** (if not already installed):

   ```powershell
   New-Item -Path "C:\Code" -ItemType Directory -Force
   pip install azure-identity azure-keyvault-secrets openai
   ```

2. **Run the below test script in the terminal**:

   ```powershell
   @'
   """
   Quick test: Azure OpenAI via Private Endpoint with Managed Identity
   """
   from azure.identity import DefaultAzureCredential
   from azure.keyvault.secrets import SecretClient
   from openai import AzureOpenAI

   credential = DefaultAzureCredential()

   # Get config from Key Vault
   kv_name = "$kvName"
   kv_url = f"https://{kv_name}.vault.azure.net"
   secret_client = SecretClient(vault_url=kv_url, credential=credential)

   openai_endpoint = secret_client.get_secret("OpenAIEndpoint").value
   chat_deployment = secret_client.get_secret("ChatModelDeployment").value
   api_version = secret_client.get_secret("OpenAIApiVersion").value

   print(f"Endpoint: {openai_endpoint}")
   print(f"Model: {chat_deployment}")

   # Create OpenAI client with managed identity
   client = AzureOpenAI(
   azure_endpoint=openai_endpoint,
   api_version=api_version,
   azure_ad_token_provider=lambda: credential.get_token(
   "https://cognitiveservices.azure.com/.default"
   ).token
   )

   # Test chat completion
   response = client.chat.completions.create(
   model=chat_deployment,
   messages=[
   {"role": "system", "content": "You are a helpful assistant."},
   {"role": "user", "content": "Explain managed identity in one sentence."}
   ],
   max_tokens=100
   )

   print(f"\nAI Response: {response.choices[0].message.content}")
   print(f"Tokens used: {response.usage.total_tokens}")
   print("\nSUCCESS: Managed identity auth to Azure OpenAI is working!")
   '@ -replace '\$kvName', $kvName | Out-File -FilePath "C:\Code\test_openai_quick.py" -Encoding UTF8

   python "C:\Code\test_openai_quick.py"
   ```

RBAC changes may take 2–3 minutes to propagate. Please wait a few minutes before testing to ensure the permissions have been applied successfully.

## Success Criteria

Validate your OpenAI setup:

- GPT model deployed (either **secure-chat** from Challenge 1 or additional deployment)
- Model deployment name stored in Key Vault as `ChatModelDeployment`
- API version stored in Key Vault as `OpenAIApiVersion`
- Test script successfully calls chat completions using managed identity (no API keys)

Now, click **Next** to continue to **Challenge 05**.
