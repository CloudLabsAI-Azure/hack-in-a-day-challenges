# Challenge: Unified Data Foundation with Fabric

**Estimated Time:** 4-5 Hours  

**Industry Focus:** Airlines / Customer Loyalty Programs / Data Engineering

## Problem Statement
Enterprises struggle with fragmented data across multiple systems—ERP, CRM, legacy databases, and unstructured storage—leading to inconsistent reporting, data quality issues, and inability to leverage advanced analytics. Manual ETL processes are slow, error-prone, and difficult to scale. There's no unified platform for data engineering, data science, and business intelligence.

In this challenge, you will build an **end-to-end data lakehouse solution** using Microsoft Fabric OneLake with the Medallion architecture (Bronze → Silver → Gold layers). You'll ingest raw flight loyalty and transaction data, apply data quality transformations with PySpark, create dimensional models for analytics, perform ML-based customer segmentation with Fabric Data Science, and build interactive Power BI dashboards—all within a unified analytics platform.

## Goals
By the end of this challenge, you will deliver a **complete data lakehouse platform that ingests dirty data, transforms it through quality layers, creates analytics-ready dimensional models, enriches with ML customer segments, and surfaces insights through interactive Power BI dashboards** including:

- Deploy Microsoft Fabric capacity from Azure and create workspaces with OneLake Lakehouses
- Implement Medallion architecture (Bronze/Silver/Gold) for data quality and governance
- Cleanse and transform data using PySpark notebooks in Fabric
- Build dimensional models with star schema design for analytics optimization
- Perform ML customer segmentation using Fabric Data Science with MLflow tracking
- Create Power BI dashboards with real-time connectivity to OneLake
- Enable self-service analytics for business users with governed data

## Prerequisites
- **Skill Level:** Basic familiarity with Python, SQL, and data concepts
- **Audience:** Data engineers, analytics engineers, BI developers, data scientists
- **Technology Stack:** Microsoft Fabric (OneLake, Data Engineering, Data Science), Azure Portal, PySpark, Delta Lake, MLflow, Power BI Desktop/Service, Python scikit-learn

## Datasets
Use the following sample datasets provided in lab files:

- **Flight Loyalty Data (flight.csv):** 62,988 customer records from airline loyalty program with data quality issues (missing values, duplicates, inconsistent formatting)
- **Customer Transactions (customer_transactions.json):** 15 transaction records in JSON format with nulls, duplicates, and inconsistent values

Download datasets from GitHub repository:
```
https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/unified-data-foundation-with-fabric.zip
```

Extract to: `C:\LabFiles\unified-data-foundation-with-fabric\dataset\`

| File Path | Description |
|-----------|-------------|
| `C:\LabFiles\unified-data-foundation-with-fabric\dataset\flight.csv` | Flight loyalty program data with data quality issues |
| `C:\LabFiles\unified-data-foundation-with-fabric\dataset\customer_transactions.json` | Customer transaction data in JSON format |

## Challenge Objectives

### **Challenge 1: Set Up Microsoft Fabric Workspace and OneLake Lakehouse**
**Estimated Duration:** 45 Minutes

#### Objective
Establish the foundational Microsoft Fabric infrastructure including capacity deployment, workspace creation, and Lakehouse initialization with Medallion architecture folder structure.

#### Tasks
1. **Deploy Microsoft Fabric Capacity from Azure Portal:**
   - Navigate to Azure Portal and search for **Microsoft Fabric (preview)**
   - Create new Fabric capacity with F2 SKU (2 vCores, 4 GB RAM)
   - Configure resource group: **challenge-rg-<inject key="DeploymentID"></inject>**
   - Set capacity name: **fabriccapacity<inject key="DeploymentID"></inject>**
   - Select region: **<inject key="Region"></inject>**
   - Assign capacity administrator: **odl_user_<inject key="DeploymentID"></inject>**
   - Wait for deployment to complete (approximately 2-3 minutes)

2. **Create Microsoft Fabric Workspace:**
   - Navigate to Microsoft Fabric portal: `https://app.fabric.microsoft.com/`
   - Create new workspace: **fabric-workspace-<inject key="DeploymentID"></inject>**
   - Configure Advanced settings to use **Fabric capacity** license mode
   - Assign the F2 capacity deployed from Azure
   - Explore Fabric workload components (Data Engineering, Data Science, Data Warehouse, Real-Time Analytics, Power BI)

3. **Understand Microsoft Fabric Architecture:**
   - **OneLake:** Single unified namespace for all data across the organization (compare to OneDrive for data)
   - All Fabric workloads automatically store data in OneLake using Delta Lake format
   - OneLake provides unified data access across Lakehouses, Warehouses, and KQL databases
   - Medallion Architecture Pattern:
     - **Bronze Layer (Raw Zone):** Stores raw, unprocessed data exactly as ingested
     - **Silver Layer (Cleansed Zone):** Contains validated, deduplicated, and standardized data
     - **Gold Layer (Curated Zone):** Business-level aggregates, star schemas, and analytics-ready models

