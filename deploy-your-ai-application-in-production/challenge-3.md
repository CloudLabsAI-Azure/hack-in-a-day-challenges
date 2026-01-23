# Challenge 03: Identity & Access Management with Entra ID

## Introduction

Network isolation alone isn't enough. Even with private endpoints, you need strong identity controls to ensure only authorized users and services can access your AI resources. In this challenge, you'll implement passwordless authentication using managed identities and configure role-based access control (RBAC) following the principle of least privilege.

**No more API keys in code or .env files!** Everything will use Entra ID authentication.

## Prerequisites

- Completed Challenge 2 (Network security configured)
- All services have public access disabled
- Private endpoints deployed and approved
- Connected to VM via Azure Bastion
- VS Code terminal open

## Challenge Objectives

- Understand managed identity vs service principal authentication
- Create a system-assigned managed identity for your VM
- Assign RBAC roles for AI services access
- Configure Key Vault access policies for the managed identity
- Store OpenAI connection details in Key Vault (no hardcoded secrets!)
- Test passwordless authentication to Azure OpenAI
- Validate least-privilege access model

## Understanding Managed Identity

```
┌────────────────────────────────────────────────────────────┐
│  Traditional Authentication (INSECURE)                      │
│                                                             │
│  Application → Hardcoded API Key → Azure OpenAI            │
│                                                             │
│  Problems:                                                  │
│  ❌ API keys stored in code/config files                   │
│  ❌ Keys can be leaked to GitHub/logs                      │
│  ❌ Manual key rotation required                           │
│  ❌ No audit trail of who used the key                     │
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│  Managed Identity Authentication (SECURE)                   │
│                                                             │
│  Application → Entra ID Token → Azure OpenAI               │
│  (VM Identity)   (Automatic)    (RBAC Check)               │
│                                                             │
│  Benefits:                                                  │
│  ✅ Zero secrets in code                                   │
│  ✅ Automatic credential rotation by Azure                 │
│  ✅ Full audit trail in Entra ID logs                      │
│  ✅ Granular RBAC permissions                              │
│  ✅ Works seamlessly with private endpoints                │
└────────────────────────────────────────────────────────────┘
```

## Steps to Complete

### Part 1: Enable System-Assigned Managed Identity on Your VM

Your VM needs an identity to authenticate to Azure services.

1. **Get your VM name**:

```powershell
$vmName = az vm list `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --query "[?contains(name, 'vm') || contains(name, 'labvm')].name" -o tsv

Write-Host "VM Name: $vmName"
```

2. **Enable system-assigned managed identity**:

```powershell
az vm identity assign `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --name $vmName
```

Output will show the `principalId` - this is your managed identity's object ID. Save it:

```powershell
$identityId = az vm identity show `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --name $vmName `
  --query principalId -o tsv

Write-Host "Managed Identity ID: $identityId"
```

3. **Verify in Azure Portal**:
   - Go to your VM resource
   - Click **Identity** in the left menu
   - Under **System assigned**, Status should be **On**
   - Note the **Object (principal) ID** - same as `$identityId`

### Part 2: Assign RBAC Roles for Azure OpenAI Access

Grant your VM's managed identity permission to use Azure OpenAI.

1. **Get your OpenAI resource ID**:

```powershell
$openaiName = az cognitiveservices account list `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --query "[?kind=='OpenAI'].name" -o tsv

$openaiId = az cognitiveservices account show `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --name $openaiName `
  --query id -o tsv

Write-Host "OpenAI Resource ID: $openaiId"
```

2. **Assign "Cognitive Services OpenAI User" role**:

This role allows reading models and making inference calls (but not managing the resource).

```powershell
az role assignment create `
  --assignee $identityId `
  --role "Cognitive Services OpenAI User" `
  --scope $openaiId
```

3. **Verify the role assignment**:

```powershell
az role assignment list `
  --assignee $identityId `
  --scope $openaiId `
  --output table
```

You should see the role assignment listed.

### Part 3: Configure Key Vault Access for Managed Identity

Key Vault will store connection strings and configuration. Grant access to your managed identity.

1. **Get Key Vault name**:

```powershell
$kvName = az keyvault list `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --query "[?contains(name, 'kv')].name" -o tsv

Write-Host "Key Vault: $kvName"
```

2. **Assign "Key Vault Secrets User" role** (modern RBAC approach):

