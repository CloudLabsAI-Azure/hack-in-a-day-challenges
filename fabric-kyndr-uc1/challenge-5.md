# Challenge 05: Integrate Azure Databricks Workloads

## Introduction

Contoso's data science team uses Azure Databricks for advanced machine learning and large-scale data processing. To avoid data silos and duplication, the team needs seamless access to the unified data stored in Microsoft Fabric's OneLake. Microsoft Fabric provides enterprise interoperability with Azure Databricks through OneLake integration—enabling Databricks clusters to directly read and write Delta Lake tables stored in Fabric Lakehouses. In this challenge, you will integrate Azure Databricks with your Fabric Lakehouse, demonstrating how both platforms can work together on the same data without data movement.

## Challenge Objectives

- Create an Azure Databricks workspace.
- Configure OneLake integration with Azure Databricks.
- Access Fabric Lakehouse Delta tables from Databricks notebooks.
- Perform data science workloads on Gold layer data using Databricks.
- Write enriched data back to Fabric Lakehouse from Databricks.

## Steps to Complete

### Part 1: Create Azure Databricks Workspace

1. In the **Azure Portal**, search for **Azure Databricks**.

1. Click **Create** to provision a new Databricks workspace:

   - Subscription: **Select the default Subscription**
   - Resource Group: **challenge-rg-<inject key="DeploymentID"></inject>**
   - Workspace Name: **contoso-databricks-<inject key="DeploymentID"></inject>**
   - Region: **<inject key="Region"></inject>**
   - Pricing Tier: **Premium** (required for Unity Catalog and OneLake integration)

1. Click **Review + Create** → **Create**

1. Once deployment completes, click **Launch Workspace** to open Azure Databricks.

### Part 2: Configure OneLake Access from Databricks

1. In the **Edge browser**, navigate to the **Microsoft Fabric** portal:

   ```
   https://app.fabric.microsoft.com/
   ```

1. Navigate to your workspace: **fabric-workspace-<inject key="DeploymentID"></inject>**

1. Open your Lakehouse: **contoso-lakehouse-<inject key="DeploymentID"></inject>**

1. Copy the **OneLake path** from the Lakehouse properties:

   - Format: `abfss://[workspace]@onelake.dfs.fabric.microsoft.com/[lakehouse]/Files`
   - Example: `abfss://fabric-workspace-12345@onelake.dfs.fabric.microsoft.com/contoso-lakehouse-12345.Lakehouse/Files`

   > **Important:** Note down this path for Databricks configuration.

1. In the Azure Portal, go to **Microsoft Entra ID** (formerly Azure Active Directory):

   - Navigate to **App registrations** → **New registration**
   - Name: **databricks-fabric-integration**
   - Click **Register**

1. After registration, note down:

   - **Application (client) ID**
   - **Directory (tenant) ID**

1. Create a **Client Secret**:

   - Go to **Certificates & secrets** → **New client secret**
   - Description: **OneLake Access**
   - Expiry: **12 months**
   - Click **Add** and **copy the secret value immediately**

1. Grant permissions to access Fabric:

   - In the Fabric workspace, go to **Manage access**
   - Add the service principal (app registration) as **Contributor**

### Part 3: Create Databricks Cluster and Configure Access

1. In the **Azure Databricks workspace**, create a new **Compute cluster**:

   - Cluster name: **contoso-analytics-cluster**
   - Cluster mode: **Single Node** (for lab purposes)
   - Databricks Runtime: **13.3 LTS** or later (includes Delta Lake support)
   - Node type: **Standard_DS3_v2**
   - Click **Create Cluster**

1. While the cluster is starting, create a **Databricks notebook**:

   - Click **Create** → **Notebook**
   - Name: **Fabric-OneLake-Integration**
   - Language: **Python**
   - Cluster: **contoso-analytics-cluster**

1. In the notebook, configure OneLake access using the service principal:

   ```python
   # Configure OneLake access credentials
   tenant_id = "<your-tenant-id>"
   client_id = "<your-client-id>"
   client_secret = "<your-client-secret>"
   
   spark.conf.set("fs.azure.account.auth.type.onelake.dfs.fabric.microsoft.com", "OAuth")
   spark.conf.set("fs.azure.account.oauth.provider.type.onelake.dfs.fabric.microsoft.com", 
                  "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
   spark.conf.set("fs.azure.account.oauth2.client.id.onelake.dfs.fabric.microsoft.com", client_id)
   spark.conf.set("fs.azure.account.oauth2.client.secret.onelake.dfs.fabric.microsoft.com", client_secret)
   spark.conf.set("fs.azure.account.oauth2.client.endpoint.onelake.dfs.fabric.microsoft.com", 
                  f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")
   
   print("✅ OneLake access configured")
   ```

   > **Note:** Replace `<your-tenant-id>`, `<your-client-id>`, and `<your-client-secret>` with values from Part 2.

### Part 4: Read Fabric Lakehouse Tables from Databricks

