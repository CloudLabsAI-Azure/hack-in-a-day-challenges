# Challenge 01: Create Azure AI Document Intelligence Resource

## Introduction
Contoso Finance, a leading enterprise, processes hundreds of invoices daily. Manual data entry from PDFs and scans causes frequent errors and delays.  
To solve this, Contoso plans to implement an **AI-based invoice automation solution** using **Azure AI Document Intelligence**.  
This service extracts structured data such as invoice numbers, totals, vendor names, and dates, saving hours of repetitive manual effort.

In this challenge, you’ll create the **Azure AI Document Intelligence** resource — the foundation for the rest of your Intelligent Document Processing solution.

## Accessing the Datasets

Please download and extract the datasets required for this challenge here - [Datasets](https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/c1-datasets.zip)

   ```
   https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/c1-datasets.zip/
   ```

## Challenge Objectives
- Create a **Document Intelligence** resource in the Azure Portal.  
- Configure correct region, resource group, and pricing tier.  
- Retrieve the **Endpoint** and **API Key** for later use.  

## Steps to Complete
1. In the Azure Portal, select **Create a resource**.  
2. Search for **Document Intelligence** and click **Create**.  
3. Under **Basics**, provide:
   - **Subscription:** Use the available subscription.  
   - **Resource Group:** Select ODL-demolab-<inject key="DeploymentID"></inject>.  
   - **Region:** <inject key="Region"></inject>.  
   - **Name:** `finance-doc-intl-<inject key="DeploymentID"></inject>.  
   - **Pricing Tier:** Choose *Free (F0)* or *Standard (S0)*.  
4. Click **Review + Create** → **Create**.  
5. After deployment succeeds, open the resource.  

## Success Criteria
- Azure AI Document Intelligence resource deployed successfully.  
- Endpoint and API Key recorded for future use.  

## Additional Resources
- [Azure AI Document Intelligence Overview](https://learn.microsoft.com/azure/ai-services/document-intelligence/overview)  
- [Quickstart: Create Document Intelligence Resource](https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/create-resource)

Now, click **Next** (bottom right corner) to continue to **Challenge 02: Extract Data Using the Prebuilt Invoice Model**.
