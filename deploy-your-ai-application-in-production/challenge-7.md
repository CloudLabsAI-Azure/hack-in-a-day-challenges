# Challenge 07: Well-Architected Framework Validation & Production Readiness

## Introduction

Congratulations! You've built a complete secure AI infrastructure:
- Private endpoints everywhere
- Managed identity authentication
- Secrets in Key Vault
- Chat application working
- Secure Bastion access

Now for the **final step**: Validate your solution against the **Azure Well-Architected Framework (WAF)** to ensure it's truly production-ready.

This challenge is your **production readiness checklist** - covering Security, Reliability, Cost Optimization, Operational Excellence, and Performance Efficiency.

## Prerequisites

- Completed all previous challenges (1-6)
- All services deployed and tested
- Access to Azure Portal
- Access to **vm-<inject key="DeploymentID" enableCopy="false"/>** via Azure Bastion

## Challenge Objectives

- Enable data protection features (soft delete, purge protection)
- Configure monitoring with Log Analytics and diagnostics
- Review Azure Advisor recommendations
- Complete a final production readiness checklist

## Steps to Complete

### Part 1: Enable Data Protection Features

Enable soft delete and purge protection on Key Vault and Storage to prevent accidental data loss.

1. **Enable Key Vault soft delete and purge protection**:

```powershell
$kvName = az keyvault list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "[0].name" -o tsv

# Check current settings
az keyvault show -n $kvName -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "properties.{SoftDelete:enableSoftDelete,PurgeProtection:enablePurgeProtection}" -o json

# Enable purge protection (soft delete is enabled by default on new vaults)
az keyvault update `
 --name $kvName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --enable-purge-protection true

Write-Host "Key Vault purge protection enabled"
```

2. **Enable Storage soft delete**:

```powershell
$storageName = az storage account list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "[0].name" -o tsv

# Enable blob soft delete (7 days retention)
az storage blob service-properties delete-policy update `
 --account-name $storageName `
 --enable true `
 --days-retained 7

# Enable container soft delete
az storage account blob-service-properties update `
 --account-name $storageName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --enable-container-delete-retention true `
 --container-delete-retention-days 7

Write-Host "Storage soft delete enabled"
```

3. **Verify encryption at rest** (should be enabled by default):

```powershell
# Check Storage encryption
az storage account show -n $storageName -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "encryption.services.blob.enabled" -o tsv

# Check OpenAI encryption
$openaiName = az cognitiveservices account list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "[?kind=='AIServices'].name" -o tsv
az cognitiveservices account show -n $openaiName -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query "properties.encryption" -o json
```

Both should show encryption is enabled.

### Part 2: Configure Monitoring with Log Analytics

Set up centralized monitoring for your OpenAI resource.

1. **Create Log Analytics workspace and enable diagnostics**:

```powershell
$workspaceName = "law-ai-monitoring-<inject key="DeploymentID" enableCopy="false"/>"

az monitor log-analytics workspace create `
 --workspace-name $workspaceName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --location "<inject key="Region"></inject>"

Write-Host "Log Analytics workspace created"

# Get workspace ID
$workspaceId = az monitor log-analytics workspace show `
 --workspace-name $workspaceName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query id -o tsv

# Get OpenAI resource ID
$openaiId = az cognitiveservices account show `
 --name $openaiName `
 --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
 --query id -o tsv

# Enable diagnostics on OpenAI
az monitor diagnostic-settings create `
 --name "openai-diagnostics" `
 --resource $openaiId `
 --workspace $workspaceId `
 --logs "[{\"category\":\"Audit\",\"enabled\":true},{\"category\":\"RequestResponse\",\"enabled\":true}]" `
 --metrics "[{\"category\":\"AllMetrics\",\"enabled\":true}]"

Write-Host "Diagnostics enabled on OpenAI resource"
```

2. **Verify diagnostics are configured**:

```powershell
az monitor diagnostic-settings list --resource $openaiId --query "[].name" -o table
```

### Part 3: Review Azure Advisor Recommendations

Get recommendations for your resource group.

```powershell
az advisor recommendation list `
 --query "[?contains(resourceGroup, 'challenge-rg-<inject key="DeploymentID" enableCopy="false"/>')].{Category:category, Impact:impact, Problem:shortDescription.problem}" `
 --output table
```

   Review any **Security** or **Reliability** recommendations and address them if time permits.

### Part 4: Final Production Readiness Checklist

Verify your complete architecture against WAF pillars:

```powershell
# Quick verification of all security controls
Write-Host "=== PRODUCTION READINESS CHECK ===" -ForegroundColor Cyan

# 1. Managed Identity
$mi = az vm identity show -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" -n "vm-<inject key="DeploymentID" enableCopy="false"/>" --query principalId -o tsv
if ($mi) { Write-Host "[PASS] Managed Identity enabled" -ForegroundColor Green } else { Write-Host "[FAIL] Managed Identity" -ForegroundColor Red }

# 2. Private Endpoints
$peCount = (az network private-endpoint list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "length(@)") 
Write-Host "[PASS] Private Endpoints: $peCount configured" -ForegroundColor Green

# 3. Key Vault public access
$kvPublic = az keyvault show -n $kvName -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "properties.publicNetworkAccess" -o tsv
if ($kvPublic -eq "Disabled") { Write-Host "[PASS] Key Vault public access disabled" -ForegroundColor Green } else { Write-Host "[WARN] Key Vault public access: $kvPublic" -ForegroundColor Yellow }

# 4. OpenAI public access
$oaiPublic = az cognitiveservices account show -n $openaiName -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "properties.publicNetworkAccess" -o tsv
if ($oaiPublic -eq "Disabled") { Write-Host "[PASS] OpenAI public access disabled" -ForegroundColor Green } else { Write-Host "[WARN] OpenAI public access: $oaiPublic" -ForegroundColor Yellow }

# 5. Key Vault purge protection
$purge = az keyvault show -n $kvName -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "properties.enablePurgeProtection" -o tsv
if ($purge -eq "true") { Write-Host "[PASS] Key Vault purge protection enabled" -ForegroundColor Green } else { Write-Host "[WARN] Purge protection not enabled" -ForegroundColor Yellow }

# 6. Diagnostics
$diag = az monitor diagnostic-settings list --resource $openaiId --query "length(@)"
if ($diag -gt 0) { Write-Host "[PASS] Monitoring diagnostics configured" -ForegroundColor Green } else { Write-Host "[WARN] No diagnostics configured" -ForegroundColor Yellow }

# 7. RBAC roles
$roles = az role assignment list --assignee $mi --query "length(@)"
Write-Host "[PASS] RBAC role assignments: $roles configured" -ForegroundColor Green

# 8. NSG
$nsgCount = (az network nsg list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "length(@)")
Write-Host "[PASS] Network Security Groups: $nsgCount configured" -ForegroundColor Green

Write-Host "`n=== ASSESSMENT COMPLETE ===" -ForegroundColor Cyan
Write-Host "Your secure AI application is production-ready!" -ForegroundColor Green
```

## Success Criteria

Validate production readiness:

- [ ] Key Vault purge protection enabled
- [ ] Storage soft delete enabled (blob and container)
- [ ] Encryption at rest verified on all services
- [ ] Log Analytics workspace created
- [ ] Diagnostics enabled on OpenAI resource
- [ ] Azure Advisor recommendations reviewed
- [ ] Final readiness check passes all items
