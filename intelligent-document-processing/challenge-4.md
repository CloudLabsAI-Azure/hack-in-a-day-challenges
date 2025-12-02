# Challenge 04: Store Extracted Results in Azure Storage

## Introduction
After validating the invoice data, Contoso Finance needs a secure way to store the extracted results.  
Azure Blob Storage provides a cost-effective, scalable, and durable location to keep structured data for auditing and analytics.

In this challenge, you will create a container in Azure Storage and upload the extracted invoice data.

## Challenge Objectives
- Create a Blob container for storing extracted data.  
- Upload JSON output files from Document Intelligence Studio.  
- Confirm successful upload and private access configuration.

## Steps to Complete
1. Createe a Storage Account for this lab:

   - In the Azure Portal click **Create a resource** → **Storage** → **Storage account**.  
   - Provide **Subscription**, create/select **Resource Group**, choose **Region:** <inject key="Region"></inject>, and enter a **Name**: storagefinanceidp1979712<inject key="GET-DEPLOYMENT-ID"></inject>.  
   - Leave default performance/replication options for the lab and click **Review + Create** → **Create**.  

2. To allow anonymous/public access for the container, configure it now:

   - Open the newly created Storage Account in the Azure Portal, select **Settings → Configuration** (or **Containers** → the container's Access level after you create it).  
   - Under **Blob public access**, set the option to enable public/anonymous access if your scenario requires it.  
   - Save the configuration changes. Note: Enabling anonymous access allows anyone with the blob URL to read blobs — only use this when necessary for demos and ensure you remove public access after the lab.

3. Open the **Storage Account** created in your environment.  
3. Select **Containers** from the left-hand menu.  
4. Click **+ Container** and configure:
   - **Name:** invoices-output-<inject key="GET-DEPLOYMENT-ID"></inject>
   - **Public Access Level:** *(allow anonymous access)*  
5. Return to **Document Intelligence Studio** and click **Download Results** to save the invoice JSON output.  
6. In your container, click **Upload** → select the downloaded JSON file → click **Upload**.  
7. Refresh the container list to verify the uploaded file appears.

## Success Criteria
- Extracted data securely stored in Azure Blob Storage.  
- Files ready for analysis and visualization.

## Additional Resources
- [Azure Blob Storage Overview](https://learn.microsoft.com/azure/storage/blobs/storage-blobs-overview)  
- [Upload and Manage Blobs in Portal](https://learn.microsoft.com/azure/storage/blobs/storage-quickstart-blobs-portal)

Now, click **Next** to continue to **Challenge 05: Visualize Extracted Invoice Summary**.
