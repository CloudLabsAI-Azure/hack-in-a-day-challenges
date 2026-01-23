# Challenge 01: Deploy Core Azure Infrastructure

## Introduction

Before deploying your secure AI application, you need to create the foundational Azure infrastructure. This challenge involves manually creating the networking and core services through the Azure Portal.

You'll provision:
- Virtual Network with segmented subnets
- Azure OpenAI resource with GPT-4 model
- Azure Key Vault for secrets management
- Azure Storage Account for data persistence

By deploying each resource manually, you'll gain deep understanding of Azure networking, security, and resource configuration.

## Challenge Objectives

- Create a Virtual Network with three subnets
- Deploy Azure OpenAI resource
- Deploy GPT-4 model for chat completions
- Create Azure Key Vault with RBAC authorization
- Deploy Azure Storage Account with security settings
- Verify all resources are accessible

## Steps to Complete

### Part 1: Verify Pre-Deployed Resource Group

1. In the **Azure Portal**, search for **Resource groups** in the top search bar and select it.

1. You should see a pre-deployed resource group named **challenge-rg-<inject key="DeploymentID"></inject>**.

1. Click on **challenge-rg-<inject key="DeploymentID"></inject>** to open it.

1. This resource group will be used for all resources you create in this hackathon.

### Part 2: Create Virtual Network

1. In the **Azure Portal**, click **+ Create a resource**.

1. Search for **Virtual Network** and select it.

1. Click **Create**.

1. Configure the Virtual Network:

   **Basics tab**:
   - **Subscription**: Select your available Azure subscription
   - **Resource group**: Select **challenge-rg-<inject key="DeploymentID"></inject>**
   - **Virtual network name**: **vnet-secureai-<inject key="DeploymentID"></inject>**
   - **Region**: **<inject key="Region"></inject>**

1. Click **Next: Security**.

   - Leave everything **turned off (default)**, then click **Next**.

1. On **IP Addresses**.

   - You'll see a **default** subnet created automatically
   - **Delete the default subnet** by clicking the delete icon next to it
   
1. Click **+ Add subnet** to add the first subnet. Configure the following:
   - **Subnet purpose**: **Default**
   - **Name**: **snet-ai-services**
   - **Starting address**: **10.0.1.0**
   - **Size**: **/24 (256 addresses)**
   - Verify **Include an IPv4 address space** is checked
   - Verify **NAT gateway**, **Network security group**, and **Route table** are set to **None**
   - Verify **Private endpoint network policy** is **Disabled**
   - Leave everything else as default
   - Click **Add**

1. Click **+ Add subnet** to add the second subnet. Configure the following:
   - **Subnet purpose**: **Default**
   - **Name**: **snet-storage-services**
   - **Starting address**: **10.0.2.0**
   - **Size**: **/24 (256 addresses)**
   - Leave everything else as default
   - Click **Add**

1. Click **+ Add subnet** to add the third subnet. Configure the following:
   - **Subnet purpose**: **Default**
   - **Name**: **snet-application**
   - **Starting address**: **10.0.3.0**
   - **Size**: **/24 (256 addresses)**
   - Leave everything else as default
   - Click **Add**

1. Click **Review + Create**.

1. Click **Create**.

1. Wait for deployment (30 seconds).

1. Once complete, click **Go to resource** to verify all three subnets were created.

### Part 3: Create Azure AI Foundry Project

1. In the **Azure Portal**, click **+ Create a resource**.

1. Search for **Azure AI Foundry** and select it.

1. Click **Create**.

1. Configure Azure AI Foundry:

   **Basics tab**:
   - **Subscription**: Select your available Azure subscription
   - **Resource group**: Select **challenge-rg-<inject key="DeploymentID"></inject>**
   - **Name**: **openai-secureai-<inject key="DeploymentID"></inject>**
   - **Region**: **<inject key="Region"></inject>**
   - **Default project name**: Keep as **proj-default**

      > **Note**: This creates both an AI Foundry Hub (resource) and a default project inside it.

