# Challenge 06: Test Secure Connectivity via Azure Bastion

## Introduction

Your secure AI application is running! Now let's validate the **secure connectivity** layer. 

In this challenge, you'll test accessing your VM and application using Azure Bastion - a fully managed PaaS service that provides secure RDP/SSH without exposing public IPs.

This proves your entire architecture works through private networking only!

## Prerequisites

- Completed Challenge 5 (Chat application deployed and tested on **vm-<inject key="DeploymentID" enableCopy="false"/>**)
- Azure Bastion deployed (from pre-configured environment)
- Chat application running on **vm-<inject key="DeploymentID" enableCopy="false"/>**
- All services using private endpoints
- VS Code open with PowerShell terminal on **vm-<inject key="DeploymentID" enableCopy="false"/>**
- Azure CLI logged in

## Challenge Objectives

- Connect to VM using Azure Bastion (no public IP!)
- Test chat application through Bastion
- Validate private endpoint DNS resolution
- Test network isolation (verify public access is blocked)
- Monitor connectivity through Network Watcher
- Document secure access patterns

## Steps to Complete

### Part 1: Verify Azure Bastion Deployment

1. **Check if Bastion exists**:

```powershell
az network bastion list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[].{Name:name, Location:location, Sku:sku.name, State:provisioningState}" `
 --output table
```

Expected:
- Name: `bastion-<DeploymentID>` or similar
- Sku: `Basic` or `Standard`
- State: `Succeeded`

2. **Get Bastion details**:

```powershell
$bastionName = az network bastion list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[0].name" -o tsv

Write-Host "Bastion Name: $bastionName"

# Get full details
az network bastion show `
 --name $bastionName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --output json
```

3. **Verify Bastion subnet**:

```powershell
az network vnet subnet show `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --vnet-name "vnet-<inject key="DeploymentID" enableCopy="false"/>" `
 --name "AzureBastionSubnet" `
 --query "{Name:name, AddressPrefix:addressPrefix, Provisioning:provisioningState}" `
 --output table
```

Expected:
- Name: `AzureBastionSubnet` (exact name required!)
- AddressPrefix: `/26` or `/27` (e.g., `10.0.255.0/26`)
- Provisioning: `Succeeded`

### Part 2: Connect to VM via Azure Bastion

