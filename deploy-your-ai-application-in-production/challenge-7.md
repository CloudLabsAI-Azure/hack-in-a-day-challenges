# Challenge 07: Deploy Application to Azure App Service

## Introduction

Your chat application works locally on the VM — but that's not production! In this challenge, you'll deploy the application to **Azure App Service**, a fully managed PaaS platform that handles scaling, patching, and availability for you.

You'll configure:
- **App Service with VNet Integration** so the app connects to your private endpoints
- **Managed Identity** on the App Service for passwordless authentication  
- **RBAC roles** so the App Service identity can access Key Vault, OpenAI, and Storage
- **Zero-touch deployment** using zip deploy from your VM

By the end, your secure chat application will be running on a production URL — fully private, fully managed, and enterprise-ready.

## Prerequisites

- Completed Challenge 6 (Application tested locally, connectivity validated)
- Chat application code at `C:\Code\hack-in-a-day-challenges-deploy-your-ai-application\codefiles` on the VM
- All private endpoints configured and DNS zones linked to VNet
- Connected to **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>** via Azure Bastion
- Azure CLI logged in (`az login` completed)

## Challenge Objectives

- Create a dedicated subnet for App Service VNet integration
- Deploy Azure App Service Plan and Web App
- Enable managed identity on App Service and assign RBAC roles
- Configure VNet integration for private endpoint connectivity
- Deploy the application code to App Service
- Verify the production deployment works end-to-end

## Steps to Complete

### Task 1: Create App Service Subnet

App Service VNet integration requires a dedicated subnet delegated to `Microsoft.Web/serverFarms`.

1. **Open VS Code PowerShell terminal** on **Hack-vm-<inject key="DeploymentID" enableCopy="false"/>** and run:

   ```powershell
   # Add a new subnet for App Service
   az network vnet subnet create `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --vnet-name "vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
   --name "snet-webapp" `
   --address-prefixes "10.0.5.0/24" `
   --delegations "Microsoft.Web/serverFarms"

   Write-Host "App Service subnet created: snet-webapp (10.0.5.0/24)"
   ```

   > **Why a dedicated subnet?** App Service VNet integration requires a subnet delegated exclusively to `Microsoft.Web/serverFarms`. This delegation allows the App Service to inject into your VNet and access private endpoints.

### Task 2: Create App Service Plan and Web App

1. **Create the App Service Plan** (Linux, Python):

   ```powershell
   az appservice plan create `
   --name "asp-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --location "<inject key="Region"></inject>" `
   --sku B1 `
   --is-linux

   Write-Host "App Service Plan created (B1 Linux)"
   ```

2. **Create the Web App**:

   ```powershell
   az webapp create `
   --name "app-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --plan "asp-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
   --runtime "PYTHON:3.11"

   Write-Host "Web App created: app-secureai-<inject key="DeploymentID" enableCopy="false"/>"
   ```

### Task 3: Enable Managed Identity and Assign RBAC Roles

The App Service needs its own managed identity to authenticate to Key Vault, OpenAI, and Storage — just like the VM.

1. **Enable system-assigned managed identity**:

   ```powershell
   az webapp identity assign `
   --name "app-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>"

   # Get the identity principal ID
   $appIdentityId = az webapp identity show `
   --name "app-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query principalId -o tsv

   Write-Host "App Service Managed Identity: $appIdentityId"
   ```

2. **Assign RBAC roles** for the App Service identity:

   ```powershell
   # Get resource IDs
   $kvName = az keyvault list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "[0].name" -o tsv
   $kvId = az keyvault show -n $kvName -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query id -o tsv

   $openaiName = az cognitiveservices account list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "[?kind=='AIServices'].name" -o tsv
   $openaiId = az cognitiveservices account show -n $openaiName -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query id -o tsv

   $storageName = az storage account list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "[0].name" -o tsv
   $storageId = az storage account show -n $storageName -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query id -o tsv

   # Assign Key Vault Secrets User
   az role assignment create `
   --assignee $appIdentityId `
   --role "Key Vault Secrets User" `
   --scope $kvId

   # Assign Cognitive Services OpenAI User
   az role assignment create `
   --assignee $appIdentityId `
   --role "Cognitive Services OpenAI User" `
   --scope $openaiId

   # Assign Storage Blob Data Contributor
   az role assignment create `
   --assignee $appIdentityId `
   --role "Storage Blob Data Contributor" `
   --scope $storageId

   Write-Host "All RBAC roles assigned to App Service identity"
   ```

   > **Note**: RBAC role assignments take **2-3 minutes** to propagate. Continue with the next steps while they take effect.

