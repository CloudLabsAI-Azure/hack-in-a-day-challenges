# Challenge 5: Integrate Azure Databricks for Advanced Analytics

**Estimated Time:** 45 minutes

## Introduction

While Microsoft Fabric provides powerful data engineering capabilities, many organizations have existing investments in Azure Databricks for machine learning and advanced analytics. In this challenge, you'll integrate Azure Databricks with your Fabric Lakehouse to perform customer segmentation analysis on your flight loyalty and transaction data using Databricks' ML capabilities.

## Prerequisites

- Completed Challenge 4 (Gold layer tables created)
- Azure subscription with permissions to create Databricks workspace
- Access to Microsoft Fabric workspace
- Gold layer tables: `dim_customers`, `fact_flights`, `fact_transactions`, `kpi_customer_value`

---

## Learning Objectives

By the end of this challenge, you will:
- Create and configure Azure Databricks workspace
- Set up OneLake integration for seamless data access
- Access Fabric Lakehouse Delta tables from Databricks
- Perform customer segmentation using ML clustering
- Write enriched analytics back to Fabric Lakehouse

## Common Use Cases

### Use Case 1: Customer Segmentation (Our Example)

**Scenario**: Perform ML-based customer segmentation using K-means clustering

**Workflow**:
1. **Fabric**: Build Bronze → Silver → Gold pipeline
2. **Databricks**: Access Gold layer customer data
3. **Databricks**: Run K-means clustering to create 5 customer segments
4. **Databricks**: Write enriched segments back to Fabric
5. **Fabric**: Visualize segments in Power BI dashboard

### Use Case 2: Predictive Maintenance

**Scenario**: Predict equipment failures using IoT sensor data

**Workflow**:
1. **Fabric**: Ingest real-time IoT data streams
2. **Fabric**: Process and cleanse data in Silver layer
3. **Databricks**: Train ML model to predict failures
4. **Databricks**: Deploy model for real-time scoring
5. **Fabric**: Display predictions in operational dashboards

### Use Case 3: Demand Forecasting

**Scenario**: Forecast product demand for inventory optimization

**Workflow**:
1. **Fabric**: Consolidate sales history, weather, promotions data
2. **Databricks**: Train time-series forecasting models
3. **Databricks**: Generate demand predictions
4. **Fabric**: Feed predictions to supply chain dashboard

---

## Technical Implementation Overview

### Step 1: OneLake Path Structure

Each Fabric Lakehouse has a unique OneLake path using workspace and lakehouse GUIDs:

```
abfss://[workspace-guid]@onelake.dfs.fabric.microsoft.com/[lakehouse-guid].Lakehouse/Tables/[table-name]
```

**To find your path**:

1. In Fabric, open your Lakehouse
2. Click on **Files** folder
3. Copy the path shown (it will contain GUIDs)
4. Replace `/Files` with `.Lakehouse/Tables/[table-name]`

Example discovered path:
```
abfss://0fe8c64f-c1a6-4a15-900c-4480d68680b1@onelake.dfs.fabric.microsoft.com/6656b396-074a-467e-b6e3-4578c08168c3/Files
```

Convert to table path:
```
abfss://0fe8c64f-c1a6-4a15-900c-4480d68680b1@onelake.dfs.fabric.microsoft.com/6656b396-074a-467e-b6e3-4578c08168c3.Lakehouse/Tables/fact_flights
```

### Step 2: Reading Data in Databricks

```python
# Configure OneLake authentication with Service Principal
tenant_id = "<YOUR_TENANT_ID>"
client_id = "<YOUR_CLIENT_ID>"
client_secret = "<YOUR_CLIENT_SECRET>"

spark.conf.set("fs.azure.account.auth.type.onelake.dfs.fabric.microsoft.com", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.onelake.dfs.fabric.microsoft.com", 
               "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.onelake.dfs.fabric.microsoft.com", client_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.onelake.dfs.fabric.microsoft.com", client_secret)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.onelake.dfs.fabric.microsoft.com", 
               f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")

# Read Delta table from OneLake (replace with your actual GUIDs)
workspace_guid = "0fe8c64f-c1a6-4a15-900c-4480d68680b1"  # Your workspace GUID
lakehouse_guid = "6656b396-074a-467e-b6e3-4578c08168c3"  # Your lakehouse GUID

onelake_path = f"abfss://{workspace_guid}@onelake.dfs.fabric.microsoft.com/{lakehouse_guid}.Lakehouse/Tables/fact_flights"
df_flights = spark.read.format("delta").load(onelake_path)

print(f"Loaded {df_flights.count()} records from Fabric")
df_flights.show(5)

# Perform ML operations
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans

# Prepare features
assembler = VectorAssembler(inputCols=["total_flights", "total_loyalty_points"], outputCol="features")
df_features = assembler.transform(df_flights)

# Train model
kmeans = KMeans(k=5, seed=42, featuresCol="features", predictionCol="segment")
model = kmeans.fit(df_features)
df_results = model.transform(df_features)

# Write results back to OneLake
output_path = f"abfss://{workspace_guid}@onelake.dfs.fabric.microsoft.com/{lakehouse_guid}.Lakehouse/Tables/customer_segments_ml"
df_results.select("customer_key", "segment", "total_flights", "total_loyalty_points") \
    .write.format("delta").mode("overwrite").save(output_path)

print(f"Results written to: {output_path}")
```

