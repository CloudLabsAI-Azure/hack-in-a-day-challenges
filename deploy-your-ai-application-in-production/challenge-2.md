# Challenge 02: Configure Network Security & Isolation

## Introduction

Infrastructure is deployed, but is it truly secure? In this challenge, you'll harden your network security by configuring Network Security Groups (NSGs), disabling all public access, and validating that your AI services are completely isolated from the internet.

This is where enterprises fail most often - deploying services with default settings that allow public access. You'll learn to lock down your environment like a production system.

## Prerequisites

- Completed Challenge 1 (Infrastructure deployed via Azure Portal)
- Resource group `challenge-rg-<inject key="DeploymentID"></inject>` contains:
  - Virtual Network with subnets
  - Azure AI Foundry (includes OpenAI)
  - Storage Account
  - Key Vault
- Azure Bastion connectivity (pre-deployed)
- Azure Cloud Shell or VM with Azure CLI

## Challenge Objectives

- Configure Network Security Group (NSG) rules for AI services subnet
- Disable public network access on all AI services
- Configure subnet delegation for private endpoints
- Validate private endpoint connectivity
- Test that public access is completely blocked
- Verify DNS resolution for private endpoints

## Understanding Network Security Layers

Your security architecture has multiple layers:

```
┌─────────────────────────────────────────────────────────┐
│  Layer 1: Network Perimeter (VNET boundary)             │
│  - Only Azure Bastion allows inbound traffic            │
│  - No public IPs on any AI services                     │
└─────────────────────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────────────────────┐
│  Layer 2: Subnet Isolation (NSG rules)                  │
│  - ai-services subnet: AI Foundry, OpenAI               │
│  - storage-services subnet: Storage, Key Vault          │
│  - application subnet: Your VM                          │
│  - Each subnet has restrictive NSG rules                │
└─────────────────────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────────────────────┐
│  Layer 3: Service-Level Security                        │
│  - Public network access: DISABLED                      │
│  - Only private endpoint connections allowed            │
│  - Firewall rules block all public IPs                  │
└─────────────────────────────────────────────────────────┘
           ↓
┌─────────────────────────────────────────────────────────┐
│  Layer 4: Identity & Access (Next Challenge)            │
│  - Managed identity authentication                      │
│  - RBAC for least-privilege access                      │
└─────────────────────────────────────────────────────────┘
```

## Steps to Complete

### Part 1: Review Current Network Configuration

First, understand what was deployed.

1. **In Azure Portal**, navigate to your resource group: `challenge-rg-<inject key="DeploymentID"></inject>`

2. **Find the Virtual Network** (name: `vnet-secureai-<inject key="DeploymentID"></inject>`)

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

Let's create an NSG with restrictive rules.

1. **In Azure Cloud Shell or your VM terminal**, create an NSG:

> **Critical**: The NSG must be created in the **exact same region** as your Virtual Network from Challenge 1. If you get an error about resource not found, check that both resources are in the same region.

```powershell
az network nsg create `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --name "nsg-ai-services" `
  --location "<inject key="Region"></inject>"
```

2. **Add a rule to allow traffic from the application subnet** (your VM needs to reach AI services):

```powershell
az network nsg rule create `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --nsg-name "nsg-ai-services" `
  --name "AllowApplicationSubnet" `
  --priority 100 `
  --source-address-prefixes "10.0.3.0/24" `
  --source-port-ranges "*" `
  --destination-address-prefixes "*" `
  --destination-port-ranges "443" `
  --access "Allow" `
  --protocol "Tcp" `
  --description "Allow HTTPS from application subnet"
```

3. **Add rule to allow Azure services** (AI Foundry needs to communicate with backend services):

```powershell
az network nsg rule create `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --nsg-name "nsg-ai-services" `
  --name "AllowAzureServices" `
  --priority 110 `
  --source-address-prefixes "AzureCloud" `
  --source-port-ranges "*" `
  --destination-address-prefixes "*" `
  --destination-port-ranges "443" `
  --access "Allow" `
  --protocol "Tcp" `
  --description "Allow Azure backend services"
```

4. **Add explicit deny rule for internet** (defense in depth):

