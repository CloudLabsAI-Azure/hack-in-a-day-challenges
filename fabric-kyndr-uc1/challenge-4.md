# Challenge 04: Build Gold Layer & Business Domains

## Introduction

The Silver layer contains clean, standardized data, but it's still organized by source systems rather than business domains. Contoso's business stakeholders need analytics-ready data models organized around their key business areas—Sales, Finance, and Operations. The Gold layer serves as the curated zone where data is modeled into star schemas with fact and dimension tables, aggregated for performance, and aligned with business reporting needs. In this challenge, you will create Gold layer tables organized by business domains, implementing dimensional models that serve as the single source of truth for analytics.

## Challenge Objectives

- Identify key business domains for Contoso (Sales, Finance, Operations).
- Create Gold layer dimension tables (Customers, Products, Time).
- Build Gold layer fact tables (Sales Facts, Order Facts).
- Apply business logic and aggregations for optimized analytics.
- Implement star schema patterns for efficient Power BI reporting.

## Steps to Complete

### Part 1: Define Business Domains

1. In the **Edge browser**, navigate to the **Microsoft Fabric** portal (if not already open):

   ```
   https://app.fabric.microsoft.com/
   ```

1. Navigate to your **Microsoft Fabric workspace**: **fabric-workspace-<inject key="DeploymentID"></inject>**

1. Navigate to your **Fabric Notebook**: **Bronze-to-Silver-Transformation** or create a new one:

   - Name: **Silver-to-Gold-Business-Models**
   - Attach to: **contoso-lakehouse-<inject key="DeploymentID"></inject>**

1. Add a markdown cell documenting the business domains:

   ```markdown
   # Contoso Business Domains
   
   ## 1. Sales Domain
   - Fact: Sales transactions with measures (Amount, Quantity, Revenue)
   - Dimensions: Customer, Product, Time, Region
   
   ## 2. Finance Domain
   - Fact: Revenue, Costs, Profit calculations
   - Dimensions: Account, Department, Time
   
   ## 3. Operations Domain
   - Fact: Order fulfillment, delivery metrics
   - Dimensions: Status, Region, Time
   ```

### Part 2: Create Gold Dimension Tables

1. Add a cell to load Silver data:

   ```python
   # Load Silver layer tables
   df_silver_customers = spark.read.table("silver_customers")
   df_silver_products = spark.read.table("silver_products")
   df_silver_orders = spark.read.table("silver_orders")
   ```

1. Create **Dim_Customer** dimension table:

   ```python
   from pyspark.sql.functions import col, current_timestamp
   
   # Create Customer Dimension with SCD Type 1 approach
   df_dim_customer = df_silver_customers.select(
       col("CustomerID").alias("CustomerKey"),
       col("FullName").alias("CustomerName"),
       col("FirstName"),
       col("LastName"),
       col("EmailAddress"),
       current_timestamp().alias("LoadDate")
   ).distinct()
   
   # Write to Gold layer
   df_dim_customer.write.format("delta").mode("overwrite").saveAsTable("gold_dim_customer")
   
   print(f"✅ Gold Dim_Customer created: {df_dim_customer.count()} records")
   df_dim_customer.show(5)
   ```

1. Create **Dim_Product** dimension table:

   ```python
   # Create Product Dimension
   df_dim_product = df_silver_products.select(
       col("ProductID").alias("ProductKey"),
       col("ProductName"),
       col("Category"),
       col("ListPrice"),
       current_timestamp().alias("LoadDate")
   ).distinct()
   
   # Write to Gold layer
   df_dim_product.write.format("delta").mode("overwrite").saveAsTable("gold_dim_product")
   
   print(f"✅ Gold Dim_Product created: {df_dim_product.count()} records")
   df_dim_product.show(5)
   ```

1. Create **Dim_Date** dimension table:

   ```python
   from pyspark.sql.functions import year, month, dayofmonth, dayofweek, quarter
   from datetime import datetime, timedelta
   
   # Generate date dimension for the past 3 years
   start_date = datetime(2022, 1, 1)
   end_date = datetime(2025, 12, 31)
   date_range = [(start_date + timedelta(days=x),) for x in range((end_date - start_date).days + 1)]
   
   df_dates = spark.createDataFrame(date_range, ["Date"])
   
   df_dim_date = df_dates.select(
       col("Date").alias("DateKey"),
       year(col("Date")).alias("Year"),
       quarter(col("Date")).alias("Quarter"),
       month(col("Date")).alias("Month"),
       dayofmonth(col("Date")).alias("Day"),
       dayofweek(col("Date")).alias("DayOfWeek")
   )
   
   # Write to Gold layer
   df_dim_date.write.format("delta").mode("overwrite").saveAsTable("gold_dim_date")
   
   print(f"✅ Gold Dim_Date created: {df_dim_date.count()} records")
   ```

### Part 3: Create Gold Fact Tables - Sales Domain