4. **Create OneLake Lakehouse with Medallion Structure:**
   - In Fabric workspace, create new **Lakehouse**: **contoso_lakehouse_<inject key="DeploymentID"></inject>**
   - Understand Lakehouse components:
     - **Files:** For storing raw files (Bronze layer)
     - **Tables:** For Delta Lake tables (Silver and Gold layers)
     - **SQL analytics endpoint:** For querying tables using T-SQL
   - Create folder structure for Medallion layers:
     - Create subfolder: **bronze** (for raw data ingestion)
     - Create subfolder: **silver** (for cleansed data)
     - Create subfolder: **gold** (for dimensional models)
   - Note the OneLake path for unified data access: `abfss://[workspace]@onelake.dfs.fabric.microsoft.com/[lakehouse]/Files`

5. **Download Sample Datasets:**
   - Download ZIP from GitHub repository
   - Extract datasets to `C:\LabFiles\unified-data-foundation-with-fabric\dataset\`
   - Verify presence of flight.csv and customer_transactions.json

#### Validation Check
- Microsoft Fabric capacity (F2 SKU) successfully deployed from Azure Portal
- Fabric workspace created with Fabric capacity assigned
- OneLake Lakehouse created with proper naming convention
- Medallion folder structure (bronze/silver/gold) created in Files section
- Sample datasets downloaded and verified in LabVM
- Understanding of OneLake unified data lake and Medallion architecture demonstrated

### **Challenge 2: Ingest Raw Data into the Bronze Layer**
**Estimated Duration:** 30 Minutes

#### Objective
Upload raw data files from multiple sources into the Bronze layer of the Lakehouse to serve as the landing zone for unprocessed data.

#### Tasks
1. **Access Sample Dataset Files:**
   - Open File Explorer in LabVM
   - Navigate to `C:\LabFiles\unified-data-foundation-with-fabric\dataset\`
   - Verify presence of:
     - `flight.csv` - 62,990 records of flight loyalty program data
     - `customer_transactions.json` - 15 transaction records in JSON format
   - Preview files to identify data quality issues:
     - Missing values represented as "." or empty strings
     - Inconsistent city/province names
     - Null values in critical fields
     - Duplicate records
     - Inconsistent formatting (status, region, payment methods)

2. **Upload CSV Data to Bronze Layer:**
   - In Microsoft Fabric portal, navigate to workspace and open Lakehouse
   - Navigate to **Files** → **bronze** folder
   - Upload **flight.csv** using Upload files option
   - Wait for upload to complete (~63K records)
   - Verify file appears in Bronze layer

3. **Upload JSON Data to Bronze Layer:**
   - In the same **bronze** folder
   - Upload **customer_transactions.json** using Upload files option
   - Verify JSON file appears in Bronze layer

4. **Preview Raw Data and Identify Quality Issues:**
   - Click on **flight.csv** to preview data
   - Observe data quality issues:
     - Missing values (represented as "." or empty strings)
     - Inconsistent city/province names ("beijing", ".", empty)
     - Mixed data types in some columns
   - Click on **customer_transactions.json** to preview
   - Observe JSON quality issues:
     - Null values in customer_id and amount fields
     - Inconsistent status values ("completed" vs "COMPLETED")
     - Duplicate transaction IDs
     - Invalid email formats
     - Inconsistent date formats
     - Mixed case region names

5. **Validate Bronze Layer Ingestion:**
   - Confirm both files are visible in **Files** → **bronze** folder
   - Verify file sizes and record counts match source files
   - Note the OneLake storage path for future reference
   - Document observed data quality issues for Silver layer transformation

#### Validation Check
- Sample datasets located in LabVM at correct path (`C:\LabFiles\unified-data-foundation-with-fabric\dataset\`)
- **flight.csv** (62,990 records) successfully uploaded to Bronze layer
- **customer_transactions.json** (15 records) successfully uploaded to Bronze layer
- Both files visible in Lakehouse Files explorer under bronze folder
- File preview displays data with identifiable quality issues
- Ready to proceed to data cleansing and transformation

### **Challenge 3: Transform Data to Silver Layer Using PySpark Notebooks**
**Estimated Duration:** 60 Minutes

#### Objective
Create PySpark transformations in Fabric Notebooks to cleanse, validate, and standardize data from Bronze layer, writing high-quality outputs to Silver layer Delta tables.

#### Tasks
1. **Create Fabric Notebook for Data Transformation:**
   - In Fabric workspace, create new **Notebook**
   - Attach notebook to Lakehouse: **contoso_lakehouse_<inject key="DeploymentID"></inject>**
   - Understand Fabric Notebooks:
     - Native PySpark and SQL support
     - Integrated with OneLake Lakehouse
     - Supports Python, R, Scala
     - Built-in visualization capabilities

2. **Load Bronze Layer Data with PySpark:**
   - Load flight.csv from Bronze layer using Spark read with header and schema inference
   - Load customer_transactions.json with multiLine option for array format
   - Display schemas to understand data structure
   - Count records to verify data loading
   - Use `printSchema()` to inspect data types

3. **Profile and Analyze Data Quality Issues:**
   - **Flight Data Quality Checks:**
     - Count missing values represented as "." in WORK_CITY, WORK_PROVINCE
     - Check for null values in critical fields (MEMBER_NO, AGE, GENDER)
     - Identify duplicate MEMBER_NO records
     - Display sample records with quality issues
   - **Transaction Data Quality Checks:**
     - Count null values in customer_id, amount, payment_method
     - Identify duplicate transaction_id records
     - Check for inconsistent status values (completed vs COMPLETED)
     - Find invalid email formats and date inconsistencies

4. **Cleanse and Standardize Flight Loyalty Data:**
   - Replace "." placeholder values with null for better handling
   - Handle empty strings as null in WORK_CITY and WORK_PROVINCE
   - Replace null/empty city and province with "Unknown"
   - Standardize city and province names using trim() and proper casing
   - Cast AGE column to proper IntegerType
   - Remove duplicate records based on MEMBER_NO (keep first occurrence)
   - Filter out records where MEMBER_NO is null
   - Display count of cleaned records and records removed

5. **Cleanse and Standardize Transaction Data:**
   - Filter out records with null customer_id
   - Standardize status values to lowercase (completed, pending)
   - Standardize region names to uppercase with trim
   - Standardize payment_method values:
     - Map variations to standard values (credit_card, debit_card, paypal, wire_transfer)
     - Convert to lowercase
   - Clean email addresses to lowercase, handle invalid formats
   - Handle invalid amounts (set to 0.0 or filter)
   - Standardize date formats using coalesce with multiple date patterns
   - Remove duplicate transactions based on transaction_id
   - Handle missing customer names (replace with "Unknown")

6. **Write Cleansed Data to Silver Layer:**
   - Write cleaned flight data to **silver_flights** Delta table using `saveAsTable()`
   - Write cleaned transaction data to **silver_transactions** Delta table
   - Use Delta format for ACID transactions and time travel capabilities
   - Overwrite mode for initial load
   - Display success message with record counts

7. **Validate Silver Layer Data Quality:**
   - Read Delta tables from Silver layer
   - Verify record counts match expected cleaned datasets
   - Check for null values in critical fields after cleaning
   - Validate data standardization:
     - Status values are lowercase
     - Region values are uppercase
     - Payment methods are standardized
   - Run SQL queries to analyze cleansed data:
     - Transaction counts by region and status
     - Revenue summaries by standardized categories
   - Verify Delta tables are visible in Lakehouse Tables section

8. **Save Transformation Notebook:**
   - Save notebook as: **Bronze-to-Silver-Transformation**
   - Verify notebook is saved in workspace

#### Validation Check
- Fabric Notebook created and attached to Lakehouse successfully
- Bronze layer data (CSV and JSON) loaded using PySpark
- Data quality issues identified and documented (nulls, duplicates, inconsistent formatting)
- Flight loyalty data cleansed with standardized city/province names
- Transaction data cleansed with standardized status, region, payment methods
- Missing values handled appropriately (Unknown, null filtering)
- Duplicates removed from both datasets
- Data types standardized (AGE as integer, amount as double)
- Silver layer Delta tables created: **silver_flights**, **silver_transactions**
- Delta tables visible in Lakehouse with correct record counts
- SQL queries return clean, standardized data from Silver layer
- Notebook saved with proper naming convention

### **Challenge 4: Build Gold Layer - Dimensional Modeling for Analytics**
**Estimated Duration:** 60 Minutes

#### Objective
Create star schema dimensional models from Silver layer data to build analytics-ready Gold layer with dimension tables, fact tables, and business KPI aggregations.

#### Tasks
1. **Create Gold Layer Modeling Notebook:**
   - Create new Notebook in Fabric workspace
   - Attach to **contoso_lakehouse_<inject key="DeploymentID"></inject>**
   - Load Silver layer tables: **silver_flights**, **silver_transactions**
   - Verify record counts and preview data schemas

2. **Understand Dimensional Modeling Concepts:**
   - **Star Schema Design:** Central fact tables surrounded by dimension tables
   - **Dimension Tables:** Descriptive attributes (customers, geography, time)
   - **Fact Tables:** Measurable metrics and foreign keys to dimensions
   - **Benefits:** Optimized for analytics queries, simplified BI reporting

3. **Create Dimension Tables:**
   - **dim_customers (Customer Dimension):**
     - Extract from silver_flights
     - Fields: customer_key (MEMBER_NO), gender, age, loyalty_tier, loyalty_join_date, first_flight_date, city, province, country
     - Add load_timestamp for audit trail
   - **dim_geography (Geography Dimension):**
     - Extract distinct geographies from silver_flights
     - Fields: geo_key (auto-generated), country, province, city
     - Use `monotonically_increasing_id()` for surrogate key
   - **dim_time (Time Dimension):**
     - Extract unique dates from transaction purchase_date
     - Fields: date, year, month, day, quarter, day_of_week
     - Use date functions: `year()`, `month()`, `quarter()`, `dayofweek()`

4. **Create Fact Tables:**
   - **fact_flights (Flight Activity Fact):**
     - One row per customer with aggregated flight metrics
     - Fields: customer_key, total_flights, base_points, year_1_flights, year_2_flights, total_km_flown, avg_flight_interval_days, max_flight_interval_days, days_since_last_flight, exchange_count, avg_discount_rate, total_loyalty_points, non_flight_points, last_flight_date
     - Add load_timestamp
   - **fact_transactions (Transaction Fact):**
     - Granular transaction-level facts
     - Fields: transaction_id, customer_key, transaction_date, transaction_amount, status, region, payment_method
     - Cast customer_id to integer to match dim_customers key type

5. **Calculate Business Metrics and KPIs:**
   - Flight Activity Metrics:
     - Total members count
     - Total flights across all members
     - Average km per member
     - Total loyalty points awarded
   - Transaction Metrics:
     - Completed transactions count
     - Total revenue from completed transactions
     - Average transaction value
   - Display metrics using Spark aggregation functions

6. **Write Gold Layer Tables to OneLake:**
   - Write dimension tables to Delta format:
     - **dim_customers**
     - **dim_geography**
     - **dim_time**
   - Write fact tables to Delta format:
     - **fact_flights**
     - **fact_transactions**
   - Use `overwriteSchema` option for initial load
   - Verify Delta tables created successfully with record counts

7. **Run Analytics Queries on Gold Layer:**
   - **Customer Loyalty Segmentation:** Analyze customers by loyalty tier with avg flights, km, and points
   - **Geographic Flight Activity:** Top 10 provinces by flight activity, member count, and total points
   - **Transaction Revenue by Region:** Revenue and transaction counts by region and status
   - **Payment Method Analysis:** Usage and revenue by payment method for completed transactions
   - **Customer Age Demographics:** Segment customers by age groups with flight and point averages

8. **Create Business KPI Aggregation Table:**
   - Build **kpi_customer_value** table combining flight and transaction data:
     - Join fact_flights with dim_customers
     - Left join with transaction aggregations (total_spent, transaction_count)
     - Calculate customer_status based on days_since_last_flight:
       - Active (≤90 days)
       - At Risk (91-180 days)
       - Inactive (>180 days)
   - Write to Delta table for Power BI consumption

9. **Verify Gold Layer in OneLake:**
   - Navigate to Lakehouse in Fabric portal
   - Verify Tables section contains all Gold layer tables
   - Check Delta format and record counts
   - Validate tables are queryable via SQL analytics endpoint

10. **Save Gold Layer Notebook:**
    - Save notebook as: **04_Gold_Layer_Dimensional_Modeling**

#### Validation Check
- Gold layer notebook created and attached to Lakehouse
- Silver layer tables successfully loaded (silver_flights, silver_transactions)
- Three dimension tables created with proper schemas:
  - **dim_customers** (customer attributes)
  - **dim_geography** (geographic hierarchy)
  - **dim_time** (date dimensions with year, month, quarter)
- Two fact tables created with metrics:
  - **fact_flights** (customer flight activity aggregations)
  - **fact_transactions** (granular transaction facts)
- Business KPI table created: **kpi_customer_value** (customer lifetime value with engagement status)
- All tables written to Gold layer as Delta Lake format
- Analytics queries return meaningful business insights:
  - Loyalty tier segmentation
  - Geographic performance rankings
  - Revenue analysis by region and payment method
  - Age demographic patterns
- Tables visible in Lakehouse with correct record counts
- Star schema design properly implemented for BI optimization

### **Challenge 5: Build ML Models with Fabric Data Science**
**Estimated Duration:** 60 Minutes

#### Objective
Use Microsoft Fabric's integrated Data Science workload to perform ML-based customer segmentation using K-Means clustering, track experiments with MLflow, and write enriched results back to the Lakehouse.

#### Tasks
1. **Create Data Science Notebook:**
   - In Fabric workspace, create new Notebook
   - Attach to Lakehouse: **contoso_lakehouse_<inject key="DeploymentID"></inject>**
   - Understand Fabric Data Science capabilities:
     - Native Python ML libraries (scikit-learn, pandas, numpy)
     - MLflow integration for experiment tracking
     - Direct read/write to OneLake Delta tables
     - Visualization support (matplotlib, seaborn)

2. **Load Gold Layer Data for ML:**
   - Load Delta tables using Spark:
     - **kpi_customer_value** (primary dataset for segmentation)
     - **dim_customers** (customer attributes)
     - **fact_flights** (flight behaviors)
     - **fact_transactions** (transaction patterns)
   - Display record counts and preview schemas

3. **Prepare Features for Customer Segmentation:**
   - Create ML feature dataset from kpi_customer_value:
     - Select features: age, total_flights, total_km_flown, total_loyalty_points, days_since_last_flight, total_spent, transaction_count
     - Handle nulls using `coalesce()` with 0 defaults
     - Drop records with remaining nulls using `na.drop()`
   - Create RFM-like behavioral scores:
     - **Recency Score:** Based on days_since_last_flight (1-5 scale)
     - **Frequency Score:** Based on total_flights (1-5 scale)
     - **Monetary Score:** Based on total_loyalty_points (1-5 scale)
   - Display prepared ML dataset with feature statistics

4. **Prepare Data for scikit-learn:**
   - Convert Spark DataFrame to Pandas for scikit-learn compatibility
   - Define feature columns for clustering model
   - Create feature matrix X with selected columns
   - Fill any remaining nulls with 0
   - Display feature matrix shape and descriptive statistics

5. **Build K-Means Clustering Model:**
   - Import required libraries: StandardScaler, KMeans, silhouette_score, MLflow
   - Scale features using StandardScaler for better clustering:
     - Fit scaler on feature matrix
     - Transform features to standardized values
   - Set up MLflow experiment: **Customer_Segmentation_Experiment**
   - Start MLflow run with run_name: **KMeans_5_Clusters**
   - Train K-Means model:
     - n_clusters=5 (five customer segments)
     - random_state=42 for reproducibility
     - n_init=10, max_iter=300
   - Predict cluster labels for all customers
   - Calculate silhouette score for clustering quality (target >0.3)

6. **Track Experiment with MLflow:**
   - Log parameters to MLflow:
     - n_clusters, algorithm, random_state
   - Log metrics to MLflow:
     - silhouette_score (clustering quality metric)
     - inertia (within-cluster sum of squares)
   - Log trained models to MLflow:
     - KMeans model
     - StandardScaler model
   - Display training results and quality metrics

7. **Analyze Customer Segment Characteristics:**
   - Add cluster labels to Pandas DataFrame
   - Calculate segment profiles using groupby aggregations:
     - Customer count per segment
     - Average age, flights, km, loyalty points
     - Average spending, days since flight
     - Average RFM scores
   - Create segment visualizations using matplotlib/seaborn:
     - Bar charts: Customers per segment, avg flights, avg points, avg spending
     - Line plot: RFM scores by segment
     - Multi-panel dashboard showing segment characteristics
   - Log visualizations to MLflow

8. **Assign Business-Friendly Segment Names:**
   - Analyze segment profiles and assign meaningful names:
     - **Premium Elite Members:** High RFM scores, frequent flyers, high spending
     - **Loyal Frequent Flyers:** Good flight frequency, moderate spending
     - **At-Risk Customers:** Low recency, declining engagement
     - **New Joiners:** Recent sign-up, low flight history
     - **Occasional Travelers:** Low frequency, sporadic engagement
   - Add segment_name field to customer data
   - Display segment distribution with business labels

9. **Write ML-Enriched Data Back to Lakehouse:**
   - Convert enriched Pandas DataFrame back to Spark DataFrame
   - Join with original kpi_customer_value to preserve all fields
   - Add segment and segment_name columns
   - Write to Gold layer as new Delta table:
     - **gold_customer_segments_ml** (customer-level data with ML segments)
   - Create segment summary table from aggregated profiles:
     - **gold_segment_summary** (segment-level statistics)
   - Verify tables written successfully with record counts

10. **Validate ML Results in Lakehouse:**
    - Read back ML-enriched tables from Delta
    - Verify gold_customer_segments_ml contains all customers with segment assignments
    - Check gold_segment_summary contains 5 segment profiles
    - Display segment distribution and sample enriched records
    - Validate data quality and segment assignments

11. **View ML Experiments in Fabric Data Science:**
    - Navigate to Fabric workspace
    - Select **Data Science** from left navigation
    - Find experiment: **Customer_Segmentation_Experiment**
    - Review run history with parameters and metrics
    - View logged models and artifacts
    - Check registered models in Models section

12. **Save ML Notebook:**
    - Save notebook as: **ML_Customer_Segmentation**

#### Validation Check
- Data Science notebook created and attached to Lakehouse
- Gold layer tables loaded successfully (kpi_customer_value, dim_customers, fact_flights, fact_transactions)
- ML features prepared with RFM scoring calculation
- Feature matrix created and scaled using StandardScaler
- K-Means clustering model trained with 5 customer segments
- MLflow experiment tracked with parameters, metrics, and models
- Silhouette score >0.3 indicating reasonable clustering quality
- Segment characteristics analyzed and visualized
- Business-friendly segment names assigned based on behavioral profiles:
  - Premium Elite Members
  - Loyal Frequent Flyers
  - At-Risk Customers
  - New Joiners
  - Occasional Travelers
- ML-enriched data written to Gold layer:
  - **gold_customer_segments_ml** table with segment assignments
  - **gold_segment_summary** table with segment statistics
- Delta tables visible in Lakehouse with correct record counts
- MLflow experiment visible in Fabric Data Science workspace
- Models and artifacts logged successfully

### **Challenge 6: Build Power BI Dashboard**
**Estimated Duration:** 75 Minutes

#### Objective
Create comprehensive, interactive Power BI dashboards that connect directly to Fabric Lakehouse Gold layer, surfacing business insights, ML customer segments, and enabling self-service analytics.

#### Tasks
1. **Connect Power BI to Fabric Lakehouse:**
   - Navigate to Microsoft Fabric portal
   - Open workspace: **fabric-workspace-<inject key="DeploymentID"></inject>**
   - Open Lakehouse: **contoso_lakehouse_<inject key="DeploymentID"></inject>**
   - Switch to **SQL analytics endpoint** view (top-right corner)
   - Create new **semantic model** (formerly Dataset):
     - Name: **Contoso-Flight-Analytics-Model**
   - Select Gold layer tables for model:
     - fact_flights
     - fact_transactions
     - dim_customers
     - dim_geography
     - dim_time
     - kpi_customer_value
     - gold_customer_segments_ml (if Challenge 5 completed)
     - gold_segment_summary (if Challenge 5 completed)
   - Confirm to create semantic model

2. **Configure Data Model Relationships:**
   - Open semantic model in **Model view**
   - Create relationships by dragging between tables:
     - **fact_flights[customer_key]** → **dim_customers[customer_key]** (Many-to-One)
     - **fact_transactions[customer_key]** → **dim_customers[customer_key]** (Many-to-One)
     - **fact_transactions[transaction_date]** → **dim_time[date]** (Many-to-One)
     - **kpi_customer_value[customer_key]** → **dim_customers[customer_key]** (Many-to-One)
     - **gold_customer_segments_ml[customer_key]** → **dim_customers[customer_key]** (One-to-One, if table exists)
   - Verify all relationships are **active** with **Single** cross-filter direction
   - Validate relationship cardinality is correct

3. **Create DAX Calculated Measures:**
   - **Transaction Measures (fact_transactions table):**
     - `Total Revenue = SUM(fact_transactions[transaction_amount])`
     - `Total Transactions = COUNTROWS(fact_transactions)`
     - `Average Transaction Value = DIVIDE([Total Revenue], [Total Transactions], 0)`
     - `Completed Revenue = CALCULATE([Total Revenue], fact_transactions[status] = "completed")`
   - **Flight Activity Measures (fact_flights table):**
     - `Total Flights = SUM(fact_flights[total_flights])`
     - `Total Loyalty Points = SUM(fact_flights[total_loyalty_points])`
     - `Total Distance KM = SUM(fact_flights[total_km_flown])`
     - `Average Flights Per Member = AVERAGE(fact_flights[total_flights])`
   - **ML Segment Measures (gold_customer_segments_ml table, if exists):**
     - `Total Customers in Segments = COUNTROWS(gold_customer_segments_ml)`
     - `Average RFM Score = AVERAGE(gold_customer_segments_ml[recency_score]) + AVERAGE(gold_customer_segments_ml[frequency_score]) + AVERAGE(gold_customer_segments_ml[monetary_score])`
     - `High Value Customers = CALCULATE(COUNTROWS(gold_customer_segments_ml), gold_customer_segments_ml[segment_name] IN {"Loyal Frequent Flyers", "Premium Elite Members"})`
   - Save semantic model

4. **Create Power BI Report - Page 1: Business Overview:**
   - From semantic model, click **Create report**
   - Power BI report canvas opens with data model connected
   - **Add KPI Cards:**
     - Card visual: **Total Revenue** (format as Currency)
     - Card visual: **Total Flights**
     - Card visual: **Total Loyalty Points**
     - Card visual: **Total Transactions**
   - **Add Line Chart - Transaction Trend:**
     - Axis: **dim_time[year]**, **dim_time[month]**
     - Values: **Total Revenue**
     - Title: "Monthly Transaction Trend"
   - **Add Clustered Column Chart - Revenue by Region:**
     - Axis: **fact_transactions[region]**
     - Values: **Total Revenue**, **Total Transactions**
     - Title: "Revenue & Transactions by Region"
   - **Add Pie Chart - Payment Methods:**
     - Legend: **fact_transactions[payment_method]**
     - Values: **Total Transactions**
     - Title: "Payment Method Distribution"
   - **Add Table Visual - Top 10 Customers:**
     - Columns: **dim_customers[customer_key]**, **kpi_customer_value[total_spent]**, **kpi_customer_value[total_flights]**, **kpi_customer_value[customer_status]**
     - Visual-level filter: Top 10 by total_spent
     - Title: "Top 10 Customers by Spending"

5. **Create Page 2: Geographic & Loyalty Analysis:**
   - Add new page: Click **+ Add page** at bottom
   - **Add Map Visual - Customer Distribution:**
     - Location: **dim_customers[province]**, **dim_customers[country]**
     - Bubble size: **Total Flights**
     - Title: "Customer Distribution by Province"
   - **Add Matrix Visual - Geographic Breakdown:**
     - Rows: **dim_customers[province]**, **dim_customers[country]**
     - Columns: **dim_customers[loyalty_tier]**
     - Values: Count of **customer_key**, **Total Flights**, **Total Loyalty Points**
     - Title: "Geographic Loyalty Analysis"
   - **Add Stacked Bar Chart - Loyalty Tier Activity:**
     - Axis: **dim_customers[loyalty_tier]**
     - Values: **Total Flights**, **Total Distance KM**
     - Title: "Flight Activity by Loyalty Tier"
   - **Add Donut Chart - Transaction Status:**
     - Legend: **fact_transactions[status]**
     - Values: **Total Transactions**
     - Title: "Transaction Status Distribution"

6. **Create Page 3: ML Customer Segmentation Insights (if Challenge 5 completed):**
   - Add new page for ML-powered segmentation analysis
   - **Add KPI Cards for ML Metrics:**
     - Card: **Total Customers in Segments**
     - Card: **High Value Customers**
     - Card: **Average RFM Score**
   - **Add Donut Chart - Segment Distribution:**
     - Legend: **gold_customer_segments_ml[segment_name]**
     - Values: Count of **customer_key**
     - Title: "ML-Based Customer Segmentation"
     - Enable data labels with percentages
   - **Add Clustered Column Chart - Segment Performance:**
     - Axis: **gold_customer_segments_ml[segment_name]**
     - Values: **Total Flights**, **Total Loyalty Points**, **Total Revenue**
     - Title: "Revenue & Engagement by Customer Segment"
     - Show legend for all three metrics
   - **Add Matrix Visual - Segment Profile:**
     - Rows: **gold_customer_segments_ml[segment_name]**
     - Columns: **dim_customers[loyalty_tier]**
     - Values: Count of **customer_key**, **Total Revenue**, **Average Transaction Value**
     - Title: "Segment × Loyalty Tier Analysis"
   - **Add Scatter Chart - RFM Behavioral Mapping:**
     - X-axis: **gold_customer_segments_ml[recency_score]**
     - Y-axis: **gold_customer_segments_ml[monetary_score]**
     - Legend: **gold_customer_segments_ml[segment_name]**
     - Size: **Total Flights**
     - Title: "Customer Behavioral Patterns (RFM Analysis)"
   - **Add Table Visual - Segment Statistics:**
     - Use **gold_segment_summary** table
     - Columns: segment_name, customer_count, avg_age, avg_total_flights, avg_loyalty_points
     - Sort by avg_loyalty_points descending
     - Title: "Customer Segment Profiles"
   - **Add Stacked Bar Chart - Segment Value:**
     - Axis: **gold_customer_segments_ml[segment_name]**
     - Values: **Total Revenue**
     - Title: "Revenue Contribution by Segment"

7. **Add Interactive Slicers and Filters:**
   - Return to Page 1: Business Overview
   - **Add Slicer - Year Filter:**
     - Field: **dim_time[year]**
     - Style: Dropdown
     - Position: Top-left corner
   - **Add Slicer - Region Filter:**
     - Field: **fact_transactions[region]**
     - Style: List
     - Position: Left side panel
   - **Add Slicer - Loyalty Tier:**
     - Field: **dim_customers[loyalty_tier]**
     - Style: Dropdown
   - **Add Slicer - Customer Status:**
     - Field: **kpi_customer_value[customer_status]**
     - Style: Dropdown
   - **Sync Slicers Across Pages:**
     - Select slicer → **View** tab → **Sync slicers**
     - Enable sync for all relevant pages

8. **Format and Polish Dashboard:**
   - Apply consistent theme:
     - Go to **View** → **Themes**
     - Select professional theme (e.g., "Executive")
   - Add report title and description:
     - Insert Text box at top
     - Title: "Contoso Flight Loyalty & Customer Analytics Dashboard"
     - Subtitle: "Real-time insights from unified data platform"
   - Add last refresh timestamp
   - Configure visual interactions:
     - Use **Format** → **Edit interactions** to control cross-filtering
   - Add navigation buttons between pages using **Buttons** → **Navigator**

9. **Publish Dashboard to Power BI Service:**
   - Save report: **Contoso-Flight-Loyalty-Dashboard**
   - Click **Publish** in Home ribbon
   - Select destination: **fabric-workspace-<inject key="DeploymentID"></inject>**
   - Wait for publishing to complete
   - Click link to open dashboard in Power BI Service

10. **Configure Scheduled Refresh (Optional):**
    - In Power BI Service, navigate to semantic model (not report)
    - Go to **Settings** → **Scheduled refresh**
    - Configure refresh schedule:
      - Frequency: Daily
      - Time: 6:00 AM
      - Time zone: Local timezone
    - Click Apply
    - Note: Direct connectivity to Fabric OneLake automatically picks up updates

11. **Test and Validate Dashboard:**
    - Open published dashboard in Power BI Service
    - Test interactivity:
      - Click provinces on map → verify other visuals filter accordingly
      - Use slicers to filter by Year, Region, Loyalty Tier, Customer Status
      - Drill through from summary to detailed tables
    - Validate data accuracy:
      - Compare Total Revenue with SQL query results
      - Verify flight metrics match fact_flights table
      - Confirm ML segment distributions (if Challenge 5 completed)
    - Share dashboard:
      - Click **Share** button
      - Enter stakeholder email addresses
      - Grant view-only permissions

#### Validation Check
- Semantic model created from Fabric Lakehouse Gold layer tables successfully
- Tables included in model:
  - fact_flights, fact_transactions, dim_customers, dim_geography, dim_time, kpi_customer_value
  - gold_customer_segments_ml, gold_segment_summary (if Challenge 5 completed)
- Data model relationships configured correctly:
  - Many-to-One relationships between facts and dimensions
  - One-to-One relationship for ML segment table
- DAX calculated measures created for:
  - Revenue and transaction metrics
  - Flight activity metrics
  - ML segment analysis (if applicable)
- Multi-page interactive dashboard created:
  - **Page 1:** Business Overview (KPIs, trends, regional analysis, top customers)
  - **Page 2:** Geographic & Loyalty Analysis (maps, matrices, tier analysis)
  - **Page 3:** ML Customer Segmentation (behavioral insights, RFM analysis, segment profiles)
- Slicers and filters implemented (Year, Region, Loyalty Tier, Customer Status)
- Slicers synced across relevant pages
- Dashboard formatted with consistent theme and professional layout
- Dashboard published to Power BI Service successfully
- Data accuracy validated between Power BI and Lakehouse source tables
- ML segment visualizations display 5 customer personas (if Challenge 5 completed)
- Interactive features working correctly (cross-filtering, drill-through)

## Success Criteria
**You will have successfully completed this challenge when you deliver:**

A **complete unified data lakehouse platform with Medallion architecture that ingests raw data, transforms through quality layers, creates analytics-ready dimensional models, enriches with ML customer segments, and surfaces insights through interactive Power BI dashboards**.

### **Technical Deliverables:**
- **Infrastructure:** Microsoft Fabric capacity (F2 SKU) deployed from Azure with workspace and OneLake Lakehouse configured
- **Medallion Architecture:** Bronze/Silver/Gold layers implemented with proper data quality governance
- **Bronze Layer:** Raw flight and transaction data ingested from CSV and JSON sources
- **Silver Layer:** PySpark transformations cleansing data (nulls handled, duplicates removed, values standardized)
- **Gold Layer:** Star schema dimensional models with:
  - 3 Dimension tables (dim_customers, dim_geography, dim_time)
  - 2 Fact tables (fact_flights, fact_transactions)
  - 1 KPI aggregation table (kpi_customer_value)
- **Data Science:** ML customer segmentation model trained with K-Means clustering
  - MLflow experiment tracking with parameters and metrics
  - 5 customer segments with business-friendly names
  - ML-enriched tables in Gold layer (gold_customer_segments_ml, gold_segment_summary)
- **Business Intelligence:** Power BI dashboards with:
  - Semantic model connected to Fabric OneLake
  - Multi-page interactive dashboards (Business Overview, Geographic Analysis, ML Segmentation)
  - DAX measures for analytics
  - Slicers and cross-filtering
  - Published to Power BI Service

### **Business Outcomes:**
- **Unified Data Platform:** Single source of truth with OneLake eliminating data silos
- **Data Quality Governance:** Medallion architecture ensures progressive data refinement
- **Self-Service Analytics:** Business users empowered with governed, high-quality data
- **ML-Powered Insights:** Customer segmentation enables targeted marketing and retention strategies
- **Real-Time Visibility:** Direct Power BI connectivity to OneLake eliminates ETL latency
- **Scalable Foundation:** Cloud-native Fabric platform ready for enterprise-scale analytics workloads

### **Real-World Applications:**
This solution demonstrates enterprise-grade capabilities applicable to:
- Airlines loyalty program analytics and customer retention
- Retail customer segmentation and personalization
- Financial services customer lifetime value optimization
- Healthcare patient journey analytics
- Manufacturing supply chain intelligence
- Telecommunications churn prediction and prevention

## Additional Resources
- [Microsoft Fabric Documentation](https://learn.microsoft.com/fabric/)
- [OneLake Overview](https://learn.microsoft.com/fabric/onelake/onelake-overview)
- [Medallion Architecture in Fabric](https://learn.microsoft.com/fabric/onelake/onelake-medallion-lakehouse-architecture)
- [Create a Lakehouse in Microsoft Fabric](https://learn.microsoft.com/fabric/data-engineering/create-lakehouse)
- [Notebooks in Microsoft Fabric](https://learn.microsoft.com/fabric/data-engineering/how-to-use-notebook)
- [PySpark DataFrame API](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html)
- [Delta Lake in Fabric](https://learn.microsoft.com/fabric/data-engineering/lakehouse-and-delta-tables)
- [Data Science in Microsoft Fabric](https://learn.microsoft.com/fabric/data-science/data-science-overview)
- [MLflow in Fabric](https://learn.microsoft.com/fabric/data-science/mlflow-autologging)
- [Power BI and Microsoft Fabric Integration](https://learn.microsoft.com/fabric/get-started/power-bi-fabric-integration)
- [DAX Functions Reference](https://learn.microsoft.com/dax/dax-function-reference)
- [Azure Fabric Capacity Planning](https://learn.microsoft.com/fabric/enterprise/licenses)
