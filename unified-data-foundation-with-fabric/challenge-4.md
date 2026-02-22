# Challenge 4: Build Gold Layer - Dimensional Modeling for Analytics

**Estimated Time:** 30 minutes

## Introduction

In this challenge, you'll create the Gold layer of your Medallion architecture. The Gold layer represents business-level aggregations and dimensional models optimized for analytics and reporting. You'll build star schema dimensions and fact tables from your cleansed Silver layer data.

## Prerequisites

- Completed Challenge 3 (Silver layer with cleaned data)
- Access to your Fabric workspace
- Silver layer tables: `silver_flights`, `silver_transactions`

## Learning Objectives

By the end of this challenge, you will:
- Understand dimensional modeling principles (star schema)
- Create dimension tables for customers, time, and geography
- Build fact tables with metrics and foreign keys
- Implement business KPIs and aggregations
- Write optimized queries for analytics

## Part 1: Load Silver Layer Data

1. In your workspace, click **+ New** and click on **Notebook**

1. Add and run the following code to load Silver layer tables:

    ```python
    from pyspark.sql.functions import *

    # Load Silver layer tables
    df_silver_flights = spark.read.table("silver_flights")
    df_silver_transactions = spark.read.table("silver_transactions")

    # Display record counts
    print(f"Silver Flights: {df_silver_flights.count()}")
    print(f"Silver Transactions: {df_silver_transactions.count()}")

    # Preview schemas
    print("\n=== Flight Data Sample ===")
    df_silver_flights.select("MEMBER_NO", "GENDER", "AGE", "WORK_CITY", "WORK_PROVINCE", 
                            "FLIGHT_COUNT", "SEG_KM_SUM", "Points_Sum").show(5)

    print("\n=== Transaction Data Sample ===")
    df_silver_transactions.select("transaction_id", "customer_id", "amount", 
                                "status", "region", "payment_method").show(5)
    ```

## Part 2: Create Dimension Tables

