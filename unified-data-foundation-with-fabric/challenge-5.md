# Challenge 5: Build ML Models with Fabric Data Science

**Estimated Time:** 40 minutes

## Introduction

Microsoft Fabric's Data Science workload provides a comprehensive environment for building, training, and deploying machine learning models-all within the unified Fabric platform. In this challenge, you'll use Fabric's Data Science capabilities to perform customer segmentation analysis on your flight loyalty and transaction data. You'll create ML experiments, build K-Means clustering models, track experiments with MLflow, and write enriched analytics back to your Fabric Lakehouse.

## Prerequisites

- Completed Challenge 4 (Gold layer tables created)
- Access to Microsoft Fabric workspace
- Gold layer tables: `dim_customers`, `fact_flights`, `fact_transactions`, `kpi_customer_value`

## Learning Objectives

By the end of this challenge, you will:
- Create Data Science experiments in Microsoft Fabric
- Load data from Fabric Lakehouse Delta tables
- Perform customer segmentation using scikit-learn K-Means clustering
- Track ML experiments and models with MLflow
- Write enriched ML results back to the Lakehouse
- Create reusable ML models for production use

## Part 1: Create a Data Science Notebook

1. Navigate to your **Microsoft Fabric workspace**: **fabric-workspace-<inject key="DeploymentID" enableCopy="false"/>**

1. Open your Lakehouse: **contoso-lakehouse-<inject key="DeploymentID" enableCopy="false"/>** 

   > **Note:** Select the **Lakehouse** where the type is Lakehouse.

1. Click on **Open notebook** and select **+ New notebook** and click on **Notebook**.

1. Attach the Lakehouse:

   - Click **Add** (next to Lakehouses in the left pane)
   - Select **Existing Lakehouse**
   - Choose: **contoso-lakehouse-<inject key="DeploymentID" enableCopy="false"/>**

## Part 2: Load Gold Layer Data

Add the following code cells to your notebook:

### Cell 1: Import libraries and load data

1. Add and run the following code.

    ```python
    # Import required libraries
    import pandas as pd
    import numpy as np
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col, when

    # Initialize Spark session (already available in Fabric)
    spark = SparkSession.builder.getOrCreate()

    # Load Gold layer tables from Lakehouse
    df_kpi = spark.read.table("kpi_customer_value")
    df_customers = spark.read.table("dim_customers")
    df_flights = spark.read.table("fact_flights")
    df_transactions = spark.read.table("fact_transactions")

    print(f"KPI Data: {df_kpi.count()} records")
    print(f"Customer Dimension: {df_customers.count()} records")
    print(f"Flight Facts: {df_flights.count()} records")
    print(f"Transaction Facts: {df_transactions.count()} records")

    # Display sample data
    display(df_kpi.limit(10))
    ```

### Cell 2: Prepare features for ML

    ```python
    from pyspark.sql.functions import col, when, coalesce, lit

    # Create enhanced features for clustering
    df_ml_features = df_kpi.select(
        col("customer_key"),
        col("age"),
        col("total_flights"),
        col("total_km_flown"),
        col("total_loyalty_points"),
        col("days_since_last_flight"),
        coalesce(col("total_spent"), lit(0)).alias("total_spent"),
        coalesce(col("transaction_count"), lit(0)).alias("transaction_count")
    ).na.drop()

    # Add RFM-like scores (Recency, Frequency, Monetary)
    df_ml_features = df_ml_features.withColumn(
        "recency_score",
        when(col("days_since_last_flight") <= 90, 5)
        .when(col("days_since_last_flight") <= 180, 4)
        .when(col("days_since_last_flight") <= 365, 3)
        .when(col("days_since_last_flight") <= 730, 2)
        .otherwise(1)
    ).withColumn(
        "frequency_score",
        when(col("total_flights") >= 40, 5)
        .when(col("total_flights") >= 20, 4)
        .when(col("total_flights") >= 10, 3)
        .when(col("total_flights") >= 5, 2)
        .otherwise(1)
    ).withColumn(
        "monetary_score",
        when(col("total_loyalty_points") >= 50000, 5)
        .when(col("total_loyalty_points") >= 20000, 4)
        .when(col("total_loyalty_points") >= 10000, 3)
        .when(col("total_loyalty_points") >= 5000, 2)
        .otherwise(1)
    )

    print(f"ML dataset prepared: {df_ml_features.count()} customers")
    display(df_ml_features.limit(10))
    ```

