# Challenge 02: Configure Network Security & Isolation

## Introduction

Infrastructure is deployed, but is it truly secure? In this challenge, you will harden your network security by configuring Network Security Groups (NSGs), disabling all public access, and validating that your AI services are completely isolated from the internet.

This is where enterprises fail most often deploying services with default settings that allow public access. You will learn to lock down your environment like a production system.

## Prerequisites

- Completed Challenge 1 (Infrastructure deployed via Azure Portal)
- Resource group **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>** contains:
   - Virtual Network with subnets
   - Application VM (Hack-vm-<inject key="DeploymentID" enableCopy="false"/>)
   - Azure AI Foundry (includes OpenAI)
   - Storage Account
   - Key Vault
- Connected to **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>** via Azure Bastion
- Configure Network Security Group (NSG) rules for the AI services subnet
- Disable public network access on all AI services
- Configure subnet delegation for private endpoints
- Validate private endpoint connectivity
- Test that public access is completely blocked
- Verify DNS resolution for private endpoints

## Steps to Complete

### Task 1: Create Network Security Group for AI Services

Let's create an NSG with restrictive rules using the Azure Portal.

1. **In Azure Portal**, click **+ Create a resource**.

1. Search for **Network security group** and select it.

1. Click **Create**.

1. Configure the NSG:

   - **Basics tab**:
      - **Subscription**: Select your available Azure subscription
      - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
      - **Name**: **nsg-ai-services**
      - **Region**: **<inject key="Region"></inject>**

1. Click **Review + Create**.

1. Click **Create**.

1. Wait for the deployment to complete; it will take a maximum of 30 seconds.

1. Once complete, click **Go to resource**.

1. **Add security rules** for the NSG, select **Settings** from the left navigation menu:

   - Click **Inbound security rules** in the left menu, then click **+ Add** to add the first rule:
   
   - On the **Add inbound security rule**, add the following:
      - **Source**: **IP Addresses**
      - **Source IP addresses/CIDR ranges**: **10.0.3.0/24**
      - **Source port ranges**: *
      - **Destination**: **Any**
      - **Service**: **HTTPS**
      - **Destination port ranges**: **443** (auto-filled)
      - **Protocol**: **TCP** (auto-filled)
      - **Action**: **Allow**
      - **Priority**: **100**
      - **Name**: **AllowApplicationSubnet**
      - **Description**: **Allow HTTPS from application subnet**
      - Click **Add**

   - Click **+ Add** again to add the second rule:
   
   - **Allow VNet Services Rule**:
      - **Source**: **Service Tag**
      - **Source service tag**: **VirtualNetwork**
      - **Source port ranges**: *
      - **Destination**: **Any**
      - **Service**: **HTTPS**
      - **Destination port ranges**: **443**
      - **Protocol**: **TCP**
      - **Action**: **Allow**
      - **Priority**: **110**
      - **Name**: **AllowVNetServices**
      - **Description**: **Allow HTTPS from virtual network**
      - Click **Add**

   - Click **+ Add** again to add the deny rule:
   
   - **Deny Internet Rule**:
      - **Source**: **Service Tag**
      - **Source service tag**: **Internet**
      - **Source port ranges**: *
      - **Destination**: **Any**
      - **Service**: **Custom**
      - **Destination port ranges**: *
      - **Protocol**: **Any**
      - **Action**: **Deny**
      - **Priority**: **4000**
      - **Name**: **DenyInternet**
      - **Description**: **Deny all inbound from internet**
      - Click **Add**

1. **Attach NSG to the ai-services subnet**:

   - Click **Subnets** in the left menu (under Settings)
   - Click **+ Associate**
   - **Virtual network**: Select **vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>**
   - **Subnet**: Select **snet-ai-services**
   - Click **OK**

### Task 2: Disable Public Access on AI Services

Now ensure no service accepts connections from the internet using the Azure Portal.

