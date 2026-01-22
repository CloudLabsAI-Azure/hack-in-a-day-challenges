# Challenge 01: Upload and Review Network Telemetry and Incident Data

## Introduction

Telecom networks generate continuous telemetry data and incident reports that are critical for monitoring performance and diagnosing issues.  
Before applying Generative AI for network diagnostics, this data must be stored in a centralized and searchable location.

In this challenge, you will upload synthetic network telemetry and incident documents into Azure Blob Storage, forming the foundation for the Network Diagnostics and Optimization Assistant.

## Challenge Objectives

- Create an Azure Storage Account for telecom diagnostics data  
- Upload synthetic network telemetry and incident reports  
- Review the dataset to ensure it is suitable for AI-driven analysis

## Accessing the Datasets

Please download and extract the synthetic datasets and code files required for this challenge by using this below labfiles link in your LabVM browser tab:

```
https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/telecom-labfiles.zip
```

> Once the file is downloaded, please extract it in any desired path in the LabVM. You will be able to see `code-files` and `datasets` folders.

## Steps to Complete

1. Sign in to the **Azure Portal**.

1. Search for **Storage accounts** and select **Create**.

1. Create a **Storage Account** with the following settings:

   - Subscription: Select the **default Subscription**
   - Resource group: **agentic-ai-<inject key="DeploymentID"></inject>**
   - Storage account name: **storage<inject key="DeploymentID"></inject>**
   - Region: **<inject key="Region"></inject>**
   - Performance: **Standard**
   - Redundancy: **Locally-redundant storage (LRS)**

1. Click **Review + Create**, then select **Create**.

1. Once deployment completes, open the Storage Account.

1. Under **Data storage**, select **Containers** → **+ Container**.

1. Create a container with:

   - Name: **datasets**
   - Public access level: **Private (no anonymous access)**

1. In the extracted labfiles folder, which you have performed earlier in this challenge, you will find a datasets folder, inside which you will be able to find the documents.

1. Upload the synthetic telecom telemetry and incident analysis documents into the **datasets** container.

1. Review the uploaded files to understand the structure of telemetry summaries, detected issues, and recommended actions.

## Success Criteria

- Storage Account created successfully  
- **datasets** container created  
- Network telemetry and incident documents uploaded  
- Dataset ready for indexing and AI diagnostics  

## Additional Resources

- [Azure Blob Storage Overview](https://learn.microsoft.com/azure/storage/blobs/)
- [AI for Telecom Networks](https://learn.microsoft.com/azure/architecture/industries/telecommunications/)

Now, click **Next** to continue to **Challenge 02**.
