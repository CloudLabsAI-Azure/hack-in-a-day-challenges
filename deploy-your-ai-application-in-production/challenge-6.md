# Challenge 06: Test Secure Connectivity via Azure Bastion

## Introduction

Your secure AI application is running! Now let's validate the **secure connectivity** layer. 

In this challenge, you'll test accessing your VM and application using Azure Bastion - a fully managed PaaS service that provides secure RDP/SSH without exposing public IPs.

This proves your entire architecture works through private networking only!

## Prerequisites

- Completed Challenge 5 (Chat application deployed and tested on **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>**)
- Azure Bastion deployed (from pre-configured environment)
- Chat application running on **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>**
- All services using private endpoints
- VS Code open with PowerShell terminal on **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>**
- Azure CLI logged in

## Challenge Objectives

- Connect to VM using Azure Bastion (no public IP!)
- Test chat application through Bastion
- Validate private endpoint DNS resolution
- Test network isolation (verify public access is blocked)
- Monitor connectivity through Network Watcher
- Document secure access patterns

## Steps to Complete

### Part 1: Verify Bastion and Connect to VM

You should already be connected to your VM via Bastion from previous challenges. If not:

1. **In Azure Portal**, navigate to **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>**.
1. Click **Connect** → **Bastion**.
1. Enter credentials:
   - **Username**: `azureuser`
   - **Password**: <inject key="VMAdminPassword"></inject>
1. Click **Connect** (opens a new browser tab with remote desktop session).

2. **Verify you're on the VM** (in PowerShell terminal):

```powershell
hostname
ipconfig | Select-String "IPv4"
# Should show private IP (10.0.3.x) - no public IP!
```

### Part 2: Run and Test Chat Application Through Bastion

1. **Start the chat app** (if not already running):

```powershell
cd C:\Code\hack-in-a-day-challenges-deploy-your-ai-application\codefiles
.\venv\Scripts\Activate.ps1
streamlit run app.py
```

2. **Open browser** to `http://localhost:8501` if it doesn't open automatically.

3. **Verify the app works**:
   - Sidebar shows **Authenticated** and **Managed Identity**
   - Send a test message: `What is Azure Bastion?`
   - Confirm you receive an AI response

### Part 3: Quick Connectivity Verification

Confirm all services resolve to private IPs from within the VNET:

```powershell
# Get resource names
$kvName = az keyvault list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "[0].name" -o tsv
$openaiName = az cognitiveservices account list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "[?kind=='AIServices'].name" -o tsv
$storageName = az storage account list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "[0].name" -o tsv

# Test DNS resolution - all should return 10.0.x.x private IPs
Write-Host "`n--- OpenAI DNS ---"
$openaiEndpoint = az cognitiveservices account show -n $openaiName -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query properties.endpoint -o tsv
$openaiHost = ([System.Uri]$openaiEndpoint).Host
Resolve-DnsName $openaiHost | Select-Object Name, IPAddress

Write-Host "`n--- Key Vault DNS ---"
Resolve-DnsName "$kvName.vault.azure.net" | Select-Object Name, IPAddress

Write-Host "`n--- Storage DNS ---"
Resolve-DnsName "$storageName.blob.core.windows.net" | Select-Object Name, IPAddress
```

All services should resolve to **10.0.x.x** private IPs, confirming private endpoint connectivity.

### Part 4: Test Session Persistence

Verify chat session history is saved to Azure Storage:

1. **Send 2-3 messages** in the chat app to build a conversation.

2. **Check if sessions are saved** (open a new PowerShell terminal):

```powershell
$storageName = az storage account list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "[0].name" -o tsv

# Assign Storage Blob Data Reader to the current user (needed for az CLI auth)
$currentUserId = az ad signed-in-user show --query id -o tsv
$storageId = az storage account show --name $storageName -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query id -o tsv

az role assignment create `
 --assignee $currentUserId `
 --role "Storage Blob Data Reader" `
 --scope $storageId

# Wait a moment for role propagation
Start-Sleep -Seconds 30

az storage blob list `
 --account-name $storageName `
 --container-name "chat-sessions" `
 --auth-mode login `
 --query "[].{Name:name, Size:properties.contentLength, LastModified:properties.lastModified}" `
 --output table
```

   You should see your session file(s) listed with timestamps matching your chat activity.

   > **Note**: If the `chat-sessions` container doesn't exist yet, the app will create it on the first message. If you see an error, send a message in the app first and retry.

## Success Criteria

Validate your secure connectivity:

- [ ] Connected to VM via Azure Bastion (no public IP)
- [ ] Chat application accessible and working through Bastion session
- [ ] DNS resolves all services to private IPs (10.0.x.x)
- [ ] Session history saved to Blob Storage