Dimensions provide context for facts. Create customer, time, and geography dimensions:

    ```python
    from pyspark.sql.functions import current_timestamp, to_date, year, month, dayofmonth, dayofweek, quarter

    # === 1. Customer Dimension (from flight loyalty data) ===
    dim_customers = df_silver_flights.select(
        col("MEMBER_NO").alias("customer_key"),
        col("GENDER").alias("gender"),
        col("AGE").alias("age"),
        col("FFP_TIER").alias("loyalty_tier"),
        col("FFP_DATE").alias("loyalty_join_date"),
        col("FIRST_FLIGHT_DATE").alias("first_flight_date"),
        col("WORK_CITY").alias("city"),
        col("WORK_PROVINCE").alias("province"),
        col("WORK_COUNTRY").alias("country")
    ).withColumn("load_timestamp", current_timestamp())

    print("=== Customer Dimension ===")
    print(f"Total Customers: {dim_customers.count()}")
    dim_customers.show(5, truncate=False)

    # === 2. Geography Dimension ===
    dim_geography = df_silver_flights.select(
        col("WORK_COUNTRY").alias("country"),
        col("WORK_PROVINCE").alias("province"),
        col("WORK_CITY").alias("city")
    ).distinct() \
    .withColumn("geo_key", monotonically_increasing_id()) \
    .withColumn("load_timestamp", current_timestamp())

    print("\n=== Geography Dimension ===")
    print(f"Total Geographies: {dim_geography.count()}")
    dim_geography.show(5, truncate=False)

    # === 3. Time Dimension (from transaction dates) ===
    # Extract unique dates from transactions
    dim_time = df_silver_transactions.select(
        to_date(col("purchase_date")).alias("date")
    ).distinct() \
    .withColumn("year", year("date")) \
    .withColumn("month", month("date")) \
    .withColumn("day", dayofmonth("date")) \
    .withColumn("quarter", quarter("date")) \
    .withColumn("day_of_week", dayofweek("date")) \
    .withColumn("load_timestamp", current_timestamp())

    print("\n=== Time Dimension ===")
    print(f"Total Date Records: {dim_time.count()}")
    dim_time.show(5, truncate=False)
    ```

    ## Part 3: Create Fact Tables

    Fact tables contain measurable metrics. Create fact tables for flight activity and transactions:

    ```python
    from pyspark.sql.functions import col, sum as spark_sum, avg as spark_avg, count, round as spark_round

    # === 1. Fact Flight Activity ===
    fact_flights = df_silver_flights.select(
        col("MEMBER_NO").alias("customer_key"),
        col("FLIGHT_COUNT").alias("total_flights"),
        col("BP_SUM").alias("base_points"),
        col("SUM_YR_1").alias("year_1_flights"),
        col("SUM_YR_2").alias("year_2_flights"),
        col("SEG_KM_SUM").alias("total_km_flown"),
        col("AVG_INTERVAL").alias("avg_flight_interval_days"),
        col("MAX_INTERVAL").alias("max_flight_interval_days"),
        col("LAST_TO_END").alias("days_since_last_flight"),
        col("EXCHANGE_COUNT").alias("exchange_count"),
        col("avg_discount").alias("avg_discount_rate"),
        col("Points_Sum").alias("total_loyalty_points"),
        col("Point_NotFlight").alias("non_flight_points"),
        to_date(col("LAST_FLIGHT_DATE")).alias("last_flight_date")
    ).withColumn("load_timestamp", current_timestamp())

    print("=== Fact Flight Activity ===")
    print(f"Total Records: {fact_flights.count()}")
    fact_flights.show(5, truncate=False)

    # === 2. Fact Transactions ===
    fact_transactions = df_silver_transactions.select(
        col("transaction_id"),
        col("customer_id").cast("int").alias("customer_key"),  # Cast to int to match dim_customers
        to_date(col("purchase_date")).alias("transaction_date"),
        col("amount").cast("double").alias("transaction_amount"),
        col("status"),
        col("region"),
        col("payment_method")
    ).withColumn("load_timestamp", current_timestamp())

    print("\n=== Fact Transactions ===")
    print(f"Total Records: {fact_transactions.count()}")
    fact_transactions.show(5, truncate=False)

    # === 3. Calculate Business Metrics ===
    print("\n=== Flight Activity Metrics ===")
    fact_flights.select(
        count("*").alias("total_members"),
        spark_sum("total_flights").alias("total_flights_all"),
        spark_round(spark_avg("total_km_flown"), 2).alias("avg_km_per_member"),
        spark_sum("total_loyalty_points").alias("total_points_awarded")
    ).show()

    print("\n=== Transaction Metrics ===")
    fact_transactions.filter(col("status") == "completed").select(
        count("*").alias("completed_transactions"),
        spark_round(spark_sum("transaction_amount"), 2).alias("total_revenue"),
        spark_round(spark_avg("transaction_amount"), 2).alias("avg_transaction_value")
    ).show()
    ```

## Part 4: Write to Gold Layer

Save dimension and fact tables to the Gold layer:

    ```python
    # === Write Customer Dimension ===
    dim_customers.write \
        .format("delta") \
        .mode("overwrite") \
        .option("overwriteSchema", "true") \
        .saveAsTable("dim_customers")

    # === Write Geography Dimension ===
    dim_geography.write \
        .format("delta") \
        .mode("overwrite") \
        .option("overwriteSchema", "true") \
        .saveAsTable("dim_geography")

    # === Write Time Dimension ===
    dim_time.write \
        .format("delta") \
        .mode("overwrite") \
        .option("overwriteSchema", "true") \
        .saveAsTable("dim_time")

    # === Write Fact Flight Activity ===
    fact_flights.write \
        .format("delta") \
        .mode("overwrite") \
        .option("overwriteSchema", "true") \
        .saveAsTable("fact_flights")

    # === Write Fact Transactions ===
    fact_transactions.write \
        .format("delta") \
        .mode("overwrite") \
        .option("overwriteSchema", "true") \
        .saveAsTable("fact_transactions")

    print("Gold layer tables created successfully!")
    print(f"  - dim_customers: {spark.read.table('dim_customers').count()} records")
    print(f"  - dim_geography: {spark.read.table('dim_geography').count()} records")
    print(f"  - dim_time: {spark.read.table('dim_time').count()} records")
    print(f"  - fact_flights: {spark.read.table('fact_flights').count()} records")
    print(f"  - fact_transactions: {spark.read.table('fact_transactions').count()} records")
    ```

