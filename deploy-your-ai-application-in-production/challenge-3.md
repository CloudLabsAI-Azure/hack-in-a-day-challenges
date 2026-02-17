# Challenge 03: Identity & Access Management with Entra ID

## Introduction

Network isolation alone isn't enough. Even with private endpoints, you need strong identity controls to ensure only authorized users and services can access your AI resources. In this challenge, you'll implement passwordless authentication using managed identities and configure role-based access control (RBAC) following the principle of least privilege.

**No more API keys in code or .env files!** Everything will use Entra ID authentication.

## Prerequisites

- Completed Challenge 2 (Network security configured)
- All services have public access disabled
- Private endpoints deployed and approved
- Connected to **vm-<inject key="DeploymentID" enableCopy="false"/>** via Azure Bastion
- VS Code open with PowerShell terminal
- Azure CLI logged in (`az login` completed)

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
+------------------------------------------------------------+
� Traditional Authentication (INSECURE) �
� �
� Application ? Hardcoded API Key ? Azure OpenAI �
� �
� Problems: �
� API keys stored in code/config files �
� Keys can be leaked to GitHub/logs �
� Manual key rotation required �
� No audit trail of who used the key �
+------------------------------------------------------------+

+------------------------------------------------------------+
� Managed Identity Authentication (SECURE) �
� �
� Application ? Entra ID Token ? Azure OpenAI �
� (VM Identity) (Automatic) (RBAC Check) �
� �
� Benefits: �
� Zero secrets in code �
� Automatic credential rotation by Azure �
� Full audit trail in Entra ID logs �
� Granular RBAC permissions �
� Works seamlessly with private endpoints �
+------------------------------------------------------------+
```

## Steps to Complete

### Part 1: Enable System-Assigned Managed Identity on Your VM

Your VM needs an identity to authenticate to Azure services. We'll configure this using the Azure Portal.

1. **In Azure Portal**, navigate to **Resource groups** and select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**.

1. Find and click on your Virtual Machine resource: **vm-<inject key="DeploymentID" enableCopy="false"/>**.

1. In the left menu, under **Security**, click **Identity**.

1. Under the **System assigned** tab:
   - Set **Status** to **On**
   - Click **Save**
   - Click **Yes** to confirm

1. Wait for the operation to complete (30 seconds).

1. Once enabled, you'll see an **Object (principal) ID** displayed - this is your managed identity's unique identifier. **Copy this ID** to Notepad for later use.

1. **Verify the identity in VS Code** (optional):

 Open VS Code PowerShell terminal and run:

```powershell
$vmName = "vm-<inject key="DeploymentID" enableCopy="false"/>"

$identityId = az vm identity show `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --name $vmName `
 --query principalId -o tsv

Write-Host "Managed Identity ID: $identityId"
```

### Part 2: Assign RBAC Roles for Azure OpenAI Access

Grant your VM's managed identity permission to use Azure OpenAI using the Azure Portal.

1. **In Azure Portal**, navigate to your **openai-secureai-<inject key="DeploymentID" enableCopy="false"/>** resource.

1. In the left menu, click **Access control (IAM)**.

1. Click **+ Add** ? **Add role assignment**.

1. On the **Role** tab:
   - Search for **Cognitive Services OpenAI User**
   - Select **Cognitive Services OpenAI User**
   - Click **Next**

   > **Note**: This role allows reading models and making inference calls (but not managing the resource).

1. On the **Members** tab:
   - **Assign access to**: Select **Managed identity**
   - Click **+ Select members**
   - **Managed identity**: Select **Virtual machine**
   - Select your VM from the list
   - Click **Select**

1. Click **Review + assign**.

1. Click **Review + assign** again to confirm.

   > **Note**: RBAC can take 2-3 minutes to propagate. Wait before testing.

### Part 3: Configure Key Vault Access for Managed Identity

Key Vault will store connection strings and configuration. Grant access to your managed identity using the Azure Portal.

1. **In Azure Portal**, navigate to your **kv-secureai-<inject key="DeploymentID" enableCopy="false"/>** Key Vault.

1. In the left menu, click **Access control (IAM)**.

1. **Assign Key Vault Secrets User role to your VM's managed identity**:

   - Click **+ Add** ? **Add role assignment**
   - On the **Role** tab, search for **Key Vault Secrets User**, select it and click **Next**
   - On the **Members** tab, select **Managed identity** for **Assign access to**
   - Click **+ Select members**, select **Virtual machine**, select your VM from the list, and click **Select**
   - Click **Review + assign** twice

1. **Assign Key Vault Secrets Officer role to yourself** (so you can create secrets):

   - Click **+ Add** ? **Add role assignment** again
   - On the **Role** tab, search for **Key Vault Secrets Officer**, select it and click **Next**
   - On the **Members** tab, select **User, group, or service principal** for **Assign access to**
   - Click **+ Select members**, search for your email: **<inject key="AzureAdUserEmail"></inject>**, select yourself and click **Select**
   - Click **Review + assign** twice

1. **Wait 2-3 minutes** for RBAC propagation.

   > **Important**: Azure AD RBAC takes time to propagate. Wait before proceeding to the next step.

### Part 4: Store OpenAI Configuration in Key Vault (Using VS Code)

Instead of storing endpoints and keys in files, store them securely in Key Vault. Since Key Vault has public access disabled, we'll temporarily enable it to add secrets from your VM.

> **Note**: Open VS Code on your JumpVM and use the PowerShell terminal. Ensure you're logged in to Azure CLI (`az login`).

1. **Get resource names and enable Key Vault public access temporarily**:

```powershell
# Get resource names
$kvName = az keyvault list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[?contains(name, 'kv')].name" -o tsv