1. **Restrict network access on Azure AI Foundry**:

   - **In Azure Portal** navigate to your **openai-secureai-<inject key="DeploymentID" enableCopy="false"/>** resource
      - Click **Networking** from the left menu under **Resource Management**.
      - Under **Firewalls and virtual networks**, choose **Selected Networks and Private Endpoints**
      - Click **+ Add existing virtual network**
   
   - **In the "Add networks" dialog**:
      - **Subscription**: Should already be selected (your current subscription)
      - **Virtual networks**: Check the box next to **vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>**
      - **Subnets**: Select all three subnets:
         - **snet-ai-services**
         - **snet-storage-services**
         - **snet-application**
      - Click **Enable** at the bottom of the dialog
      - Click **Add**
   
   - **Back on the Networking page**:

      - Verify your VNet and subnets are listed under "Virtual networks"
      - Click **Save** at the top
      - Wait 1-2 minutes for the change to propagate

         > **What this does**: Restricts AI Foundry to only accept connections from your Virtual Network subnets, blocking all public internet access.

2. **Disable public access on Storage Account**:

   - **In Azure Portal** navigate to your **stsecureai<inject key="DeploymentID" enableCopy="false"/>** Storage Account
      - Click **Networking** in the left menu under **Security + networking**
      - Under **Public network access**, select **Manage**
      - On the **Public network access** select **Disable**. Select **Proceed** on the **Disabling public network access** pop-up.
      - Click **Save**
      - Wait for the deployment to complete; it will take a maximum of 30 seconds.

3. **Disable public access on Key Vault**:

   - **In Azure Portal** navigate to your **kv-secureai-<inject key="DeploymentID" enableCopy="false"/>** key Vault.
      - Click **Networking** in the left menu under Settings
      - Under **Firewalls and virtual networks**, select **Disable public access**
      - Click **Apply**

### Task 3: Create Private Endpoint for Azure Key Vault

Now that public access is disabled, create a private endpoint to enable secure connectivity from your VNet.

1. **In Azure Portal**, navigate to your **kv-secureai-<inject key="DeploymentID" enableCopy="false"/>** Key Vault.

1. In the left navigation, under **Settings** click **Networking** → **Private endpoint connections** tab.

1. Click **+ Create**.

