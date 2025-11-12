# Challenge 01: Create and Review the Sample Manufacturing Dataset

## Introduction
Contoso Manufacturing operates a network of machines across multiple plants.  
Each machine logs temperature, vibration, and downtime events. Before using Generative AI to analyze this data, you’ll first upload and familiarize yourself with a synthetic dataset.

## Accessing the Azure portal

1. To access the Azure portal, click on the **Azure Portal** Microsoft edge shortcut that is created in the desktop.

1. On the Sign in to Microsoft Azure tab, you will see a login screen. Enter the following email/username, and then click on Next.

   - Email/Username: <inject key="AzureAdUserEmail"></inject>

   - Password: <inject key="AzureAdUserPassword"></inject>

1. If you see the pop-up Stay Signed in?, click No.

1. If you see the pop-up You have free Azure Advisor recommendations!, close the window to continue with the challenge.

1. If a Welcome to Microsoft Azure pop-up window appears, click Cancel to skip the tour.

## Challenge Objectives
- Access the sample manufacturing dataset provided in your lab environment.  
- Upload the dataset to Azure Storage for easy access.  
- Explore the data schema (columns such as timestamp, machine ID, temperature, status).

## Steps to Complete
1. In the Azure Portal, create a **Storage Account** (named `mfgdata<uniqueID>`).  
2. Open **Containers** → click **+ Container** → name it `manufacturing-logs`.  
3. Set **Access Level** to *Private*.  
4. Upload the provided CSV file (`machine_sensor_data.csv`) from the lab VM or downloads folder.  
5. After upload, click the file and note the Blob URL (location for later use).  
6. (Optional) Open the CSV in Excel or VS Code to inspect columns and data range.

## Success Criteria
- Dataset uploaded successfully to Azure Blob Storage.  
- Data structure understood and ready for AI processing.

## Additional Resources
- [Quickstart: Upload data to Azure Blob Storage](https://learn.microsoft.com/azure/storage/blobs/storage-quickstart-blobs-portal)
- [Sample Manufacturing Data Generator (GitHub)](https://github.com/Azure-Samples)

Now, click **Next** to continue to **Challenge 02: Deploy Azure OpenAI Service**.