```powershell
az network nsg rule create `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --nsg-name "nsg-ai-services" `
  --name "DenyInternet" `
  --priority 4000 `
  --source-address-prefixes "Internet" `
  --source-port-ranges "*" `
  --destination-address-prefixes "*" `
  --destination-port-ranges "*" `
  --access "Deny" `
  --protocol "*" `
  --description "Deny all inbound from internet"
```

5. **Attach NSG to ai-services subnet**:

First, get the VNET name:

```powershell
$vnetName = az network vnet list `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --query "[?contains(name, 'vnet')].name" -o tsv

Write-Host "VNET Name: $vnetName"
```

Then attach the NSG:

```powershell
az network vnet subnet update `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --vnet-name $vnetName `
  --name "snet-ai-services" `
  --network-security-group "nsg-ai-services"
```

### Part 3: Disable Public Access on AI Services

Now ensure no service accepts connections from the internet.

1. **Restrict network access on Azure AI Foundry**:

   > **Note**: The Azure CLI doesn't yet support network configuration for AI Foundry. Use the Azure Portal instead.

   **In Azure Portal**:
   - Navigate to your **openai-secureai-<inject key="DeploymentID"></inject>** resource
   - Click **Networking** in the left menu
   - Under **Firewalls and virtual networks**, select **Selected Networks and Private Endpoints**
   - Click **+ Add existing virtual network**
   
   **In the "Add networks" dialog**:
   - **Subscription**: Should already be selected (your current subscription)
   - **Virtual networks**: Check the box next to **vnet-secureai-<inject key="DeploymentID"></inject>**
   - **Subnets**: Select all three subnets:
     - ✅ **snet-ai-services**
     - ✅ **snet-storage-services**
     - ✅ **snet-application**
   - Click **Add** at the bottom of the dialog
   
   **Back on the Networking page**:
   - Verify your VNet and subnets are listed under "Virtual networks"
   - Click **Save** at the top
   - Wait 1-2 minutes for the change to propagate

   > **What this does**: Restricts AI Foundry to only accept connections from your Virtual Network subnets, blocking all public internet access.

2. **Disable public access on Storage Account**:

Get storage account name:

```powershell
$storageName = az storage account list `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --query "[?contains(name, 'st')].name" -o tsv

Write-Host "Storage Account: $storageName"
```

Disable public access:

```powershell
az storage account update `
  --name $storageName `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --public-network-access Disabled
```

3. **Disable public access on Key Vault**:

Get Key Vault name:

```powershell
$kvName = az keyvault list `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --query "[?contains(name, 'kv')].name" -o tsv

Write-Host "Key Vault: $kvName"
```

Disable public access:

```powershell
az keyvault update `
  --name $kvName `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --public-network-access Disabled
```

### Part 4: Validate Private Endpoint Connectivity

Ensure all services are reachable via private endpoints only.

1. **List all private endpoints**:

```powershell
az network private-endpoint list `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --query "[].{Name:name, Subnet:subnet.id, State:privateLinkServiceConnections[0].privateLinkServiceConnectionState.status}" `
  --output table
```

All should show `State: Approved`

2. **Check private DNS zones**:

```powershell
az network private-dns zone list `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --query "[].name" `
  --output table
```

You should see zones like:
- `privatelink.openai.azure.com`
- `privatelink.blob.core.windows.net`
- `privatelink.vaultcore.azure.net`
- `privatelink.api.azureml.ms`

3. **Verify VNET link for DNS zones**:

```powershell
$dnsZone = "privatelink.openai.azure.com"

az network private-dns link vnet list `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --zone-name $dnsZone `
  --query "[].{Name:name, VNet:virtualNetwork.id, Status:registrationEnabled}" `
  --output table
```

The VNET should be linked to enable DNS resolution.

### Part 5: Test DNS Resolution for Private Endpoints

Verify that service names resolve to private IP addresses (not public).

1. **Test OpenAI endpoint DNS resolution**:

```powershell
nslookup "$openaiName.openai.azure.com"
```

The returned IP should be in the `10.0.x.x` range (private), NOT a public IP!

2. **Test Storage endpoint**:

```powershell
nslookup "$storageName.blob.core.windows.net"
```

Should also return a private IP (`10.0.x.x`).

3. **Test Key Vault endpoint**:

```powershell
nslookup "$kvName.vault.azure.net"
```

Should return a private IP.

4. **If you get public IPs**, DNS is not properly configured. Check:
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

This confirms public access is blocked! ✅

2. **Try accessing Key Vault publicly** (should also fail):

```
https://<your-kv-name>.vault.azure.net
```

Should return an error - public access denied.

3. **Check Azure Portal indicators**:

- Go to your OpenAI resource in the portal
- Click **Networking** in left menu
- Under "Firewalls and virtual networks", it should show:
  - **Public network access**: Disabled
  - **Private endpoint connections**: Approved

### Part 7: Configure NSG for Storage Subnet

Repeat NSG creation for the storage subnet.

1. **Create NSG for storage services**:

```powershell
az network nsg create `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --name "nsg-storage-services" `
  --location "<inject key="Region"></inject>"
