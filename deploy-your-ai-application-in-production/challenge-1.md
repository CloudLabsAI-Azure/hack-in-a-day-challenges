# Challenge 01: Deploy Secure AI Infrastructure with Azure Developer CLI

## Introduction

Welcome to your first challenge! Instead of clicking through the Azure Portal for hours, you'll deploy a complete secure AI infrastructure stack in minutes using **Azure Developer CLI (AZD)** - Microsoft's modern infrastructure-as-code tool.

By the end of this challenge, you'll have:
- Azure AI Foundry Hub & Project (with private endpoint)
- Azure OpenAI service (with private endpoint)
- Azure Key Vault (with private endpoint)
- Azure Storage Account (with private endpoint)
- Virtual Network (VNET) with subnets
- All services connected via private networking
- Managed identity configured
- Zero public internet access

All deployed with a single command! 🚀

## Prerequisites

- Completed the **Getting Started** guide
- Connected to your VM via Azure Bastion
- VS Code open with PowerShell terminal
- Azure CLI logged in (`az login` successful)
- Resource Group: `challenge-rg-<inject key="DeploymentID"></inject>` visible in Azure Portal

## Challenge Objectives

- Install Azure Developer CLI (AZD)
- Initialize an AZD project using Microsoft's secure AI template
- Configure deployment parameters
- Deploy the complete infrastructure stack
- Verify all resources are deployed with private endpoints
- Understand the deployed architecture

## Architecture You'll Deploy

```
┌───────────────────────────────────────────────────────────────┐
│  Resource Group: challenge-rg-<DeploymentID>                  │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  Virtual Network: ai-vnet-<DeploymentID>                 │ │
│  │  Address Space: 10.0.0.0/16                              │ │
│  │                                                           │ │
│  │  ┌─────────────────────────────────────────────────────┐ │ │
│  │  │  Subnet: ai-services (10.0.1.0/24)                  │ │ │
│  │  │  - AI Foundry private endpoint                      │ │ │
│  │  │  - OpenAI private endpoint                          │1 │ │
│  │  └─────────────────────────────────────────────────────┘ │ │
│  │                                                           │ │
│  │  ┌─────────────────────────────────────────────────────┐ │ │
│  │  │  Subnet: storage-services (10.0.2.0/24)             │ │ │
│  │  │  - Storage Account private endpoint                 │ │ │
│  │  │  - Key Vault private endpoint                       │ │ │
│  │  └─────────────────────────────────────────────────────┘ │ │
│  │                                                           │ │
│  │  ┌─────────────────────────────────────────────────────┐ │ │
│  │  │  Subnet: application (10.0.3.0/24)                  │ │ │
│  │  │  - Your VM will connect here                        │ │ │
│  │  └─────────────────────────────────────────────────────┘ │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
│  Services Deployed:                                            │
│  • AI Foundry Hub (secure-ai-hub-<DeploymentID>)             │
│  • AI Foundry Project (secure-ai-project-<DeploymentID>)     │
│  • Azure OpenAI (aoai-<DeploymentID>)                        │
│  • Key Vault (kv-<DeploymentID>)                             │
│  • Storage Account (st<DeploymentID>)                        │
│  • Managed Identity (ai-identity-<DeploymentID>)             │
│  • Private DNS Zones (for private endpoint DNS resolution)   │
└───────────────────────────────────────────────────────────────┘
```

## Steps to Complete

### Part 1: Install Azure Developer CLI

Azure Developer CLI (AZD) is a modern tool for deploying cloud applications with infrastructure-as-code.

1. **Open PowerShell terminal in VS Code** (on your VM via Bastion)

2. **Install AZD** using winget:

```powershell
winget install microsoft.azd
```

3. **Close and reopen your terminal** to refresh the PATH

4. **Verify installation**:

```powershell
azd version
```

You should see output like: `azd version 1.x.x`

### Part 2: Create a Working Directory

1. **Create a project folder**:

```powershell
New-Item -Path "C:\LabFiles\SecureAI" -ItemType Directory -Force
cd C:\LabFiles\SecureAI
```

2. **Verify you're in the right location**:

```powershell
Get-Location
```

Should show: `C:\LabFiles\SecureAI`

### Part 3: Initialize AZD Project with Secure Template

Microsoft provides official templates for secure AI deployments. We'll use the AI Foundry starter template with private networking.

1. **Initialize the project** with the secure AI template:

```powershell
azd init --template Azure-Samples/azure-ai-studio-secure-bicep
```

2. **When prompted for environment name**, enter:

```
secure-ai-<inject key="DeploymentID"></inject>
```

