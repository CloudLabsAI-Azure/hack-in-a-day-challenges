# Challenge 03: Transform Data to Silver Layer Using Notebooks

## Introduction

The Bronze layer contains raw, unprocessed data with significant quality issues—missing values, duplicates, inconsistent formats, and mixed data types. Contoso's analytics team needs clean, standardized data for reliable reporting and analysis. The Silver layer serves as the cleansed and validated zone where data quality rules are applied, datatypes are standardized, and inconsistencies are resolved. In this challenge, you will use PySpark and SQL in Fabric Notebooks to transform dirty Bronze data (flight loyalty program data and customer transactions) into clean Silver tables.

## Challenge Objectives

- Create a Fabric Notebook for data transformation.
- Load and inspect flight loyalty data (CSV) and customer transaction data (JSON).
- Apply data quality checks: identify and handle nulls, remove duplicates, and validate data types.
- Standardize inconsistent values (status codes, region names, date formats).
- Clean and transform both structured (CSV) and semi-structured (JSON) data.
- Write transformed outputs to the **Silver layer** as Delta Lake tables.

## Steps to Complete

### Part 1: Create a Transformation Notebook

1. In the **Edge browser**, navigate to the **Microsoft Fabric** portal (if not already open):

   ```
   https://app.fabric.microsoft.com/
   ```

1. Navigate to your **Microsoft Fabric workspace**: **fabric-workspace-<inject key="DeploymentID" enableCopy="false"/>**

1. Select **+ New** and click on **Notebook**.

1. Attach the notebook to your Lakehouse:

   - Click **Add** (next to Lakehouses in the left pane)
   - Select **Existing Lakehouse**
   - Choose: **contoso-lakehouse-<inject key="DeploymentID" enableCopy="false"/>**

1. In the first cell, load Bronze data from CSV and JSON files:

   ```python
   # Load Bronze layer data - Flight loyalty data (CSV) and Transactions (JSON)
   from pyspark.sql.functions import col
   
   # Load flight data from CSV
   df_flights = spark.read.option("header", "true").option("inferSchema", "true").csv("Files/bronze/flight.csv")
   
   # Load customer transactions from JSON (multiLine option for array format)
   df_transactions = spark.read.option("multiLine", "true").json("Files/bronze/customer_transactions.json")
   
   print(f"Flight Records: {df_flights.count()}")
   print(f"Transaction Records: {df_transactions.count()}")
   
   # Display schema to understand structure
   print("\n=== Flight Data Schema ===")
   df_flights.printSchema()
   
   print("\n=== Transaction Data Schema ===")
   df_transactions.printSchema()
   ```

1. Run the cell to verify data loads successfully.

### Part 2: Apply Data Quality Checks and Cleansing - Flight Data

1. Add a new cell to inspect data quality issues in flight data:

   ```python
   # Profile the flight data - check for data quality issues
   from pyspark.sql.functions import col, count, when, countDistinct, isnan
   
   print("=== Flight Data Quality Profile ===")
   print(f"Total Records: {df_flights.count()}")
   print(f"Unique Members: {df_flights.select(countDistinct('MEMBER_NO')).collect()[0][0]}")
   
   # Check for missing values in critical fields
   print("\n=== Missing Values Check ===")
   missing_check = df_flights.select([
       count(when(col(c) == ".", c)).alias(c + "_dot") 
       for c in ["WORK_CITY", "WORK_PROVINCE", "WORK_COUNTRY"]
   ])
   missing_check.show()
   
   # Check for null values
   null_check = df_flights.select([
       count(when(col(c).isNull(), c)).alias(c + "_null") 
       for c in ["MEMBER_NO", "AGE", "GENDER"]
   ])
   null_check.show()
   
   # Display sample records with quality issues
   print("\n=== Sample Records with Missing City/Province ===")
   df_flights.filter((col("WORK_CITY") == ".") | (col("WORK_PROVINCE") == "")).select(
       "MEMBER_NO", "WORK_CITY", "WORK_PROVINCE", "WORK_COUNTRY", "AGE"
   ).show(10, truncate=False)
   ```

