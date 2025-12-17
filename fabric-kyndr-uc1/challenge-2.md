# Challenge 02: Ingest Raw Data into the Bronze Layer

## Introduction

Contoso Enterprises needs to consolidate data from multiple disparate sources—CSV files from legacy systems, Parquet files from cloud storage, ERP/CRM databases, and unstructured files like JSON logs and application events. The Bronze layer serves as the landing zone for all raw data before any transformation or cleansing. In this challenge, you will use Microsoft Fabric's Data Pipelines and Dataflows Gen2 to ingest structured and unstructured data from various sources into the Bronze layer of your Lakehouse.

## Challenge Objectives

- Use **Data Pipelines** to orchestrate data ingestion from Azure Blob Storage.
- Use **Dataflows Gen2** to ingest CSV and Parquet files.
- Ingest sample ERP/CRM tables into Bronze as-is.
- Load unstructured files (JSON, logs) into the Bronze Files section.
- Validate data ingestion using the Lakehouse Explorer.

## Steps to Complete

### Part 1: Set Up Sample Data Source

1. In the **Azure Portal**, create a **Storage Account** for sample source data:

   - Subscription: **Select the default Subscription**
   - Resource Group: **challenge-rg-<inject key="DeploymentID"></inject>**
   - Storage Account Name: **contosodata<inject key="DeploymentID"></inject>**
   - Region: **<inject key="Region"></inject>**
   - Performance: **Standard**
   - Redundancy: **Locally-redundant storage (LRS)**

1. Inside the Storage Account, under **Data storage** section, create a **container** named:

   - Name: **raw-source-data**

1. Upload sample files to the container (download provided sample datasets):

   - `customers.csv` - Customer master data
   - `orders.parquet` - Sales orders
   - `products.csv` - Product catalog
   - `transactions.json` - Transaction logs (unstructured)
   - `app-logs.txt` - Application logs

   > **Note:** Sample files should be extracted from the provided dataset package in your lab environment.

### Part 2: Create Data Pipeline for Structured Data Ingestion

1. In the **Edge browser**, navigate to the **Microsoft Fabric** portal (if not already open):

   ```
   https://app.fabric.microsoft.com/
   ```

1. Navigate to your **Microsoft Fabric workspace**: **fabric-workspace-<inject key="DeploymentID"></inject>**

1. Select **+ New** → **Data Pipeline**

   - Name: **Bronze-Ingestion-Pipeline**

1. In the pipeline canvas, add a **Copy Data** activity:

   - Activity name: **Copy-Customers-CSV**

1. Configure the **Source** settings:

   - Connection: Create new connection to **Azure Blob Storage**
   - Storage account: **contosodata<inject key="DeploymentID"></inject>**
   - Container: **raw-source-data**
   - File path: **customers.csv**
   - File format: **DelimitedText**
   - First row as header: **Checked**

1. Configure the **Destination** settings:

   - Workspace: **fabric-workspace-<inject key="DeploymentID"></inject>**
   - Lakehouse: **contoso-lakehouse-<inject key="DeploymentID"></inject>**
   - Root folder: **Files**
   - File path: **bronze/customers/**
   - File format: **Parquet** (preserve raw data in optimized format)

1. Add additional **Copy Data** activities for:

   - **Copy-Orders-Parquet**: Source `orders.parquet` → Destination `bronze/orders/`
   - **Copy-Products-CSV**: Source `products.csv` → Destination `bronze/products/`

1. **Save** and **Run** the pipeline:

   - Click **Run** from the toolbar
   - Monitor execution in the **Output** pane
   - Verify all activities complete successfully

### Part 3: Ingest Unstructured Data (JSON & Logs)

1. In the Fabric workspace, create a new **Dataflow Gen2**:

   - Name: **Bronze-Unstructured-Ingestion**

1. Select **Get Data** → **Azure Blob Storage**

1. Connect to the storage account and select **transactions.json**

1. In the Power Query editor:

   - Keep the JSON structure as-is (no transformations)
   - Set destination to: **bronze/transactions/** in the Lakehouse

1. Add another query to ingest **app-logs.txt**:

   - Destination: **bronze/logs/**

1. Click **Publish** to save and run the dataflow

### Part 4: Create Bronze Tables from ERP/CRM Sample Data

1. In the Fabric workspace, select **+ New** → **Dataflow Gen2**

   - Name: **Bronze-ERP-CRM-Ingestion**

1. Select **Get Data** → **Blank table** (for simulation of ERP data)

   > **Note:** In production, you would connect to actual ERP/CRM systems using connectors like SAP, Dynamics 365, Salesforce, etc.

1. Create a sample ERP table with columns:

   ```
   OrderID, CustomerID, OrderDate, Amount, Region, Status
   ```

1. Add sample rows manually or import from CSV provided in lab files

1. Set destination:

   - Lakehouse: **contoso-lakehouse-<inject key="DeploymentID"></inject>**
   - Table name: **bronze_erp_orders**
   - Write mode: **Append**

1. **Publish** the dataflow

### Part 5: Validate Bronze Layer Ingestion

1. Navigate to your **Lakehouse**: **contoso-lakehouse-<inject key="DeploymentID"></inject>**

1. In the **Files** section, verify the following folders contain data:

   - `bronze/customers/`
   - `bronze/orders/`
   - `bronze/products/`
   - `bronze/transactions/`
   - `bronze/logs/`

1. In the **Tables** section, verify:

   - **bronze_erp_orders** table exists and contains records

1. Query the data using SQL analytics endpoint:

   ```sql
   SELECT COUNT(*) FROM bronze_erp_orders;
   SELECT * FROM bronze_erp_orders LIMIT 10;
   ```

<validation step="b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e" />

> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Storage Account created and sample files uploaded successfully.
- Data Pipeline created and executed to ingest structured files into Bronze layer.
- Dataflow Gen2 used to ingest unstructured JSON and log files.
- Bronze layer validated with all expected files and tables present in Lakehouse Explorer.
- SQL queries return data from Bronze tables successfully.

## Additional Resources

- [Data Pipelines in Microsoft Fabric](https://learn.microsoft.com/fabric/data-factory/data-factory-overview)
- [Dataflows Gen2 in Microsoft Fabric](https://learn.microsoft.com/fabric/data-factory/dataflows-gen2-overview)
- [Copy Activity in Data Pipelines](https://learn.microsoft.com/fabric/data-factory/copy-data-activity)
- [Lakehouse Files and Tables](https://learn.microsoft.com/fabric/data-engineering/lakehouse-overview)

Now, click **Next** to continue to **Challenge 03**.