### Task 4: Configure VNet Integration

Connect the App Service to your VNet so it can reach private endpoints.

1. **Enable VNet integration**:

   ```powershell
   az webapp vnet-integration add `
   --name "app-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --vnet "vnet-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
   --subnet "snet-webapp"

   Write-Host "VNet integration configured"
   ```

2. **Enable Route All** so all outbound traffic goes through the VNet (required for private endpoint DNS resolution):

   ```powershell
   # Route all outbound traffic through VNet
   az resource update `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --name "app-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
   --resource-type "Microsoft.Web/sites" `
   --api-version "2023-12-01" `
   --set properties.vnetRouteAllEnabled=true

   Write-Host "Route All enabled - all traffic goes through VNet"
   ```

      > **Why Route All?** Without this, the App Service would resolve DNS using public DNS servers and try to connect to the public endpoints (which are disabled). With Route All enabled, DNS queries go through Azure DNS in the VNet, which resolves private DNS zones to private IPs.
      >
      > **Note**: We use `az resource update` with API version `2023-12-01` because the `--vnet-route-all-enabled` flag on `az webapp config set` is deprecated in newer Azure CLI versions and may silently fail.

### Task 5: Configure App Settings and Startup Command

1. **Set application settings** (these become environment variables for the app):

   ```powershell
   $kvName = az keyvault list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "[0].name" -o tsv

   az webapp config appsettings set `
   --name "app-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --settings `
      KEY_VAULT_NAME=$kvName `
      SCM_DO_BUILD_DURING_DEPLOYMENT=true `
      WEBSITE_DNS_SERVER=168.63.129.16 `
      ENABLE_SESSION_HISTORY=true `
      SESSION_CONTAINER=chat-sessions

   Write-Host "App Settings configured"
   ```

      > **Note**: The Azure CLI output may show all setting values as `null` — this is expected behavior in newer CLI versions that mask values for security. The settings are applied correctly. You can verify with:
      > ```powershell
      > az webapp config appsettings list --name "app-secureai-<inject key="DeploymentID" enableCopy="false"/>" --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "[].{Name:name, Value:value}" -o table
      > ```

      > **Key Settings Explained**:
      > - `KEY_VAULT_NAME`: The only config needed — all secrets come from Key Vault at runtime
      > - `SCM_DO_BUILD_DURING_DEPLOYMENT`: Tells Oryx to run `pip install -r requirements.txt` during deployment
      > - `WEBSITE_DNS_SERVER=168.63.129.16`: Uses Azure DNS for private endpoint resolution

2. **Set the startup command** for Streamlit:

   ```powershell
   az webapp config set `
   --name "app-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --startup-file "python -m streamlit run app.py --server.port 8000 --server.address 0.0.0.0 --server.enableCORS false --server.enableXsrfProtection false --server.fileWatcherType none"

   Write-Host "Startup command configured for Streamlit"
   ```

      > **Why this startup command?** Azure App Service (Python) defaults to Gunicorn, but Streamlit has its own web server. This command tells App Service to run Streamlit on port 8000 (the expected internal port) with settings optimized for production.

### Task 6: Deploy the Application Code

