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

1. In the first cell, load Bronze data from CSV files:

   ```python
   # Load Bronze layer data from CSV files
   df_customers = spark.read.option("header", "true").option("inferSchema", "true").csv("Files/bronze/customers.csv")
   df_orders = spark.read.option("header", "true").option("inferSchema", "true").csv("Files/bronze/orders.csv")
   df_products = spark.read.option("header", "true").option("inferSchema", "true").csv("Files/bronze/products.csv")
   df_sales = spark.read.option("header", "true").option("inferSchema", "true").csv("Files/bronze/sales.csv")
   
   print(f"Customers: {df_customers.count()} records")
   print(f"Orders: {df_orders.count()} records")
   print(f"Products: {df_products.count()} records")
   print(f"Sales: {df_sales.count()} records")
   
   # Display schema
   print("\n=== Customers Schema ===")
   df_customers.printSchema()
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
       "FirstName": "Unknown",
       "LastName": "Unknown",
       "EmailAddress": "noemail@adventure-works.com"
   })
   
   # Remove duplicate customers based on CustomerID
   df_customers_clean = df_customers_clean.dropDuplicates(["CustomerID"])
   
   print(f"Cleaned Customers: {df_customers_clean.count()} records")
   ```

1. Add a cell to standardize data types and formats:

   ```python
   from pyspark.sql.functions import upper, trim, to_date, concat_ws
   from pyspark.sql.types import IntegerType, DoubleType
   
   # Standardize text fields: trim whitespace and convert to uppercase
   # Combine FirstName and LastName into FullName
   df_customers_clean = df_customers_clean.withColumn(
       "FullName", concat_ws(" ", col("FirstName"), col("LastName"))
   )
   
   # Clean Orders data - cast datatypes
   df_orders_clean = df_orders.withColumn(
       "SalesOrderID", col("SalesOrderID").cast(IntegerType())
   ).withColumn(
       "OrderQty", col("OrderQty").cast(IntegerType())
   ).withColumn(
       "LineItemTotal", col("LineItemTotal").cast(DoubleType())
   ).withColumn(
       "OrderDate", to_date(col("OrderDate"))
   )
   
   # Remove duplicates from orders
   df_orders_clean = df_orders_clean.dropDuplicates(["SalesOrderID", "LineItem"])
   
   print(f"Cleaned Orders: {df_orders_clean.count()} records")
   ```

### Part 3: Clean Products and Sales Data

1. Add a cell to clean Products data:

   ```python
   # Clean Products data
   df_products_clean = df_products.filter(col("ProductID").isNotNull())
   df_products_clean = df_products_clean.dropDuplicates(["ProductID"])
   
   # Cast ListPrice to Double
   df_products_clean = df_products_clean.withColumn(
       "ListPrice", col("ListPrice").cast(DoubleType())
   )
   
   print(f"Cleaned Products: {df_products_clean.count()} records")
   ```

1. Add a cell to clean and enrich Sales data:

   ```python
   # Clean Sales data
   df_sales_clean = df_sales.withColumn(
       "OrderDate", to_date(col("OrderDate"))
   ).withColumn(
       "Quantity", col("Quantity").cast(IntegerType())
   ).withColumn(
       "UnitPrice", col("UnitPrice").cast(DoubleType())
   ).withColumn(
       "TaxAmount", col("TaxAmount").cast(DoubleType())
   )
   
   # Calculate total amount
   df_sales_clean = df_sales_clean.withColumn(
       "TotalAmount", (col("Quantity") * col("UnitPrice")) + col("TaxAmount")
   )
   
   print(f"Cleaned Sales: {df_sales_clean.count()} records")
   df_sales_clean.show(10)
   ```

### Part 4: Write to Silver Layer

1. Add a cell to write Silver tables:

   ```python
   # Write Customers to Silver layer
   df_customers_clean.write.format("delta").mode("overwrite").saveAsTable("silver_customers")
   
   # Write Products to Silver layer
   df_products_clean.write.format("delta").mode("overwrite").saveAsTable("silver_products")
   
   # Write Orders to Silver layer
   df_orders_clean.write.format("delta").mode("overwrite").saveAsTable("silver_orders")
   
   # Write Sales to Silver layer
   df_sales_clean.write.format("delta").mode("overwrite").saveAsTable("silver_sales")
   
   print("✅ Silver layer tables created successfully!")
   ```

### Part 5: Validate Silver Layer

1. Add a cell to validate data quality in Silver layer:

   ```python
   # Validate Silver tables
   silver_customers = spark.read.table("silver_customers")
   silver_products = spark.read.table("silver_products")
   silver_orders = spark.read.table("silver_orders")
   silver_sales = spark.read.table("silver_sales")
   
   print(f"Silver Customers: {silver_customers.count()} records")
   print(f"Silver Products: {silver_products.count()} records")
   print(f"Silver Orders: {silver_orders.count()} records")
   print(f"Silver Sales: {silver_sales.count()} records")
   
   # Check for nulls in critical fields
   print("\n=== Null Check on Silver Sales ===")
   silver_sales.select([
       count(when(col(c).isNull(), c)).alias(c) 
       for c in ["SalesOrderNumber", "CustomerName", "Item"]
   ]).show()
   ```

1. Query Silver tables using SQL:

   ```sql
   %%sql
   -- Analyze sales by product category
   SELECT 
       p.Category, 
       COUNT(DISTINCT s.SalesOrderNumber) as OrderCount, 
       SUM(s.TotalAmount) as TotalRevenue,
       AVG(s.TotalAmount) as AvgOrderValue
   FROM silver_sales s
   INNER JOIN silver_products p ON s.Item = p.ProductName
   GROUP BY p.Category
   ORDER BY TotalRevenue DESC;
   ```

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
