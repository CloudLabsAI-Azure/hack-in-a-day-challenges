# Challenge 01: Understand Fabric, OneLake & Medallion Architecture

## Introduction

Contoso Enterprises operates across multiple business units with data scattered across different systems-ERP, CRM, legacy databases, and unstructured file storage. To unify this data landscape, Contoso has decided to adopt Microsoft Fabric and OneLake as its single logical data lake. Before building data pipelines, it's essential to understand the platform architecture, OneLake's unified storage model, and the Medallion architecture pattern (Bronze → Silver → Gold) that will structure your data transformation journey.

## Accessing the Datasets

1. On your lab VM, open a terminal PowerShel.

1. Create a working directory:

   ```powershell
   mkdir C:\working-dir
   ```

1. **Download the code package**:
   
   Access the link mentioned below using browser:
   ```
   https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/unified-data-foundation-with-fabric.zip
   ```

1. **Extract the ZIP file**:
   
   - Right-click on the downloaded `unified-data-foundation-with-fabric.zip` file
   - Select the **Extract All...** option
   - Choose a location `C:\working-dir`
   - Click on **Extract**

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
   - **Workspace type**: Select **Fabric**   
   - **Details**: Ensure its selected to **fabriccapacity<inject key="DeploymentID" enableCopy="false"/>**.
   - **Semantic model storage format**: Keep **Small semantic model storage format**
   - Click **Apply**

1. The following illustrates the **Medallion Architecture** pattern that you will implement:

   - **Bronze Layer (Raw Zone)**: Stores raw, unprocessed data exactly as ingested from source systems (CSV, JSON, Parquet, logs)
   - **Silver Layer (Cleansed Zone)**: Contains validated, deduplicated, and standardized data with quality checks applied
   - **Gold Layer (Curated Zone)**: Business-level aggregates, star schemas, and domain-specific models ready for analytics

1. Create your first **Lakehouse** that will hold all three layers:

   - In the Fabric workspace which is **fabric-workspace-<inject key="DeploymentID" enableCopy="false"/>**
   - select **+ New**.
   - Search and Select **Lakehouse**.
   - Name: **contoso_lakehouse_<inject key="DeploymentID" enableCopy="false"/>**
   - Location: **fabric-workspace-<inject key="DeploymentID" enableCopy="false"/>**
   - Click **Create**

1. Within the Lakehouse, we will now create a folders for the Medallion layers:

1. In the **Files** section, create three folders:
   - **bronze**
   - **silver** 
   - **gold**

   > **Hint:** Hover over the **Files** folder, click the **...** and select **New subfolder**.

   > **Important:** Create the folders using the exact names shown above, ensuring the correct spelling and case sensitivity.

1. Take note of the **OneLake path** displayed in the properties:

   - Format: `abfss://[workspace]@onelake.dfs.fabric.microsoft.com/[lakehouse]/Files`
   - This path can be used across all Fabric workloads for unified data access

   > **Hint:** Hover over the **Files** folder, click the **...**, select **Properties**, and copy the OneLake path. Save this value in a Notepad file for later use.

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