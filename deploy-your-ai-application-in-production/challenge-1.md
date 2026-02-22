# Challenge 01: Deploy Core Azure Infrastructure

## Introduction

Before deploying your secure AI application, you need to create the foundational Azure infrastructure. This challenge involves manually creating the networking and core services through the Azure Portal.

You will provision:
- Virtual Network with segmented subnets
- Windows VM for application hosting
- Azure OpenAI resource with GPT-4.1 model
- Azure Key Vault for secrets management
- Azure Storage Account for data persistence

By deploying each resource manually, you will gain a deep understanding of Azure networking, security, and resource configuration.

## Challenge Objectives

- Create a Virtual Network with three subnets
- Deploy Windows VM in application subnet
- Deploy Azure OpenAI resource
- Deploy GPT model for chat completions
- Create Azure Key Vault with RBAC authorization
- Deploy Azure Storage Account with security settings
- Verify all resources are accessible

## Steps to Complete

### Task 1: Verify Pre-Deployed Resource Group

1. In the **Azure Portal**, search for **Resource groups** in the top search bar and select it.

1. You should see a pre-deployed resource group named **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**.

1. Click on **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>** to open it.

1. This resource group will be used for all resources you create in this hackathon.

### Task 2: Create Virtual Network

1. In the **Azure Portal**, navigate to the **Home** page and click **+ Create a resource**.

1. Search for **Virtual Network** and select it.

1. Click **Create**.

1. Configure the Virtual Network:

   - **Basics tab**:
      - **Subscription**: Select your available Azure subscription
      - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
      - **Virtual network name**: **vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>**
      - **Region**: **<inject key="Region"></inject>**

1. Click **Next**. On the **Security** tab, leave everything **turned off (default)**, then click **Next**.

1. On **IP Addresses**.

   - You'll see a **default** subnet created automatically
   - **Delete the default subnet** by clicking the delete icon next to it
 
1. Click **+ Add subnet** to add the first subnet. Configure the following:

   - **Subnet purpose**: **Default**
   - **Name**: **snet-ai-services**
   - Verify **Include an IPv4 address space** is checked
   - **Starting address**: **10.0.1.0**
   - **Size**: **/24 (256 addresses)**
   - Verify **NAT gateway**, **Network security group**, and **Route table** are set to **None**
   - Verify **Private endpoint network policy** is **Disabled**
   - Leave everything else as default
   - Click **Save**

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

1. Wait for the deployment to complete; it will take a maximum of 30 seconds.

1. Once the deployment is complete, click **Go to resource**. To verify that all three subnets were created, select **Settings** > **Subnets** from the left navigation menu.


### Task 3: Create Application Virtual Machine

Now you'll deploy a Windows VM in the application subnet where you'll host the secure chat application.

1. In the **Azure Portal**, search for **Virtual Machines** and select it.

1. Click **Create** > **Virtual machine**.

