# Challenge 03: Transform Data to Silver Layer Using Notebooks

## Introduction

The Bronze layer contains raw, unprocessed data with potential quality issues—duplicates, null values, inconsistent formats, and unjoined datasets. Contoso's analytics team needs clean, standardized data for reliable reporting and analysis. The Silver layer serves as the cleansed and validated zone where data quality rules are applied, datatypes are standardized, and related datasets are joined. In this challenge, you will use PySpark and SQL in Fabric Notebooks to transform Bronze data into clean Silver tables.

## Challenge Objectives

- Create a Fabric Notebook for data transformation.
- Apply data quality checks: handle nulls, remove duplicates, validate data types.
- Join related datasets (Customers, Orders, Products) into unified Silver tables.
- Standardize codes and formats (Region, Product Family, Status codes).
- Write transformed outputs to **Silver layer** as Delta Lake tables.

## Steps to Complete

### Part 1: Create a Transformation Notebook

1. In the **Edge browser**, navigate to the **Microsoft Fabric** portal (if not already open):

   ```
   https://app.fabric.microsoft.com/
   ```

1. Navigate to your **Microsoft Fabric workspace**: **fabric-workspace-<inject key="DeploymentID"></inject>**

1. Select **+ New** → **Notebook**

   - Name: **Bronze-to-Silver-Transformation**

1. Attach the notebook to your Lakehouse:

   - Click **Add** (next to Lakehouses in the left pane)
   - Select **Existing Lakehouse**
   - Choose: **contoso-lakehouse-<inject key="DeploymentID"></inject>**

1. In the first cell, load Bronze data from files:

   ```python
   # Load Bronze layer data
   df_customers = spark.read.parquet("Files/bronze/customers/")
   df_orders = spark.read.parquet("Files/bronze/orders/")
   df_products = spark.read.parquet("Files/bronze/products/")
   
   print(f"Customers: {df_customers.count()} records")
   print(f"Orders: {df_orders.count()} records")
   print(f"Products: {df_products.count()} records")
   ```

1. Run the cell to verify data loads successfully.

### Part 2: Apply Data Quality Checks and Cleansing

1. Add a new cell to inspect data quality:

   ```python
   # Check for null values in customers
   from pyspark.sql.functions import col, count, when
   
   df_customers.select([
       count(when(col(c).isNull(), c)).alias(c) 
       for c in df_customers.columns
   ]).show()
   ```

1. Add a cell to handle null values and duplicates:

   ```python
   # Remove rows with null CustomerID (critical field)
   df_customers_clean = df_customers.filter(col("CustomerID").isNotNull())
   
   # Fill null values in non-critical fields
   df_customers_clean = df_customers_clean.fillna({
       "Phone": "Unknown",
       "Email": "noemail@contoso.com"
   })
   
   # Remove duplicate customers based on CustomerID
   df_customers_clean = df_customers_clean.dropDuplicates(["CustomerID"])
   
   print(f"Cleaned Customers: {df_customers_clean.count()} records")
   ```

1. Add a cell to standardize data types and formats:

   ```python
   from pyspark.sql.functions import upper, trim, to_date
   from pyspark.sql.types import IntegerType, DoubleType
   
   # Standardize text fields: trim whitespace and convert to uppercase
   df_customers_clean = df_customers_clean.withColumn(
       "CustomerName", upper(trim(col("CustomerName")))
   )
   
   # Cast datatypes
   df_orders_clean = df_orders.withColumn(
       "OrderID", col("OrderID").cast(IntegerType())
   ).withColumn(
       "Amount", col("Amount").cast(DoubleType())
   ).withColumn(
       "OrderDate", to_date(col("OrderDate"))
   )
   
   # Remove duplicates from orders
   df_orders_clean = df_orders_clean.dropDuplicates(["OrderID"])
   ```

