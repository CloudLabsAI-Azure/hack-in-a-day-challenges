# Challenge 02: Ingest Raw Data into the Bronze Layer

## Introduction

Contoso Enterprises needs to consolidate data from multiple disparate sources—CSV files from legacy systems, Parquet files from cloud storage, ERP/CRM databases, and unstructured files like JSON logs and application events. The Bronze layer serves as the landing zone for all raw data before any transformation or cleansing. In this challenge, you will use Microsoft Fabric's Data Pipelines and Dataflows Gen2 to ingest structured and unstructured data from various sources into the Bronze layer of your Lakehouse.

## Challenge Objectives

- Access and verify sample dataset files downloaded in Challenge 01.
- Upload CSV files directly to the Bronze layer in Fabric Lakehouse.
- Optionally create Delta tables for direct SQL querying.
- Validate data ingestion using the Lakehouse Explorer.

## Steps to Complete

### Part 1: Access Sample Dataset Files

1. On the **LabVM**, open **File Explorer** and navigate to the dataset folder:

   ```
   C:\LabFiles\fabric-kyndr-uc1\dataset\
   ```

   > **Note:** If you haven't downloaded the datasets yet, refer to Challenge 01 for the download link and extract the ZIP file to `C:\LabFiles\`

1. Verify the following sample files are available:

   - `customers.csv` - Customer master data (848 records)
   - `orders.csv` - Sales order details (544 records)
   - `products.csv` - Product catalog (296 products)
   - `sales.csv` - Sales transaction data (32,720 records)

1. Keep the File Explorer window open for easy access during upload steps.

### Part 2: Upload Sample Data to Bronze Layer

1. In the **Edge browser**, navigate to the **Microsoft Fabric** portal (if not already open):

   ```
   https://app.fabric.microsoft.com/
   ```

1. Navigate to your **Microsoft Fabric workspace**: **fabric-workspace-<inject key="DeploymentID"></inject>**

1. Open your Lakehouse: **contoso-lakehouse-<inject key="DeploymentID"></inject>**

1. In the Lakehouse Explorer, navigate to **Files** → **bronze** folder.

1. Upload **customers.csv** to Bronze layer:

   - Click the **...** (more options) next to the **bronze** folder
   - Select **Upload** → **Upload files**
   - Browse to `C:\LabFiles\fabric-kyndr-uc1\dataset\`
   - Select **customers.csv**
   - Click **Upload**

1. Repeat the upload process for the remaining files:

   - **orders.csv** → Upload to `bronze/` folder
   - **products.csv** → Upload to `bronze/` folder
   - **sales.csv** → Upload to `bronze/` folder

1. Verify all files are uploaded:

   - Navigate to **Files** → **bronze**
   - Confirm you see all 4 CSV files listed

### Part 3: Load CSV Files as Delta Tables (Optional - For Direct Querying)

1. In the Lakehouse, you can optionally convert CSV files to Delta tables:

   - Right-click on **customers.csv** in the bronze folder
   - Select **Load to Tables**
   - Table name: **bronze_customers**
   - Click **Load**

1. Repeat for other CSV files if needed:

   - **orders.csv** → **bronze_orders**
   - **products.csv** → **bronze_products**
   - **sales.csv** → **bronze_sales**

   > **Note:** This step is optional. In Part 3 (Challenge 3), you'll read directly from CSV files in the bronze folder.

### Part 4: Validate Bronze Layer Ingestion

1. Navigate to your **Lakehouse**: **contoso-lakehouse-<inject key="DeploymentID"></inject>** (if not already open)

1. In the **Files** section, verify the bronze folder contains:

   - `customers.csv`
   - `orders.csv`
   - `products.csv`
   - `sales.csv`

1. Click on any CSV file to preview its contents and verify data loaded correctly.

1. If you created Delta tables in Part 3, query them using SQL analytics endpoint:

   - Click on **SQL analytics endpoint** in the top-right corner
   - Run a query:

   ```sql
   -- Query bronze tables if created
   SELECT COUNT(*) as TotalCustomers FROM bronze_customers;
   SELECT TOP 10 * FROM bronze_sales ORDER BY OrderDate DESC;
   ```


> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Sample dataset files located in the LabVM.
- All 4 CSV files (customers, orders, products, sales) uploaded to Bronze layer in Lakehouse.
- Files are visible in the Lakehouse Files explorer under the bronze folder.
- File preview shows data loaded correctly.
- (Optional) Delta tables created from CSV files for direct SQL querying.

## Additional Resources

- [Data Pipelines in Microsoft Fabric](https://learn.microsoft.com/fabric/data-factory/data-factory-overview)
- [Dataflows Gen2 in Microsoft Fabric](https://learn.microsoft.com/fabric/data-factory/dataflows-gen2-overview)
- [Copy Activity in Data Pipelines](https://learn.microsoft.com/fabric/data-factory/copy-data-activity)
- [Lakehouse Files and Tables](https://learn.microsoft.com/fabric/data-engineering/lakehouse-overview)

Now, click **Next** to continue to **Challenge 03**.