## Part 3: Perform Customer Segmentation with K-Means

### Cell 3: Convert to Pandas and prepare for scikit-learn

1. Add and run the following code.

    ```python
    # Convert to Pandas DataFrame for scikit-learn
    df_pandas = df_ml_features.toPandas()

    # Select features for clustering
    feature_cols = ["age", "total_flights", "total_km_flown", "total_loyalty_points", 
                    "days_since_last_flight", "total_spent", "transaction_count",
                    "recency_score", "frequency_score", "monetary_score"]

    X = df_pandas[feature_cols].fillna(0)

    print(f"Feature matrix shape: {X.shape}")
    print(f"Features: {feature_cols}")
    print("\n=== Feature Statistics ===")
    print(X.describe())
    ```

### Cell 4: Scale features and train K-Means model

1. Add and run the following code.

    ```python
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score
    import mlflow
    import mlflow.sklearn

    # Scale features for better clustering
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Start MLflow experiment
    mlflow.set_experiment("Customer_Segmentation_Experiment")

    with mlflow.start_run(run_name="KMeans_5_Clusters"):
        
        # Train K-Means with 5 customer segments
        n_clusters = 5
        kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10, max_iter=300)
        
        # Fit model and predict clusters
        cluster_labels = kmeans.fit_predict(X_scaled)
        
        # Calculate silhouette score for model quality
        silhouette = silhouette_score(X_scaled, cluster_labels)
        
        # Log parameters and metrics to MLflow
        mlflow.log_param("n_clusters", n_clusters)
        mlflow.log_param("algorithm", "KMeans")
        mlflow.log_param("random_state", 42)
        mlflow.log_metric("silhouette_score", silhouette)
        mlflow.log_metric("inertia", kmeans.inertia_)
        
        # Log the model
        mlflow.sklearn.log_model(kmeans, "kmeans_model")
        
        # Log the scaler as well
        mlflow.sklearn.log_model(scaler, "scaler_model")
        
        print(f"Model trained successfully!")
        print(f"Number of clusters: {n_clusters}")
        print(f"Silhouette Score: {silhouette:.4f}")
        print(f"Inertia: {kmeans.inertia_:.2f}")
        
        # Add cluster labels to dataframe
        df_pandas['segment'] = cluster_labels

    # Display cluster distribution
    print("\n=== Cluster Distribution ===")
    print(df_pandas['segment'].value_counts().sort_index())
    ```

### Cell 5: Analyze segment characteristics