## Part 5: Run Analytics Queries

Test your dimensional model with business intelligence queries:

    ```python
    # === Query 1: Customer Loyalty Segmentation ===
    print("=== Customer Loyalty Segmentation ===")
    spark.sql("""
        SELECT 
            CASE 
                WHEN c.loyalty_tier = 4 THEN 'Gold'
                WHEN c.loyalty_tier = 5 THEN 'Platinum'
                WHEN c.loyalty_tier = 6 THEN 'Diamond'
                ELSE 'Silver'
            END as tier_name,
            c.loyalty_tier,
            COUNT(*) as customer_count,
            ROUND(AVG(f.total_flights), 2) as avg_flights,
            ROUND(AVG(f.total_km_flown), 2) as avg_km,
            ROUND(AVG(f.total_loyalty_points), 2) as avg_points
        FROM fact_flights f
        JOIN dim_customers c ON f.customer_key = c.customer_key
        GROUP BY c.loyalty_tier
        ORDER BY c.loyalty_tier
    """).show(truncate=False)

    # === Query 2: Geographic Flight Activity ===
    print("\n=== Top 10 Provinces by Flight Activity ===")
    spark.sql("""
        SELECT 
            c.province,
            c.country,
            COUNT(DISTINCT c.customer_key) as member_count,
            SUM(f.total_flights) as total_flights,
            ROUND(SUM(f.total_km_flown), 2) as total_km,
            ROUND(SUM(f.total_loyalty_points), 2) as total_points
        FROM fact_flights f
        JOIN dim_customers c ON f.customer_key = c.customer_key
        WHERE c.province != 'Unknown'
        GROUP BY c.province, c.country
        ORDER BY total_flights DESC
        LIMIT 10
    """).show(truncate=False)

    # === Query 3: Transaction Revenue by Region and Status ===
    print("\n=== Transaction Revenue by Region ===")
    spark.sql("""
        SELECT 
            region,
            status,
            COUNT(*) as transaction_count,
            ROUND(SUM(transaction_amount), 2) as total_revenue,
            ROUND(AVG(transaction_amount), 2) as avg_transaction
        FROM fact_transactions
        WHERE region != 'Unknown'
        GROUP BY region, status
        ORDER BY total_revenue DESC
    """).show(truncate=False)

    # === Query 4: Payment Method Analysis ===
    print("\n=== Payment Method Performance ===")
    spark.sql("""
        SELECT 
            payment_method,
            COUNT(*) as usage_count,
            ROUND(SUM(transaction_amount), 2) as total_amount,
            ROUND(AVG(transaction_amount), 2) as avg_amount
        FROM fact_transactions
        WHERE status = 'completed' AND payment_method != 'unknown'
        GROUP BY payment_method
        ORDER BY total_amount DESC
    """).show(truncate=False)

    # === Query 5: Customer Age Demographics ===
    print("\n=== Customer Age Demographics ===")
    spark.sql("""
        SELECT 
            CASE 
                WHEN age < 30 THEN '18-29'
                WHEN age >= 30 AND age < 40 THEN '30-39'
                WHEN age >= 40 AND age < 50 THEN '40-49'
                WHEN age >= 50 AND age < 60 THEN '50-59'
                ELSE '60+'
            END as age_group,
            COUNT(*) as customer_count,
            ROUND(AVG(f.total_flights), 2) as avg_flights,
            ROUND(AVG(f.total_loyalty_points), 2) as avg_points
        FROM dim_customers c
        JOIN fact_flights f ON c.customer_key = f.customer_key
        WHERE c.age IS NOT NULL
        GROUP BY 
            CASE 
                WHEN age < 30 THEN '18-29'
                WHEN age >= 30 AND age < 40 THEN '30-39'
                WHEN age >= 40 AND age < 50 THEN '40-49'
                WHEN age >= 50 AND age < 60 THEN '50-59'
                ELSE '60+'
            END
        ORDER BY age_group
    """).show(truncate=False)
    ```