1. Click **Review + Create**.

1. Click **Create**.

1. Wait for deployment (**3-5 minutes** this creates multiple resources).

1. Once complete, click **Go to resource**.

### Part 4: Deploy GPT-4 Model in Azure AI Foundry

1. In your **openai-secureai-<inject key="DeploymentID"></inject>** resource.

1. Click on **Go to Foundry portal**.

1. In Azure AI Foundry portal, verify your project is: **proj-default**.

1. In the left navigation, click **Models + Endpoints**.

1. Click **+ Deploy model** → **Deploy base model**.

1. Search for and select **gpt-4.1** from the model catalog.

1. Click **Confirm**.

1. Configure the deployment:
   - **Deployment name**: **secure-chat**
   - **Deployment type**: **Global Standard**
   - **Tokens per Minute Rate Limit (thousands)**: **40K**

   > **Important**: Do not increase TPM beyond 20K to avoid quota issues.

1. Click **Deploy**.

1. Wait for deployment to complete (30-60 seconds).

### Part 5: Test the Model Deployment

1. In the **Models + Endpoints** page, find your **secure-chat** deployment.

1. Click **Open in playground**.

1. In the **Chat session** section, test with this prompt:
   ```
   Explain the principle of least privilege in cloud security.
   ```

1. Verify you get a response from GPT-4.

1. Click **View code** (top right).

1. Select the **Python** tab.

1. Copy the endpoint URL - you'll need this later.

1. Close the playground.

### Part 6: Create Azure Key Vault

1. In the **Azure Portal**, click **+ Create a resource**.

1. Search for **Key Vault** and select it.

1. Click **Create**.

1. Configure Key Vault:

   **Basics tab**:
   - **Subscription**: Select your available Azure subscription
   - **Resource group**: Select **challenge-rg-<inject key="DeploymentID"></inject>**
   - **Key vault name**: **kv-secureai-<inject key="DeploymentID"></inject>**
   - **Region**: **<inject key="Region"></inject>**
   - **Pricing tier**: **Standard**

1. Click **Next: Access configuration**.

   **Access configuration tab**:
   - **Permission model**: Select **Azure role-based access control (RBAC)**
   
   > This is more secure than the legacy access policies model.

1. Click **Review + Create**.

1. Click **Create**.

1. Wait for deployment (30 seconds).

1. Once complete, click **Go to resource**.

### Part 7: Assign Key Vault Permissions

1. In your **kv-secureai-<inject key="DeploymentID"></inject>** Key Vault.

1. In the left navigation, click **Access control (IAM)**.

1. Click **+ Add** → **Add role assignment**.

1. In the **Role** tab:
   - Search for **Key Vault Administrator**
   - Select **Key Vault Administrator**
   - Click **Next**

1. In the **Members** tab:
   - **Assign access to**: Select **User, group, or service principal**
   - Click **+ Select members**
   - Search for your email: **<inject key="AzureAdUserEmail"></inject>**
   - Select yourself
   - Click **Select**

1. Click **Review + assign**.

1. Click **Review + assign** again.

   > **Note**: RBAC can take 2-3 minutes to propagate. Wait before testing.

### Part 8: Create Azure Storage Account

1. In the **Azure Portal**, click **+ Create a resource**.

1. Search for **Storage account** and select it.

1. Click **Create**.

1. Configure Storage Account:

   **Basics tab**:
   - **Subscription**: Select your available Azure subscription
   - **Resource group**: Select **challenge-rg-<inject key="DeploymentID"></inject>**
   - **Storage account name**: **stsecureai<inject key="DeploymentID"></inject>** (lowercase, no hyphens)
   - **Region**: **<inject key="Region"></inject>**
   - **Performance**: **Standard**
   - **Redundancy**: **Locally-redundant storage (LRS)**