Example: If your DeploymentID is 2034545, enter `secure-ai-2034545`

3. **AZD will download the template** and create the project structure. You'll see files being created:
   - `infra/` - Bicep templates for infrastructure
   - `azure.yaml` - AZD configuration
   - `.azure/` - AZD environment files

### Part 4: Configure Deployment Parameters

Now you'll configure where and how to deploy the infrastructure.

1. **Set your Azure subscription** (AZD needs to know which subscription to use):

```powershell
azd env set AZURE_SUBSCRIPTION_ID "<inject key="SubscriptionId"></inject>"
```

2. **Set the target resource group**:

```powershell
azd env set AZURE_RESOURCE_GROUP "challenge-rg-<inject key="DeploymentID"></inject>"
```

3. **Set the Azure region** (use the same region as your resource group):

```powershell
azd env set AZURE_LOCATION "<inject key="Region"></inject>"
```

4. **Set deployment naming prefix** (for unique resource names):

```powershell
azd env set AZURE_ENV_NAME "secureai<inject key="DeploymentID"></inject>"
```

5. **Enable private networking** (this is critical!):

```powershell
azd env set DEPLOY_PRIVATE_NETWORKING "true"
```

6. **Disable public access** (enterprise security requirement):

```powershell
azd env set PUBLIC_NETWORK_ACCESS "Disabled"
```

7. **Review your configuration**:

```powershell
azd env get-values
```

You should see all your configured values listed.

### Part 5: Deploy the Infrastructure

This is where the magic happens! One command deploys everything.

1. **Login to Azure with AZD** (separate from Azure CLI):

```powershell
azd auth login
```

A browser will open. Sign in with your lab credentials:
- **Username**: <inject key="AzureAdUserEmail"></inject>
- **Password**: <inject key="AzureAdUserPassword"></inject>

2. **Provision the infrastructure**:

```powershell
azd provision
```

**What happens now:**
- AZD reads the Bicep templates
- Creates/validates the resource group
- Deploys VNET and subnets
- Deploys AI Foundry Hub
- Deploys Azure OpenAI
- Deploys Storage Account
- Deploys Key Vault
- Creates managed identity
- Configures private endpoints
- Sets up private DNS zones
- Configures RBAC roles

**This will take 15-20 minutes.** ☕ Perfect time for a coffee break!

3. **Watch the progress** in the terminal. You'll see:
   - Each resource being created
   - Progress indicators
   - Success/failure messages

4. **When complete**, you'll see:

```
SUCCESS: Your application was provisioned in Azure in XX minutes XX seconds.
```

### Part 6: Verify the Deployment

Let's confirm everything deployed correctly.

1. **Open the Azure Portal** in a browser (keep your VM session open)

2. **Navigate to your Resource Group**: `challenge-rg-<inject key="DeploymentID"></inject>`

3. **Verify these resources exist**:

| Resource Type | Expected Name Pattern | Purpose |
|--------------|----------------------|---------|
| AI Services | `secureai<DeploymentID>` or similar | AI Foundry Hub |
| Azure OpenAI | `aoai-<DeploymentID>` | OpenAI service |
| Storage Account | `st<DeploymentID>` | AI project storage |
| Key Vault | `kv-<DeploymentID>` | Secret management |
| Virtual Network | `ai-vnet-<DeploymentID>` | Network isolation |
| Managed Identity | `ai-identity-<DeploymentID>` | Passwordless auth |
| Private Endpoints | Multiple | Private connectivity |
| Private DNS Zones | Multiple | DNS resolution |

4. **Check the Virtual Network**:
   - Click on the Virtual Network resource
   - Go to **Subnets**
   - Verify you see subnets like: `ai-services`, `storage-services`, `application`

5. **Check Private Endpoints**:
   - In the resource group, filter by type: "Private endpoint"
   - You should see 4+ private endpoints (one for each service)
   - Click on any private endpoint
   - Go to **DNS configuration**
   - Verify the Private DNS zone is linked

