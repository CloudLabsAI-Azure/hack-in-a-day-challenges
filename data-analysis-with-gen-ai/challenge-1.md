# Challenge 01: Create and Review the Sample Manufacturing Dataset

## Introduction
Contoso Manufacturing operates a network of machines across multiple plants.  
Each machine logs temperature, vibration, and downtime events. Before using Generative AI to analyze this data, you’ll first upload and familiarize yourself with a synthetic dataset.

## Accessing the Datasets

Please copy the link below and paste it into a new browser tab inside your LabVM to download the required datasets and code files for the use case and extract them.

```
https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/c2-datasets.zip
```

## Challenge Objectives

- Access the sample manufacturing dataset provided in your lab environment.  
- Upload the dataset to Azure Storage for easy access.  
- Explore the data schema (columns such as timestamp, machine ID, temperature, status).

## Steps to Complete

1. In the Azure Portal, search **Storage Account** in the search bar and select it.

1. Create a **Storage Account** with: 
    
    - Subscription: Select the **defualt Subscription**.
    - Resource group: Select **challenge-rg-<inject key="DeploymentID"></inject>**.
    - Storage account name: Type **mfgdatagenai<inject key="DeploymentID"></inject>**.  
    - Region: **<inject key="Region"></inject>**.
    - Performance: **Standard**.
    - Redundancy: **Locally-redundant storage (LRS)**
    - Click **Review Create** and press **Create** again.

1. Open **Containers** → click **+ Container** → name it manufacturing-logs-<inject key="DeploymentID"></inject>.  

1. Set **Access Level** to *Private*.  

1. Upload the provided CSV files from the downloads folder. 

1. After upload, click the file and note the Blob URL (location for later use). 

1. (Optional) Open the CSV in Excel or VS Code to inspect columns and data range.

## Success Criteria

- Dataset uploaded successfully to Azure Blob Storage.  
- Data structure understood and ready for AI processing.

## Additional Resources

- [Quickstart: Upload data to Azure Blob Storage](https://learn.microsoft.com/azure/storage/blobs/storage-quickstart-blobs-portal)
- [Sample Manufacturing Data Generator (GitHub)](https://github.com/Azure-Samples)

Now, click **Next** to continue to **Challenge 02: Deploy Microsoft Foundry**.