1. **Prepare the deployment package** (clean up local-only files):

   ```powershell
   # Ensure you are in the chat application directory
   Set-Location "C:\Code\hack-in-a-day-challenges-deploy-your-ai-application\codefiles"

   # Verify you are in the correct directory (should contain app.py, requirements.txt, etc.)
   Get-ChildItem -Name

   # Remove local-only files that shouldn't be deployed
   Remove-Item -Path ".\venv" -Recurse -Force -ErrorAction SilentlyContinue
   Remove-Item -Path ".\.env" -Force -ErrorAction SilentlyContinue
   Remove-Item -Path ".\secure-chatbot.py" -Force -ErrorAction SilentlyContinue
   Get-ChildItem -Path "." -Directory -Filter "__pycache__" -Recurse | Remove-Item -Recurse -Force

   Write-Host "Cleaned up local files"
   ```

      > **Note**: We remove `.env` because App Settings replace it on App Service. We remove `venv/` because Oryx creates its own virtual environment during deployment. We remove `__pycache__/` for a clean deployment.
      >
      > **Important**: You must be in the `C:\Code\hack-in-a-day-challenges-deploy-your-ai-application\codefiles` directory (set up in Challenge 5). If this path does not exist, go back to Challenge 5 and complete the code download steps first.

2. **Deploy to App Service**:

   ```powershell
   # Deploy directly from the current directory (builds and deploys in one step)
   az webapp up `
   --name "app-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --runtime "PYTHON:3.11"

   Write-Host "Deployment complete!"
   ```

      > **Why `az webapp up`?** This command bundles build and deployment into a single step. It uploads your code, triggers the **Oryx build pipeline** (which detects `requirements.txt` and runs `pip install`), and deploys the result. The deployment takes **5-10 minutes** on B1 tier.

3. **Wait for deployment to complete** (Oryx will install Python dependencies — this takes **3-5 minutes**):

   ```powershell
   # Check deployment status
   az webapp log deployment show `
   --name "app-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query "[?status=='Success' || status=='Failed'].{Status:status, Time:endTime}" `
   --output table
   ```

      > **What happens during deployment?** Oryx (Azure's build engine) detects `requirements.txt`, creates a virtual environment, and installs all dependencies (`streamlit`, `azure-identity`, `openai`, etc.). Then it starts the app using your startup command.

### Task 7: Verify Production Deployment

1. **Get the App Service URL**:

   ```powershell
   $appUrl = az webapp show `
   --name "app-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query "defaultHostName" -o tsv

   Write-Host "Your production URL: https://$appUrl"
   ```

2. **Open your browser** and navigate to:
   ```
   https://app-secureai-<inject key="DeploymentID" enableCopy="false"/>.azurewebsites.net
   ```

3. **Verify the application**:

   - The **Secure Enterprise Chat** UI should load
   - Sidebar shows **Authenticated** with Managed Identity
   - Model name and security status displayed

4. **Test chat functionality** — send a message:

   ```
   What is Azure App Service and how does it handle scaling?
   ```
   - You should receive an AI response
   - This confirms: App Service → VNet → Private Endpoint → Azure OpenAI is working end-to-end