$openaiName = az cognitiveservices account list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[?kind=='OpenAI'].name" -o tsv

Write-Host "Key Vault: $kvName"
Write-Host "OpenAI Resource: $openaiName"

# Get OpenAI endpoint
$openaiEndpoint = az cognitiveservices account show `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --name $openaiName `
 --query properties.endpoint -o tsv

Write-Host "OpenAI Endpoint: $openaiEndpoint"

# Verify the endpoint format (should be custom domain)
if ($openaiEndpoint -notlike "*$openaiName*") {
    Write-Warning "WARNING: Endpoint should contain custom domain!"
    Write-Warning "Expected format: https://<resource-name>.openai.azure.com/"
    Write-Warning "If you see a generic endpoint, go back to Challenge 1 Part 5 and configure custom domain."
    Write-Warning "Current endpoint: $openaiEndpoint"
}

# Temporarily enable Key Vault public access
az keyvault update `
 --name $kvName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --public-network-access Enabled

Write-Host "Key Vault public access enabled temporarily"
```

2. **Store the OpenAI configuration secrets**:

```powershell
# Store OpenAI endpoint
az keyvault secret set `
 --vault-name $kvName `
 --name "OpenAIEndpoint" `
 --value $openaiEndpoint

Write-Host "Stored OpenAI Endpoint"

# Store deployment name
az keyvault secret set `
 --vault-name $kvName `
 --name "OpenAIDeployment" `
 --value "secure-chat"

Write-Host "Stored OpenAI Deployment name"

# Store resource name
az keyvault secret set `
 --vault-name $kvName `
 --name "OpenAIResourceName" `
 --value $openaiName

Write-Host "Stored OpenAI Resource name"
```

3. **Disable public access again** (restore security):

```powershell
az keyvault update `
 --name $kvName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --public-network-access Disabled

Write-Host "Key Vault secured - public access disabled"
```

### Part 5: Configure Storage Account Access for Managed Identity

Grant your VM's managed identity permission to read/write blobs using Azure Portal.

1. **In Azure Portal**, navigate to your **stsecureai<inject key="DeploymentID" enableCopy="false"/>** Storage Account.

1. In the left menu, click **Access control (IAM)**.

1. Click **+ Add** ? **Add role assignment**.

1. On the **Role** tab:
   - Search for **Storage Blob Data Contributor**
   - Select it and click **Next**

1. On the **Members** tab:
   - **Assign access to**: Select **Managed identity**
   - Click **+ Select members**
   - **Managed identity**: Select **Virtual machine**
   - Select your VM from the list
   - Click **Select**

1. Click **Review + assign** twice.

1. **Store Storage Account name in Key Vault** (using VS Code PowerShell terminal):

```powershell
# Get storage name
$storageName = az storage account list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[?contains(name, 'st')].name" -o tsv

Write-Host "Storage Account: $storageName"

# Get Key Vault name
$kvName = az keyvault list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[?contains(name, 'kv')].name" -o tsv

# Enable public access temporarily
az keyvault update `
 --name $kvName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --public-network-access Enabled

# Store the secret
az keyvault secret set `
 --vault-name $kvName `
 --name "StorageAccountName" `
 --value $storageName

Write-Host "Stored Storage Account name"

# Disable public access again
az keyvault update `
 --name $kvName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --public-network-access Disabled

Write-Host "Key Vault secured"
```

1. **Verify all secrets are stored** (optional):

```powershell
# Enable public access temporarily to list secrets
az keyvault update `
 --name $kvName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --public-network-access Enabled

# List all secrets
az keyvault secret list --vault-name $kvName --query "[].name" -o table

# Disable public access again
az keyvault update `
 --name $kvName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --public-network-access Disabled
```

Expected secrets:
- OpenAIEndpoint
- OpenAIDeployment
- OpenAIResourceName
- StorageAccountName
 --name $kvName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --public-network-access Disabled
```

You should see:
- `OpenAIEndpoint`
- `OpenAIDeployment`
- `OpenAIResourceName`
- `StorageAccountName`

### Part 6: Summary of RBAC Assignments

Verify all role assignments are in place:

1. **List all role assignments for your VM's managed identity**:

```powershell
az role assignment list --assignee $identityId --output table
```

