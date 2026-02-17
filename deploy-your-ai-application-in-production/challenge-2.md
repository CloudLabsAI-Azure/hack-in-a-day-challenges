# Challenge 02: Configure Network Security & Isolation

## Introduction

Infrastructure is deployed, but is it truly secure? In this challenge, you'll harden your network security by configuring Network Security Groups (NSGs), disabling all public access, and validating that your AI services are completely isolated from the internet.

This is where enterprises fail most often - deploying services with default settings that allow public access. You'll learn to lock down your environment like a production system.

## Prerequisites

- Completed Challenge 1 (Infrastructure deployed via Azure Portal)
- Resource group `challenge-rg-<inject key="DeploymentID" enableCopy="false"/>` contains:
 - Virtual Network with subnets
  - Application VM (vm-<inject key="DeploymentID" enableCopy="false"/>)
  - Azure AI Foundry (includes OpenAI)
  - Storage Account
  - Key Vault
- Connected to **vm-<inject key="DeploymentID" enableCopy="false"/>** via Azure Bastion
- Configure Network Security Group (NSG) rules for AI services subnet
- Disable public network access on all AI services
- Configure subnet delegation for private endpoints
- Validate private endpoint connectivity
- Test that public access is completely blocked
- Verify DNS resolution for private endpoints

## Understanding Network Security Layers

Your security architecture has multiple layers:

```
+---------------------------------------------------------+
¦ Layer 1: Network Perimeter (VNET boundary) ¦
¦ - Only Azure Bastion allows inbound traffic ¦
¦ - No public IPs on any AI services ¦
+---------------------------------------------------------+
 ?
+---------------------------------------------------------+
¦ Layer 2: Subnet Isolation (NSG rules) ¦
¦ - ai-services subnet: AI Foundry, OpenAI ¦
¦ - storage-services subnet: Storage, Key Vault ¦
¦ - application subnet: Application VM (vm-DID) ¦
¦ - Each subnet has restrictive NSG rules ¦
+---------------------------------------------------------+
 ?
+---------------------------------------------------------+
¦ Layer 3: Service-Level Security ¦
¦ - Public network access: DISABLED ¦
¦ - Only private endpoint connections allowed ¦
¦ - Firewall rules block all public IPs ¦
+---------------------------------------------------------+
 ?
+---------------------------------------------------------+
¦ Layer 4: Identity & Access (Next Challenge) ¦
¦ - Managed identity authentication ¦
¦ - RBAC for least-privilege access ¦
+---------------------------------------------------------+
```

## Steps to Complete

### Part 1: Review Current Network Configuration

First, understand what was deployed.

1. **In Azure Portal**, navigate to your resource group: `challenge-rg-<inject key="DeploymentID" enableCopy="false"/>`

2. **Find the Virtual Network** (name: `vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>`)

3. Click on it, then click **Subnets** in the left menu

4. **Note the subnets created**:
 - `snet-ai-services` - For AI Foundry and OpenAI private endpoints
 - `snet-storage-services` - For Storage and Key Vault private endpoints
 - `snet-application` - For your application/VM

5. Click on **snet-ai-services** subnet

6. **Check if an NSG is attached**:
 - Look for "Network security group" field
 - If it says "None", you'll create one
 - If there's already one attached, note its name

### Part 2: Create Network Security Group for AI Services

Let's create an NSG with restrictive rules using the Azure Portal.

1. **In Azure Portal**, click **+ Create a resource**.

1. Search for **Network security group** and select it.

1. Click **Create**.

1. Configure the NSG:

 **Basics tab**:
 - **Subscription**: Select your available Azure subscription
 - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
 - **Name**: **nsg-ai-services**
 - **Region**: **<inject key="Region"></inject>**

1. Click **Review + Create**.

1. Click **Create**.

1. Wait for deployment (30 seconds).

1. Once complete, click **Go to resource**.