### Step 3: Accessing in Fabric

Once written back, the table appears automatically in your Fabric Lakehouse and can be queried in Power BI, Dataflows, or Notebooks.

---

## Best Practices for Integration

### 1. Design Considerations

- **Use Fabric for**: ETL, data pipelines, data warehousing, BI
- **Use Databricks for**: ML model training, complex feature engineering, large-scale Spark jobs
- **Store in OneLake**: All data in Delta Lake format for compatibility

### 2. Performance Optimization

- **Partition data** appropriately for efficient reads/writes
- **Use Z-ordering** in Delta tables for query performance
- **Cache frequently accessed tables** in Databricks
- **Minimize data movement** between systems

### 3. Governance & Security

- **Unified permissions**: Manage access at OneLake level
- **Data lineage**: Track data flow across both platforms
- **Audit logging**: Monitor access from both Fabric and Databricks
- **Encryption**: OneLake provides encryption at rest and in transit

---

## Conceptual Exercise

**Scenario**: Your organization wants to implement churn prediction for the flight loyalty program.

**Task**: Design the data flow using Fabric + Databricks integration

**Solution Architecture**:

1. **Data Ingestion (Fabric)**
   - Ingest flight bookings, customer profiles, loyalty transactions
   - Store raw data in Bronze layer

2. **Data Preparation (Fabric)**
   - Clean and standardize data in Silver layer
   - Create customer activity features in Gold layer

3. **Model Training (Databricks)**
   - Access Gold layer customer features from OneLake
   - Train binary classification model (churn/no-churn)
   - Evaluate model performance using MLflow
   - Write model predictions back to OneLake

4. **Operationalization (Fabric)**
   - Load predictions into Gold layer table
   - Create Power BI dashboard showing at-risk customers
   - Set up alerts for high-risk churn predictions

5. **Continuous Improvement (Databricks)**
   - Monitor model performance over time
   - Retrain model monthly with new data
   - Version models using MLflow

---

## When NOT to Use This Integration

**You might not need Databricks if**:
- Fabric's native Spark notebooks meet your needs
- You don't require advanced ML frameworks (XGBoost, TensorFlow, PyTorch)
- Your team doesn't have Databricks expertise
- Budget constraints limit additional platform adoption

**Fabric alone can handle**:
- Standard data transformations
- Basic machine learning with AutoML
- SQL-based analytics
- Power BI reporting

---

## Success Criteria

- Understanding of how Databricks integrates with Fabric OneLake
- Knowledge of OneLake path structure for data access
- Awareness of authentication options (Service Principal, Managed Identity)
- Ability to design data workflows across both platforms
- Recognition of when to use each platform

---

## Additional Resources