1. Add and run the following code.

    ```python
    # Analyze each segment's profile
    segment_profile = df_pandas.groupby('segment').agg({
        'customer_key': 'count',
        'age': 'mean',
        'total_flights': 'mean',
        'total_km_flown': 'mean',
        'total_loyalty_points': 'mean',
        'days_since_last_flight': 'mean',
        'total_spent': 'mean',
        'recency_score': 'mean',
        'frequency_score': 'mean',
        'monetary_score': 'mean'
    }).round(2)

    segment_profile.columns = ['customer_count', 'avg_age', 'avg_flights', 'avg_km', 
                                'avg_points', 'avg_days_since_flight', 'avg_spent',
                                'avg_recency', 'avg_frequency', 'avg_monetary']

    print("=== Customer Segment Profiles ===")
    print(segment_profile)

    # Visualize segment profiles
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Set style
    sns.set_style("whitegrid")

    # Create subplots for key metrics
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Customer Segment Analysis', fontsize=16, fontweight='bold')

    # Plot 1: Customer count
    axes[0, 0].bar(segment_profile.index, segment_profile['customer_count'], color='steelblue')
    axes[0, 0].set_title('Customers per Segment')
    axes[0, 0].set_xlabel('Segment')
    axes[0, 0].set_ylabel('Count')

    # Plot 2: Average flights
    axes[0, 1].bar(segment_profile.index, segment_profile['avg_flights'], color='darkorange')
    axes[0, 1].set_title('Average Flights')
    axes[0, 1].set_xlabel('Segment')
    axes[0, 1].set_ylabel('Flights')

    # Plot 3: Average loyalty points
    axes[0, 2].bar(segment_profile.index, segment_profile['avg_points'], color='green')
    axes[0, 2].set_title('Average Loyalty Points')
    axes[0, 2].set_xlabel('Segment')
    axes[0, 2].set_ylabel('Points')

    # Plot 4: Average spending
    axes[1, 0].bar(segment_profile.index, segment_profile['avg_spent'], color='purple')
    axes[1, 0].set_title('Average Spending')
    axes[1, 0].set_xlabel('Segment')
    axes[1, 0].set_ylabel('Amount')

    # Plot 5: RFM Scores
    x_pos = np.arange(len(segment_profile))
    axes[1, 1].plot(x_pos, segment_profile['avg_recency'], marker='o', label='Recency', linewidth=2)
    axes[1, 1].plot(x_pos, segment_profile['avg_frequency'], marker='s', label='Frequency', linewidth=2)
    axes[1, 1].plot(x_pos, segment_profile['avg_monetary'], marker='^', label='Monetary', linewidth=2)
    axes[1, 1].set_title('RFM Scores by Segment')
    axes[1, 1].set_xlabel('Segment')
    axes[1, 1].set_ylabel('Score')
    axes[1, 1].set_xticks(x_pos)
    axes[1, 1].legend()

    # Plot 6: Days since last flight
    axes[1, 2].bar(segment_profile.index, segment_profile['avg_days_since_flight'], color='red')
    axes[1, 2].set_title('Avg Days Since Last Flight')
    axes[1, 2].set_xlabel('Segment')
    axes[1, 2].set_ylabel('Days')

    plt.tight_layout()
    plt.show()

    # Log visualizations to MLflow
    mlflow.log_figure(fig, "segment_analysis.png")
    ```

### Cell 6: Assign business-friendly segment names

1. Add and run the following code.

    ```python
    # Assign business-friendly names based on segment characteristics
    # Analyze each segment and assign meaningful names

    def assign_segment_name(row):
        segment = row['segment']
        
        # Segment 0: High recency, low frequency/monetary - likely churned
        # Segment 1: High all-round scores - premium customers
        # Segment 2: Moderate scores - regular customers
        # Segment 3: Low frequency but recent - new joiners
        # Segment 4: Low engagement - at risk
        
        # You should analyze segment_profile and adjust these mappings
        segment_names = {
            0: "At-Risk Customers",
            1: "Premium Elite Members",
            2: "Loyal Frequent Flyers",
            3: "New Joiners",
            4: "Occasional Travelers"
        }
        
        return segment_names.get(segment, "Uncategorized")

    df_pandas['segment_name'] = df_pandas.apply(assign_segment_name, axis=1)

    print("=== Segment Name Distribution ===")
    print(df_pandas['segment_name'].value_counts())

    # Display sample of enriched data
    print("\n=== Sample Enriched Customer Data ===")
    print(df_pandas[['customer_key', 'age', 'total_flights', 'total_loyalty_points', 
                    'segment', 'segment_name']].head(20))
    ```

## Part 4: Write Enriched Data Back to Lakehouse

### Cell 7: Create enriched customer table

1. Add and run the following code.

    ```python
    # Convert back to Spark DataFrame
    df_enriched_spark = spark.createDataFrame(df_pandas)

    # Join with original KPI data to get all fields
    df_customers_enriched = df_kpi.join(
        df_enriched_spark.select("customer_key", "segment", "segment_name"),
        on="customer_key",
        how="left"
    )

    print(f"Enriched customer data created: {df_customers_enriched.count()} records")

    # Display sample
    display(df_customers_enriched.select("customer_key", "age", "total_flights", 
                                        "total_loyalty_points", "customer_status", 
                                        "segment", "segment_name").limit(20))
    ```

### Cell 8: Write ML results to Gold layer