1. Add a cell to clean and standardize flight data:

   ```python
   from pyspark.sql.functions import when, trim, upper, regexp_replace
   from pyspark.sql.types import IntegerType, DoubleType, DateType
   
   # Start with the raw data
   df_flights_clean = df_flights
   
   # Replace "." with null for better handling
   for column in ["WORK_CITY", "WORK_PROVINCE", "AGE"]:
       df_flights_clean = df_flights_clean.withColumn(
           column,
           when(col(column) == ".", None).otherwise(col(column))
       )
   
   # Handle empty strings as null
   df_flights_clean = df_flights_clean.withColumn(
       "WORK_CITY",
       when((col("WORK_CITY") == "") | (col("WORK_CITY").isNull()), "Unknown").otherwise(col("WORK_CITY"))
   )
   
   df_flights_clean = df_flights_clean.withColumn(
       "WORK_PROVINCE",
       when((col("WORK_PROVINCE") == "") | (col("WORK_PROVINCE").isNull()), "Unknown").otherwise(col("WORK_PROVINCE"))
   )
   
   # Standardize city and province names - trim and convert to proper case
   df_flights_clean = df_flights_clean.withColumn(
       "WORK_CITY", trim(col("WORK_CITY"))
   ).withColumn(
       "WORK_PROVINCE", trim(col("WORK_PROVINCE"))
   )
   
   # Ensure AGE is proper integer type
   df_flights_clean = df_flights_clean.withColumn(
       "AGE", col("AGE").cast(IntegerType())
   )
   
   # Remove duplicates based on MEMBER_NO (keep first occurrence)
   df_flights_clean = df_flights_clean.dropDuplicates(["MEMBER_NO"])
   
   # Filter out records where critical fields are still null
   df_flights_clean = df_flights_clean.filter(col("MEMBER_NO").isNotNull())
   
   print(f"Cleaned Flight Records: {df_flights_clean.count()}")
   print(f"Records removed: {df_flights.count() - df_flights_clean.count()}")
   
   # Show sample of cleaned data
   df_flights_clean.select("MEMBER_NO", "WORK_CITY", "WORK_PROVINCE", "AGE", "GENDER").show(10, truncate=False)
   ```

### Part 3: Clean and Standardize JSON Transaction Data

1. Add a cell to inspect transaction data quality:

   ```python
   # Profile transaction data quality
   print("=== Transaction Data Quality Profile ===")
   print(f"Total Records: {df_transactions.count()}")
   print(f"Unique Transactions: {df_transactions.select(countDistinct('transaction_id')).collect()[0][0]}")
   
   # Check for null values in critical fields
   print("\n=== Null Values Check ===")
   null_check_txn = df_transactions.select([
       count(when(col(c).isNull(), c)).alias(c) 
       for c in ["customer_id", "amount", "payment_method"]
   ])
   null_check_txn.show()
   
   # Check for duplicate transactions
   duplicate_txn = df_transactions.groupBy("transaction_id").count().filter("count > 1")
   print(f"\nDuplicate Transactions: {duplicate_txn.count()}")
   
   # Display sample records with issues
   print("\n=== Sample Records with Quality Issues ===")
   df_transactions.filter(
       col("customer_id").isNull() | col("amount").isNull() | (col("email") == "")
   ).show(truncate=False)
   ```

1. Add a cell to clean and standardize transaction data:

   ```python
   from pyspark.sql.functions import lower, upper, regexp_replace, to_date, coalesce, lit
   
   # Start cleaning transactions
   df_transactions_clean = df_transactions
   
   # Handle null customer_ids - filter them out or assign default
   df_transactions_clean = df_transactions_clean.filter(col("customer_id").isNotNull())
   
   # Standardize status values to lowercase
   df_transactions_clean = df_transactions_clean.withColumn(
       "status",
       lower(trim(col("status")))
   )
   
   # Standardize region names - convert to proper case
   df_transactions_clean = df_transactions_clean.withColumn(
       "region",
       when(col("region").isNull() | (col("region") == ""), "Unknown")
       .otherwise(trim(upper(col("region"))))
   )
   
   # Standardize payment_method - clean up inconsistencies
   df_transactions_clean = df_transactions_clean.withColumn(
       "payment_method",
       when(col("payment_method").isNull() | (col("payment_method") == "."), "unknown")
       .when(lower(col("payment_method")).like("%credit%card%"), "credit_card")
       .when(lower(col("payment_method")).like("%debit%card%"), "debit_card")
       .when(lower(col("payment_method")).like("%paypal%"), "paypal")
       .when(lower(col("payment_method")).like("%wire%transfer%"), "wire_transfer")
       .otherwise(lower(trim(col("payment_method"))))
   )
   
   # Standardize email - convert to lowercase
   df_transactions_clean = df_transactions_clean.withColumn(
       "email",
       when((col("email") == "") | (col("email") == "invalid-email"), None)
       .otherwise(lower(trim(col("email"))))
   )
   
   # Handle invalid amounts - filter out or set to 0
   df_transactions_clean = df_transactions_clean.withColumn(
       "amount",
       when(col("amount").isNull() | (col("amount") == "invalid"), 0.0)
       .otherwise(col("amount").cast(DoubleType()))
   )
   
   # Standardize date format (handle multiple formats)
   df_transactions_clean = df_transactions_clean.withColumn(
       "purchase_date",
       coalesce(
           to_date(col("purchase_date"), "yyyy-MM-dd"),
           to_date(col("purchase_date"), "MM/dd/yyyy"),
           to_date(col("purchase_date"), "yyyy/MM/dd")
       )
   )
   
   # Remove duplicate transactions
   df_transactions_clean = df_transactions_clean.dropDuplicates(["transaction_id"])
   
   # Handle missing customer names
   df_transactions_clean = df_transactions_clean.withColumn(
       "customer_name",
       when((col("customer_name") == "") | (col("customer_name") == "."), "Unknown")
       .otherwise(trim(col("customer_name")))
   )
   
   print(f"Cleaned Transaction Records: {df_transactions_clean.count()}")
   print(f"Records removed: {df_transactions.count() - df_transactions_clean.count()}")
   
   # Show sample of cleaned data
   df_transactions_clean.show(10, truncate=False)
   ```