1. **Add security rules** for the NSG:

 Click **Inbound security rules** in the left menu, then click **+ Add** to add the first rule:
 
 **Allow Application Subnet Rule**:
 - **Source**: **IP Addresses**
 - **Source IP addresses/CIDR ranges**: **10.0.3.0/24**
 - **Source port ranges**: *****
 - **Destination**: **Any**
 - **Service**: **HTTPS**
 - **Destination port ranges**: **443** (auto-filled)
 - **Protocol**: **TCP** (auto-filled)
 - **Action**: **Allow**
 - **Priority**: **100**
 - **Name**: **AllowApplicationSubnet**
 - **Description**: **Allow HTTPS from application subnet**
 - Click **Add**

 Click **+ Add** again to add the second rule:
 
 **Allow Azure Services Rule**:
 - **Source**: **Service Tag**
 - **Source service tag**: **AzureCloud**
 - **Source port ranges**: *****
 - **Destination**: **Any**
 - **Service**: **HTTPS**
 - **Destination port ranges**: **443**
 - **Protocol**: **TCP**
 - **Action**: **Allow**
 - **Priority**: **110**
 - **Name**: **AllowAzureServices**
 - **Description**: **Allow Azure backend services**
 - Click **Add**

 Click **+ Add** again to add the deny rule:
 
 **Deny Internet Rule**:
 - **Source**: **Service Tag**
 - **Source service tag**: **Internet**
 - **Source port ranges**: *****
 - **Destination**: **Any**
 - **Service**: **Custom**
 - **Destination port ranges**: *****
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

### Part 3: Disable Public Access on AI Services

Now ensure no service accepts connections from the internet using the Azure Portal.

1. **Restrict network access on Azure AI Foundry**:

 **In Azure Portal**:
 - Navigate to your **openai-secureai-<inject key="DeploymentID" enableCopy="false"/>** resource
 - Click **Networking** in the left menu
 - Under **Firewalls and virtual networks**, select **Selected Networks and Private Endpoints**
 - Click **+ Add existing virtual network**
 
 **In the "Add networks" dialog**:
 - **Subscription**: Should already be selected (your current subscription)
 - **Virtual networks**: Check the box next to **vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>**
 - **Subnets**: Select all three subnets:
 - **snet-ai-services**
 - **snet-storage-services**
 - **snet-application**
 - Click **Add** at the bottom of the dialog
 
 **Back on the Networking page**:
 - Verify your VNet and subnets are listed under "Virtual networks"
 - Click **Save** at the top
 - Wait 1-2 minutes for the change to propagate

 > **What this does**: Restricts AI Foundry to only accept connections from your Virtual Network subnets, blocking all public internet access.

2. **Disable public access on Storage Account**:

 **In Azure Portal**:
 - Navigate to your **stsecureai<inject key="DeploymentID" enableCopy="false"/>** Storage Account
 - Click **Networking** in the left menu under Settings
 - Under **Public network access**, select **Disabled**
 - Click **Save**
 - Wait for the setting to apply (30 seconds)

3. **Disable public access on Key Vault**:

 **In Azure Portal**:
 - Navigate to your **kv-secureai-<inject key="DeploymentID" enableCopy="false"/>** Key Vault
 - Click **Networking** in the left menu under Settings
 - Under **Firewalls and virtual networks**, select **Disable public access**
 - Click **Apply**
 - Wait for the setting to apply (30 seconds)

### Part 4: Create Private Endpoint for Azure Key Vault

Now that public access is disabled, create a private endpoint to enable secure connectivity from your VNET.

1. **In Azure Portal**, navigate to your **kv-secureai-<inject key="DeploymentID" enableCopy="false"/>** Key Vault.

1. In the left navigation, click **Networking** ? **Private endpoint connections** tab.

1. Click **+ Create**.