1. Click **Next: Advanced**.

   **Advanced tab**:
   - **Require secure transfer for REST API operations**: **Enabled** (should be checked)
   - **Allow enabling public access on containers**: **Disabled** (uncheck this!)
   - **Minimum TLS version**: **Version 1.2**

1. Click **Next: Networking**.

   **Networking tab**:
   - **Network access**: Select **Enable public access from all networks** (we'll restrict in Challenge 2)

1. Click **Review + Create**.

1. Click **Create**.

1. Wait for deployment (1-2 minutes).

1. Once complete, click **Go to resource**.

### Part 9: Create Blob Container

1. In your **stsecureai<inject key="DeploymentID"></inject>** Storage Account.

1. In the left navigation, under **Data storage**, click **Containers**.

1. Click **+ Container** (top button).

1. Configure the container:
   - **Name**: **chat-sessions**
   - **Public access level**: **Private (no anonymous access)**

1. Click **Create**.

1. Verify the **chat-sessions** container appears in the list.

### Part 10: Verify All Resources

1. Navigate back to your resource group: **challenge-rg-<inject key="DeploymentID"></inject>**.

1. Verify you see the following resources:
   - ✅ **vnet-secureai-<inject key="DeploymentID"></inject>** (Virtual network)
   - ✅ **openai-secureai-<inject key="DeploymentID"></inject>** (Azure OpenAI)
   - ✅ **kv-secureai-<inject key="DeploymentID"></inject>** (Key vault)
   - ✅ **stsecureai<inject key="DeploymentID"></inject>** (Storage account)

1. Click on the **Virtual network** resource.

1. In the left navigation, click **Subnets**.

1. Verify all three subnets exist:
   - ✅ snet-ai-services (10.0.1.0/24)
   - ✅ snet-storage-services (10.0.2.0/24)
   - ✅ snet-application (10.0.3.0/24)

### Part 11: Save Configuration Details

Open Notepad on your VM and document the following:

```
==============================================
SECURE AI INFRASTRUCTURE - DEPLOYMENT SUMMARY
==============================================
Deployment ID: <inject key="DeploymentID"></inject>
Region: <inject key="Region"></inject>

NETWORKING:
-----------
Virtual Network: vnet-secureai-<inject key="DeploymentID"></inject>
  Address Space: 10.0.0.0/16
  
Subnets:
  - snet-ai-services: 10.0.1.0/24
  - snet-storage-services: 10.0.2.0/24
  - snet-application: 10.0.3.0/24

AZURE OPENAI:
-------------
Resource Name: openai-secureai-<inject key="DeploymentID"></inject>
Endpoint: [paste the endpoint you copied earlier]
Model Deployment: secure-chat

KEY VAULT:
----------
Name: kv-secureai-<inject key="DeploymentID"></inject>
Vault URI: https://kv-secureai-<inject key="DeploymentID"></inject>.vault.azure.net/
Authorization: RBAC (Key Vault Administrator assigned)

STORAGE ACCOUNT:
----------------
Name: stsecureai<inject key="DeploymentID"></inject>
Container: chat-sessions
Public Access: Disabled
HTTPS Only: Enabled

NEXT STEPS:
-----------
✅ Challenge 1: COMPLETE!
➡️ Challenge 2: Configure Network Security & Private Endpoints
➡️ Challenge 3: Setup Identity & Access Management
➡️ Challenge 4: Deploy Additional AI Models
➡️ Challenge 5: Deploy Chat Application
➡️ Challenge 6: Test Secure Connectivity
➡️ Challenge 7: Production Readiness Validation
==============================================
```

Save this file as: **C:\LabFiles\deployment-summary.txt**

## Success Criteria

Verify you completed all tasks:

- [ ] Virtual Network created with 10.0.0.0/16 address space
- [ ] Three subnets created:
  - [ ] snet-ai-services (10.0.1.0/24)
  - [ ] snet-storage-services (10.0.2.0/24)
  - [ ] snet-application (10.0.3.0/24)
- [ ] Azure OpenAI resource deployed
- [ ] GPT-4 model deployed as "secure-chat"
- [ ] Model tested successfully in playground
- [ ] Azure Key Vault created with RBAC authorization
- [ ] Key Vault Administrator role assigned to yourself
- [ ] Azure Storage Account created with public access disabled
- [ ] Blob container "chat-sessions" created
- [ ] All resources visible in resource group
- [ ] Configuration details saved to deployment-summary.txt

## Troubleshooting

### Issue: Virtual Network creation fails

**Solution**:
- Verify you selected the correct resource group
- Ensure the region matches your resource group's region
- Check that address space is 10.0.0.0/16 (not overlapping with existing networks)

---

### Issue: Azure OpenAI quota exceeded

**Solution**:
- Some regions have limited OpenAI availability
- Try these alternative regions:
  - East US
  - East US 2
  - Sweden Central
  - Switzerland North
- In the Azure Portal, go to **Quotas** and request an increase if needed

---

### Issue: Key Vault name already exists

**Solution**:
- Key Vault names are globally unique
- If you deleted a Key Vault, it's soft-deleted for 90 days
- Change the name slightly (e.g., add "v2": kv-secureai-<inject key="DeploymentID"></inject>v2)
- Or purge the deleted vault:
  1. Go to Key Vaults in the portal
  2. Click **Manage deleted vaults**
  3. Select your region
  4. Find the deleted vault and click **Purge**

---

### Issue: Storage account name is invalid

**Solution**:
- Must be **lowercase only**
- No hyphens or special characters
- 3-24 characters
- Globally unique
- Use exactly: **stsecureai<inject key="DeploymentID"></inject>**

---

### Issue: Cannot create blob container

**Solution**:
- Wait 2-3 minutes after storage account creation
- Refresh the page
- Verify storage account deployment completed successfully
- Ensure you have Contributor permissions on the resource group

---

### Issue: GPT-4 model deployment fails

**Solution**:
- Reduce TPM to 10K instead of 20K
- Or deploy **gpt-35-turbo** instead:
  - Model: gpt-35-turbo
  - Deployment name: gpt-35-turbo-chat
  - TPM: 50K
- Check quota in Azure OpenAI Studio → Quotas

## Bonus Challenges

1. **Deploy a Second Model**:
   - In Azure OpenAI Studio, deploy **text-embedding-ada-002**
   - Deployment name: **text-embedding**
   - Use for semantic search in future challenges

2. **Enable Soft Delete on Key Vault**:
   - Go to Key Vault → Properties
   - Enable **Soft delete** with 90-day retention
   - Enable **Purge protection** (prevents permanent deletion)

3. **Create a Network Security Group**:
   - Create NSG named **nsg-application**
   - Associate it with **snet-application** subnet
   - We'll add rules in Challenge 2

4. **Add Resource Tags**:
   - Tag all resources with:
     - Project: SecureAI
     - Environment: Production
     - Owner: [Your Name]

## What You Learned

In this challenge, you:

✅ Created a segmented Virtual Network for network isolation  
✅ Deployed Azure OpenAI and configured GPT-4 model  
✅ Set up Azure Key Vault with modern RBAC authorization  
✅ Deployed Azure Storage with security best practices  
✅ Learned Azure resource naming conventions  
✅ Understood foundational cloud security concepts  

Your infrastructure is deployed, but **not yet secure** - all services still allow public access from the internet!

## Next Steps

Infrastructure deployed: ✅

In **Challenge 2**, you'll secure this infrastructure by:
- Creating private endpoints for all services
- Disabling public network access
- Configuring private DNS zones
- Implementing complete network isolation

Head to **challenge-2.md** to lock down your environment! 🔒

---

**Important Note**: Save your deployment-summary.txt file! You'll need the resource names and endpoints throughout the remaining challenges.
