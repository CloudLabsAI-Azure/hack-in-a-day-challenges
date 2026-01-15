# Challenge 5: Enrich Data with Customer Segmentation

**Estimated Time:** 25 minutes

## Introduction

In this challenge, you'll create ML-based customer segments using Fabric Notebooks to enrich your Gold layer data. These segments will categorize customers based on their flight behavior, loyalty points, and transaction patterns, providing valuable insights for targeted marketing and business intelligence. The enriched data will be visualized in Power BI dashboards in Challenge 6.

## Prerequisites

- Completed Challenge 4 (Gold layer tables created)
- Access to your Fabric workspace
- Gold layer tables: `dim_customers`, `fact_flights`, `fact_transactions`, `kpi_customer_value`

## Learning Objectives

By the end of this challenge, you will:
- Use PySpark ML to perform K-means clustering for customer segmentation
- Create business-friendly segment names based on customer behavior
- Write enriched customer segments to the Gold layer
- Prepare ML-enhanced data for Power BI visualization

---

## Part 1: Create Customer Segmentation Notebook

1. In the **Microsoft Fabric** portal, navigate to your workspace: **fabric-workspace-<inject key="DeploymentID"></inject>**

2. Click **+ New** → **Notebook**

   - Name: **Customer_Segmentation_ML**

3. Attach the notebook to your Lakehouse:

   - Click **Add** (next to Lakehouses in the left pane)
   - Select **Existing Lakehouse**
   - Choose: **contoso-lakehouse-<inject key="DeploymentID"></inject>**

---

## Part 2: Load Gold Layer Data

1. In the first cell, add and run the following code to load your Gold layer data:

```python
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Load Gold layer tables
df_customers = spark.read.table("dim_customers")
df_flights = spark.read.table("fact_flights")
df_kpi = spark.read.table("kpi_customer_value")

print(f"Customers: {df_customers.count()}")
print(f"Flight Facts: {df_flights.count()}")
print(f"KPI Data: {df_kpi.count()}")

# Preview KPI data that will be used for segmentation
print("\n=== Customer KPI Data Sample ===")
df_kpi.select("customer_key", "age", "total_flights", "total_loyalty_points", 
              "total_spent", "customer_status").show(5, truncate=False)
```

2. Run the cell to verify data loads successfully.

---

## Part 3: Prepare Features for ML Clustering

1. Add a new cell to create features for machine learning:

```python
# Prepare ML features for customer segmentation
df_ml_features = df_kpi.select(
    col("customer_key"),
    col("age").cast("double"),
    col("total_flights").cast("double"),
    col("total_km_flown").cast("double"),
    col("total_loyalty_points").cast("double"),
    col("days_since_last_flight").cast("double"),
    col("total_spent").cast("double"),
    col("transaction_count").cast("double")
).na.drop()  # Remove any rows with null values

print(f"ML dataset prepared: {df_ml_features.count()} customers")
print("\n=== Feature Statistics ===")
df_ml_features.describe().show()
```

---

## Part 4: Apply K-Means Clustering

1. Add a new cell to perform K-means clustering:

```python
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.clustering import KMeans

# Assemble features into a vector
feature_cols = ["age", "total_flights", "total_km_flown", "total_loyalty_points", 
                "days_since_last_flight", "total_spent", "transaction_count"]

assembler = VectorAssembler(inputCols=feature_cols, outputCol="features_raw")
df_assembled = assembler.transform(df_ml_features)

# Scale features for better clustering
scaler = StandardScaler(inputCol="features_raw", outputCol="features", 
                        withStd=True, withMean=True)
scaler_model = scaler.fit(df_assembled)
df_scaled = scaler_model.transform(df_assembled)

# Train K-Means with 5 customer segments
print("Training K-Means clustering model...")
kmeans = KMeans(k=5, seed=42, featuresCol="features", predictionCol="segment")
model = kmeans.fit(df_scaled)

# Make predictions
df_segmented = model.transform(df_scaled)

print("✅ Customer segmentation complete!")
print(f"\n=== Segment Distribution ===")
df_segmented.groupBy("segment").count().orderBy("segment").show()
```

2. Run the cell and observe the segment distribution.

---

## Part 5: Analyze Segment Characteristics

1. Add a new cell to analyze each segment's profile:

```python
# Analyze segment characteristics
segment_profile = df_segmented.groupBy("segment").agg(
    count("*").alias("customer_count"),
    round(avg("age"), 1).alias("avg_age"),
    round(avg("total_flights"), 1).alias("avg_flights"),
    round(avg("total_km_flown"), 0).alias("avg_km"),
    round(avg("total_loyalty_points"), 0).alias("avg_points"),
    round(avg("days_since_last_flight"), 0).alias("avg_days_since_flight"),
    round(avg("total_spent"), 2).alias("avg_spent")
).orderBy("segment")

print("=== Customer Segment Profiles ===")
segment_profile.show(truncate=False)
```