1. Create **Fact_Sales** table with business logic:

   ```python
   from pyspark.sql.functions import sum, count, avg, round, year, month
   
   # Create Sales Fact table from Silver Sales
   # Join with products to get ProductID for dimensional modeling
   df_products_lookup = df_silver_products.select("ProductID", "ProductName")
   
   df_fact_sales = df_silver_sales.join(
       df_products_lookup,
       df_silver_sales.Item == df_products_lookup.ProductName,
       "left"
   ).select(
       col("SalesOrderNumber").alias("OrderNumber"),
       col("SalesOrderLineNumber").alias("LineNumber"),
       col("OrderDate").alias("DateKey"),
       col("CustomerName"),
       col("ProductID").alias("ProductKey"),
       col("Item").alias("ProductName"),
       col("Quantity"),
       col("UnitPrice"),
       col("TaxAmount"),
       col("TotalAmount").alias("SalesAmount"),
       (col("TotalAmount") * 0.7).alias("Cost"),  # Assume 30% margin
       (col("TotalAmount") * 0.3).alias("Profit")  # 30% profit
   )
   
   # Write to Gold layer
   df_fact_sales.write.format("delta").mode("overwrite").saveAsTable("gold_fact_sales")
   
   print(f"✅ Gold Fact_Sales created: {df_fact_sales.count()} records")
   df_fact_sales.show(5)
   ```

1. Create aggregated sales summary for performance:

   ```python
   # Create aggregated Sales Summary by Year and Month
   df_sales_summary = df_fact_sales.groupBy(
       year(col("DateKey")).alias("Year"),
       month(col("DateKey")).alias("Month"),
       col("ProductKey")
   ).agg(
       count("OrderNumber").alias("OrderCount"),
       round(sum("SalesAmount"), 2).alias("TotalSales"),
       round(sum("Profit"), 2).alias("TotalProfit"),
       round(avg("SalesAmount"), 2).alias("AvgLineItemValue")
   )
   
   # Write to Gold layer
   df_sales_summary.write.format("delta").mode("overwrite").saveAsTable("gold_sales_summary")
   
   print(f"✅ Gold Sales_Summary created: {df_sales_summary.count()} records")
   df_sales_summary.show(10)
   ```

### Part 4: Create Finance Domain View

1. Create a consolidated Finance view:

   ```sql
   %%sql
   CREATE OR REPLACE VIEW gold_finance_revenue AS
   SELECT 
       YEAR(DateKey) as FiscalYear,
       MONTH(DateKey) as FiscalMonth,
       SUM(SalesAmount) as TotalRevenue,
       SUM(Cost) as TotalCost,
       SUM(Profit) as NetProfit,
       (SUM(Profit) / SUM(SalesAmount) * 100) as ProfitMarginPercent,
       COUNT(DISTINCT OrderNumber) as TotalOrders
   FROM gold_fact_sales
   GROUP BY YEAR(DateKey), MONTH(DateKey)
   ORDER BY FiscalYear DESC, FiscalMonth DESC;
   ```

1. Query the Finance view:

   ```sql
   %%sql
   SELECT * FROM gold_finance_revenue;
   ```

### Part 5: Validate Gold Layer and Star Schema

1. Add a cell to validate all Gold tables:

   ```python
   # List all Gold layer tables
   gold_tables = [table.name for table in spark.catalog.listTables() if table.name.startswith("gold_")]
   
   print("📊 Gold Layer Tables:")
   for table in gold_tables:
       count = spark.read.table(table).count()
       print(f"  ✅ {table}: {count} records")
   ```

1. Document the star schema relationships:

   ```python
   print("""
   ⭐ Star Schema Design:
   
   FACT TABLES:
   - gold_fact_sales (Grain: One row per sales order line item)
   
   DIMENSION TABLES:
   - gold_dim_customer (Customer attributes: ID, Name, Email)
   - gold_dim_product (Product attributes: ID, Name, Category, Price)
   - gold_dim_date (Date attributes: Year, Quarter, Month, Day)
   
   AGGREGATE TABLES:
   - gold_sales_summary (Pre-aggregated by Year/Month/Product)
   
   RELATIONSHIPS:
   - Fact_Sales -> Dim_Product (ProductKey = ProductID)
   - Fact_Sales -> Dim_Date (DateKey = OrderDate)
   - Fact_Sales -> Dim_Customer (CustomerName lookup)
   """)
   ```

<validation step="d4e5f6a7-b8c9-4d0e-1f2a-3b4c5d6e7f8a" />

> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Business domains identified: Sales, Finance, Operations.
- Dimension tables created (Dim_Customer, Dim_Product, Dim_Date) with proper attributes.
- Fact tables created (Fact_Sales, Fact_Operations) with business measures.
- Star schema relationships documented and validated.
- Aggregated summary tables created for optimized query performance.
- Finance domain view created with revenue and profit calculations.

## Additional Resources

- [Dimensional Modeling Best Practices](https://learn.microsoft.com/power-bi/guidance/star-schema)
- [Delta Lake Tables in Fabric](https://learn.microsoft.com/fabric/data-engineering/lakehouse-and-delta-tables)
- [Star Schema Design](https://learn.microsoft.com/power-bi/guidance/star-schema)
- [Slowly Changing Dimensions](https://learn.microsoft.com/sql/integration-services/dimension-processing-destination)

Now, click **Next** to continue to **Challenge 05**.
