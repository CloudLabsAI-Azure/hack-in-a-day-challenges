# Challenge 05: Deploy Secure Chat Application

## Introduction

All the infrastructure is ready! Now comes the fun part deploying a secure, production-ready chat application that uses everything you have built:

- Private endpoints (no public access)
- Managed identity (no API keys)
- Key Vault secrets (zero hardcoded credentials)
- Azure OpenAI (chat models ready)

The application code is already pre-built for you. You'll download it, configure the `.env` file with your Key Vault name, install dependencies, and run it. **No code changes required!**

Let’s build a secure ChatGPT-like experience.

## Prerequisites

- Completed Challenge 4 (OpenAI models deployed and tested)
- All Key Vault secrets created (OpenAIEndpoint, ChatModelDeployment, etc.)
- Managed identity configured on **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>** with proper RBAC roles
- Python 3.11 and VS Code installed on **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>**
- Connected to **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>** via Azure Bastion

## Challenge Objectives

- Download the pre-built secure chat application
- Configure `.env` file with the Key Vault name
- Install Python dependencies
- Run the chat app locally on the VM
- Test chat functionality with managed identity
- Validate security (no API keys, private endpoints only)
- Test session history with Storage Account

## Steps to Complete

### Task 1: Download and Extract Application Code

The application code is provided in a pre-built package.

1. In the Bastion VM, open an Edge browser tab download the code package, and select **Open file**:
   
   Visit this link in your browser:
   ```
   https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/deploy-your-ai-application.zip
   ```

2. **Extract the ZIP file**:
   
   - Right-click the downloaded `hack-in-a-day-challenges-deploy-your-ai-application.zip` file
   - Select **Extract All...**
   - Choose a location `C:\Code\`
   - Click **Extract**

3. **Navigate to the codefiles folder**:
   
   - Open VSCode, select **File** > click on **Open Folder** and select the folder `C:\Code\hack-in-a-day-challenges-deploy-your-ai-application\codefiles`

### Task 2: Configure the Application

1. **Rename `.env.example` to create your `.env` file**:

   ```powershell
   Copy-Item -Path ".env.example" -Destination ".env"
   Write-Host "Created .env file from template"
   ```

2. **Get your Key Vault name**:

   ```powershell
   $kvName = az keyvault list `
   --query "[0].name" -o tsv

   Write-Host "Your Key Vault name: $kvName"
   ```

3. **Update the `.env` file with your Key Vault name**:

   ```powershell
   # Replace the placeholder with your actual Key Vault name
   (Get-Content ".env") -replace 'kv-secureai-XXXXXXX', $kvName | Set-Content ".env"

   Write-Host "Updated .env with Key Vault name: $kvName"
   ```

4. **Verify the `.env` file**:

   ```powershell
   Get-Content ".env"
   ```

   - You should see **KEY_VAULT_NAME=kv-secureai-<inject key="DeploymentID" enableCopy="false"/>** (with your actual deployment ID).

      > **Important**: The `.env` file contains **only non-sensitive configuration**. All secrets (OpenAI endpoint, deployment name, API version, storage account name) are retrieved from Azure Key Vault at runtime using Managed Identity. No API keys anywhere!

### Task 3: Store Storage Account Name in Key Vault

The app saves chat session history to Blob Storage. Store the storage account name in Key Vault so the app can retrieve it securely.

```powershell
$kvName = az keyvault list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[0].name" -o tsv

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

   > **Note**: If you already stored `StorageAccountName` in Challenge 3, this step will simply update the existing secret with the same value.

### Task 4: Install Dependencies

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

   - This will take 2-3 minutes to complete.

      > **Note**: The `requirements.txt` pins `openai>=1.12.0,<2.0.0`. Versions earlier than 1.x will fail with errors like "Client.__init__() got an unexpected keyword argument 'proxies'" due to breaking changes in the OpenAI Python SDK.

### Task 5: Verify Storage Account Access

Verify managed identity has access to Blob Storage for session history (should be assigned from Challenge 3).

```powershell
$identityId = az vm show `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --name "Hack-vm-<inject key="DeploymentID" enableCopy="false"/>" `
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

### Task 6: Run the Chat Application

Moment of truth!

1. **Make sure you're in the app directory with the virtual environment activated**:

   ```powershell
   Set-Location "C:\Code\hack-in-a-day-challenges-deploy-your-ai-application\codefiles"
   .\venv\Scripts\Activate.ps1
   ```

2. **Start the app**:

   ```powershell
   streamlit run app.py
   ```

   >**Note:** When asked for **Email** type **<inject key="DeploymentID" enableCopy="false"/>** and press enter.

3. **Expected output**:

   ```
   You can now view your Streamlit app in your browser.

   Local URL: http://localhost:8501
   Network URL: http://10.0.3.4:8501
   ```

4. **Open browser**:

   - The browser should open automatically.
   - If not, manually navigate to `http://localhost:8501`

5. **You should see**:

   - The **Secure Enterprise Chat** application with a professional enterprise UI
   - Sidebar showing: **Authenticated** with Managed Identity
   - Model name displayed
   - "Auth: Managed Identity" and "Network: Private Only"
   - Chat input box ready

### Task 7: Test the Chat Application

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

      - The response should reference the previous question

3. **Verify no API keys in code** (quick security check):

   - Open a **new** PowerShell terminal (keep the app running) and run:

      ```powershell
      Select-String -Path "C:\Code\hack-in-a-day-challenges-deploy-your-ai-application\codefiles\app.py" -Pattern "api[_-]?key" -CaseSensitive:$false
      # Should return NO MATCHES - all auth goes through Managed Identity!
      ```

## Success Criteria

Validate your app deployment:

- Application code downloaded and extracted to `C:\Code\hack-in-a-day-challenges-deploy-your-ai-application\codefiles`
- `.env` file configured with your Key Vault name (no secrets in the file!)
- Virtual environment created and dependencies installed
- The app starts without errors (`streamlit run app.py`)
- Sidebar shows "Authenticated" with Managed Identity
- Chat completions work
- Multi-turn conversations work (context maintained)
- No API keys in code or config files

Now, click **Next** to continue to **Challenge 06**.