1. Configure the private endpoint:

 **Basics tab**:
 - **Subscription**: Select your available Azure subscription
 - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
 - **Name**: **pe-keyvault-<inject key="DeploymentID" enableCopy="false"/>**
 - **Network Interface Name**: **nic-pe-keyvault-<inject key="DeploymentID" enableCopy="false"/>**
 - **Region**: **<inject key="Region"></inject>**
 - Click **Next: Resource**

 **Resource tab**:
 - **Connection method**: **Connect to an Azure resource in my directory**
 - **Subscription**: Should be pre-selected
 - **Resource type**: **Microsoft.KeyVault/vaults**
 - **Resource**: Select **kv-secureai-<inject key="DeploymentID" enableCopy="false"/>**
 - **Target sub-resource**: **vault** (should be selected automatically)
 - Click **Next: Virtual Network**

 **Virtual Network tab**:
 - **Virtual network**: Select **vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>**
 - **Subnet**: Select **snet-storage-services (10.0.2.0/24)**
 - **Private IP configuration**: **Dynamically allocate IP address**
 - **Application security group**: Leave blank
 - Click **Next: DNS**

 **DNS tab**:
 - **Integrate with private DNS zone**: **Yes**
 - **Subscription**: Should be pre-selected
 - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
 - **Private DNS zones**: Should show **privatelink.vaultcore.azure.net** (will be created if it doesn't exist)
 - Click **Next: Tags**

 **Tags tab**:
 - Leave blank
 - Click **Next: Review + create**

1. Click **Create**.

1. Wait for deployment (**1-2 minutes**).

1. Once complete, click **Go to resource** to view the private endpoint details.

1. **Note the private IP address** assigned (should be in 10.0.2.x range).

### Part 5: Create Private Endpoint for Azure OpenAI

Create a private endpoint for your OpenAI service to ensure all AI traffic stays within your VNET.

1. **In Azure Portal**, navigate to your **openai-secureai-<inject key="DeploymentID" enableCopy="false"/>** Azure AI Foundry resource.

1. In the left navigation, click **Networking** ? **Private endpoint connections** tab.

1. Click **+ Private endpoint**.

1. Configure the private endpoint:

 **Basics tab**:
 - **Subscription**: Select your available Azure subscription
 - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
 - **Name**: **pe-openai-<inject key="DeploymentID" enableCopy="false"/>**
 - **Network Interface Name**: **nic-pe-openai-<inject key="DeploymentID" enableCopy="false"/>**
 - **Region**: **<inject key="Region"></inject>**
 - Click **Next: Resource**

 **Resource tab**:
 - **Connection method**: **Connect to an Azure resource in my directory**
 - **Subscription**: Should be pre-selected
 - **Resource type**: **Microsoft.CognitiveServices/accounts**
 - **Resource**: Select **openai-secureai-<inject key="DeploymentID" enableCopy="false"/>**
 - **Target sub-resource**: **account** (should be selected automatically)
 - Click **Next: Virtual Network**

 **Virtual Network tab**:
 - **Virtual network**: Select **vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>**
 - **Subnet**: Select **snet-ai-services (10.0.1.0/24)**
 - **Private IP configuration**: **Dynamically allocate IP address**
 - **Application security group**: Leave blank
 - Click **Next: DNS**

 **DNS tab**:
 - **Integrate with private DNS zone**: **Yes**
 - **Subscription**: Should be pre-selected
 - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
 - **Private DNS zones**: Should show **privatelink.openai.azure.com** (will be created if it doesn't exist)
 - Click **Next: Tags**

 **Tags tab**:
 - Leave blank
 - Click **Next: Review + create**

1. Click **Create**.

1. Wait for deployment (**1-2 minutes**).

1. Once complete, click **Go to resource** to view the private endpoint details.

1. **Note the private IP address** assigned (should be in 10.0.1.x range).

### Part 6: Verify Private DNS Configuration

After creating private endpoints, verify that the Private DNS zones were created and linked to your VNET.

1. **In Azure Portal**, navigate to your resource group **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**.

1. Look for Private DNS zone resources (filter by type "Private DNS zone"):
   - **privatelink.vaultcore.azure.net**
   - **privatelink.openai.azure.com**

1. Click on **privatelink.vaultcore.azure.net**.

1. In the left navigation, click **Virtual network links**.

1. Verify that **vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>** is listed with **Link status: Completed**.

1. Click **Overview** in the left navigation.

1. Verify you see an **A record** pointing to the private IP (10.0.2.x) of your Key Vault.

1. **Repeat steps 3-7** for **privatelink.openai.azure.com** (should show A record to 10.0.1.x).

> **Why this matters**: Private DNS zones ensure that when your VM resolves names like `kv-secureai-<DID>.vault.azure.net`, it resolves to the private IP address instead of the public endpoint. This keeps all traffic within your VNET.

### Part 7: Validate Private Endpoint Connectivity (Using VS Code)

Ensure all services are reachable via private endpoints only. For this validation, we'll use VS Code on **vm-<inject key="DeploymentID" enableCopy="false"/>**.

> **Note**: Connect to **vm-<inject key="DeploymentID" enableCopy="false"/>** via Bastion, open VS Code, open a PowerShell terminal (Ctrl + `), and ensure you're logged in to Azure CLI (`az login`).

1. **List all private endpoints**:

 In VS Code PowerShell terminal:

```powershell
az network private-endpoint list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[].{Name:name, Subnet:subnet.id, State:privateLinkServiceConnections[0].privateLinkServiceConnectionState.status}" `
 --output table
```

All should show `State: Approved`

2. **Check private DNS zones**:

```powershell
az network private-dns zone list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[].name" `
 --output table
```

You should see zones like:
- `privatelink.openai.azure.com`
- `privatelink.vaultcore.azure.net`

3. **Verify VNET link for DNS zones**:

```powershell
$dnsZone = "privatelink.openai.azure.com"

az network private-dns link vnet list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --zone-name $dnsZone `
 --query "[].{Name:name, VNet:virtualNetwork.id, Status:registrationEnabled}" `
 --output table
```

The VNET should be linked to enable DNS resolution.

### Part 8: Test DNS Resolution for Private Endpoints (Using VS Code)

Verify that service names resolve to private IP addresses (not public). Continue using VS Code PowerShell terminal.

1. **Test OpenAI endpoint DNS resolution**:

```powershell
nslookup openai-secureai-<inject key="DeploymentID" enableCopy="false"/>.openai.azure.com
```

The returned IP should be in the `10.0.1.x` range (private), NOT a public IP!

Expected output:
```
Server:  UnKnown
Address:  168.63.129.16

Non-authoritative answer:
Name:    openai-secureai-<DID>.openai.azure.com
Address:  10.0.1.4
```

2. **Test Key Vault endpoint**:

```powershell
nslookup kv-secureai-<inject key="DeploymentID" enableCopy="false"/>.vault.azure.net
```

Expected private IP in `10.0.2.x` range.

3. **Test connectivity to Key Vault**:

```powershell
# Try to list secrets (you should get an access denied, but connection should work)
az keyvault secret list --vault-name kv-secureai-<inject key="DeploymentID" enableCopy="false"/>
```

If you see a permission error (not a network error), private endpoint is working!

### Part 9: Test Public Access is Blocked

Validate that trying to access services from the internet fails (security validation).

**From your local machine** (not the VM):

1. **Open PowerShell** on your local machine.

1. **Try to access Key Vault** from your local machine:

```powershell
az keyvault secret list --vault-name kv-secureai-<inject key="DeploymentID" enableCopy="false"/>
```

**Expected result**: Should fail with error:
```
(Forbidden) Public network access is disabled and request is not from a trusted service nor via an approved private link.
```

? **This is the desired behavior!** It proves your Key Vault is completely isolated from the internet.

3. **Test Storage Account**:

```powershell
nslookup "$storageName.blob.core.windows.net"
```

Should also return a private IP (`10.0.x.x`).

4. **Test Key Vault endpoint**:

```powershell
nslookup "$kvName.vault.azure.net"
```

Should return a private IP.

5. **If you get public IPs**, DNS is not properly configured. Check:
 - Private DNS zones are created
 - VNET is linked to the zones
 - Your VM's VNET DNS is using Azure-provided DNS (168.63.129.16)

### Part 6: Validate Public Access is Blocked

Let's prove that services are truly inaccessible from the internet.

1. **Try to access OpenAI from the internet** (this should fail):

Open your **local machine** browser (NOT the VM), and try to navigate to:

```
https://<your-openai-name>.openai.azure.com
```

You should get:
- **Error 403: Forbidden** or
- **Connection timeout** or 
- **This service is not accessible from this network**

This confirms public access is blocked!

2. **Try accessing Key Vault publicly** (should also fail):

```
https://<your-kv-name>.vault.azure.net
```

Should return an error - public access denied.

3. **Check Azure Portal indicators**:

- Go to your OpenAI resource in the portal
- Click **Networking** in left menu
- Under "Firewalls and virtual networks", it should show:
 - **Public network access**: Disabled (or Selected Networks)
 - **Private endpoint connections**: Approved

### Part 7: Create NSG for Storage Subnet (Using Portal)

Repeat NSG creation for the storage subnet using Azure Portal.

1. **In Azure Portal**, click **+ Create a resource**.

1. Search for **Network security group** and select it.

1. Click **Create**.

1. Configure the NSG:

 **Basics tab**:
 - **Subscription**: Select your available Azure subscription
 - **Resource group**: Select **challenge-rg-<inject key="DeploymentID" enableCopy="false"/>**
 - **Name**: **nsg-storage-services**
 - **Region**: **<inject key="Region"></inject>**

1. Click **Review + Create**, then **Create**.

1. Once complete, click **Go to resource**.

1. **Add security rules**:

 Click **Inbound security rules**, then **+ Add**:
 
 **Allow Application Subnet Rule**:
 - **Source**: **IP Addresses**
 - **Source IP addresses/CIDR ranges**: **10.0.3.0/24**
 - **Source port ranges**: *****
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

### Part 8: Document Your Network Configuration (Using VS Code)

Save your network topology for reference using VS Code PowerShell terminal.

1. **Create a network diagram document**:

```powershell
# Get VNET name
$vnetName = az network vnet list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[?contains(name, 'vnet')].name" -o tsv

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
- OpenAI: DISABLED
- Storage: DISABLED
- Key Vault: DISABLED

DNS Configuration:
- Private DNS zones created for all services
- VNET linked to DNS zones for resolution
- Services resolve to private IPs only

Security Posture: LOCKED DOWN
"@ | Out-File -FilePath "C:\LabFiles\network-config.txt"

Write-Host "Network configuration documented at C:\LabFiles\network-config.txt"
notepad C:\LabFiles\network-config.txt
```

## Success Criteria

Verify your network is fully secured:

- [ ] NSG `nsg-ai-services` created and attached to ai-services subnet
- [ ] NSG `nsg-storage-services` created and attached to storage-services subnet
- [ ] NSG rules allow traffic from application subnet to AI services on port 443
- [ ] NSG rules explicitly deny internet traffic
- [ ] Azure OpenAI public network access is DISABLED
- [ ] Storage Account public network access is DISABLED
- [ ] Key Vault public network access is DISABLED
- [ ] All private endpoints show status: Approved
- [ ] Private DNS zones exist for all services
- [ ] VNET is linked to all private DNS zones
- [ ] DNS resolution returns private IPs (10.0.x.x) not public IPs
- [ ] Accessing services from public internet is BLOCKED (403/timeout errors)
- [ ] Network configuration documented in `network-config.txt`

## Troubleshooting

### Issue: NSG creation fails

**Solution**:
- Ensure you're using the correct resource group name
- Verify the location matches your VNET region
- Check if an NSG with the same name already exists in the portal
- Navigate to Resource Groups ? Network security groups to verify

---

### Issue: DNS still resolves to public IPs

**Solution**:
- Check VM's DNS settings. It should use Azure DNS (168.63.129.16)
- In Azure Portal, verify private DNS zones are linked to your VNET:
 - Go to Private DNS zones
 - Select each zone
 - Check Virtual network links
- Flush DNS cache on the VM using VS Code PowerShell terminal:
 ```powershell
 Clear-DnsClientCache
 ipconfig /flushdns
 ```

---

### Issue: Can't disable public access on a service

**Solution**:
- Ensure private endpoint is successfully created first
- Check the service supports disabling public access
- Try using Azure Portal Networking settings
- Wait 2-3 minutes and try again

---

### Issue: Private endpoint shows "Pending" status

**Solution**:
- Private endpoint approval is automatic for same-subscription deployments
- If stuck, delete and recreate using Azure Portal:
 - Go to Private endpoints
 - Delete the pending endpoint
 - Recreate from the service's Networking blade

---

### Issue: Services unreachable even from VM

**Solution**:
- Verify NSG rules allow traffic on port 443 in Azure Portal
- Check private endpoint is in "Approved" state
- Ensure VM is in the correct subnet (snet-application)
- Test connectivity using VS Code PowerShell terminal:
 ```powershell
 Test-NetConnection -ComputerName "$openaiName.openai.azure.com" -Port 443
 ```

## Bonus Challenges

1. **Create NSG Flow Logs**:
 - Enable NSG flow logs to monitor traffic patterns
 - Store logs in your storage account
 - Analyze allowed/denied traffic

2. **Implement Service Tags**:
 - Replace IP-based rules with Azure service tags
 - Use `AzureAI`, `AzureMonitor` tags for more granular control

3. **Configure Application Security Groups**:
 - Create ASGs for logical grouping (AI services, storage services)
 - Use ASGs in NSG rules instead of IP addresses

4. **Test Port Scanning**:
 - From your VM, scan the private endpoint IPs
 - Verify only port 443 is open
 ```powershell
 Test-NetConnection -ComputerName "10.0.1.4" -Port 443
 Test-NetConnection -ComputerName "10.0.1.4" -Port 80 # Should fail
 ```

## What You Learned

In this challenge, you:

Created and configured Network Security Groups with restrictive rules 
Disabled public network access on all AI services 
Validated private endpoint connectivity and approval 
Configured private DNS zones for name resolution 
Tested and verified complete internet isolation 
Implemented defense-in-depth network security 
Documented your network topology 

Your AI environment is now completely isolated from the internet with multiple security layers!

## Next Steps

Network security: COMPLETE!

In **Challenge 3**, you'll configure identity and access management using Entra ID, managed identities, and RBAC to ensure only authorized identities can access your services.

Head to **challenge-3.md** to continue!

---

**Security Reminder**: In production, regularly audit NSG rules, review flow logs, and test private connectivity to ensure the network remains secure over time.