6. **Check AI Foundry Hub**:
   - Navigate to [https://ai.azure.com](https://ai.azure.com)
   - Sign in with your lab credentials
   - Click on **All hubs** (left menu)
   - You should see your hub: `secureai<DeploymentID>` or similar
   - Click on it to view details

### Part 7: Retrieve Connection Information

You'll need these values for future challenges.

1. **Back in your VM terminal**, get the AI Foundry endpoint:

```powershell
azd env get-values | Select-String "AI_PROJECT_ENDPOINT"
```

Copy this value - you'll need it later!

2. **Get the Key Vault name**:

```powershell
azd env get-values | Select-String "KEY_VAULT_NAME"
```

3. **Get the Storage Account name**:

```powershell
azd env get-values | Select-String "STORAGE_ACCOUNT_NAME"
```

4. **Get the OpenAI endpoint**:

```powershell
azd env get-values | Select-String "OPENAI_ENDPOINT"
```

5. **Save these values** in a text file on your VM for reference:

```powershell
azd env get-values > C:\LabFiles\deployment-info.txt
notepad C:\LabFiles\deployment-info.txt
```

## Success Criteria

Verify you've completed the challenge successfully:

- [ ] Azure Developer CLI (AZD) is installed and working (`azd version` shows version)
- [ ] AZD project initialized in `C:\LabFiles\SecureAI`
- [ ] Deployment parameters configured (subscription, region, resource group)
- [ ] `azd provision` completed successfully (no errors)
- [ ] Resource group contains all expected resources (AI Foundry, OpenAI, Storage, Key Vault, VNET)
- [ ] Virtual Network has 3+ subnets
- [ ] Private endpoints are deployed (4+ endpoints visible)
- [ ] Private DNS zones are created and linked
- [ ] AI Foundry Hub is visible at [ai.azure.com](https://ai.azure.com)
- [ ] Connection information saved to `deployment-info.txt`

## Troubleshooting

### Issue: `azd: command not found`

**Solution**:
- Close and reopen your PowerShell terminal
- Or manually refresh PATH:
  ```powershell
  $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
  ```

---

### Issue: `azd provision` fails with "Resource group not found"

**Solution**:
- Verify the resource group exists in Azure Portal
- Double-check the name matches exactly: `challenge-rg-<inject key="DeploymentID"></inject>`
- Re-run the configuration command:
  ```powershell
  azd env set AZURE_RESOURCE_GROUP "challenge-rg-<inject key="DeploymentID"></inject>"
  ```

---

### Issue: Deployment fails with "Quota exceeded"

**Solution**:
- Azure OpenAI has regional quota limits
- Check if your region has available quota
- If not, try a different region:
  ```powershell
  azd env set AZURE_LOCATION "eastus2"
  azd provision
  ```

---

### Issue: "Permission denied" or "Authorization failed"

**Solution**:
- Verify you're logged in with AZD:
  ```powershell
  azd auth login --use-device-code
  ```
- Ensure your lab account has Contributor role on the subscription
- Check in Azure Portal: **Subscriptions** → **Access control (IAM)** → **Role assignments**

---

### Issue: Private endpoint deployment fails

**Solution**:
- Ensure the VNET and subnets are created first
- Check if private endpoint subnet has `privateEndpointNetworkPolicies` disabled
- Re-run the deployment:
  ```powershell
  azd provision
  ```

---

### Issue: Deployment takes too long (>30 minutes)

**Solution**:
- Check the Azure Portal for deployment status
- Go to Resource Group → **Deployments** → Click on the running deployment
- Look for errors or stuck resources
- If stuck, cancel and retry:
  ```powershell
  azd provision
  ```

## Bonus Challenges

Want to go deeper? Try these:

1. **Explore the Bicep Templates**:
   - Open `C:\LabFiles\SecureAI\infra\main.bicep` in VS Code
   - Understand how the VNET and private endpoints are defined
   - Identify where managed identity is configured

2. **Customize the Deployment**:
   - Modify the VNET address space to use `10.10.0.0/16` instead
   - Re-deploy and observe the changes

3. **Check Deployment Logs**:
   - In Azure Portal, go to Resource Group → **Deployments**
   - Click on the most recent deployment
   - Review the deployment template and outputs

4. **Understand Private DNS**:
   - In the Portal, search for "Private DNS zones"
   - Click on one of the zones (e.g., `privatelink.openai.azure.com`)
   - Go to **Virtual network links**
   - Understand how DNS resolution works for private endpoints

## What You Learned

In this challenge, you:

✅ Installed and used Azure Developer CLI for infrastructure deployment  
✅ Deployed a complete secure AI environment with private networking  
✅ Created a VNET with multiple subnets for service isolation  
✅ Configured private endpoints for all AI services (zero public access)  
✅ Set up managed identity for passwordless authentication  
✅ Deployed infrastructure-as-code using Bicep templates  
✅ Understood the architecture of a secure AI deployment  

## Next Steps

Your infrastructure is ready! In **Challenge 2**, you'll configure Network Security Groups to further lock down your network and validate that all public access is disabled.

Head to **challenge-2.md** to continue! 🔒

---

**Pro Tip**: Keep the `deployment-info.txt` file handy - you'll reference these values throughout the remaining challenges!