1. Configure the Virtual Machine:

   - **Basics tab**:
      - **Subscription**: Select your available Azure subscription
      - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
      - **Virtual machine name**: **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>**
      - **Region**: **<inject key="Region"></inject>**
      - **Availability options**: **No infrastructure redundancy required**
      - **Security type**: **Standard**
      - **Image**: **See all images** > **Windows server** > **Windows Server 2022 Datacenter: Azure Edition - x64 Gen2**
      - **Size**: Click **See all sizes**, search for **Standard_B2s**, select it, and click **Select**
   
         > **Note**: We are using Standard_B2s (2 vCPU, 4GB RAM), which is cost-effective for testing while providing adequate performance for this lab.
   
   - **Administrator account**:
      - **Username**: **azureuser**
      - **Password**: **SecureAI@2026**
      - **Confirm password**: **SecureAI@2026**
   
   - **Inbound port rules**:
      - **Public inbound ports**: **None** (we'll use Azure Bastion)
   
1. Click **Next: Disks >**.

   - **Disks tab**:
      - **OS disk type**: **Standard SSD (locally-redundant storage)**
      - Leave everything else as default
      - Click **Next: Networking**

1. **Networking tab**:
   - **Virtual network**: Select **vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>**
   - **Subnet**: Select **snet-application (10.0.3.0/24)**
   - **Public IP**: Select **None**
   - **NIC network security group**: **Basic**
   - **Public inbound ports**: **None**
   - Click **Next: Management**

1. **Management tab**:
   - **Enable system assigned managed identity**: **Off** (we'll enable this in Challenge 3)
   - **Enable auto-shutdown**: **Off**
   - Leave everything else as default
   - Click **Next: Monitoring**

1. **Monitoring tab**:
   - **Boot diagnostics**: **Enable with managed storage account (recommended)**
   - Leave everything else as default
   - Click **Next: Advanced**

1. **Advanced tab**:
   - Leave all settings as default.
   - **Do not add Custom Script Extension** (we'll install software manually after connecting via Bastion)

1. Click **Review + create**.

1. Review the configuration and click **Create**.

1. Wait for the deployment to complete; it will take a maximum of **3-5 minutes**.

1. Once complete, click **Go to resource**.

### Task 4: Create Azure Bastion Subnet

Before we can connect to the VM, we need to create a dedicated subnet for Azure Bastion.

1. In the **Azure Portal**, navigate to your **vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>** virtual network.

1. In the left navigation, click **Settings** > **Subnets**.

1. Click **+ Subnet**.

1. Configure the Bastion subnet:
   - **Name**: **AzureBastionSubnet** (must be exactly this name)
   - **Subnet purpose**: **Azure Bastion**
   - **Starting address**: **10.0.4.0**
   - **Subnet size**: **/26 (64 addresses)**
   
      > **Important**: Azure Bastion requires a dedicated subnet named exactly "AzureBastionSubnet" with at least /26 CIDR.

1. Click **Add**.

1. Wait for the deployment to complete; it will take a maximum of 30 seconds.

### Task 5: Test VM Connection via Bastion

Now let's install Azure Bastion and connect to the VM.

1. In the **Azure Portal**, navigate to your **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>** Virtual Machine resource.

1. In the left navigation, click **Connect** > **Connect via Bastion**.

1. On the **Hack-vm-<inject key="DeploymentID" enableCopy="false"/> | Bastion** page, expand **Dedicated Deployment Options**. Select **Configure manually**

1. Configure Bastion:
   - **Name**: **bastion-<inject key="DeploymentID" enableCopy="false"/>**
   - **Tier**: **Standard**
   - **Virtual network**: **vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>**
   - **Subnet**: **AzureBastionSubnet (10.0.4.0/26)** 
   - **Public IP address**: Click **Create new**
     - **Name**: **bastion-ip-<inject key="DeploymentID" enableCopy="false"/>**

1. Click **Review + create**, then click **Create**

1. Wait for the deployment to complete; it will take a maximum of **8-12 minutes**. 

1. Navigate to your **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>** Virtual Machine resource.

1. In the left navigation, click **Connect** > **Connect via Bastion**.

1. Expand **Connection Settings**:

   - **Authentication Type**: **Password**
   - **Username**: **azureuser**
   - **Password**: **SecureAI@2026**

1. Click **Connect**.

   >**Note:** If the error message appears—“**A pop-up blocker is preventing a new window from opening. Please allow pop-ups and retry.**”—enable pop-ups from the top navigation menu and try again.

1. A new browser tab will open with a Remote Desktop session.

1. Wait for Windows to finish setup (may take 1-2 minutes on first connection).

### Task 6: Install Required Software and Set Up VM

The VM is a fresh Windows Server 2022 instance. You'll install Chocolatey (package manager), then use it to install Python 3.11, VS Code, Azure CLI, and Git.

1. Once connected to **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>**, open **PowerShell as Administrator** (right-click Start → Windows PowerShell (Admin)).

1. **Install Chocolatey** (Windows package manager):
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force
   [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
   Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```

1. **Close and reopen PowerShell as Administrator** to refresh the PATH.

1. **Install Python 3.11, VS Code, Azure CLI, and Git**:
   ```powershell
   choco install python311 vscode azure-cli git -y
   ```

1. **Close and reopen PowerShell as Administrator** again to refresh the PATH after installation.

1. **Verify all tools are installed**:
   ```powershell
   python --version    # Should show: Python 3.11.x
   code --version      # Should show VS Code version
   az --version        # Should show Azure CLI version
   git --version       # Should show Git version
   ```

   > **Note**: If `python` is not recognized, try `python3 --version` or run `refreshenv` to reload environment variables.

1. **Create working directory**:
   ```powershell
   New-Item -Path "C:\Code" -ItemType Directory -Force
   ```

1. Keep the bastion session open you will use it throughout the hackathon. Username: **azureuser**, Password: **SecureAI@2026**

1. Inside the bastion VM, open **File Explorer**, and create a folder named `Code` inside `C:\`.

   >**Note:** If it is already created, skip this step and proceed to the next part.

### Task 7: Create Microsoft Foundry Project

1. In the **Azure Portal**, from the **Home** page, click **+ Create a resource**.

1. Search for **Microsoft Foundry** and select it.

1. Click **Create**.

1. Configure Microsoft Foundry:

   - **Basics tab**:
      - **Subscription**: Select your available Azure subscription
      - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
      - **Name**: **openai-secureai-<inject key="DeploymentID" enableCopy="false"/>**
      - **Region**: **<inject key="Region"></inject>**
      - **Default project name**: Keep as **proj-default**

         > **Note**: This creates both a Microsoft Foundry Hub (resource) and a default project inside it.

1. Click **Review + Create**.

1. Click **Create**.

1. Wait for the deployment to complete; it will take a maximum of **3-5 minutes**.

1. Once complete, click **Go to resource**.

### Task 8: Configure Custom Domain for Azure OpenAI (Critical for Private Endpoints)

Now that the Azure AI Foundry resource is created, you must configure a custom subdomain for it. This is a requirement for token-based authentication with managed identities and private endpoints.

> **Why this is required**: When using private endpoints with managed identity authentication, Azure OpenAI needs a custom subdomain to properly route token-based authentication requests. Without this, you'll get errors like "Please provide a custom subdomain for token authentication".

**Using VS Code on Hack-vm-<inject key="DeploymentID" enableCopy="false"/>**:

1. Switch to the Bastion VM, **Open VS Code**.

1. **Open a PowerShell terminal**, by pressing `Ctrl+J` in the keyboard.

1. **Login to Azure**:

   ```powershell
   az login
   ```
1. Log in with your Azure credentials. Press Enter when prompted for the subscription.

1. **Configure custom domain** for your OpenAI resource:

   ```powershell
   az cognitiveservices account update `
     --name openai-secureai-<inject key="DeploymentID" enableCopy="false"/> `
     --resource-group challenge-rg-<inject key="DeploymentID" enableCopy="false"/> `
     --custom-domain openai-secureai-<inject key="DeploymentID" enableCopy="false"/> `
     --output none
   ```
   
   > **Note**: The `--output none` flag suppresses the verbose JSON output.

1. **Verify the custom domain** was set:

   ```powershell
   az cognitiveservices account show `
     --name openai-secureai-<inject key="DeploymentID" enableCopy="false"/> `
     --resource-group challenge-rg-<inject key="DeploymentID" enableCopy="false"/> `
     --query "properties.customSubDomainName" -o tsv
   ```
   
   - Should return:

      ```
      openai-secureai-<inject key="DeploymentID" enableCopy="false"/>
      ```

   - You can also confirm the OpenAI endpoint is available:

      ```powershell
      az cognitiveservices account show `
      --name openai-secureai-<inject key="DeploymentID" enableCopy="false"/> `
      --resource-group challenge-rg-<inject key="DeploymentID" enableCopy="false"/> `
      --query "properties.endpoints" -o json | Select-String "openai.azure.com"
      ```
   
   - You should see a line containing:

      ```
      https://openai-secureai-<inject key="DeploymentID" enableCopy="false"/>.openai.azure.com/
      ```

      > **Note**: The primary `properties.endpoint` returns a `cognitiveservices.azure.com` URL since AI Foundry creates a multi-service resource. For OpenAI API calls, use the `.openai.azure.com` endpoint shown above.

> **Important**: Complete this step before proceeding to Challenge 2. Without the custom domain, private endpoint creation will succeed but authentication will fail.

### Task 9: Deploy GPT-4.1 Model in Azure AI Foundry

1. Switch to the **Azure portal**.

1. Open **openai-secureai-<inject key="DeploymentID" enableCopy="false"/>** resource.

1. Click on the **Go to Foundry portal**.

1. In Microsoft Foundry portal, verify your project is: **proj-default**.

1. In the left navigation, click **Models + Endpoints**.

1. Click **+ Deploy model** > **Deploy base model**.

1. Search for and select **gpt-4.1** from the model catalog.

1. Click **Confirm**.

1. Configure the deployment:

   - **Deployment name**: **secure-chat**
   - **Deployment type**: **Global Standard**
   - Select **Customize**
   - **Tokens per Minute Rate Limit (thousands)**: **40K**

      > **Important**: Do not increase TPM beyond 40K to avoid quota issues. We're using 40K to allow sufficient capacity for testing.

1. Click **Deploy**.

### Task 10: Test the Model Deployment

1.  On the **secure-chat** deployment page, click **Open in playground**.

1. In the **Chat session** section, test with this prompt:

   ```
   Explain the principle of least privilege in cloud security.
   ```

1. Verify that you receive a response from GPT-4.1.

1. Click **View code** (top left).

1. Select the **Python** tab.

1. **Note the endpoint format** it should look like the below:

   ```
   https://openai-secureai-<inject key="DeploymentID" enableCopy="false"/>.openai.azure.com/
   ```
   This is the custom domain you configured in Task 8. You'll store this in Key Vault in the next challenge.

1. Close the playground.

### Task 11: Create Azure Key Vault

1. In the **Azure Portal**, click **+ Create a resource**.

1. Search for **Key Vault** and select it.

1. Click **Create**.

1. Configure Key Vault:

   - **Basics tab**:

      - **Subscription**: Select your available Azure subscription
      - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
      - **Key vault name**: **kv-secureai-<inject key="DeploymentID" enableCopy="false"/>**
      - **Region**: **<inject key="Region"></inject>**
      - **Pricing tier**: **Standard**

1. Click **Next**.

   - **Access configuration tab**:

      - **Permission model**: Select **Azure role-based access control (RBAC)**
   
         > This is more secure than the legacy access policies model.

1. Click **Review + Create**.

1. Click **Create**.

1. Wait for the deployment to complete; it will take a maximum of 30 seconds.

1. Once complete, click **Go to resource**.

### Task 12: Assign Key Vault Permissions

1. In your **kv-secureai-<inject key="DeploymentID" enableCopy="false"/>** Key Vault.

1. In the left navigation, click **Access control (IAM)**.

1. Click **+ Add** > **Add role assignment**.

1. In the **Role** tab:

   - Search for **Key Vault Administrator**
   - Select **Key Vault Administrator**
   - Click **Next**

1. In the **Members** tab:

   - **Assign access to**: Select **User, group, or service principal**
   - Click **+ Select members**
   - Search and select: **<inject key="AzureAdUserEmail"></inject>**
   - Click **Select**

1. Click **Review + assign**.

1. Click **Review + assign** again.

   > **Note**: RBAC changes may take 2–3 minutes to propagate. Please wait a few minutes before testing to ensure the permissions have been applied successfully.

### Task 13: Create Azure Storage Account

1. In the **Azure Portal**, click **+ Create a resource**.

1. Search for **Storage account** and select it.

1. Click **Create**.

1. Configure Storage Account:

   - **Basics tab**:
      - **Subscription**: Select your available Azure subscription
      - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
      - **Storage account name**: **stsecureai<inject key="DeploymentID" enableCopy="false"/>**
      - **Region**: **<inject key="Region"></inject>**
      - **Performance**: **Standard**
      - **Redundancy**: **Locally-redundant storage (LRS)**

1. Click **Next**.

   - **Advanced tab**:
      - **Require secure transfer for REST API operations**: **Enabled** (should be checked)
      - **Allow enabling public access on containers**: **Disabled** (uncheck this!)
      - **Minimum TLS version**: **Version 1.2**

1. Click **Next**.

   - **Networking tab**:
      - **Public network access scope**: Select **Enable from all networks** (we'll restrict in Challenge 2)

1. Click **Review + Create**.

1. Click **Create**.

1. Wait for the deployment to complete; it will take a maximum of 1-2 minutes.

1. Once complete, click **Go to resource**.

### Task 14: Create Blob Container

1. In your **stsecureai<inject key="DeploymentID" enableCopy="false"/>** Storage Account.

1. In the left navigation, under **Data storage**, click **Containers**.

1. Click **+ Add container**.

1. Configure the container:

   - **Name**: **chat-sessions**

1. Click **Create**.

1. Verify the **chat-sessions** container appears in the list.

### Task 15: Verify All Resources

1. Navigate back to your resource group: **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**.

1. Verify you see the following resources:

   - **vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>** (Virtual network)

   - **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>** (Virtual machine)

1. In the left navigation, click **Subnets**.

1. Verify all three subnets exist:

   - snet-ai-services (10.0.1.0/24)
   - snet-storage-services (10.0.2.0/24)
   - snet-application (10.0.3.0/24)

### Task 16: Save Configuration Details

Open Notepad on your VM and document the following:

```
SECURE AI INFRASTRUCTURE – DEPLOYMENT SUMMARY
Connect to **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>** via Bastion, open Notepad, and document the following:

```

Deployment ID: <inject key="DeploymentID" enableCopy="false"/>
Region: <inject key="Region"></inject>

## Success Criteria

- Virtual Network created with three subnets (snet-ai-services, snet-storage-services, snet-application) and AzureBastionSubnet
- Windows VM deployed in the application subnet with no public IP
- Azure Bastion deployed and VM accessible via Bastion
- Required software installed on VM (Python 3.11, VS Code, Azure CLI)
- Azure AI Foundry project created with the GPT-4.1 model successfully deployed
- Custom domain configured on the Azure OpenAI resource
- Model tested in Chat Playground and working correctly
- Azure Key Vault created with RBAC authorization and Key Vault Administrator role assigned
- Azure Storage Account created with blob container (chat-sessions)
- All resources are deployed in the same resource group and region

## Additional Resources

- [Azure OpenAI in AI Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft Foundry Overview](https://learn.microsoft.com/azure/ai-studio/)
- [Azure Virtual Network](https://learn.microsoft.com/azure/virtual-network/virtual-networks-overview)
- [Azure Bastion](https://learn.microsoft.com/azure/bastion/bastion-overview)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/general/overview)

Now, click **Next** to continue to **Challenge 02**.
