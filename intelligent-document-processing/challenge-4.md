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

1. Create a Storage Account for this lab:

   - In the Azure Portal click **Create a resource** → **Storage** → **Storage account**.  
   - Select **Subscription**
   - Select **Resource Group**: ODL-demolab-<inject key="DeploymentID"></inject>.
   - Choose **Region:** <inject key="Region"></inject>.
   - And enter a **Name**: storagefinanceidp<inject key="DeploymentID"></inject>.  
   - And click **Review + Create** → **Create**.  

1. To allow anonymous/public access for the container, configure it now:

   - Open the newly created Storage Account in the Azure Portal, select **Settings → Configuration** (or **Containers** → the container's Access level after you create it).  
   - Under **Blob public access**, set the option to enable public/anonymous access if your scenario requires it.  
   - Save the configuration changes. Note: Enabling anonymous access allows anyone with the blob URL to read blobs — only use this when necessary for demos and ensure you remove public access after the lab.

1. Open the **Storage Account** created in your environment.  

1. Select **Containers** from the left-hand menu.  

1. Click **+ Container** and configure:
   - **Name:** invoices-output-<inject key="DeploymentID"></inject>
   - **Public Access Level:** *(allow anonymous access)*  

1. Return to **Document Intelligence Studio** and click **Download Results** to save the invoice JSON output.  

1. In your container, click **Upload** → select the downloaded JSON file → click **Upload**.  

1. Refresh the container list to verify the uploaded file appears.

1. Copy the Storage Account name and access key for later use:

   - In the Storage Account blade, select **Access keys** under **Security + networking**.
   - Copy the **Storage account name** and **Key1** (connection string or key) and store them securely — you will need these to connect Power BI or programmatic clients.
   - Keep keys private; rotate or revoke them when the lab is complete.

<validation step="a25a62f8-6a37-4812-ad34-69f2b01476c2" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria
- Extracted data securely stored in Azure Blob Storage.  
- Files ready for analysis and visualization.

## Additional Resources
- [Azure Blob Storage Overview](https://learn.microsoft.com/azure/storage/blobs/storage-blobs-overview)  
- [Upload and Manage Blobs in Portal](https://learn.microsoft.com/azure/storage/blobs/storage-quickstart-blobs-portal)

Now, click **Next** to continue to **Challenge 05**.
