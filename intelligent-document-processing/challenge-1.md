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

1. In the Azure Portal, search for **Document Intelligence** and click **Create**. 

1. Under **Basics**, provide:
   - **Subscription:** Use the available subscription.  
   - **Resource Group:** Select challenge-rg-<inject key="DeploymentID"></inject>.  
   - **Region:** <inject key="Region"></inject>.  
   - **Name:** `finance-doc-intl-<inject key="DeploymentID"></inject>.  
   - **Pricing Tier:** Choose *Free (F0)* or *Standard (S0)*.  

1. Click **Review + Create** → **Create**.  

1. After deployment succeeds, open the resource.  

<validation step="54001904-186d-42a7-bee3-a6508c5797c5" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Azure AI Document Intelligence resource deployed successfully.  
- Endpoint and API Key recorded for future use.  

## Additional Resources

- [Azure AI Document Intelligence Overview](https://learn.microsoft.com/azure/ai-services/document-intelligence/overview)  
- [Quickstart: Create Document Intelligence Resource](https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/create-resource)

Now, click **Next** to continue to **Challenge 02**.