1. **Using Azure Portal** (Recommended for first-time):

   - Open [Azure Portal](https://portal.azure.com)
   - Navigate to: Resource Groups ? `challenge-rg-<inject key="DeploymentID" enableCopy="false"/>`
   - Click on your VM: `vm-<inject key="DeploymentID" enableCopy="false"/>`
   - Click **Connect** (top menu)
   - Select **Bastion**
   - Enter credentials:
   - **Username**: `azureuser` or the admin username you configured
   - **Password**: `<inject key="VMAdminPassword"></inject>`
   - Click **Connect**

   Expected:
   - New browser tab opens with remote desktop session
   - Connected to VM desktop
   - No public IP used!

2. **Using Azure CLI** (Alternative):

```powershell
# Get your subscription ID
$subscriptionId = az account show --query id -o tsv

# Note: This opens a tunnel, then you RDP through localhost
az network bastion tunnel `
 --name $bastionName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --target-resource-id "/subscriptions/$subscriptionId/resourceGroups/challenge-rg-<inject key="DeploymentID" enableCopy="false"/>/providers/Microsoft.Compute/virtualMachines/vm-<inject key="DeploymentID" enableCopy="false"/>" `
 --resource-port 3389 `
 --port 55000
```

Then in another window:
```powershell
mstsc /v:localhost:55000
```

3. **Verify you're connected**:

Inside the Bastion session, open PowerShell:

```powershell
# Check VM name
hostname

# Check IP address (should be 10.0.3.x - private only!)
ipconfig | Select-String "IPv4"

# Verify no public IP
(Invoke-WebRequest -Uri "http://ifconfig.me/ip" -UseBasicParsing).Content
# This should FAIL or return Bastion's IP, not the VM's
```

### Part 3: Test Chat Application Through Bastion

Now let's access the chat app through the secure Bastion session!

1. **Inside Bastion session**, open PowerShell:

```powershell
cd C:\LabFiles\SecureAI\chat-app
.\venv\Scripts\Activate.ps1
streamlit run app.py
```

2. **Browser should open automatically** to `http://localhost:8501`

   If not, manually open browser and go to: `http://localhost:8501`

3. **Test the application**:

   - Chat interface loads
   - Sidebar shows "Authenticated"
   - Send a test message: `What is Azure Bastion?`
   - Receive AI response explaining Bastion!

4. **Verify security indicators**:

   - Sidebar should show:
   - Auth: Managed Identity
   - Network: Private Only
   - Storage: Enabled

### Part 4: Validate Private Endpoint Connectivity

Let's prove all connections go through private endpoints!

1. **Test DNS resolution** (inside Bastion session):

```powershell
# Get OpenAI endpoint from Key Vault
$kvName = az keyvault list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "[0].name" -o tsv
$openaiEndpoint = az keyvault secret show --vault-name $kvName --name "OpenAIEndpoint" --query value -o tsv
$openaiHost = ($openaiEndpoint -replace "https://","") -replace "/",""

Write-Host "Testing DNS for: $openaiHost"

# Resolve DNS
nslookup $openaiHost
```

Expected:
```
Name: <your-openai>.openai.azure.com
Address: 10.0.1.x <-- PRIVATE IP!
```

If you see a public IP (like `20.x.x.x`), private endpoint DNS is NOT working!

2. **Test Key Vault DNS**:

```powershell
$kvHost = "$kvName.vault.azure.net"
nslookup $kvHost
```

Expected:
```
Address: 10.0.2.x <-- PRIVATE IP!
```

3. **Test Storage DNS**:

```powershell
$storageName = az storage account list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "[0].name" -o tsv
$storageHost = "$storageName.blob.core.windows.net"
nslookup $storageHost
```

Expected:
```
Address: 10.0.2.x <-- PRIVATE IP!
```

4. **Verify private endpoints are approved**:

```powershell
# List all private endpoints
az network private-endpoint list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[].{Name:name, Connection:privateLinkServiceConnections[0].provisioningState}" `
 --output table
```

Expected: All show `Succeeded`

### Part 5: Test Network Isolation (Public Access Blocked)

Let's verify that public access is actually blocked!

1. **Try to access OpenAI from the internet**:

Inside Bastion session:
```powershell
# This should FAIL because public access is disabled
try {
 $response = Invoke-WebRequest -Uri "https://$openaiHost/openai/deployments?api-version=2024-02-01" -Method GET
 Write-Host "PROBLEM: Public access is NOT blocked!"
} catch {
 Write-Host "SUCCESS: Public access is blocked (expected error)"
 Write-Host "Error: $($_.Exception.Message)"
}
```

Expected:
- Request fails with `403 Forbidden` or timeout
- This proves public access is disabled!

2. **Try to access Key Vault from internet**:

```powershell
try {
 $response = Invoke-WebRequest -Uri "https://$kvHost/secrets?api-version=7.4" -Method GET
 Write-Host "PROBLEM: Public access is NOT blocked!"
} catch {
 Write-Host "SUCCESS: Key Vault public access blocked"
 Write-Host "Error: $($_.Exception.Message)"
}
```

3. **Verify NSG rules are enforced**:

```powershell
# Get NSG associated with application subnet
$nsgName = az network nsg list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[?contains(name, 'app')].name" -o tsv

if ($nsgName) {
 az network nsg rule list `
 --nsg-name $nsgName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[].{Name:name, Priority:priority, Access:access, Direction:direction, Protocol:protocol, Source:sourceAddressPrefix, Destination:destinationAddressPrefix}" `
 --output table
} else {
 Write-Host "No NSG found for application subnet"
}
```

### Part 6: Monitor Connectivity with Network Watcher

Use Azure Network Watcher to validate connectivity paths.

1. **Enable Network Watcher** (if not already):

```powershell
az network watcher configure `
 --resource-group "NetworkWatcherRG" `
 --locations "<inject key="Region"></inject>" `
 --enabled true
```

2. **Test connectivity from VM to OpenAI private endpoint**:

```powershell
# Get OpenAI private IP
$openaiPE = az network private-endpoint list `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "[?contains(name, 'openai')].name" -o tsv

$openaiIP = az network private-endpoint show `
 --name $openaiPE `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "customDnsConfigs[0].ipAddresses[0]" -o tsv

Write-Host "OpenAI Private IP: $openaiIP"

# Get subscription ID
$subscriptionId = az account show --query id -o tsv

# Test connectivity (this will take 2-3 minutes)
az network watcher test-connectivity `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --source-resource "/subscriptions/$subscriptionId/resourceGroups/challenge-rg-<inject key="DeploymentID" enableCopy="false"/>/providers/Microsoft.Compute/virtualMachines/vm-<inject key="DeploymentID" enableCopy="false"/>" `
 --dest-address $openaiIP `
 --dest-port 443 `
 --output table
```

Expected:
- ConnectionStatus: `Reachable`
- Hops: Shows path through VNET

3. **Test connectivity to Key Vault**:

```powershell
$kvPE = az network private-endpoint list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "[?contains(name, 'kv')].name" -o tsv
$kvIP = az network private-endpoint show --name $kvPE -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "customDnsConfigs[0].ipAddresses[0]" -o tsv

# Get subscription ID if not already set
$subscriptionId = az account show --query id -o tsv

az network watcher test-connectivity `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --source-resource "/subscriptions/$subscriptionId/resourceGroups/challenge-rg-<inject key="DeploymentID" enableCopy="false"/>/providers/Microsoft.Compute/virtualMachines/vm-<inject key="DeploymentID" enableCopy="false"/>" `
 --dest-address $kvIP `
 --dest-port 443 `
 --output table
```

### Part 7: Test Session Persistence Across Bastion Sessions

Let's verify session history persists!

1. **Start a chat session** (if not already running):

   - In Bastion session, ensure chat app is running
   - Send 3-4 messages to build conversation history
   - Note the Session ID in the sidebar (first 8 characters)

2. **Disconnect from Bastion**:
   - Close the Bastion browser tab
   - This simulates connection loss

3. **Reconnect via Bastion**:
   - Go back to Azure Portal
   - Connect to VM via Bastion again

4. **Restart the chat app**:

```powershell
cd C:\LabFiles\SecureAI\chat-app
.\venv\Scripts\Activate.ps1
streamlit run app.py
```

5. **Verify session history was saved**:

```powershell
# List all saved sessions
az storage blob list `
 --account-name $storageName `
 --container-name "chat-sessions" `
 --auth-mode login `
 --query "[].{Name:name, Size:properties.contentLength, LastModified:properties.lastModified}" `
 --output table
```

Expected:
- Your previous session(s) listed
- Timestamps show when you chatted
- File sizes match conversation length

### Part 8: Performance Testing

Let's benchmark the secure connectivity!

1. **Test latency to OpenAI** (inside Bastion session):

```powershell
@'
import time
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from openai import AzureOpenAI

# Setup
credential = DefaultAzureCredential()
kv_name = "$kvName"
kv_url = f"https://{kv_name}.vault.azure.net"
secret_client = SecretClient(vault_url=kv_url, credential=credential)

openai_endpoint = secret_client.get_secret("OpenAIEndpoint").value
chat_deployment = secret_client.get_secret("ChatModelDeployment").value
api_version = secret_client.get_secret("OpenAIApiVersion").value

client = AzureOpenAI(
 azure_endpoint=openai_endpoint,
 api_version=api_version,
 azure_ad_token_provider=lambda: credential.get_token("https://cognitiveservices.azure.com/.default").token
)

# Benchmark
print("Performance Benchmark - 10 Requests\n")
latencies = []

for i in range(10):
 start = time.time()
 response = client.chat.completions.create(
 model=chat_deployment,
 messages=[{"role": "user", "content": "Say 'OK'"}],
 max_tokens=10
 )
 end = time.time()
 latency = (end - start) * 1000 # Convert to ms
 latencies.append(latency)
 print(f"Request {i+1}: {latency:.0f}ms")

print(f"\nResults:")
print(f" Average: {sum(latencies)/len(latencies):.0f}ms")
print(f" Min: {min(latencies):.0f}ms")
print(f" Max: {max(latencies):.0f}ms")
print(f"\nAll requests via private endpoint!")
'@ -replace '\$kvName', $kvName | Out-File -FilePath "C:\LabFiles\benchmark.py" -Encoding UTF8

python C:\LabFiles\benchmark.py
```

Expected:
- Average latency: 500-1500ms (varies by region and model)
- All requests succeed
- Consistent performance

2. **Compare to public endpoint** (theoretical - we can't test since public is disabled!):

Typically, private endpoints add ~10-50ms latency vs public, but provide:
- No internet exposure
- No data exfiltration risk
- Compliance with data residency
- Defense-in-depth security

### Part 9: Document Connectivity Testing

```powershell
@"
=== Secure Connectivity Testing Report ===
Date: $(Get-Date)

Azure Bastion Configuration:
- Name: $bastionName
- Connection Method: Browser-based (HTTPS/443)
- VM Public IP: NONE
- Authentication: Entra ID + VM password
- Session: Fully isolated per user

Connectivity Tests:
1. Bastion to VM:
 - Status: PASSED
 - Method: RDP over TLS
 - No public IP required
 
2. VM to Azure OpenAI:
 - Status: PASSED
 - IP Resolution: 10.0.1.x (private)
 - Public Access: BLOCKED
 
3. VM to Key Vault:
 - Status: PASSED
 - IP Resolution: 10.0.2.x (private)
 - Public Access: BLOCKED
 
4. VM to Storage:
 - Status: PASSED
 - IP Resolution: 10.0.2.x (private)
 - Public Access: BLOCKED

Network Watcher Results:
- OpenAI Private Endpoint: Reachable
- Key Vault Private Endpoint: Reachable
- Storage Private Endpoint: Reachable
- Path: VM ? VNET ? Private Endpoint

Chat Application Testing:
- Access Method: Bastion ? VM ? localhost:8501
- Authentication: Managed Identity
- All API calls: Via private endpoints
- Session Persistence: Working

Performance Benchmark:
- Average Latency: $(if (Test-Path C:\LabFiles\benchmark.py) { "See benchmark results" } else { "Not yet tested" })
- Connectivity: 100% success rate
- Private network only: CONFIRMED

Security Validation:
- Public access to OpenAI: BLOCKED
- Public access to Key Vault: BLOCKED
- Public access to Storage: BLOCKED
- VM public IP: NONE
- NSG rules: ENFORCED

Session Persistence:
- Sessions saved to Blob Storage: YES
- Accessible across connections: YES
- Container: chat-sessions

Conclusion:
All connectivity tests PASSED
Zero public internet exposure
100% private network architecture
Production-ready secure access pattern

Ready for WAF Validation: YES
"@ | Out-File -FilePath "C:\LabFiles\connectivity-test-report.txt"

notepad C:\LabFiles\connectivity-test-report.txt
```

## Success Criteria

Validate your secure connectivity:

- [ ] Azure Bastion deployed and operational
- [ ] Connected to VM via Bastion (no public IP!)
- [ ] Chat application accessible through Bastion session
- [ ] DNS resolves all services to private IPs (10.0.x.x)
- [ ] Public access to OpenAI is BLOCKED
- [ ] Public access to Key Vault is BLOCKED
- [ ] Public access to Storage is BLOCKED
- [ ] Network Watcher confirms private endpoint connectivity
- [ ] Session history persists across Bastion sessions
- [ ] Performance benchmarks completed
- [ ] All tests passed (no public internet access)
- [ ] Connectivity documented in report