```powershell
$kvId = az keyvault show `
  --name $kvName `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --query id -o tsv

az role assignment create `
  --assignee $identityId `
  --role "Key Vault Secrets User" `
  --scope $kvId
```

3. **Also add yourself as Key Vault Secrets Officer** (so you can create secrets):

```powershell
$currentUserId = az ad signed-in-user show --query id -o tsv

az role assignment create `
  --assignee $currentUserId `
  --role "Key Vault Secrets Officer" `
  --scope $kvId
```

4. **Wait 2-3 minutes** for RBAC propagation (Azure AD replication takes time)

```powershell
Write-Host "Waiting for RBAC to propagate..."
Start-Sleep -Seconds 120
Write-Host "RBAC should be ready now!"
```

### Part 4: Store OpenAI Configuration in Key Vault

Instead of storing endpoints and keys in files, store them securely in Key Vault.

1. **Get OpenAI endpoint**:

```powershell
$openaiEndpoint = az cognitiveservices account show `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --name $openaiName `
  --query properties.endpoint -o tsv

Write-Host "OpenAI Endpoint: $openaiEndpoint"
```

2. **Store the endpoint in Key Vault as a secret**:

```powershell
az keyvault secret set `
  --vault-name $kvName `
  --name "OpenAIEndpoint" `
  --value $openaiEndpoint
```

3. **Store the resource name** (needed for some SDK operations):

```powershell
az keyvault secret set `
  --vault-name $kvName `
  --name "OpenAIResourceName" `
  --value $openaiName
```

4. **Store the AI Foundry project endpoint** (for future challenges):

Get it from your deployment info:

```powershell
$projectEndpoint = Get-Content "C:\LabFiles\deployment-info.txt" | Select-String "AI_PROJECT_ENDPOINT" | ForEach-Object { $_ -replace '.*=\s*"?([^"]+)"?', '$1' }

if ($projectEndpoint) {
    az keyvault secret set `
      --vault-name $kvName `
      --name "AIProjectEndpoint" `
      --value $projectEndpoint
}
```

5. **List all secrets** to verify:

```powershell
az keyvault secret list --vault-name $kvName --query "[].name" -o table
```

You should see: `OpenAIEndpoint`, `OpenAIResourceName`, `AIProjectEndpoint`

### Part 5: Test Managed Identity Authentication

Let's prove passwordless auth works!

1. **Install Azure Identity library** (for managed identity auth):

```powershell
pip install azure-identity azure-ai-openai
```

2. **Create a test script** to authenticate using managed identity:

```powershell
@'
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

# Initialize managed identity credential
credential = DefaultAzureCredential()

# Get Key Vault name from environment
kv_name = "$kvName"
kv_url = f"https://{kv_name}.vault.azure.net"

print(f"Connecting to Key Vault: {kv_url}")
print("Using Managed Identity (no passwords!)")

try:
    # Connect to Key Vault using managed identity
    secret_client = SecretClient(vault_url=kv_url, credential=credential)
    
    # Retrieve OpenAI endpoint from Key Vault
    endpoint_secret = secret_client.get_secret("OpenAIEndpoint")
    openai_endpoint = endpoint_secret.value
    
    print(f"\n✅ Successfully retrieved secret from Key Vault!")
    print(f"OpenAI Endpoint: {openai_endpoint}")
    print("\n🎉 Managed Identity authentication is working!")
    
except Exception as e:
    print(f"\n❌ Error: {str(e)}")
    print("Make sure RBAC roles have propagated (wait 2-3 minutes)")
    
'@ -replace '\$kvName', $kvName | Out-File -FilePath "C:\LabFiles\test_managed_identity.py" -Encoding UTF8

python "C:\LabFiles\test_managed_identity.py"
```

**Expected Output:**
```
Connecting to Key Vault: https://kv-xxxxx.vault.azure.net
Using Managed Identity (no passwords!)

✅ Successfully retrieved secret from Key Vault!
OpenAI Endpoint: https://aoai-xxxxx.openai.azure.com/
🎉 Managed Identity authentication is working!
```

If you get an error, wait 2-3 minutes for RBAC to propagate, then retry.

### Part 6: Test Azure OpenAI Access with Managed Identity

Now test that you can call OpenAI using managed identity (no API keys!).

1. **First, deploy a GPT model** (you'll configure this fully in Challenge 4):

```powershell
az cognitiveservices account deployment create `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --name $openaiName `
  --deployment-name "gpt-4" `
  --model-name "gpt-4" `
  --model-version "0613" `
  --model-format "OpenAI" `
  --sku-name "Standard" `
  --sku-capacity 10
```

