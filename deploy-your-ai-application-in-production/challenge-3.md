# Challenge 03: Identity & Access Management with Entra ID

## Introduction

Network isolation alone isn't enough. Even with private endpoints, you need strong identity controls to ensure only authorized users and services can access your AI resources. In this challenge, you will implement passwordless authentication using managed identities and configure role-based access control (RBAC) following the principle of least privilege.

**No more API keys in code or .env files!** Everything will use Entra ID authentication.

## Prerequisites

- Completed Challenge 2 (Network security configured)
- All services have public access disabled
- Private endpoints deployed and approved
- Connected to **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>** via Azure Bastion
- VS Code open with PowerShell terminal
- Azure CLI logged in (`az login` completed)

## Challenge Objectives

- Understand managed identity vs service principal authentication
- Enable a system-assigned managed identity on your VM
- Assign RBAC roles for Azure OpenAI, Key Vault, and Storage Account access
- Store OpenAI connection details securely in Key Vault (no hardcoded secrets!)
- Configure Storage Account access for managed identity
- Validate least-privilege access model

In the **VS Code PowerShell terminal**, run the provided commands to complete the configuration tasks.

### Task 1: Enable System-Assigned Managed Identity on Your VM

Your VM needs an identity to authenticate to Azure services without passwords or API keys.

1. **Open VS Code PowerShell terminal** on **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>** and run:

   ```powershell
   $vmName = "Hack-vm-<inject key="DeploymentID" enableCopy="false"/>"

   # Enable system-assigned managed identity
   az vm identity assign `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --name $vmName

   # Get the identity principal ID
   $identityId = az vm identity show `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --name $vmName `
   --query principalId -o tsv

   Write-Host "Managed Identity ID: $identityId"
   ```

      > **Note**: Copy the `$identityId` value you will need it for RBAC assignments next.

### Task 2: Assign RBAC Roles for Azure OpenAI and Key Vault

Grant your VM's managed identity the necessary permissions via CLI.

1. **Get resource IDs and assign all RBAC roles**:

   ```powershell
   # Get OpenAI resource ID
   $openaiName = az cognitiveservices account list `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query "[?kind=='AIServices'].name" -o tsv

   $openaiId = az cognitiveservices account show `
   --name $openaiName `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query id -o tsv

   # Assign Cognitive Services OpenAI User to VM managed identity
   az role assignment create `
   --assignee $identityId `
   --role "Cognitive Services OpenAI User" `
   --scope $openaiId

   Write-Host "Assigned: Cognitive Services OpenAI User on $openaiName"
   ```

2. **Assign Key Vault roles**:

   ```powershell
   # Get Key Vault resource ID
   $kvName = az keyvault list `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query "[?contains(name, 'kv')].name" -o tsv

   $kvId = az keyvault show `
   --name $kvName `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query id -o tsv

   # Assign Key Vault Secrets User to VM managed identity
   az role assignment create `
   --assignee $identityId `
   --role "Key Vault Secrets User" `
   --scope $kvId

   Write-Host "Assigned: Key Vault Secrets User on $kvName"

   # Assign Key Vault Secrets Officer to yourself (to create secrets)
   $userEmail = "<inject key="AzureAdUserEmail"></inject>"

   az role assignment create `
   --assignee $userEmail `
   --role "Key Vault Secrets Officer" `
   --scope $kvId

   Write-Host "Assigned: Key Vault Secrets Officer to $userEmail"
   ```

   > **Important**: RBAC changes may take 2–3 minutes to propagate. Please wait a few minutes before testing to ensure the permissions have been applied successfully.

### Task 3: Store OpenAI Configuration in Key Vault (Using VS Code)

Instead of storing endpoints and keys in files, store them securely in Key Vault. Since Key Vault has public access disabled, you will temporarily enable it to add secrets from your VM.

1. **Get resource names and enable Key Vault public access temporarily**:

   ```powershell
   # Get resource names
   $kvName = az keyvault list `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query "[?contains(name, 'kv')].name" -o tsv

   $openaiName = az cognitiveservices account list `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query "[?kind=='AIServices'].name" -o tsv

   Write-Host "Key Vault: $kvName"
   Write-Host "OpenAI Resource: $openaiName"

   # Get OpenAI endpoint
   $openaiEndpoint = az cognitiveservices account show `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --name $openaiName `
   --query properties.endpoint -o tsv

   Write-Host "OpenAI Endpoint: $openaiEndpoint"

   # Verify the endpoint format (should contain your resource name)
   if ($openaiEndpoint -notlike "*$openaiName*") {
      Write-Warning "WARNING: Endpoint should contain your resource name!"
      Write-Warning "Expected format: https://<resource-name>.cognitiveservices.azure.com/"
      Write-Warning "If you see a generic endpoint, go back to Challenge 1 Task 5 and configure custom domain."
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

   # Store chat model deployment name
   az keyvault secret set `
   --vault-name $kvName `
   --name "ChatModelDeployment" `
   --value "secure-chat"

   Write-Host "Stored ChatModelDeployment"

   # Store API version
   az keyvault secret set `
   --vault-name $kvName `
   --name "OpenAIApiVersion" `
   --value "2024-12-01-preview"

   Write-Host "Stored OpenAIApiVersion"

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

### Task 4: Configure Storage Account Access for Managed Identity

Grant your VM's managed identity permission to read/write blobs.

1. **Assign Storage Blob Data Contributor role via CLI**:

   ```powershell
   # Get storage account resource ID
   $storageName = az storage account list `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query "[?contains(name, 'st')].name" -o tsv

   $storageId = az storage account show `
   --name $storageName `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query id -o tsv

   az role assignment create `
   --assignee $identityId `
   --role "Storage Blob Data Contributor" `
   --scope $storageId

   Write-Host "Assigned: Storage Blob Data Contributor on $storageName"
   ```

2. **Store Storage Account name in Key Vault**:

   ```powershell
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

### Task 5: Verify RBAC Assignments

Confirm all role assignments are in place:

```powershell
az role assignment list --assignee $identityId --all --output table
```

You should see:
- **Cognitive Services OpenAI User** on openai-secureai-xxx
- **Key Vault Secrets User** on kv-secureai-xxx
- **Storage Blob Data Contributor** on stsecureaixxx

## Success Criteria

Verify your identity setup is complete:

- VM has system-assigned managed identity enabled
- Managed identity has "Cognitive Services OpenAI User" role on OpenAI resource
- Managed identity has the "Key Vault Secrets User" role on the Key Vault
- Managed identity has the "Storage Blob Data Contributor" role on the Storage Account
- Your user account has the "Key Vault Secrets Officer" role (to create secrets)
- OpenAI endpoint and deployment name stored in Key Vault as secrets
- Storage Account name stored in Key Vault

Now, click **Next** to continue to **Challenge 04**.