1. Add and run the following code.

    ```python
    # Write the enriched customer segments to Gold layer
    df_customers_enriched.write \
        .format("delta") \
        .mode("overwrite") \
        .option("overwriteSchema", "true") \
        .saveAsTable("gold_customer_segments_ml")

    print("ML-enriched customer segments written to Gold layer!")
    print(f"  Table: gold_customer_segments_ml")
    print(f"  Records: {df_customers_enriched.count()}")

    # Create segment summary table
    df_segment_summary_spark = spark.createDataFrame(segment_profile.reset_index())

    df_segment_summary_spark.write \
        .format("delta") \
        .mode("overwrite") \
        .option("overwriteSchema", "true") \
        .saveAsTable("gold_segment_summary")

    print("\nSegment summary table created!")
    print(f"  Table: gold_segment_summary")

    # Display the summary
    display(df_segment_summary_spark)
    ```

## Part 5: Validate ML Results in Lakehouse

### Cell 9: Query the new ML-enriched tables

1. Add and run the following code.

    ```python
    # Verify the tables were created successfully
    print("=== Validating Gold Layer ML Tables ===\n")

    # Check gold_customer_segments_ml
    ml_segments = spark.read.table("gold_customer_segments_ml")
    print(f"gold_customer_segments_ml: {ml_segments.count()} records")

    # Check gold_segment_summary
    segment_summary = spark.read.table("gold_segment_summary")
    print(f"gold_segment_summary: {segment_summary.count()} records")

    # Show segment distribution
    print("\n=== Segment Distribution ===")
    ml_segments.groupBy("segment_name").count().orderBy("count", ascending=False).show()

    # Show sample enriched records
    print("\n=== Sample Enriched Customer Records ===")
    display(ml_segments.select("customer_key", "age", "gender", "loyalty_tier", 
                            "total_flights", "total_loyalty_points", "total_spent",
                            "customer_status", "segment", "segment_name").limit(20))
    ```

## Part 6: View ML Experiments in Fabric

1. Navigate to your Fabric workspace

1. Click on the left navigation and select **Data Science**

1. Find your experiment: **Customer-Segmentation-Experiment**

1. Click on the experiment to view:
   - Run history
   - Parameters (n_clusters, algorithm, random_state)
   - Metrics (silhouette_score, inertia)
   - Artifacts (models, visualizations)

1. View the registered model:
   - Click on **Models** in the left navigation
   - Find your **kmeans_model**
   - View model details, versions, and lineage

## Part 7: Save the Notebook

1. Click the **Save as**.

1. In the "Save as new notebook" dialog:
   - **Name**: **ML_Customer_Segmentation**
   - **Select location**: **fabric-workspace-<inject key="DeploymentID" enableCopy="false"/>**
   - Click **Save**

<validation step="35ad3f50-8129-449e-a122-1c1737eec0db" />

> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Data Science notebook created in Fabric successfully
- Gold layer tables loaded from Lakehouse (kpi_customer_value, dim_customers, fact_flights, fact_transactions)
- Features prepared for ML (RFM scores calculated)
- K-Means clustering model trained (5 segments)
- MLflow experiment tracked with parameters and metrics
- Silhouette score > 0.3 (indicates reasonable clustering quality)
- Segment visualizations created and logged
- Business-friendly segment names assigned
- Enriched data written back to Lakehouse (gold_customer_segments_ml, gold_segment_summary)
- New tables visible in Lakehouse with correct record counts
- ML experiment visible in Fabric Data Science workspace

## Additional Resources

- [Data Science in Microsoft Fabric](https://learn.microsoft.com/fabric/data-science/data-science-overview)
- [MLflow in Fabric](https://learn.microsoft.com/fabric/data-science/mlflow-autologging)
- [Scikit-learn K-Means Clustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
- [Customer Segmentation with ML](https://learn.microsoft.com/azure/machine-learning/how-to-auto-train-models-v1)

## Summary

In this challenge, you built a complete ML pipeline within Microsoft Fabric:
- **Loaded data** from Lakehouse Delta tables
- **Prepared features** with RFM scoring methodology
- **Trained K-Means model** for customer segmentation (5 segments)
- **Tracked experiments** with MLflow for reproducibility
- **Created visualizations** to analyze segment characteristics
- **Enriched customer data** with ML-predicted segments
- **Wrote results back** to Gold layer for Power BI consumption

Your customer segmentation model is now ready for business intelligence and targeted marketing campaigns!

## Next Steps

Proceed to **Challenge 6** to build Power BI dashboards that visualize your ML-enriched customer segments and loyalty program insights.