1. Add a cell to read Gold layer tables from OneLake:

   ```python
   # Define OneLake path to your Lakehouse
   onelake_path = "abfss://fabric-workspace-<inject key='DeploymentID'></inject>@onelake.dfs.fabric.microsoft.com/contoso-lakehouse-<inject key='DeploymentID'></inject>.Lakehouse/Tables"
   
   # Read Gold layer tables
   df_fact_sales = spark.read.format("delta").load(f"{onelake_path}/gold_fact_sales")
   df_dim_customer = spark.read.format("delta").load(f"{onelake_path}/gold_dim_customer")
   df_dim_product = spark.read.format("delta").load(f"{onelake_path}/gold_dim_product")
   
   print(f"✅ Fact_Sales: {df_fact_sales.count()} records")
   print(f"✅ Dim_Customer: {df_dim_customer.count()} records")
   print(f"✅ Dim_Product: {df_dim_product.count()} records")
   
   # Display sample data
   display(df_fact_sales.limit(10))
   ```

1. Verify that data from Fabric Lakehouse is accessible in Databricks.

### Part 5: Perform Data Science Workloads on Fabric Data

1. Add a cell to perform advanced analytics on the Gold layer:

   ```python
   # Calculate customer lifetime value (CLV)
   from pyspark.sql.functions import sum, count, avg, round
   
   df_customer_metrics = df_fact_sales.join(
       df_dim_customer, 
       df_fact_sales.CustomerKey == df_dim_customer.CustomerKey
   ).groupBy("CustomerName", "CustomerRegion").agg(
       count("SalesKey").alias("TotalOrders"),
       round(sum("SalesAmount"), 2).alias("TotalSpent"),
       round(avg("SalesAmount"), 2).alias("AvgOrderValue"),
       round(sum("Profit"), 2).alias("TotalProfit")
   ).orderBy(col("TotalSpent").desc())
   
   print("📊 Top 10 Customers by Total Spent:")
   display(df_customer_metrics.limit(10))
   ```

1. Add a cell to create ML features for predictive modeling:

   ```python
   # Prepare features for ML (customer segmentation)
   df_ml_features = df_customer_metrics.select(
       "CustomerName",
       "TotalOrders",
       "TotalSpent",
       "AvgOrderValue"
   )
   
   # Create customer segments based on spending
   from pyspark.sql.functions import when
   
   df_customer_segments = df_ml_features.withColumn(
       "Segment",
       when(col("TotalSpent") > 50000, "Premium")
       .when(col("TotalSpent") > 20000, "Gold")
       .when(col("TotalSpent") > 5000, "Silver")
       .otherwise("Bronze")
   )
   
   print("✅ Customer Segments Created")
   display(df_customer_segments.groupBy("Segment").count())
   ```

### Part 6: Write Enriched Data Back to Fabric Lakehouse

1. Add a cell to write the customer segments back to OneLake:

   ```python
   # Write customer segments to Gold layer in Fabric Lakehouse
   output_path = f"{onelake_path}/gold_customer_segments"
   
   df_customer_segments.write \
       .format("delta") \
       .mode("overwrite") \
       .save(output_path)
   
   print(f"✅ Customer segments written to: {output_path}")
   ```

1. Verify the data is written successfully:

   ```python
   # Read back to verify
   df_verify = spark.read.format("delta").load(output_path)
   print(f"✅ Verified: {df_verify.count()} customer segments written")
   display(df_verify.limit(10))
   ```

### Part 7: Validate Integration in Fabric

1. Return to **Microsoft Fabric workspace** in the browser.

1. Navigate to your Lakehouse: **contoso-lakehouse-<inject key="DeploymentID"></inject>**

1. In the **Tables** section, verify that **gold_customer_segments** table appears.

1. Query the table using SQL analytics endpoint:

   ```sql
   SELECT Segment, COUNT(*) as CustomerCount, SUM(TotalSpent) as TotalRevenue
   FROM gold_customer_segments
   GROUP BY Segment
   ORDER BY TotalRevenue DESC;
   ```

1. Confirm that data written from Databricks is accessible in Fabric.

> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Azure Databricks workspace created and cluster provisioned.
- OneLake access configured using service principal authentication.
- Fabric Lakehouse Gold layer tables successfully read from Databricks.
- Data science workloads (customer analytics, segmentation) performed on Fabric data.
- Enriched data written back to Fabric Lakehouse from Databricks.
- Bidirectional integration validated: Databricks ↔️ Fabric OneLake.

## Additional Resources

- [Azure Databricks Overview](https://learn.microsoft.com/azure/databricks/introduction/)
- [OneLake Integration with Databricks](https://learn.microsoft.com/fabric/onelake/onelake-access-databricks)
- [Service Principal Authentication](https://learn.microsoft.com/azure/databricks/dev-tools/service-principals)
- [Delta Lake Best Practices](https://learn.microsoft.com/azure/databricks/delta/best-practices)

Now, click **Next** to continue to **Challenge 06**.