**Note**: If GPT-4 quota is unavailable, use GPT-3.5-Turbo:

```powershell
az cognitiveservices account deployment create `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --name $openaiName `
  --deployment-name "gpt-35-turbo" `
  --model-name "gpt-35-turbo" `
  --model-version "0613" `
  --model-format "OpenAI" `
  --sku-name "Standard" `
  --sku-capacity 10
```

2. **Create test script for OpenAI with managed identity**:

```powershell
@'
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from openai import AzureOpenAI

# Get credentials using managed identity
credential = DefaultAzureCredential()

# Get Key Vault name
kv_name = "$kvName"
kv_url = f"https://{kv_name}.vault.azure.net"

print("🔐 Authenticating with Managed Identity...")

# Get OpenAI endpoint from Key Vault
secret_client = SecretClient(vault_url=kv_url, credential=credential)
openai_endpoint = secret_client.get_secret("OpenAIEndpoint").value

print(f"📡 OpenAI Endpoint: {openai_endpoint}")

# Create OpenAI client using managed identity
client = AzureOpenAI(
    azure_endpoint=openai_endpoint,
    api_version="2024-02-15-preview",
    azure_ad_token_provider=lambda: credential.get_token("https://cognitiveservices.azure.com/.default").token
)

print("\n💬 Testing AI chat (with managed identity, no API keys!)...\n")

# Test completion
response = client.chat.completions.create(
    model="gpt-4",  # or "gpt-35-turbo" if you deployed that
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain managed identity in one sentence."}
    ],
    max_tokens=100
)

print(f"AI Response: {response.choices[0].message.content}\n")
print("✅ SUCCESS! Passwordless authentication to Azure OpenAI is working!")
print("🔒 Zero API keys were used - only managed identity!")

'@ -replace '\$kvName', $kvName | Out-File -FilePath "C:\LabFiles\test_openai_auth.py" -Encoding UTF8

python "C:\LabFiles\test_openai_auth.py"
```

**Expected Output:**
```
🔐 Authenticating with Managed Identity...
📡 OpenAI Endpoint: https://aoai-xxxxx.openai.azure.com/

💬 Testing AI chat (with managed identity, no API keys!)...

AI Response: Managed identity is an Azure feature that provides applications with an automatically managed identity in Entra ID for authenticating to Azure services without storing credentials.

✅ SUCCESS! Passwordless authentication to Azure OpenAI is working!
🔒 Zero API keys were used - only managed identity!
```

### Part 7: Configure RBAC for Storage Account

Your chat app will need to access storage for session history.

1. **Get storage account resource ID**:

```powershell
$storageName = az storage account list `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --query "[?contains(name, 'st')].name" -o tsv

$storageId = az storage account show `
  --name $storageName `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --query id -o tsv
```

2. **Assign Storage Blob Data Contributor role**:

```powershell
az role assignment create `
  --assignee $identityId `
  --role "Storage Blob Data Contributor" `
  --scope $storageId
```

### Part 8: Document Your Identity Configuration

Create a reference document for your RBAC setup.

```powershell
@"
=== Entra ID & RBAC Configuration ===
Date: $(Get-Date)

Managed Identity:
- Principal ID: $identityId
- Type: System-assigned
- Attached to: $vmName

RBAC Role Assignments:
1. Cognitive Services OpenAI User → $openaiName
   - Scope: OpenAI resource
   - Permissions: Read models, make inference calls

2. Key Vault Secrets User → $kvName
   - Scope: Key Vault resource
   - Permissions: Read secrets (no write/delete)

3. Storage Blob Data Contributor → $storageName
   - Scope: Storage Account
   - Permissions: Read/write blobs

Key Vault Secrets:
- OpenAIEndpoint: $openaiEndpoint
- OpenAIResourceName: $openaiName
- AIProjectEndpoint: [stored in Key Vault]

Authentication Flow:
1. Application requests Entra ID token using managed identity
2. Azure automatically provides token (no password needed)
3. Token presented to Azure OpenAI/Key Vault/Storage
4. Service validates token against RBAC roles
5. Access granted if role permits the operation