```

2. **Add allow rule for application subnet**:

```powershell
az network nsg rule create `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --nsg-name "nsg-storage-services" `
  --name "AllowApplicationSubnet" `
  --priority 100 `
  --source-address-prefixes "10.0.3.0/24" `
  --destination-address-prefixes "*" `
  --destination-port-ranges "443" `
  --access "Allow" `
  --protocol "Tcp"
```

3. **Attach to subnet**:

```powershell
az network vnet subnet update `
  --resource-group "challenge-rg-<inject key="DeploymentID"></inject>" `
  --vnet-name $vnetName `
  --name "storage-services" `
  --network-security-group "nsg-storage-services"
```

### Part 8: Document Your Network Configuration

Save your network topology for reference.

1. **Create a network diagram document**:

```powershell
@"
=== Secure AI Network Configuration ===
Date: $(Get-Date)

VNET Name: $vnetName
Address Space: 10.0.0.0/16

Subnets:
- ai-services: 10.0.1.0/24 (NSG: nsg-ai-services)
- storage-services: 10.0.2.0/24 (NSG: nsg-storage-services)
- application: 10.0.3.0/24

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

Security Posture: LOCKED DOWN ✅
"@ | Out-File -FilePath "C:\LabFiles\network-config.txt"

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
- Check if an NSG with the same name already exists:
  ```powershell
  az network nsg list -g "challenge-rg-<inject key="DeploymentID"></inject>" -o table
  ```

---

### Issue: DNS still resolves to public IPs

**Solution**:
- Check VM's DNS settings. It should use Azure DNS (168.63.129.16)
- Verify private DNS zones are linked to your VNET:
  ```powershell
  az network private-dns link vnet list -g "challenge-rg-<inject key="DeploymentID"></inject>" --zone-name "privatelink.openai.azure.com" -o table
  ```
- Flush DNS cache on the VM:
  ```powershell
  Clear-DnsClientCache
  ipconfig /flushdns
  ```

---

### Issue: Can't disable public access on a service

**Solution**:
- Ensure private endpoint is successfully created first
- Check the service supports disabling public access
- Try using Azure Portal instead:
  - Go to the resource → Networking → Disable public access

---

### Issue: Private endpoint shows "Pending" status

**Solution**:
- Private endpoint approval is automatic for same-subscription deployments
- If stuck, delete and recreate:
  ```powershell
  az network private-endpoint delete -n <pe-name> -g "challenge-rg-<inject key="DeploymentID"></inject>"
  ```
  Then redeploy with AZD

---

### Issue: Services unreachable even from VM

**Solution**:
- Verify NSG rules allow traffic on port 443
- Check private endpoint is in "Approved" state
- Ensure VM is in the correct subnet (application subnet)
- Test connectivity:
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
   Test-NetConnection -ComputerName "10.0.1.4" -Port 80  # Should fail
   ```

## What You Learned

In this challenge, you:

✅ Created and configured Network Security Groups with restrictive rules  
✅ Disabled public network access on all AI services  
✅ Validated private endpoint connectivity and approval  
✅ Configured private DNS zones for name resolution  
✅ Tested and verified complete internet isolation  
✅ Implemented defense-in-depth network security  
✅ Documented your network topology  

Your AI environment is now completely isolated from the internet with multiple security layers!

## Next Steps

Network security: ✅ Complete!

In **Challenge 3**, you'll configure identity and access management using Entra ID, managed identities, and RBAC to ensure only authorized identities can access your services.

Head to **challenge-3.md** to continue! 🔐

---

**Security Reminder**: In production, regularly audit NSG rules, review flow logs, and test private connectivity to ensure the network remains secure over time.
