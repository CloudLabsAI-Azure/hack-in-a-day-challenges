# Challenge 02: Ingest Raw Data into the Bronze Layer

## Introduction

Contoso Enterprises needs to consolidate data from multiple disparate sources-CSV files from legacy systems, Parquet files from cloud storage, ERP/CRM databases, and unstructured files like JSON logs and application events. The Bronze layer serves as the landing zone for all raw data before any transformation or cleansing. In this challenge, you will use Microsoft Fabric's Data Pipelines and Dataflows Gen2 to ingest structured and unstructured data from various sources into the Bronze layer of your Lakehouse.

## Challenge Objectives

- Access and verify the sample dataset files downloaded in Challenge 01.
- Upload CSV files directly to the Bronze layer in Fabric Lakehouse.

## Steps to Complete

### Part 1: Access Sample Dataset Files

1. On the **LabVM**, open **File Explorer** and navigate to the dataset folder from `C:\working-dir\hack-in-a-day-challenges-unified-data-foundation-with-fabric` (or to the location where the files were extracted).

   > **Note:** If you haven't downloaded the datasets yet, refer to Challenge 01 for the download link and extract the ZIP file.
   
1. Verify the following sample files are available:

   - `flight.csv` - Flight loyalty program data with data quality issues (62,990 records)
   - `customer_transactions.json` - Customer transaction data in JSON format with inconsistencies (15 records)

      > **Note:** These datasets intentionally contain data quality issues (nulls, duplicates, inconsistent formatting) to demonstrate real-world data cleansing scenarios.

1. Keep the File Explorer window open for easy access during upload steps.

### Part 2: Upload Sample Data to Bronze Layer

1. In the **Edge browser**, navigate to the **Microsoft Fabric** portal (if not already open):

   ```
   https://app.fabric.microsoft.com/
   ```

1. Navigate to your **Microsoft Fabric workspace**: **fabric-workspace-<inject key="DeploymentID" enableCopy="false"/>**

1. Open your Lakehouse: **contoso-lakehouse-<inject key="DeploymentID" enableCopy="false"/>** 

   > **Note:** Select the **Lakehouse** where the type is Lakehouse.

1. In the Lakehouse Explorer, navigate to **Files** and then click on **bronze** folder.

1. Upload **flight.csv** to Bronze layer:

   - Click the **...** (more options) next to the **bronze** folder
   - Select **Upload** and click on **Upload files**
   - Browse to the dataset extracted folder.
   - Select **flight.csv** and **customer_transactions.json**.
   - Click **Upload**

1. Verify all files are uploaded:

   - Navigate to **Files** and click on **bronze** fodler.

1. Confirm you see:

   - `flight.csv` (CSV format)
   - `customer_transactions.json` (JSON format)

### Part 3: Preview Raw Data and Identify Quality Issues

1. In the Lakehouse, preview the **flight.csv** file:

   - Click on **flight.csv** in the bronze folder
   - Review the data preview

1. Observe data quality issues:
   - Missing values represented as "." or empty strings
   - Inconsistent city/province names (e.g., "beijing", ".", empty)
   - Mixed data types in some columns

1. Preview the **customer_transactions.json** file:

   - Click on **customer_transactions.json**
   - Review the JSON structure

1. Observe data quality issues:
   - Null values in critical fields (customer_id, amount)
   - Inconsistent status values ("completed", "COMPLETED", "pending", "PENDING")
   - Duplicate transactions
   - Invalid email formats
   - Inconsistent date formats
   - Mixed case region names

      > **Note:** In Challenge 3, you'll clean and standardize this data as part of the Bronze to Silver transformation.

## Success Criteria

- Sample dataset files located in the LabVM at `C:\LabFiles\unified-data-foundation-with-fabric\dataset\`.
- Both files (flight.csv and customer_transactions.json) were uploaded successfully to the Bronze layer.
- Files are visible in the Lakehouse Files explorer under the bronze folder.

## Additional Resources

- [Data Pipelines in Microsoft Fabric](https://learn.microsoft.com/fabric/data-factory/data-factory-overview)
- [Dataflows Gen2 in Microsoft Fabric](https://learn.microsoft.com/fabric/data-factory/dataflows-gen2-overview)
- [Copy Activity in Data Pipelines](https://learn.microsoft.com/fabric/data-factory/copy-data-activity)
- [Lakehouse Files and Tables](https://learn.microsoft.com/fabric/data-engineering/lakehouse-overview)

Now, click **Next** to continue to **Challenge 03**.