1. Configure the private endpoint:

   - **Basics tab**:
      - **Subscription**: Select your available Azure subscription
      - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
      - **Name**: **pe-keyvault-<inject key="DeploymentID" enableCopy="false"/>**
      - **Network Interface Name**: **nic-pe-keyvault-<inject key="DeploymentID" enableCopy="false"/>**
      - **Region**: **<inject key="Region"></inject>**
      - Click **Next: Resource**

   - **Resource tab**:
      - **Connection method**: **Connect to an Azure resource in my directory**
      - **Subscription**: Should be pre-selected
      - **Resource type**: **Microsoft.KeyVault/vaults**
      - **Resource**: Select **kv-secureai-<inject key="DeploymentID" enableCopy="false"/>**
      - **Target sub-resource**: **vault** (should be selected automatically)
      - Click **Next: Virtual Network**

   - **Virtual Network tab**:
      - **Virtual network**: Select **vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>**
      - **Subnet**: Select **snet-storage-services (10.0.2.0/24)**
      - **Private IP configuration**: **Dynamically allocate IP address**
      - **Application security group**: Leave blank
      - Click **Next: DNS**

   - **DNS tab**:
      - **Integrate with private DNS zone**: **Yes**
      - **Subscription**: Should be pre-selected
      - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
      - **Private DNS zones**: Should show **privatelink.vaultcore.azure.net** (will be created if it doesn't exist)
      - Click **Next: Tags**

   - **Tags tab**:
      - Leave blank
      - Click **Next: Review + create**

1. Click **Create**.

1. Wait for the deployment to complete; it will take a maximum of **1-2 minutes**.

1. Once complete, click **Go to resource** to view the private endpoint details.

1. From the left select **DNS configuration**. **Note the private IP address** assigned (should be in 10.0.2.x range).

### Task 4: Create Private Endpoint for Azure OpenAI

Create a private endpoint for your OpenAI service to ensure all AI traffic stays within your VNET.

1. **In Azure Portal**, navigate to your **openai-secureai-<inject key="DeploymentID" enableCopy="false"/>** Azure AI Foundry resource.

1. In the left navigation, click **Resource Management** → **Networking** → **Private endpoint connections** tab.

1. Click **+ Private endpoint**.

1. Configure the private endpoint:

   - **Basics tab**:
      - **Subscription**: Select your available Azure subscription
      - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
      - **Name**: **pe-openai-<inject key="DeploymentID" enableCopy="false"/>**
      - **Network Interface Name**: **nic-pe-openai-<inject key="DeploymentID" enableCopy="false"/>**
      - **Region**: **<inject key="Region"></inject>**
      - Click **Next: Resource**

   - **Resource tab**:
      - **Connection method**: **Connect to an Azure resource in my directory**
      - **Subscription**: Should be pre-selected
      - **Resource type**: **Microsoft.CognitiveServices/accounts**
      - **Resource**: Select **openai-secureai-<inject key="DeploymentID" enableCopy="false"/>**
      - **Target sub-resource**: **account** (should be selected automatically)
      - Click **Next: Virtual Network**

   - **Virtual Network tab**:
      - **Virtual network**: Select **vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>**
      - **Subnet**: Select **snet-ai-services (10.0.1.0/24)**
      - **Private IP configuration**: **Dynamically allocate IP address**
      - **Application security group**: Leave blank
      - Click **Next: DNS**

   - **DNS tab**:
      - **Integrate with private DNS zone**: **Yes**
      - **Subscription**: Should be pre-selected
      - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
      - **Private DNS zones**: Should show **privatelink.openai.azure.com** (will be created if it doesn't exist)
      - Click **Next: Tags**

   - **Tags tab**:
      - Leave blank
      - Click **Next: Review + create**

1. Click **Create**.

1. Wait for the deployment to complete; it will take a maximum of **1-2 minutes**.

1. Once complete, click **Go to resource** to view the private endpoint details.

1. From the left select **DNS configuration**. **Note the private IP address** assigned (should be in 10.0.1.x range).

### Task 5: Create Private Endpoint for Azure Storage Account

Create a private endpoint for your Storage Account so that blob storage traffic stays within your VNET.

1. **In Azure Portal**, navigate to your **stsecureai<inject key="DeploymentID" enableCopy="false"/>** Storage Account.

1. In the left navigation, click **Networking** → **Private endpoint connections** tab.

1. Click **+ Create private endpoint**.

1. Configure the private endpoint:

   - **Basics tab**:
      - **Subscription**: Select your available Azure subscription
      - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
      - **Name**: **pe-storage-<inject key="DeploymentID" enableCopy="false"/>**
      - **Network Interface Name**: **nic-pe-storage-<inject key="DeploymentID" enableCopy="false"/>**
      - **Region**: **<inject key="Region"></inject>**
      - Click **Next: Resource**

   - **Resource tab**:
      - **Connection method**: **Connect to an Azure resource in my directory**
      - **Subscription**: Should be pre-selected
      - **Resource type**: **Microsoft.Storage/storageAccounts**
      - **Resource**: Select **stsecureai<inject key="DeploymentID" enableCopy="false"/>**
      - **Target sub-resource**: **blob**
      - Click **Next: Virtual Network**

   - **Virtual Network tab**:
      - **Virtual network**: Select **vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>**
      - **Subnet**: Select **snet-storage-services (10.0.2.0/24)**
      - **Private IP configuration**: **Dynamically allocate IP address**
      - **Application security group**: Leave blank
      - Click **Next: DNS**

   - **DNS tab**:
      - **Integrate with private DNS zone**: **Yes**
      - **Subscription**: Should be pre-selected
      - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
      - **Private DNS zones**: Should show **3** DNS zones.
      - Click **Next: Tags**

   - **Tags tab**:
      - Leave blank
      - Click **Next: Review + create**

1. Click **Create**.

1. Wait for the deployment to complete; it will take a maximum of **1-2 minutes**.

1. Once complete, click **Go to resource** to view the private endpoint details.

1. From the left, select **DNS configuration**. **Note the private IP address** assigned (should be in 10.0.2.x range).

### Task 6: Validate Private Endpoint Connectivity (Using VS Code)

Ensure all services are reachable via private endpoints only. For this validation, we'll use VS Code on **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>**.

1. Connect to **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>** via Bastion, open VS Code, open a PowerShell terminal (`Ctrl+J`), and ensure you're logged in to Azure CLI (`az login`).

1. **List all private endpoints**:

   - In VS Code PowerShell terminal:

      ```powershell
      az network private-endpoint list `
      --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
      --query "[].{Name:name, Subnet:subnet.id, State:privateLinkServiceConnections[0].privateLinkServiceConnectionState.status}" `
      --output table
      ```

   - All should show `State: Approved`

2. **Check private DNS zones**:

   ```powershell
   az network private-dns zone list `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query "[].name" `
   --output table
   ```

1. You should see zones like:

- `privatelink.openai.azure.com`
- `privatelink.vaultcore.azure.net`
- `privatelink.blob.core.windows.net`

3. **Verify VNET link for DNS zones**:

   ```powershell
   $dnsZone = "privatelink.openai.azure.com"

   az network private-dns link vnet list `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --zone-name $dnsZone `
   --query "[].{Name:name, VNet:virtualNetwork.id, Status:registrationEnabled}" `
   --output table
   ```

The VNet should be linked to enable DNS resolution.

### Task 7: Test DNS Resolution for Private Endpoints (Using VS Code)

Verify that service names resolve to private IP addresses (not public). Continue using VS Code PowerShell terminal.

1. **Test OpenAI endpoint DNS resolution**:

   ```powershell
   nslookup openai-secureai-<inject key="DeploymentID" enableCopy="false"/>.openai.azure.com
   ```

   - The returned IP should be in the `10.0.1.x` range (private), not a public IP.

   - Expected output:
      ```
      Server:  UnKnown
      Address:  168.63.129.16

      Non-authoritative answer:
      Name:    openai-secureai-<inject key="DeploymentID" enableCopy="false"/>.openai.azure.com
      Address:  10.0.1.4
      ```

2. **Test Key Vault endpoint**:

   ```powershell
   nslookup kv-secureai-<inject key="DeploymentID" enableCopy="false"/>.vault.azure.net
   ```

   - Expected private IP in `10.0.2.x` range.

3. **Test Storage Account endpoint**:

   ```powershell
   nslookup stsecureai<inject key="DeploymentID" enableCopy="false"/>.blob.core.windows.net
   ```

   - Expected private IP in `10.0.2.x` range.

4. **Test connectivity to Key Vault**:

   ```powershell
   # Try to list secrets (you should get an access denied, but connection should work)
   az keyvault secret list --vault-name kv-secureai-<inject key="DeploymentID" enableCopy="false"/>
   ```

   - If you see a permission error (not a network error), the private endpoint is working!

> **Note:** If the output returns an empty list `[]`, that's completely expected; no secrets have been added to the Key Vault yet. The important thing is that the command didn't return a network error, which confirms that private endpoint connectivity to Key Vault is working correctly.

### Task 8: Validate Public Access is Blocked

Verify that your services are properly locked down by checking network settings in the Azure Portal.

1. **Verify Azure OpenAI network settings**:

   - In Azure Portal, navigate to **openai-secureai-<inject key="DeploymentID" enableCopy="false"/>**
   - Click **Networking** in the left menu
   - Under **Firewalls and virtual networks**, confirm:
     - **Public network access**: **Selected Networks and Private Endpoints** (only your VNET is listed)
     - Under **Private endpoint connections** tab: private endpoint shows **Approved**

2. **Verify Storage Account network settings**:

   - Navigate to **stsecureai<inject key="DeploymentID" enableCopy="false"/>**
   - Click **Networking** in the left menu
   - Confirm **Public network access** is set to **Disabled**
   - Under **Private endpoint** tab: private endpoint shows **Approved**

3. **Verify Key Vault network settings**:

   - Navigate to **kv-secureai-<inject key="DeploymentID" enableCopy="false"/>**
   - Click **Networking** in the left menu
   - Confirm **Public network access** is set to **Disabled**
   - Under **Private endpoint** tab: private endpoint shows **Approved**

4. **Test public access is blocked** (optional):

   Open a browser on your **local machine** (NOT the VM) and navigate to:

   ```
   https://openai-secureai-<inject key="DeploymentID" enableCopy="false"/>.openai.azure.com
   ```

   - You should get **Error 403: Forbidden** or **Connection timeout** — This confirms that public access is blocked.

### Task 9: Create NSG for Storage Subnet (Using Portal)

Repeat NSG creation for the storage subnet using Azure Portal.

1. **In Azure Portal**, click **+ Create a resource**.

1. Search for **Network security group** and select it.

1. Click **Create**.

1. Configure the NSG:

   - **Basics tab**:
      - **Subscription**: Select your available Azure subscription
      - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
      - **Name**: **nsg-storage-services**
      - **Region**: **<inject key="Region"></inject>**

1. Click **Review + Create**, then **Create**.

1. Once complete, click **Go to resource**.

1. **Add security rules**:

   - From the left navigation menu, under **Settings**, click **Inbound security rules**, then **+ Add**:
   
      - **Allow Application Subnet Rule**:
         - **Source**: **IP Addresses**
         - **Source IP addresses/CIDR ranges**: **10.0.3.0/24**
         - **Source port ranges**: *
         - **Destination**: **Any**
         - **Service**: **HTTPS**
         - **Destination port ranges**: **443**
         - **Protocol**: **TCP**
         - **Action**: **Allow**
         - **Priority**: **100**
         - **Name**: **AllowApplicationSubnet**
         - **Description**: **Allow HTTPS from application subnet**
         - Click **Add**

1. **Attach NSG to subnet**:

   - Click **Subnets** in the left menu
   - Click **+ Associate**
   - **Virtual network**: Select **vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>**
   - **Subnet**: Select **snet-storage-services**
   - Click **OK**

### Task 10: Document Your Network Configuration (Using VS Code)

Save your network topology for reference using VS Code PowerShell terminal.

1. **Create a network diagram document**:

   ```powershell
   # Get resource names
   $vnetName = az network vnet list `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query "[?contains(name, 'vnet')].name" -o tsv

   $openaiName = "openai-secureai-<inject key="DeploymentID" enableCopy="false"/>"
   $storageName = "stsecureai<inject key="DeploymentID" enableCopy="false"/>"
   $kvName = "kv-secureai-<inject key="DeploymentID" enableCopy="false"/>"

   # Create documentation
   @"
   === Secure AI Network Configuration ===
   Date: $(Get-Date)

   VNET Name: $vnetName
   Address Space: 10.0.0.0/16

   Subnets:
   - snet-ai-services: 10.0.1.0/24 (NSG: nsg-ai-services)
   - snet-storage-services: 10.0.2.0/24 (NSG: nsg-storage-services)
   - snet-application: 10.0.3.0/24

   Private Endpoints:
   - OpenAI: $openaiName (Private IP in ai-services subnet)
   - Storage: $storageName (Private IP in storage-services subnet)
   - Key Vault: $kvName (Private IP in storage-services subnet)

   Public Access Status:
   - OpenAI: Selected Networks (VNET only)
   - Storage: DISABLED
   - Key Vault: DISABLED

   DNS Configuration:
   - Private DNS zones created for all services
   - VNET linked to DNS zones for resolution
   - Services resolve to private IPs only

   Security Posture: LOCKED DOWN
   "@ | Out-File -FilePath "C:\Code\network-config.txt"

   Write-Host "Network configuration documented at C:\Code\network-config.txt"
   notepad C:\Code\network-config.txt
   ```

## Success Criteria

Verify your network is fully secured:

- NSG `nsg-ai-services` created and attached to ai-services subnet
- NSG `nsg-storage-services` created and attached to storage-services subnet
- NSG rules allow traffic from application subnet to AI services on port 443
- NSG rules explicitly deny Internet traffic
- Azure OpenAI public network access is disabled
- Storage Account public network access is disabled
- Key Vault public network access is disabled
- All private endpoints show status: Approved
- Private DNS zones exist for all services
- VNET is linked to all private DNS zones
- DNS resolution returns private IPs (10.0.x.x) not public IPs
- Accessing services from public internet is BLOCKED (403/timeout errors)
- Private endpoint for Storage Account created and approved
- Network configuration documented in `network-config.txt`

## Additional Resources

- [Azure Network Security Groups](https://learn.microsoft.com/azure/virtual-network/network-security-groups-overview)
- [Azure Private Endpoints](https://learn.microsoft.com/azure/private-link/private-endpoint-overview)
- [Azure Private DNS Zones](https://learn.microsoft.com/azure/dns/private-dns-overview)
- [Azure OpenAI Network Security](https://learn.microsoft.com/azure/ai-services/openai/how-to/managed-identity)

Now, click **Next** to continue to **Challenge 03**.
