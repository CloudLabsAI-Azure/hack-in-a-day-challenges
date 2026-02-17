# Challenge 01: Understand Fabric, OneLake & Medallion Architecture

## Introduction

Contoso Enterprises operates across multiple business units with data scattered across different systems—ERP, CRM, legacy databases, and unstructured file storage. To unify this data landscape, Contoso has decided to adopt Microsoft Fabric and OneLake as its single logical data lake. Before building data pipelines, it's essential to understand the platform architecture, OneLake's unified storage model, and the Medallion architecture pattern (Bronze → Silver → Gold) that will structure your data transformation journey.

## Accessing the Datasets

Please copy the link below and paste it into a new browser tab inside your LabVM to download the required datasets for the lab and extract them.

```
https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/unified-data-foundation-with-fabric.zip
```

> **Note:** Extract the downloaded ZIP file to `C:\LabFiles\` so that the dataset folder is located at `C:\LabFiles\unified-data-foundation-with-fabric\dataset\`

## Challenge Objectives

- Explore Microsoft Fabric workspace and understand its key components.
- Learn about OneLake as a single logical data lake for all analytics workloads.
- Understand the Medallion architecture pattern: Bronze (raw data), Silver (cleansed data), and Gold (curated business models).
- Create a new Lakehouse in Microsoft Fabric to serve as your data foundation.

## Steps to Complete

### Task 1: Create Fabric Workspace

1. In the **Edge browser**, navigate to the **Microsoft Fabric** portal.

   ```
   https://app.fabric.microsoft.com/
   ```

   > **Note:** If prompted, sign in with the provided credentials: <inject key="AzureAdUserEmail"></inject>

1. Click on **Workspaces** from the left navigation pane.

1. Click **+ New workspace** to create a workspace:

   - **Workspace Name**: **fabric-workspace-<inject key="DeploymentID" enableCopy="false"/>**
   - **Description**: **Contoso unified analytics workspace**

1. In the **Advanced settings** section:
   - **Workspace type**: Select **Fabric Trial**  
   - **Fabric capacity**: Keep the default  
   - **Semantic model storage format**: Keep **Small semantic model storage format**

      > **Note:** If you are unable to use the **Fabric Trial** and have deployed a Fabric capacity from the Azure portal, select **Fabric** as the **Workspace type**, and then choose the Fabric capacity that you deployed in Azure. Make sure the workspace is assigned to an active Fabric capacity, or it will not function properly.

1. Click **Apply**

1. Once the workspace is created, explore the **Home** page to familiarize yourself with Fabric components:

   - **Data Engineering**: Lakehouses, Data Pipelines, Notebooks
   - **Data Science**: ML models, experiments
   - **Data Warehouse**: SQL analytics endpoints
   - **Real-Time Analytics**: Event streams and KQL databases
   - **Power BI**: Reports and dashboards

1. Navigate to the **OneLake catalog** from the left navigation pane to understand:

   - OneLake provides a **single unified namespace** for all data across your organization
   - All Fabric workloads (Lakehouses, Warehouses, KQL databases) automatically store data in OneLake
   - OneLake uses **Delta Lake** format by default for transactional consistency

1. Review the **Medallion Architecture** pattern you'll implement:

   - **Bronze Layer (Raw Zone)**: Stores raw, unprocessed data exactly as ingested from source systems (CSV, JSON, Parquet, logs)
   - **Silver Layer (Cleansed Zone)**: Contains validated, deduplicated, and standardized data with quality checks applied
   - **Gold Layer (Curated Zone)**: Business-level aggregates, star schemas, and domain-specific models ready for analytics

1. Create your first **Lakehouse** that will hold all three layers:

   - In the Fabric workspace, select **+ New** → **Lakehouse**
   - Name: **contoso_lakehouse_<inject key="DeploymentID" enableCopy="false"/>**
   - Click **Create**

1. Once created, explore the Lakehouse structure:

   - **Files**: For storing raw files (Bronze layer)
   - **Tables**: For Delta Lake tables (Silver and Gold layers)
   - **SQL analytics endpoint**: For querying tables using T-SQL

1. Within the Lakehouse, create a folder structure for the Medallion layers:

1. In the **Files** section, create three folders:
   - **bronze**
   - **silver** 
   - **gold**

   > **Hint:** Click on the **...** (more options) next to Files and select **New subfolder**.

1. Take note of the **OneLake path** displayed in the properties:

   - Format: `abfss://[workspace]@onelake.dfs.fabric.microsoft.com/[lakehouse]/Files`
   - This path can be used across all Fabric workloads for unified data access

## Success Criteria

- Microsoft Fabric workspace created successfully.
- Understanding of OneLake as a unified data lake is demonstrated.
- Medallion architecture pattern (Bronze → Silver → Gold) explained.
- Lakehouse created with proper folder structure for data layers.

## Additional Resources

- [What is Microsoft Fabric?](https://learn.microsoft.com/fabric/get-started/microsoft-fabric-overview)
- [OneLake Overview](https://learn.microsoft.com/fabric/onelake/onelake-overview)
- [Medallion Architecture in Fabric](https://learn.microsoft.com/fabric/onelake/onelake-medallion-lakehouse-architecture)
- [Create a Lakehouse in Microsoft Fabric](https://learn.microsoft.com/fabric/data-engineering/create-lakehouse)

Now, click **Next** to continue to **Challenge 02**.