1. Add a cell to standardize codes:

   ```python
   from pyspark.sql.functions import when
   
   # Standardize Region codes
   df_orders_clean = df_orders_clean.withColumn(
       "Region",
       when(col("Region").isin(["East", "EAST", "E"]), "EAST")
       .when(col("Region").isin(["West", "WEST", "W"]), "WEST")
       .when(col("Region").isin(["North", "NORTH", "N"]), "NORTH")
       .when(col("Region").isin(["South", "SOUTH", "S"]), "SOUTH")
       .otherwise("UNKNOWN")
   )
   
   # Standardize Status codes
   df_orders_clean = df_orders_clean.withColumn(
       "Status",
       when(col("Status").isin(["Completed", "COMPLETED", "Complete"]), "COMPLETED")
       .when(col("Status").isin(["Pending", "PENDING", "In Progress"]), "PENDING")
       .when(col("Status").isin(["Cancelled", "CANCELLED", "Cancel"]), "CANCELLED")
       .otherwise("UNKNOWN")
   )
   ```

### Part 3: Join Related Datasets

1. Add a cell to clean Products data:

   ```python
   # Clean Products data
   df_products_clean = df_products.filter(col("ProductID").isNotNull())
   df_products_clean = df_products_clean.dropDuplicates(["ProductID"])
   
   # Standardize Product Family
   df_products_clean = df_products_clean.withColumn(
       "ProductFamily", upper(trim(col("ProductFamily")))
   )
   ```

1. Add a cell to join Orders with Customers and Products:

   ```python
   # Join Orders with Customers
   df_silver_orders = df_orders_clean.join(
       df_customers_clean,
       on="CustomerID",
       how="left"
   )
   
   # Join with Products
   df_silver_orders = df_silver_orders.join(
       df_products_clean,
       on="ProductID",
       how="left"
   )
   
   # Select relevant columns for Silver layer
   df_silver_orders = df_silver_orders.select(
       "OrderID",
       "OrderDate",
       "CustomerID",
       "CustomerName",
       "ProductID",
       "ProductName",
       "ProductFamily",
       "Amount",
       "Region",
       "Status"
   )
   
   print(f"Silver Orders (joined): {df_silver_orders.count()} records")
   df_silver_orders.show(10)
   ```

### Part 4: Write to Silver Layer

1. Add a cell to write Silver tables:

   ```python
   # Write Customers to Silver layer
   df_customers_clean.write.format("delta").mode("overwrite").saveAsTable("silver_customers")
   
   # Write Products to Silver layer
   df_products_clean.write.format("delta").mode("overwrite").saveAsTable("silver_products")
   
   # Write joined Orders to Silver layer
   df_silver_orders.write.format("delta").mode("overwrite").saveAsTable("silver_orders")
   
   print("✅ Silver layer tables created successfully!")
   ```

### Part 5: Validate Silver Layer

1. Add a cell to validate data quality in Silver layer:

   ```python
   # Validate Silver tables
   silver_customers = spark.read.table("silver_customers")
   silver_products = spark.read.table("silver_products")
   silver_orders = spark.read.table("silver_orders")
   
   print(f"Silver Customers: {silver_customers.count()} records")
   print(f"Silver Products: {silver_products.count()} records")
   print(f"Silver Orders: {silver_orders.count()} records")
   
   # Check for nulls in critical fields
   silver_orders.select([
       count(when(col(c).isNull(), c)).alias(c) 
       for c in ["OrderID", "CustomerID", "ProductID"]
   ]).show()
   ```

1. Query Silver tables using SQL:

   ```sql
   %%sql
   SELECT Region, Status, COUNT(*) as OrderCount, SUM(Amount) as TotalAmount
   FROM silver_orders
   GROUP BY Region, Status
   ORDER BY TotalAmount DESC;
   ```

<validation step="c3d4e5f6-a7b8-4c9d-0e1f-2a3b4c5d6e7f" />

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
- [Data Quality Best Practices](https://learn.microsoft.com/azure/databricks/lakehouse/data-quality)

Now, click **Next** to continue to **Challenge 04**.
