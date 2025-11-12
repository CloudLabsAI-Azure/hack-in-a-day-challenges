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
1. Open the **Storage Account** created in your environment.  
2. Select **Containers** from the left-hand menu.  
3. Click **+ Container** and configure:
   - **Name:** `invoices-output`
   - **Public Access Level:** *Private (no anonymous access)*  
4. Return to **Document Intelligence Studio** and click **Download Results** to save the invoice JSON output.  
5. In your container, click **Upload** → select the downloaded JSON file → click **Upload**.  
6. Refresh the container list to verify the uploaded file appears.

## Success Criteria
- Extracted data securely stored in Azure Blob Storage.  
- Files ready for analysis and visualization.

## Additional Resources
- [Azure Blob Storage Overview](https://learn.microsoft.com/azure/storage/blobs/storage-blobs-overview)  
- [Upload and Manage Blobs in Portal](https://learn.microsoft.com/azure/storage/blobs/storage-quickstart-blobs-portal)

Now, click **Next** to continue to **Challenge 05: Visualize Extracted Invoice Summary**.
