# Deploy Your AI Application in Production

## Overview

Most AI projects fail to reach production not due to model quality, but because of security and compliance gaps. Public endpoints, weak identity controls, lack of network isolation, and non-compliant architectures block enterprise AI adoption. Security teams reject deployments that don't meet standards.

In this hands-on hackathon, you'll deploy an enterprise-ready AI application following Microsoft's Well-Architected Framework. You'll build a secure chat application using Azure AI Foundry with complete network isolation, private endpoints, managed identities, and zero public access.

## The Challenge

Deploy a secure AI chat application that meets enterprise security requirements:

- **Network Isolation**: Private VNETs, private endpoints, no public internet access
- **Identity Security**: Entra ID managed identities, RBAC, zero API keys in code
- **Data Protection**: Azure Key Vault for secrets, encrypted storage, private connectivity
- **Compliance**: WAF alignment, security posture validation, audit readiness

## What You'll Build

A fully secure AI chat application with:

1. **Azure AI Foundry Hub & Project** with private endpoints
2. **Azure OpenAI** deployed inside a private network
3. **Azure Key Vault** for secret management (no hardcoded credentials)
4. **Azure Storage** with private endpoints (for AI project assets)
5. **Virtual Network (VNET)** with proper subnet segmentation
6. **Network Security Groups (NSGs)** with restrictive rules
7. **Managed Identity** for passwordless authentication
8. **Pre-built Chat Application** with Streamlit UI (just configure & run)
9. **External access** via the VM's public IP for real-world testing

## Technologies Used

- **Azure AI Foundry**: Enterprise AI platform with built-in security
- **Azure OpenAI**: GPT-4.1 models with private endpoints
- **Azure Virtual Network**: Network isolation and segmentation
- **Private Endpoints**: Secure connectivity without public IPs
- **Azure Key Vault**: Centralized secret management
- **Azure Storage**: Secure blob storage with private access
- **Entra ID**: Identity and access management with RBAC
- **Managed Identity**: Passwordless authentication
- **Azure Bastion**: Secure RDP/SSH without public IPs
- **Network Security Groups**: Layer 4 firewall rules
- **Streamlit**: Python-based chat UI framework

## Learning Outcomes

By completing this Hack in a Day lab, you will:

### Security & Compliance
- Design secure AI architectures aligned with WAF principles
- Configure complete network isolation with VNETs and private endpoints
- Eliminate public endpoints and internet exposure
- Implement defense-in-depth security layers

### Identity & Access Management
- Deploy managed identities for passwordless authentication
- Configure Entra ID RBAC with least-privilege access
- Secure secrets in Azure Key Vault
- Understand service principal vs managed identity patterns

### Network Security
- Design VNET topology with proper subnet segmentation
- Configure NSG rules for restrictive traffic control
- Deploy and validate private endpoints
- Understand DNS resolution for private endpoints

### Infrastructure Automation
- Deploy and configure Azure resources via Portal and CLI
- Work with az CLI for resource management
- Implement repeatable configuration patterns
- Understand Azure resource relationships

## Challenge Structure

This hackathon consists of **5 progressive challenges**:

### Challenge 1: Deploy Core Azure Infrastructure
Manually create the foundational Azure resources via the Portal: Virtual Network with subnets, Windows VM with Bastion access, Microsoft Foundry with GPT-4.1 model deployment, Key Vault with RBAC authorization, and Storage Account. Install required development tools on the VM.

### Challenge 2: Configure Network Security & Isolation
Create Network Security Groups with restrictive rules, disable public access on all services, and deploy private endpoints for Key Vault, Azure OpenAI, and Storage Account. Validate private endpoint connectivity and DNS resolution.

### Challenge 3: Identity & Access Management with Entra ID
Enable managed identity on the VM, assign RBAC roles for Azure OpenAI, Key Vault, and Storage Account. Store all connection configuration securely in Key Vault. Implement fully passwordless authentication with zero API keys.

### Challenge 4: Secure Azure OpenAI Deployment
Verify the GPT model deployment, store model configuration in Key Vault, and test chat completions end-to-end using managed identity authentication through a Python test script.

### Challenge 5: Deploy and Run the Secure Chat Application
Download the pre-built secure chat application, configure it with your Key Vault name, install dependencies, and run it on the VM. Test chat functionality with managed identity, then make the application accessible from any device using the VM's public IP address.

## Success Criteria

Your deployment is ready when:

- All AI services are accessible only via private endpoints
- Managed identity is used for all authentication (zero API keys in code)
- All secrets are stored in Azure Key Vault
- NSG rules follow least-privilege principle
- Chat application works perfectly inside the isolated network
- Azure Bastion provides secure access (no RDP/SSH over internet)
- Application is accessible from any device via the VM's public IP on port 8501

## Resources

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/)
- [Azure Well-Architected Framework](https://learn.microsoft.com/azure/well-architected/)
- [Azure Private Link Documentation](https://learn.microsoft.com/azure/private-link/)
- [Managed Identity Best Practices](https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/overview)

Ready to build enterprise-grade AI? Let's get started! 