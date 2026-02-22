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
9. **Azure App Service** deployment with VNet integration

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
- **Azure App Service**: PaaS hosting with VNet integration
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

This hackathon consists of **7 progressive challenges**:

### Challenge 1: Deploy Core Azure Infrastructure
Manually create the foundational Azure resources via the Portal: Virtual Network with subnets, Windows VM, Microsoft Foundry with GPT Model, Key Vault, Storage Account, and Azure Bastion.

### Challenge 2: Configure Network Security & Isolation
Configure Network Security Groups, disable all public access, and validate private endpoint connectivity. Ensure zero internet exposure for AI services.

### Challenge 3: Identity & Access Management with Entra ID
Set up managed identities, configure RBAC roles, and establish Key Vault access policies. Implement passwordless authentication patterns.

### Challenge 4: Secure Azure OpenAI Deployment
Deploy the GPT model with a private endpoint, configure deployment settings, and secure API configuration in Key Vault. Test private connectivity.

### Challenge 5: Deploy and Configure the Chat Application
Download the pre-built secure chat application, configure environment variables with private endpoints, and run the application on your VM.

### Challenge 6: Test Secure Connectivity via Azure Bastion
Connect to the VM using Azure Bastion (no public IP needed), validate the chat application works, and verify all traffic flows through the private network.

### Challenge 7: Deploy Application to Azure App Service
Deploy the chat application to Azure App Service with VNet integration, managed identity, and private endpoint connectivity. Verify the deployment works end-to-end.

## Success Criteria

Your deployment is ready when:

- All services are accessible only via private endpoints
- No public IP addresses are exposed
- Managed identity is used for all authentication (zero API keys in code)
- All secrets are stored in Azure Key Vault
- NSG rules follow least-privilege principle
- Chat application works perfectly inside the isolated network
- Azure Bastion provides secure access (no RDP/SSH over internet)
- Application deployed to Azure App Service
- App Service uses managed identity and private endpoints

## Resources

- [Azure App Service Documentation](https://learn.microsoft.com/azure/app-service/)
- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/)
- [Azure Well-Architected Framework](https://learn.microsoft.com/azure/well-architected/)
- [Azure Private Link Documentation](https://learn.microsoft.com/azure/private-link/)
- [Managed Identity Best Practices](https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/overview)

Ready to build enterprise-grade AI? Let's get started! 