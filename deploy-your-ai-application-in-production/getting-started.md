# Getting Started

## Welcome to the Secure AI Deployment Hackathon!

In this hands-on challenge, you'll deploy a production-ready AI application with enterprise-grade security. You'll work with Azure AI Foundry, private networking, managed identities, and secure deployment patterns that meet real-world compliance requirements.

## What You'll Need

### Pre-Configured Lab Environment

Your lab environment is already set up with:

- **Azure Subscription**: Pre-provisioned with credits
- **Resource Group**: `challenge-rg-<inject key="DeploymentID"></inject>`
- **Virtual Machine**: Windows Server with pre-installed tools
  - Visual Studio Code
  - Python 3.11
  - Azure CLI
  - Git
- **Azure Bastion**: For secure VM access (no public RDP)
- **Network Access**: Connectivity to deploy Azure resources

### Tools You'll Use

All tools are pre-installed on your VM:

1. **Azure CLI** - For Azure resource management
2. **Azure Developer CLI (AZD)** - For infrastructure deployment (you'll install this in Challenge 1)
3. **Python 3.11** - For running the chat application
4. **VS Code** - For viewing and editing code
5. **PowerShell** - For running commands
6. **Git** - For cloning repositories

## Accessing Your Lab Environment

### Step 1: Connect to Azure Portal

1. Open your browser and navigate to: [https://portal.azure.com](https://portal.azure.com)

2. Sign in with your lab credentials:
   - **Username**: <inject key="AzureAdUserEmail"></inject>
   - **Password**: <inject key="AzureAdUserPassword"></inject>

3. If prompted for MFA, follow the on-screen instructions

### Step 2: Verify Your Resource Group

1. In the Azure Portal, click the **Resource groups** icon in the left menu

2. Find your resource group: `challenge-rg-<inject key="DeploymentID"></inject>`

3. Click on it to view pre-deployed resources:
   - Virtual Machine
   - Virtual Network (for VM)
   - Network Security Group
   - Azure Bastion
   - Storage Account (for VM diagnostics)

### Step 3: Connect to Your Virtual Machine

You'll use Azure Bastion for secure access (no public IPs!):

1. In the Azure Portal, navigate to your Resource Group

2. Click on the Virtual Machine resource (name: `labvm-<inject key="DeploymentID"></inject>`)

3. Click **Connect** → **Connect via Bastion**

4. Enter credentials:
   - **Username**: `labuser`
   - **Password**: <inject key="VMAdminPassword"></inject>

5. Click **Connect**

6. A new browser tab will open with the VM desktop

### Step 4: Open VS Code on the VM

1. Once connected to the VM, open the **Start Menu**

2. Search for **Visual Studio Code**

3. Open VS Code

4. Open a new **PowerShell Terminal** in VS Code:
   - Press `` Ctrl + ` `` (backtick)
   - Or click **Terminal** → **New Terminal**

### Step 5: Verify Azure CLI Login

In the VS Code terminal on your VM, run:

```powershell
az login
```

This will open a browser for authentication. Use your lab credentials:
- **Username**: <inject key="AzureAdUserEmail"></inject>
- **Password**: <inject key="AzureAdUserPassword"></inject>

After successful login, you should see your subscription details.

### Step 6: Verify Python Installation

In the terminal, run:

```powershell
python --version
```

You should see: `Python 3.11.x`

If not, try:

```powershell
py -3.11 --version
```

## Lab Structure

This hackathon consists of 7 progressive challenges:

| Challenge | Title | Duration | Focus |
|-----------|-------|----------|-------|
| 1 | Deploy Secure AI Infrastructure with AZD | 45 min | Infrastructure deployment |
| 2 | Configure Network Security & Isolation | 30 min | Network security |
| 3 | Identity & Access Management with Entra ID | 45 min | Identity & RBAC |
| 4 | Secure Azure OpenAI Deployment | 30 min | AI service security |
| 5 | Deploy and Configure the Chat Application | 45 min | Application deployment |
| 6 | Test Secure Connectivity via Azure Bastion | 30 min | Connectivity validation |
| 7 | Validate Production Readiness & WAF Compliance | 45 min | Compliance & validation |

**Total Estimated Time**: 4-6 hours

## Challenge Workflow

Each challenge follows this pattern:

1. **Introduction**: Understand what you'll accomplish
2. **Prerequisites**: Ensure previous challenges are complete
3. **Steps to Complete**: Detailed instructions
4. **Success Criteria**: How to verify you're done
5. **Troubleshooting**: Common issues and solutions
6. **Bonus Challenges**: Extra learning opportunities

## Tips for Success

### Do's ✅

- **Read instructions carefully** before executing commands
- **Verify each step** before moving to the next
- **Use inject keys** exactly as shown (e.g., `<inject key="DeploymentID"></inject>`)
- **Check the Azure Portal** to understand what resources are created
- **Ask for help** if stuck - that's what hackathons are for!
- **Take screenshots** of your successful deployments

### Don'ts ❌

- **Don't skip challenges** - they build on each other
- **Don't hardcode values** - use inject keys for dynamic values
- **Don't expose secrets** - always use Key Vault
- **Don't enable public access** - this defeats the security purpose
- **Don't delete resources** until all challenges are complete

## Understanding Inject Keys

Throughout the challenges, you'll see placeholders like `<inject key="DeploymentID"></inject>`. These are automatically replaced with your unique values:

- `<inject key="DeploymentID"></inject>` → Your unique deployment ID (e.g., `2034545`)
- `<inject key="AzureAdUserEmail"></inject>` → Your lab username
- `<inject key="VMAdminPassword"></inject>` → Your VM password

**Important**: Copy commands exactly as shown - the lab environment will replace these automatically.

## Key Concepts You'll Learn

### Network Security
- Virtual Networks (VNETs) and subnets
- Private endpoints vs public endpoints
- Network Security Groups (NSGs)
- Azure Bastion for secure access

### Identity & Access
- Managed identities (system-assigned vs user-assigned)
- Role-Based Access Control (RBAC)
- Azure Key Vault for secret management
- Entra ID integration

### AI Services
- Azure AI Foundry hub and projects
- Azure OpenAI private deployment
- Secure API access patterns
- Model deployment and configuration

### Infrastructure as Code
- Azure Developer CLI (AZD)
- Bicep/ARM templates
- Azure Verified Modules (AVM)
- Repeatable deployments

### Well-Architected Framework
- Security best practices
- Reliability patterns
- Cost optimization
- Operational excellence

## Getting Help

If you encounter issues:

1. **Check the Troubleshooting section** in each challenge
2. **Review the Azure Portal** for resource status and errors
3. **Check activity logs** in the portal for deployment errors
4. **Ask your instructor** or use the Q&A channel
5. **Review documentation links** provided in each challenge

## Resources

Keep these links handy:

- [Azure Portal](https://portal.azure.com)
- [Azure AI Foundry](https://ai.azure.com)
- [Azure CLI Documentation](https://learn.microsoft.com/cli/azure/)
- [Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/)
- [Well-Architected Framework](https://learn.microsoft.com/azure/well-architected/)

## Ready to Start?

Once you've completed all the steps above and verified:

- ✅ You can access the Azure Portal
- ✅ You can connect to the VM via Bastion
- ✅ VS Code is open with a terminal
- ✅ Azure CLI login is successful
- ✅ Python 3.11 is verified

**You're ready to begin Challenge 1!** 🚀

Head to **challenge-1.md** to deploy your secure AI infrastructure.

---

**Pro Tip**: Keep the Azure Portal open in one browser tab and the VM (with VS Code) in another. This makes it easy to verify resources as you create them!