You should see:
- **Cognitive Services OpenAI User** on openai-secureai-xxx
- **Key Vault Secrets User** on kv-secureai-xxx
- **Storage Blob Data Contributor** on stsecureaixxx

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
 
 print(f"\nSuccessfully retrieved secret from Key Vault!")
 print(f"OpenAI Endpoint: {openai_endpoint}")
 print("\nManaged Identity authentication is working!")
 
except Exception as e:
 print(f"\nError: {str(e)}")
 print("Make sure RBAC roles have propagated (wait 2-3 minutes)")
 
'@ -replace '\$kvName', $kvName | Out-File -FilePath "C:\LabFiles\test_managed_identity.py" -Encoding UTF8

python "C:\LabFiles\test_managed_identity.py"
```

**Expected Output:**
```
Connecting to Key Vault: https://kv-xxxxx.vault.azure.net
Using Managed Identity (no passwords!)

Successfully retrieved secret from Key Vault!
OpenAI Endpoint: https://aoai-xxxxx.openai.azure.com/
Managed Identity authentication is working!
```

If you get an error, wait 2-3 minutes for RBAC to propagate, then retry.

### Part 6: Test Azure OpenAI Access with Managed Identity

Now test that you can call OpenAI using managed identity (no API keys!).

1. **First, deploy a GPT model** (you'll configure this fully in Challenge 4):

```powershell
az cognitiveservices account deployment create `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
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
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
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

print("Authenticating with Managed Identity...")

# Get OpenAI endpoint from Key Vault
secret_client = SecretClient(vault_url=kv_url, credential=credential)
openai_endpoint = secret_client.get_secret("OpenAIEndpoint").value

print(f"OpenAI Endpoint: {openai_endpoint}")

# Create OpenAI client using managed identity
client = AzureOpenAI(
 azure_endpoint=openai_endpoint,
 api_version="2024-02-15-preview",
 azure_ad_token_provider=lambda: credential.get_token("https://cognitiveservices.azure.com/.default").token
)

print("\nTesting AI chat (with managed identity, no API keys!)...\n")

# Test completion
response = client.chat.completions.create(
 model="gpt-4", # or "gpt-35-turbo" if you deployed that
 messages=[
 {"role": "system", "content": "You are a helpful assistant."},
 {"role": "user", "content": "Explain managed identity in one sentence."}
 ],
 max_tokens=100
)

print(f"AI Response: {response.choices[0].message.content}\n")
print("SUCCESS! Passwordless authentication to Azure OpenAI is working!")
print("Zero API keys were used - only managed identity!")

'@ -replace '\$kvName', $kvName | Out-File -FilePath "C:\LabFiles\test_openai_auth.py" -Encoding UTF8

python "C:\LabFiles\test_openai_auth.py"
```

**Expected Output:**
```
Authenticating with Managed Identity...
OpenAI Endpoint: https://aoai-xxxxx.openai.azure.com/

Testing AI chat (with managed identity, no API keys!)...

AI Response: Managed identity is an Azure feature that provides applications with an automatically managed identity in Entra ID for authenticating to Azure services without storing credentials.

SUCCESS! Passwordless authentication to Azure OpenAI is working!
Zero API keys were used - only managed identity!
```

### Part 7: Configure RBAC for Storage Account

Your chat app will need to access storage for session history.

1. **Get storage account resource ID**:

```powershell
$storageName = az storage account list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[?contains(name, 'st')].name" -o tsv

$storageId = az storage account show `
 --name $storageName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
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
1. Cognitive Services OpenAI User ? $openaiName
 - Scope: OpenAI resource
 - Permissions: Read models, make inference calls

2. Key Vault Secrets User ? $kvName
 - Scope: Key Vault resource
 - Permissions: Read secrets (no write/delete)

3. Storage Blob Data Contributor ? $storageName
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
Zero secrets in code or config files
Automatic credential rotation by Azure
Full audit trail in Entra ID logs
Granular, least-privilege access control
Works seamlessly with private endpoints
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
- Check if Key Vault uses access policies instead of RBAC: Go to Portal ? Key Vault ? Access configuration and verify it is set to "Azure role-based access control"

---

### Issue: Managed identity authentication fails with "credential not found"

**Solution**:
- Ensure you're running the script ON THE VM (not your local machine)
- Managed identity only works from within the VM
- Verify identity is enabled:
 ```powershell
 az vm identity show -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" -n $vmName
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

Enabled managed identity on a VM for passwordless authentication 
Configured RBAC roles following least-privilege principle 
Granted access to Azure OpenAI without API keys 
Stored configuration securely in Key Vault 
Retrieved secrets programmatically using managed identity 
Successfully called Azure OpenAI with zero hardcoded credentials 
Implemented enterprise-grade identity security 

Your application can now authenticate to Azure services without ever storing a password or API key!

## Next Steps

Identity & access: Secured!

In **Challenge 4**, you'll complete the Azure OpenAI configuration by deploying models, testing embeddings, and preparing the OpenAI service for the chat application.

Head to **challenge-4.md** to continue!

---

**Security Best Practice**: Never use API keys when managed identities are available. Managed identities eliminate the #1 cause of security breaches: leaked credentials.