## Part 6: Create Business KPI Table

Create a summary table for dashboard consumption:

    ```python
    # === Customer Lifetime Value (CLV) Summary ===
    kpi_customer_value = spark.sql("""
        SELECT 
            c.customer_key,
            c.gender,
            c.age,
            c.loyalty_tier,
            c.province,
            f.total_flights,
            f.total_km_flown,
            f.total_loyalty_points,
            f.days_since_last_flight,
            COALESCE(t.total_spent, 0) as total_spent,
            COALESCE(t.transaction_count, 0) as transaction_count,
            CASE 
                WHEN f.days_since_last_flight <= 90 THEN 'Active'
                WHEN f.days_since_last_flight <= 180 THEN 'At Risk'
                ELSE 'Inactive'
            END as customer_status
        FROM fact_flights f
        JOIN dim_customers c ON f.customer_key = c.customer_key
        LEFT JOIN (
            SELECT 
                customer_key,
                SUM(transaction_amount) as total_spent,
                COUNT(*) as transaction_count
            FROM fact_transactions
            WHERE status = 'completed'
            GROUP BY customer_key
        ) t ON c.customer_key = t.customer_key
    """)

    # Write KPI table
    kpi_customer_value.write \
        .format("delta") \
        .mode("overwrite") \
        .option("overwriteSchema", "true") \
        .saveAsTable("kpi_customer_value")

    print("Business KPI table created!")
    print(f"  - kpi_customer_value: {spark.read.table('kpi_customer_value').count()} records")

    # Preview KPIs
    kpi_customer_value.show(10, truncate=False)
    ```

## Part 7: Verify Gold Layer in OneLake

1. **Navigate to your Lakehouse** in the Fabric portal

2. **Open the Tables section** and verify:

   - `dim_customers` table exists
   - `dim_geography` table exists
   - `dim_time` table exists
   - `fact_flights` table exists
   - `fact_transactions` table exists
   - `kpi_customer_value` table exists

3. **Check the Tables folder** in Lakehouse explorer:

   - All Gold layer tables should be visible with the Delta Lake format

## Part 8: Save the Notebook

1. Click the **Save** icon (or press Ctrl+S)

1. In the "Save as new notebook" dialog:
   - **Name**: **04_Gold_Layer_Dimensional_Modeling**
   - **Select location**: **fabric-workspace-<inject key="DeploymentID" enableCopy="false"/>**
   - Click **Save**

## Success Criteria

- Customer, geography, and time dimensions created
- Fact tables for flights and transactions created
- Business KPI table for customer value analysis
- All tables saved to the Gold layer with the Delta Lake format
- Analytics queries return meaningful insights
- Tables visible in OneLake catalog

## Validation Checkpoint

**Copy this GUID and submit for validation:** `{{guid-challenge-4}}`

## Summary

In this challenge, you built a complete Gold layer with:
- **3 Dimension Tables**: Customers, Geography, Time
- **2 Fact Tables**: Flight Activity, Transactions
- **1 KPI Table**: Customer Lifetime Value with engagement status
- **5 Analytics Queries**: Loyalty segmentation, geographic analysis, revenue metrics, payment patterns, demographics

Your data is now structured for optimal analytics performance and ready for Power BI dashboards!

## Next Steps

Proceed to **Challenge 5** to build machine learning models using Fabric's Data Science workload for advanced customer analytics.