Security Benefits:
✅ Zero secrets in code or config files
✅ Automatic credential rotation by Azure
✅ Full audit trail in Entra ID logs
✅ Granular, least-privilege access control
✅ Works seamlessly with private endpoints
"@ | Out-File -FilePath "C:\LabFiles\identity-config.txt"

notepad C:\LabFiles\identity-config.txt
```

## Success Criteria

Verify your identity setup is complete:

- [ ] VM has system-assigned managed identity enabled
- [ ] Managed identity has "Cognitive Services OpenAI User" role on OpenAI resource
- [ ] Managed identity has "Key Vault Secrets User" role on Key Vault
- [ ] Managed identity has "Storage Blob Data Contributor" role on Storage Account
- [ ] Your user account has "Key Vault Secrets Officer" role (to create secrets)
- [ ] OpenAI endpoint stored in Key Vault as secret
- [ ] Test script successfully retrieves secrets from Key Vault using managed identity
- [ ] Test script successfully calls Azure OpenAI using managed identity (no API key)
- [ ] GPT-4 (or GPT-3.5-turbo) model deployed
- [ ] Identity configuration documented in `identity-config.txt`

## Troubleshooting

### Issue: "Access denied" when accessing Key Vault

**Solution**:
- RBAC can take 2-5 minutes to propagate
- Wait a few minutes and retry
- Verify role assignment:
  ```powershell
  az role assignment list --assignee $identityId --scope $kvId -o table
  ```
- Check if Key Vault uses access policies instead of RBAC:
  - Portal → Key Vault → Access configuration
  - Should be "Azure role-based access control"

---

### Issue: Managed identity authentication fails with "credential not found"

**Solution**:
- Ensure you're running the script ON THE VM (not your local machine)
- Managed identity only works from within the VM
- Verify identity is enabled:
  ```powershell
  az vm identity show -g "challenge-rg-<inject key="DeploymentID"></inject>" -n $vmName
  ```

---

### Issue: OpenAI deployment fails with "Insufficient quota"

**Solution**:
- Your region may not have GPT-4 quota available
- Use GPT-3.5-Turbo instead:
  ```powershell
  az cognitiveservices account deployment create ... --model-name "gpt-35-turbo" --deployment-name "gpt-35-turbo"
  ```
- Or request quota increase in Azure Portal

---

### Issue: Python script errors with "No module named 'azure'"

**Solution**:
- Install required packages:
  ```powershell
  pip install azure-identity azure-keyvault-secrets azure-ai-openai openai
  ```

---

### Issue: "The client does not have permission to perform action"

**Solution**:
- Wait 5 minutes for RBAC to fully propagate
- Verify the role assignment exists and is at the correct scope
- Ensure you're using the system-assigned identity, not user-assigned
- Check Azure AD service health (rare outages can delay RBAC)

## Bonus Challenges

1. **Implement User-Assigned Managed Identity**:
   - Create a separate user-assigned managed identity
   - Attach it to the VM alongside system-assigned
   - Assign different roles to each identity
   - Test which identity is used by default

2. **Configure Conditional Access**:
   - Create a conditional access policy in Entra ID
   - Require MFA for accessing AI services
   - Apply policy to the managed identity

3. **Enable Diagnostic Logging**:
   - Turn on diagnostic logs for Key Vault
   - Monitor who accesses which secrets
   - Set up alerts for unauthorized access attempts

4. **Test Least Privilege**:
   - Try to delete a secret (should fail - you only have "Secrets User")
   - Try to create a new OpenAI deployment (should fail - not an admin)
   - Verify you can only perform allowed operations

## What You Learned

In this challenge, you:

✅ Enabled managed identity on a VM for passwordless authentication  
✅ Configured RBAC roles following least-privilege principle  
✅ Granted access to Azure OpenAI without API keys  
✅ Stored configuration securely in Key Vault  
✅ Retrieved secrets programmatically using managed identity  
✅ Successfully called Azure OpenAI with zero hardcoded credentials  
✅ Implemented enterprise-grade identity security  

Your application can now authenticate to Azure services without ever storing a password or API key!

## Next Steps

Identity & access: ✅ Secured!

In **Challenge 4**, you'll complete the Azure OpenAI configuration by deploying models, testing embeddings, and preparing the OpenAI service for the chat application.

Head to **challenge-4.md** to continue! 🤖

---

**Security Best Practice**: Never use API keys when managed identities are available. Managed identities eliminate the #1 cause of security breaches: leaked credentials.