5. **Verify the production security posture**:

   ```powershell
   Write-Host "=== PRODUCTION DEPLOYMENT CHECK ===" -ForegroundColor Cyan

   # 1. App Service Managed Identity
   $appMI = az webapp identity show `
   --name "app-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query principalId -o tsv
   if ($appMI) { Write-Host "[PASS] App Service Managed Identity enabled" -ForegroundColor Green } else { Write-Host "[FAIL] Managed Identity" -ForegroundColor Red }

   # 2. VNet Integration
   $vnetInt = az webapp vnet-integration list `
   --name "app-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query "[0].name" -o tsv
   if ($vnetInt) { Write-Host "[PASS] VNet Integration: $vnetInt" -ForegroundColor Green } else { Write-Host "[FAIL] VNet Integration" -ForegroundColor Red }

   # 3. Route All
   $routeAll = az webapp show `
   --name "app-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
   --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" `
   --query "outboundVnetRouting.allTraffic" -o tsv
   if ($routeAll -eq "true") { Write-Host "[PASS] Route All enabled" -ForegroundColor Green } else { Write-Host "[WARN] Route All: $routeAll (try: az resource update --resource-group challenge-rg-<inject key='DeploymentID' enableCopy='false'/> --name app-secureai-<inject key='DeploymentID' enableCopy='false'/> --resource-type Microsoft.Web/sites --api-version 2023-12-01 --set properties.vnetRouteAllEnabled=true)" -ForegroundColor Yellow }

   # 4. Private Endpoints
   $peCount = (az network private-endpoint list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "length(@)")
   Write-Host "[PASS] Private Endpoints: $peCount configured" -ForegroundColor Green

   # 5. Key Vault public access
   $kvName = az keyvault list -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "[0].name" -o tsv
   $kvPublic = az keyvault show -n $kvName -g "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>" --query "properties.publicNetworkAccess" -o tsv
   if ($kvPublic -eq "Disabled") { Write-Host "[PASS] Key Vault public access disabled" -ForegroundColor Green } else { Write-Host "[WARN] Key Vault public access: $kvPublic" -ForegroundColor Yellow }

   # 6. RBAC roles for App Service
   $roles = az role assignment list --assignee $appMI --query "length(@)"
   Write-Host "[PASS] App Service RBAC roles: $roles assigned" -ForegroundColor Green

   Write-Host "`n=== DEPLOYMENT COMPLETE ===" -ForegroundColor Cyan
   Write-Host "Production URL: https://app-secureai-<inject key="DeploymentID" enableCopy="false"/>.azurewebsites.net" -ForegroundColor Green
   Write-Host "Your secure AI application is now deployed in production!" -ForegroundColor Green
   ```

### Troubleshooting

If the app doesn't load or shows errors:

1. **Check deployment logs**:

   ```powershell
   az webapp log tail `
    --name "app-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
    --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>"
   ```
   Press `Ctrl+C` to stop log streaming.

2. **Restart the App Service** (if RBAC is still propagating):

   ```powershell
   az webapp restart `
    --name "app-secureai-<inject key="DeploymentID" enableCopy="false"/>" `
    --resource-group "challenge-rg-<inject key="DeploymentID" enableCopy="false"/>"
   ```

3. **Common issues**:

   - **"Key Vault Secrets User" error**: RBAC takes 2-3 min to propagate. Restart the app and try again.
   - **DNS resolution error**: Verify Route All is enabled and `WEBSITE_DNS_SERVER=168.63.129.16` is set.
   - **Startup timeout**: Streamlit can take 1-2 minutes to start on B1 tier. Wait and refresh.

## Success Criteria

Validate your production deployment:

- App Service subnet created (`snet-webapp`, 10.0.5.0/24) with `Microsoft.Web/serverFarms` delegation
- App Service Plan (Linux, B1) and Web App created
- System-assigned managed identity enabled on App Service
- RBAC roles assigned (Key Vault Secrets User, Cognitive Services OpenAI User, Storage Blob Data Contributor)
- VNet integration configured with Route All enabled
- Application deployed via zip deploy
- App loads at `https://app-secureai-<inject key="DeploymentID" enableCopy="false"/>.azurewebsites.net`
- Chat functionality works (AI responses via private endpoints)
- Production readiness check passes all items

## Additional Resources

- [Azure App Service Documentation](https://learn.microsoft.com/azure/app-service/)
- [App Service VNet Integration](https://learn.microsoft.com/azure/app-service/overview-vnet-integration)
- [Deploy Python Web Apps to App Service](https://learn.microsoft.com/azure/app-service/quickstart-python)
- [Managed Identity for App Service](https://learn.microsoft.com/azure/app-service/overview-managed-identity)
- [Private Endpoints with App Service](https://learn.microsoft.com/azure/app-service/networking/private-endpoint)