---

## Part 6: Assign Business-Friendly Segment Names

1. Add a new cell to create meaningful segment names:

```python
# Assign business-friendly names based on characteristics
# Adjust the logic based on your actual segment profiles from the previous step

df_enriched = df_segmented.withColumn(
    "segment_name",
    when(col("segment") == 0, "Occasional Travelers")
    .when(col("segment") == 1, "Loyal Frequent Flyers")
    .when(col("segment") == 2, "At-Risk Customers")
    .when(col("segment") == 3, "Premium Elite Members")
    .when(col("segment") == 4, "New Joiners")
    .otherwise("Uncategorized")
)

# Join back with original KPI data to include all fields
df_customer_segments = df_kpi.join(
    df_enriched.select("customer_key", "segment", "segment_name"),
    on="customer_key",
    how="left"
)

print("✅ Business-friendly segment names assigned!")
print("\n=== Enriched Customer Data Sample ===")
df_customer_segments.select("customer_key", "age", "total_flights", 
                             "total_loyalty_points", "customer_status", 
                             "segment", "segment_name").show(10, truncate=False)

# Show segment distribution with names
print("\n=== Segment Distribution ===")
df_customer_segments.groupBy("segment", "segment_name").count().orderBy("segment").show(truncate=False)
```

---

## Part 7: Write Enriched Data to Gold Layer

1. Add a new cell to save the enriched customer segments:

```python
# Write enriched customer segments to Gold layer
df_customer_segments.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("gold_customer_segments_ml")

print("✅ Enriched customer segments written to Gold layer!")
print(f"Table: gold_customer_segments_ml")
print(f"Records: {spark.read.table('gold_customer_segments_ml').count()}")

# Create summary table for dashboard consumption
segment_summary = df_customer_segments.groupBy("segment", "segment_name").agg(
    count("*").alias("customer_count"),
    round(avg("total_flights"), 1).alias("avg_flights"),
    round(avg("total_loyalty_points"), 0).alias("avg_points"),
    round(avg("total_spent"), 2).alias("avg_revenue")
).orderBy("segment")

segment_summary.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gold_segment_summary")

print("\n✅ Segment summary table created!")
print(f"Table: gold_segment_summary")
segment_summary.show(truncate=False)
```

---

## Part 8: Validate Enriched Tables

1. In your Fabric workspace, navigate to your **Lakehouse**: **contoso-lakehouse-<inject key="DeploymentID"></inject>**

2. In the **Tables** section, verify you now see:

   - `gold_customer_segments_ml` - Full customer data with ML segments
   - `gold_segment_summary` - Aggregated segment metrics

3. Click on **gold_customer_segments_ml** to preview the data and verify:

   - All customers have segment assignments (0-4)
   - Segment names are displayed (Premium Elite, Loyal Frequent Flyers, etc.)
   - Original customer attributes are preserved

4. Query the enriched data using a new notebook cell:

```python
# Validate the enriched data
df_segments = spark.read.table("gold_customer_segments_ml")

print("=== Validation: Segment Coverage ===")
print(f"Total Customers: {df_segments.count()}")
print(f"Customers with Segments: {df_segments.filter(col('segment').isNotNull()).count()}")

print("\n=== Top Customers by Segment ===")
df_segments.filter(col("segment_name") == "Premium Elite Members") \
    .orderBy(col("total_loyalty_points").desc()) \
    .select("customer_key", "age", "total_flights", "total_loyalty_points", "total_spent") \
    .show(5, truncate=False)
```

---

## Success Criteria

- Customer segmentation notebook created and attached to Lakehouse.
- K-means clustering model trained successfully with 5 segments.
- Segment characteristics analyzed and business-friendly names assigned.
- `gold_customer_segments_ml` table created in Gold layer with enriched data.
- `gold_segment_summary` table created for dashboard consumption.
- All customers have ML-based segment assignments.
- Tables are visible in Fabric Lakehouse and ready for Power BI visualization.

---

## Additional Resources

- [PySpark ML Clustering](https://spark.apache.org/docs/latest/ml-clustering.html)
- [K-Means Algorithm Overview](https://spark.apache.org/docs/latest/ml-clustering.html#k-means)
- [Feature Scaling in ML](https://spark.apache.org/docs/latest/ml-features.html#standardscaler)

---

Now, click **Next** to continue to **Challenge 06** where you'll visualize these customer segments in an interactive Power BI dashboard!

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