- [OneLake and Databricks Integration](https://learn.microsoft.com/fabric/onelake/onelake-azure-databricks)
- [Access OneLake from Databricks](https://learn.microsoft.com/fabric/onelake/onelake-access-databricks)
- [Delta Lake in Microsoft Fabric](https://learn.microsoft.com/fabric/data-engineering/lakehouse-and-delta-tables)
- [Azure Databricks ML Runtime](https://learn.microsoft.com/azure/databricks/release-notes/runtime/mlruntime)

---

## Summary

In this conceptual challenge, you learned:

- How Azure Databricks integrates with Microsoft Fabricthrough OneLake  
- The benefits of a unified lakehouse architecture  
- Common use cases for Fabric + Databricks integration  
- Technical implementation patterns for reading/writing data  
- Best practices for cross-platform data workflows  

While you didn't perform hands-on implementation, you now understand how organizations leverage both platforms together for end-to-end data and AI solutions. This knowledge will help you design scalable architectures that use the right tool for each workload.

---

Now, click **Next** to continue to **Challenge 06** where you'll build a Power BI dashboard using your Gold layer tables.

1. **Open the Azure Portal**: Navigate to [https://portal.azure.com](https://portal.azure.com)

2. **Create Databricks workspace**:

   - Search for **"Azure Databricks"** in the top search bar
   - Click **+ Create**
   - Configure the workspace:
     - **Subscription**: Your Azure subscription
     - **Resource Group**: **challenge-rg-<inject key="DeploymentID"></inject>**
     - **Workspace Name**: `databricks-fabric-integration`
     - **Region**: **<inject key="Region"></inject>**
     - **Pricing Tier**: **Standard** (Apache Spark, Secure with Microsoft Entra ID)
     - **Workspace type**: **Hybrid**
   - Click **Next: Networking**

3. **Under Networking tab** (keep defaults):

   - **Deploy Azure Databricks workspace with Secure Cluster Connectivity (No Public IP)**: Select **No**
   - **Deploy Azure Databricks workspace in your own Virtual Network (VNet)**: Select **No**
   
4. Click **Review + Create** → **Create**

5. Wait for deployment (3-5 minutes)

6. Once complete, click **Go to resource** → **Launch Workspace**

## Part 2: Configure OneLake Access from Databricks

### Get Fabric Lakehouse Connection Details

1. **Return to Microsoft Fabric portal**: [https://app.fabric.microsoft.com](https://app.fabric.microsoft.com)

2. Navigate to your **Lakehouse**

3. Click on the **SQL analytics endpoint** in the top ribbon

4. Copy the **SQL connection string** - you'll need the workspace and lakehouse names

5. Note the **OneLake path** format:
   ```
   abfss://[WorkspaceName]@onelake.dfs.fabric.microsoft.com/[LakehouseName].Lakehouse/Tables
   ```

### Create Service Principal for Authentication

1. **In Azure Portal**, go to **Microsoft Entra ID** (formerly Azure AD)

2. Navigate to **App registrations** → **+ New registration**

3. Configure the app:
   - **Name**: `databricks-onelake-access`
   - **Supported account types**: Single tenant
   - Click **Register**

4. **Copy the following values** (save them securely):

   - **Application (client) ID**
   - **Directory (tenant) ID**

5. **Create a client secret**:

   - Go to **Certificates & secrets** → **+ New client secret**
   - **Description**: `fabric-access`
   - **Expires**: 12 months
   - Click **Add**
   - **Copy the secret VALUE immediately** (you can't view it again)

6. **Grant Fabric workspace permissions**:

   - Return to **Fabric portal** → Your workspace
   - Click **Manage access**
   - Click **+ Add people or groups**
   - Search for your app registration name: `databricks-onelake-access`
   - Grant **Contributor** role
   - Click **Add**

---

## Part 3: Create Databricks Cluster and Notebook

1. **In Databricks workspace**, click **Compute** in left sidebar

2. **Create new cluster**:

   - **Cluster name**: `fabric-analytics-cluster`
   - **Cluster mode**: Single Node (for lab)
   - **Databricks Runtime**: **13.3 LTS** or later
   - **Node type**: `Standard_DS3_v2` (4 cores, 14 GB)
   - **Terminate after**: 30 minutes of inactivity
   - Click **Create Cluster**

3. Wait for cluster to start (2-3 minutes)

4. **Create a new notebook**:

   - Click **Workspace** in left sidebar
   - Click your username folder
   - Click **⋮** (three dots) → **Create** → **Notebook**
   - **Name**: `Fabric_OneLake_Customer_Analytics`
   - **Default Language**: Python
   - **Cluster**: Select `fabric-analytics-cluster`

---

## Part 4: Configure OneLake Access in Databricks

Add the following code cells to your Databricks notebook:

### Cell 1: Set up authentication

```python
# Configure OneLake access credentials
# Replace with your actual values
tenant_id = "<YOUR_TENANT_ID>"
client_id = "<YOUR_CLIENT_ID>"
client_secret = "<YOUR_CLIENT_SECRET>"

# Configure Spark to use OAuth for OneLake access
spark.conf.set("fs.azure.account.auth.type.onelake.dfs.fabric.microsoft.com", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.onelake.dfs.fabric.microsoft.com", 
               "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.onelake.dfs.fabric.microsoft.com", client_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.onelake.dfs.fabric.microsoft.com", client_secret)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.onelake.dfs.fabric.microsoft.com", 
               f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")

print("OneLake authentication configured")
```

### Cell 2: Read Gold layer tables from Fabric

```python
# Define your OneLake path - REPLACE with your actual workspace and lakehouse names
workspace_name = "your-workspace-name"  # e.g., "fabric-workspace-12345"
lakehouse_name = "your-lakehouse-name"  # e.g., "DataLakehouse"

onelake_base_path = f"abfss://{workspace_name}@onelake.dfs.fabric.microsoft.com/{lakehouse_name}.Lakehouse/Tables"

# Read Gold layer tables
df_customers = spark.read.format("delta").load(f"{onelake_base_path}/dim_customers")
df_flights = spark.read.format("delta").load(f"{onelake_base_path}/fact_flights")
df_transactions = spark.read.format("delta").load(f"{onelake_base_path}/fact_transactions")
df_kpi = spark.read.format("delta").load(f"{onelake_base_path}/kpi_customer_value")

print(f"Customers: {df_customers.count()}")
print(f"Flight Facts: {df_flights.count()}")
print(f"Transactions: {df_transactions.count()}")
print(f"KPI Data: {df_kpi.count()}")

# Preview data
display(df_kpi.limit(10))
```

---

## Part 5: Perform Customer Segmentation with ML

Now use Databricks ML to perform RFM (Recency, Frequency, Monetary) segmentation:

### Cell 3: Prepare features for ML clustering

```python
from pyspark.sql.functions import col, when, lit
from pyspark.ml.feature import VectorAssembler, StandardScaler

# Create enhanced features for clustering
df_ml_features = df_kpi.select(
    col("customer_key"),
    col("age"),
    col("total_flights"),
    col("total_km_flown"),
    col("total_loyalty_points"),
    col("days_since_last_flight"),
    col("total_spent"),
    col("transaction_count"),
    # Create RFM-like scores
    when(col("days_since_last_flight") <= 90, 5)
     .when(col("days_since_last_flight") <= 180, 4)
     .when(col("days_since_last_flight") <= 365, 3)
     .when(col("days_since_last_flight") <= 730, 2)
     .otherwise(1).alias("recency_score"),
    
    when(col("total_flights") >= 40, 5)
     .when(col("total_flights") >= 20, 4)
     .when(col("total_flights") >= 10, 3)
     .when(col("total_flights") >= 5, 2)
     .otherwise(1).alias("frequency_score"),
    
    when(col("total_loyalty_points") >= 50000, 5)
     .when(col("total_loyalty_points") >= 20000, 4)
     .when(col("total_loyalty_points") >= 10000, 3)
     .when(col("total_loyalty_points") >= 5000, 2)
     .otherwise(1).alias("monetary_score")
).na.drop()

print(f"ML dataset prepared: {df_ml_features.count()} customers")
display(df_ml_features.limit(10))
```

### Cell 4: Feature engineering and scaling

```python
# Assemble features into vector
feature_cols = ["age", "total_flights", "total_km_flown", "total_loyalty_points", 
                "days_since_last_flight", "total_spent", "transaction_count",
                "recency_score", "frequency_score", "monetary_score"]

assembler = VectorAssembler(inputCols=feature_cols, outputCol="features_raw")
df_assembled = assembler.transform(df_ml_features)

# Scale features for better clustering
scaler = StandardScaler(inputCol="features_raw", outputCol="features", withStd=True, withMean=True)
scaler_model = scaler.fit(df_assembled)
df_scaled = scaler_model.transform(df_assembled)

print("Features scaled and ready for clustering")
display(df_scaled.select("customer_key", "features").limit(5))
```

### Cell 5: K-Means clustering

```python
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

# Train K-Means with 5 customer segments
kmeans = KMeans(k=5, seed=42, featuresCol="features", predictionCol="segment")
model = kmeans.fit(df_scaled)

# Make predictions
df_segmented = model.transform(df_scaled)

# Evaluate clustering quality
evaluator = ClusteringEvaluator(featuresCol="features", predictionCol="segment", metricName="silhouette")
silhouette = evaluator.evaluate(df_segmented)

print(f"Customer segmentation complete!")
print(f"Silhouette Score: {silhouette:.4f}")
print(f"\nCluster Centers:")
centers = model.clusterCenters()
for i, center in enumerate(centers):
    print(f"Segment {i}: {center[:3]}")  # Show first 3 dimensions

# Show segment distribution
display(df_segmented.groupBy("segment").count().orderBy("segment"))
```

### Cell 6: Analyze segment characteristics

```python
from pyspark.sql.functions import avg, count, round

# Analyze each segment's profile
segment_profile = df_segmented.groupBy("segment").agg(
    count("*").alias("customer_count"),
    round(avg("age"), 1).alias("avg_age"),
    round(avg("total_flights"), 1).alias("avg_flights"),
    round(avg("total_km_flown"), 0).alias("avg_km"),
    round(avg("total_loyalty_points"), 0).alias("avg_points"),
    round(avg("days_since_last_flight"), 0).alias("avg_days_since_flight"),
    round(avg("total_spent"), 2).alias("avg_spent"),
    round(avg("recency_score"), 2).alias("avg_recency"),
    round(avg("frequency_score"), 2).alias("avg_frequency"),
    round(avg("monetary_score"), 2).alias("avg_monetary")
).orderBy("segment")

print("=== Customer Segment Profiles ===")
display(segment_profile)

# Assign business-friendly names based on characteristics
# You can customize these based on your actual results
segment_names = {
    0: "Occasional Travelers",
    1: "Loyal Frequent Flyers",
    2: "At-Risk Customers",
    3: "Premium Elite Members",
    4: "New Joiners"
}
```

### Cell 7: Create an enriched customer table with segments

```python
from pyspark.sql.functions import when, col

# Join segments back with original customer data
df_customers_enriched = df_kpi.join(
    df_segmented.select("customer_key", "segment"),
    on="customer_key",
    how="left"
)

# Add business-friendly segment names
df_customers_enriched = df_customers_enriched.withColumn(
    "segment_name",
    when(col("segment") == 0, "Occasional Travelers")
    .when(col("segment") == 1, "Loyal Frequent Flyers")
    .when(col("segment") == 2, "At-Risk Customers")
    .when(col("segment") == 3, "Premium Elite Members")
    .when(col("segment") == 4, "New Joiners")
    .otherwise("Uncategorized")
)

print("Customer data enriched with ML segments")
display(df_customers_enriched.select("customer_key", "age", "total_flights", 
                                      "total_loyalty_points", "customer_status", 
                                      "segment", "segment_name").limit(20))
```

---

## Part 6: Write Enriched Data Back to Fabric

### Cell 8: Write ML results back to OneLake

```python
# Write the enriched customer segments back to Fabric Gold layer
output_path = f"{onelake_base_path}/gold_customer_segments_ml"

df_customers_enriched.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .save(output_path)

print(f"ML-enriched customer segments written back to Fabric!")
print(f"Location: {output_path}")
print(f"Records: {df_customers_enriched.count()}")

# Also create a summary table
segment_summary = df_customers_enriched.groupBy("segment", "segment_name").agg(
    count("*").alias("customer_count"),
    round(avg("total_flights"), 1).alias("avg_flights"),
    round(avg("total_loyalty_points"), 0).alias("avg_points"),
    round(avg("total_spent"), 2).alias("avg_revenue")
).orderBy("segment")

summary_path = f"{onelake_base_path}/gold_segment_summary"
segment_summary.write \
    .format("delta") \
    .mode("overwrite") \
    .save(summary_path)

print(f"Segment summary table created!")
display(segment_summary)
```

---

## Part 7: Verify in Fabric Lakehouse

1. **Return to Microsoft Fabric portal**

2. **Navigate to your Lakehouse**

3. **Refresh the Tables view** - you should now see:

   - `gold_customer_segments_ml` - Full enriched customer data with ML segments
   - `gold_segment_summary` - Aggregated segment profiles

4. **Query the new tables** using SQL endpoint:

```sql
-- View segment distribution
SELECT segment_name, COUNT(*) as customer_count
FROM gold_customer_segments_ml
GROUP BY segment_name
ORDER BY customer_count DESC;

-- Compare segments by loyalty tier
SELECT segment_name, loyalty_tier, COUNT(*) as count
FROM gold_customer_segments_ml
GROUP BY segment_name, loyalty_tier
ORDER BY segment_name, loyalty_tier;
```

---

## Success Criteria

- Azure Databricks workspace created and configured
- OneLake authentication working (can read Fabric tables)
- Successfully loaded Gold layer tables in Databricks
- ML customer segmentation completed (5 segments)
- Enriched data written back to Fabric Lakehouse
- New Gold tables visible in Fabric (gold_customer_segments_ml, gold_segment_summary)
- Silhouette score > 0.3 (indicates reasonable clustering quality)

---

## Validation Checkpoint

**Copy this GUID and submit for validation:** `{{guid-challenge-5}}`

---

## Summary

In this challenge, you:
- **Integrated Azure Databricks** with Microsoft Fabric OneLake
- **Performed advanced ML analytics** using K-Means clustering for customer segmentation
- **Created 5 customer segments** based on flight behavior, loyalty points, and spending
- **Wrote results back to Fabric** seamlessly without data duplication
- **Enabled bi-directional data flow** between Databricks and Fabric

Your enriched customer segments are now available in Fabric for Power BI dashboards!

---

## Next Steps

Proceed to **Challenge 6** to build a Power BI dashboard visualizing your ML-enhanced customer segments and business KPIs.