### Part 4: Write to Silver Layer

1. Add a cell to write Silver tables:

   ```python
   # Write cleaned Flight data to Silver layer
   df_flights_clean.write.format("delta").mode("overwrite").saveAsTable("silver_flights")
   
   # Write cleaned Transaction data to Silver layer
   df_transactions_clean.write.format("delta").mode("overwrite").saveAsTable("silver_transactions")
   
   print("Silver layer tables created successfully!")
   print(f"  - silver_flights: {df_flights_clean.count()} records")
   print(f"  - silver_transactions: {df_transactions_clean.count()} records")
   ```

### Part 5: Validate Silver Layer

1. Add a cell to validate data quality in Silver layer:

   ```python
   # Validate Silver tables
   silver_flights = spark.read.table("silver_flights")
   silver_transactions = spark.read.table("silver_transactions")
   
   print("=== Silver Layer Validation ===")
   print(f"Silver Flights: {silver_flights.count()} records")
   print(f"Silver Transactions: {silver_transactions.count()} records")
   
   # Check for null values in critical fields after cleaning
   print("\n=== Silver Flights - Null Check ===")
   silver_flights.select([
       count(when(col(c).isNull(), c)).alias(c) 
       for c in ["MEMBER_NO", "WORK_CITY", "WORK_PROVINCE"]
   ]).show()
   
   print("\n=== Silver Transactions - Null Check ===")
   silver_transactions.select([
       count(when(col(c).isNull(), c)).alias(c) 
       for c in ["transaction_id", "customer_id", "status", "region"]
   ]).show()
   
   # Verify data standardization
   print("\n=== Standardized Status Values ===")
   silver_transactions.groupBy("status").count().show()
   
   print("\n=== Standardized Region Values ===")
   silver_transactions.groupBy("region").count().show()
   
   print("\n=== Standardized Payment Methods ===")
   silver_transactions.groupBy("payment_method").count().show()
   ```

1. Query Silver tables using SQL:

   ```sql
   %%sql
   -- Analyze transactions by region and status
   SELECT 
       region,
       status,
       COUNT(*) as transaction_count,
       SUM(amount) as total_amount,
       AVG(amount) as avg_amount
   FROM silver_transactions
   WHERE amount > 0
   GROUP BY region, status
   ORDER BY total_amount DESC;
   ```

### Part 6: Save the Notebook

1. Click the **Save** icon (or press Ctrl+S)

1. In the "Save as new notebook" dialog:
   - **Name**: **Bronze-to-Silver-Transformation**
   - **Select location**: **fabric-workspace-<inject key="DeploymentID" enableCopy="false"/>**
   - Click **Save**

## Success Criteria

- Fabric Notebook created and attached to Lakehouse successfully.
- Flight data (CSV) and transaction data (JSON) loaded from the Bronze layer.
- Data quality issues identified: missing values (".", empty strings, nulls), inconsistent formatting, duplicates.
- Data quality checks applied: nulls handled, duplicates removed, datatypes standardized.
- Inconsistent values standardized (status, region, payment_method, city/province names).
- Both structured (CSV) and semi-structured (JSON) data were cleaned successfully.
- Silver layer tables created in Delta Lake format with validated data quality.
- SQL queries return clean, standardized data from Silver tables.

## Additional Resources

- [Notebooks in Microsoft Fabric](https://learn.microsoft.com/fabric/data-engineering/how-to-use-notebook)
- [PySpark DataFrame API](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html)
- [Delta Lake in Fabric](https://learn.microsoft.com/fabric/data-engineering/lakehouse-and-delta-tables)
- [Data Quality in Fabric](https://learn.microsoft.com/fabric/data-engineering/data-quality-overview)
- [Working with JSON in PySpark](https://spark.apache.org/docs/latest/sql-data-sources-json.html)

Now, click **Next** to continue to **Challenge 04**.
   GROUP BY p.Category
   ORDER BY TotalRevenue DESC;

<validation step="f5d9a7e3-f2cd-4603-82ce-b275098789c9" />

> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Fabric Notebook created and attached to Lakehouse successfully.
- Data quality checks applied: nulls handled, duplicates removed, datatypes standardized.
- Related datasets (Customers, Orders, Products) joined successfully.
- Codes standardized (Region, Status, Product Family).
- Silver layer tables created in Delta Lake format with validated data quality.

## Additional Resources

- [Notebooks in Microsoft Fabric](https://learn.microsoft.com/fabric/data-engineering/how-to-use-notebook)
- [PySpark DataFrame API](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html)
- [Delta Lake in Fabric](https://learn.microsoft.com/fabric/data-engineering/lakehouse-and-delta-tables)
- [Data Quality in Fabric](https://learn.microsoft.com/fabric/data-engineering/data-quality-overview)

Now, click **Next** to continue to **Challenge 04**.
