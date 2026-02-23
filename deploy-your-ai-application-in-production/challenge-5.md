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
- Make the application accessible from any device via the VM's public IP

## Steps to Complete

### Task 1: Download and Extract Application Code

The application code is provided in a pre-built package.

1. In the Bastion VM, open an Edge browser tab download the code package, and select **Open file**:
   
   Visit this link in your browser:
   ```
   https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/deploy-your-ai-application.zip
   ```

1. **Extract the ZIP file**:
   
   - Right-click the downloaded `hack-in-a-day-challenges-deploy-your-ai-application.zip` file
   - Select **Extract All...**
   - Choose a location `C:\Code\`
   - Click **Extract**

1. **Navigate to the codefiles folder**:
   
   - Open VSCode, select **File** > click on **Open Folder** and select the folder `C:\Code\hack-in-a-day-challenges-deploy-your-ai-application\codefiles`

### Task 2: Configure the Application

1. **Rename `.env.example` to create your `.env` file**:

   ```powershell
   Copy-Item -Path ".env.example" -Destination ".env"
   Write-Host "Created .env file from template"
   ```

1. **Get your Key Vault name**:

   ```powershell
   $kvName = az keyvault list `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query "[0].name" -o tsv

   Write-Host "Your Key Vault name: $kvName"
   ```

1. **Update the `.env` file with your Key Vault name**:

   ```powershell
   # Replace the placeholder with your actual Key Vault name
   (Get-Content ".env") -replace 'kv-secureai-XXXXXXX', $kvName | Set-Content ".env"

   Write-Host "Updated .env with Key Vault name: $kvName"
   ```

1. **Verify the `.env` file**:

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

   > **Note**: If you already stored `StorageAccountName` in Challenge 3, this step will simply update the existing secret with the same value. This is intentionally included here to ensure the secret exists regardless of whether Challenge 3 was fully completed.

### Task 4: Install Dependencies

1. **Create a virtual environment** (best practice):

   ```powershell
   python -m venv venv

   # Activate it
   .\venv\Scripts\Activate.ps1
   ```

1. **Upgrade pip**:

   ```powershell
   python -m pip install --upgrade pip
   ```

1. **Install requirements**:

   ```powershell
   pip install -r requirements.txt
   ```

   - This will take 2-3 minutes to complete.

      > **Note**: The `requirements.txt` pins `openai>=1.12.0,<2.0.0`. Versions earlier than 1.x will fail with errors like "Client.__init__() got an unexpected keyword argument 'proxies'" due to breaking changes in the OpenAI Python SDK.

### Task 5: Verify Storage Account Access

1. Verify managed identity has access to Blob Storage for session history (should be assigned from Challenge 3).

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

1. **Start the app**:

   ```powershell
   streamlit run app.py
   ```

   >**Note:** When asked for **Email** press **enter**.

1. **Expected output**:

   ```
   You can now view your Streamlit app in your browser.

   Local URL: http://localhost:8501
   Network URL: http://10.0.3.4:8501
   ```

1. **Open browser**:

   - The browser should open automatically.
   - If not, manually navigate to `http://localhost:8501`

1. **You should see**:

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

1. **Send a follow-up** to test multi-turn conversation:

   ```
   How does that apply to Azure managed identities?
   ```

      - The response should reference the previous question

1. **Verify no API keys in code** (quick security check):

   - Open a **new** PowerShell terminal (keep the app running) and run:

      ```powershell
      Select-String -Path "C:\Code\hack-in-a-day-challenges-deploy-your-ai-application\codefiles\app.py" -Pattern "api[_-]?key" -CaseSensitive:$false
      # Should return NO MATCHES - all auth goes through Managed Identity!
      ```

### Task 8: Make the Application Accessible from Any Device

The app currently runs on `localhost` inside the VM. Now let's make it accessible from any device on the internet using the VM's public IP address.

1. **Stop the running Streamlit app** by pressing `Ctrl+C` in the terminal where it's running.

1. **Add a Windows Firewall rule** to allow inbound traffic on port 8501:

   ```powershell
   New-NetFirewallRule -DisplayName "Streamlit Port 8501" -Direction Inbound -LocalPort 8501 -Protocol TCP -Action Allow
   ```

1. **Restart Streamlit** bound to all network interfaces (`0.0.0.0`) so it accepts connections from outside the VM:

   ```powershell
   streamlit run app.py --server.address=0.0.0.0
   ```

   >**Note:** When asked for **Email** press **enter**.

1. **Get the VM's public IP address** (open a **new** PowerShell terminal):

   ```powershell
   az vm show -d `
    --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
    --name "Hack-vm-<inject key="DeploymentID" enableCopy="false"/>" `
    --query publicIps -o tsv
   ```

   >**Note:** You can get the VM’s public IP address from the Azure Portal:
   - Search for and select **Virtual machines**
   - Select **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>**
   - In the **Overview** page, copy the **Public IP address**

1. **Access the app from any device**:

   - Open a browser on **any device** (your laptop, phone, tablet, etc.)
   - Navigate to: `http://<YOUR-VM-PUBLIC-IP>:8501`
   - For example: `http://20.91.200.211:8501`

1. **Verify**:

   - The **Secure Enterprise Chat** application loads in your browser
   - You can send messages and receive AI responses just like you did locally on the VM

   > **Important - HTTP Only (No SSL)**: The application is currently served over **HTTP**, not HTTPS, because no SSL/TLS certificate has been configured. This means the connection is **unencrypted** and is not suitable for handling sensitive data in this state. In a production environment, you would place the application behind a reverse proxy (such as Azure Application Gateway or Nginx) with a valid SSL/TLS certificate to enable HTTPS, or deploy to a PaaS service like Azure App Service that provides managed SSL/TLS out of the box. For the purposes of this lab, HTTP is sufficient to demonstrate the functionality.

<validation step="2fdf5b82-f5c0-403b-bf34-a222b7a5daa4" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

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
- Windows Firewall rule allows inbound traffic on port 8501
- Application is accessible from any device via `http://<VM-PUBLIC-IP>:8501`

**Congratulations!** You have successfully completed all challenges in this hackathon. You built and deployed a fully secure, enterprise-ready AI chat application with network isolation, managed identity authentication, Key Vault secret management, and external accessibility — all without a single API key in your code.
