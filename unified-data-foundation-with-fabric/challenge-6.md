# Challenge 06: Build a Power BI Dashboard

## Introduction

Contoso's business stakeholders need intuitive, interactive dashboards to visualize sales trends, track regional performance, monitor operational KPIs, and analyze customer segments. Power BI, natively integrated with Microsoft Fabric, provides seamless connectivity to Gold layer tables without requiring data movement or duplication. In this final challenge, you will create a comprehensive Power BI dashboard that connects directly to your Fabric Lakehouse Gold layer, enabling business users to explore governed, high-quality data through beautiful visualizations.

## Challenge Objectives

- Connect Power BI to the Fabric Lakehouse Gold layer.
- Create a semantic model (dataset) from Gold layer tables.
- Build visualizations: sales trends, regional comparisons, KPIs, customer segments.
- Design an interactive dashboard with slicers and filters.
- Publish the dashboard to Power BI Service for organization-wide access.

## Steps to Complete

### Part 1: Connect Power BI to Fabric Lakehouse

1. In the **Edge browser**, navigate to the **Microsoft Fabric** portal (if not already open):

   ```
   https://app.fabric.microsoft.com/
   ```

1. Navigate to your workspace: **fabric-workspace-<inject key="DeploymentID"></inject>**

1. Open your Lakehouse: **contoso-lakehouse-<inject key="DeploymentID"></inject>**

1. From the Lakehouse, click on **SQL analytics endpoint** in the top-right corner.

   > **Note:** This provides a T-SQL interface to your Delta Lake tables for Power BI connectivity.

1. Click **New semantic model** (formerly known as Dataset):

   - Name: **Contoso-Flight-Analytics-Model**
   - Select the following Gold layer tables:
     - fact_flights
     - fact_transactions
     - dim_customers
     - dim_geography
     - dim_time
     - kpi_customer_value
     - gold_customer_segments_ml (from Databricks integration)

1. Click **Confirm** to create the semantic model.

### Part 2: Configure Relationships in Semantic Model

1. Once the semantic model opens, you'll see the **Model view**.

1. Create relationships between tables by dragging between fields:

   - **fact_flights[customer_key]** → **dim_customers[customer_key]**  
     Cardinality: Many-to-One (*)
   
   - **fact_transactions[customer_key]** → **dim_customers[customer_key]**  
     Cardinality: Many-to-One (*)
   
   - **fact_transactions[transaction_date]** → **dim_time[date]**  
     Cardinality: Many-to-One (*)
   
   - **kpi_customer_value[customer_key]** → **dim_customers[customer_key]**  
     Cardinality: Many-to-One (*)

1. Verify that all relationships are **active** and have the correct **cross-filter direction**:

   - Set cross-filter direction to **Single** for all relationships (default)

1. Add calculated measures to the **fact_transactions** table:

   - Right-click **fact_transactions** → **New measure**
   
   ```DAX
   Total Revenue = SUM(fact_transactions[transaction_amount])
   ```
   
   ```DAX
   Total Transactions = COUNTROWS(fact_transactions)
   ```
   
   ```DAX
   Average Transaction Value = DIVIDE([Total Revenue], [Total Transactions], 0)
   ```
   
   ```DAX
   Completed Revenue = CALCULATE([Total Revenue], fact_transactions[status] = "completed")
   ```

1. Add calculated measures to the **fact_flights** table:

   - Right-click **fact_flights** → **New measure**
   
   ```DAX
   Total Flights = SUM(fact_flights[total_flights])
   ```
   
   ```DAX
   Total Loyalty Points = SUM(fact_flights[total_loyalty_points])
   ```
   
   ```DAX
   Total Distance KM = SUM(fact_flights[total_km_flown])
   ```
   
   ```DAX
   Average Flights Per Member = AVERAGE(fact_flights[total_flights])
   ```

1. **Save** the semantic model.

### Part 3: Create Power BI Report

1. From the semantic model, click **Create report** in the top ribbon.

1. The Power BI report canvas will open with your data model connected.

#### Page 1: Business Overview Dashboard

1. Add a **Card visual** for Total Revenue:

   - Drag **Total Revenue** measure to the canvas
   - Format: Currency, no decimals
   - Title: "Total Transaction Revenue"

1. Add three more **Card visuals** for KPIs:

   - **Total Flights**
   - **Total Loyalty Points**
   - **Total Transactions**

1. Add a **Line chart** for Transaction Trend over Time:

   - Axis: **dim_time[year]** and **dim_time[month]**
   - Values: **Total Revenue**
   - Title: "Monthly Transaction Trend"

1. Add a **Clustered column chart** for Revenue by Region:

   - Axis: **fact_transactions[region]**
   - Values: **Total Revenue**, **Total Transactions**
   - Title: "Revenue & Transactions by Region"

1. Add a **Pie chart** for Transactions by Payment Method:

   - Legend: **fact_transactions[payment_method]**
   - Values: **Total Transactions**
   - Title: "Payment Method Distribution"

1. Add a **Table visual** for Top 10 Customers:

   - Columns: **dim_customers[customer_key]**, **kpi_customer_value[total_spent]**, **kpi_customer_value[total_flights]**, **kpi_customer_value[customer_status]**
   - Add visual-level filter: Top 10 by **total_spent**
   - Title: "Top 10 Customers by Spending"

#### Page 2: Geographic & Loyalty Analysis

1. Add a new page: Click **+ Add page** at the bottom

1. Add a **Map visual** for Customer Distribution:

   - Location: **dim_customers[province]**, **dim_customers[country]**
   - Bubble size: **Total Flights**
   - Title: "Customer Distribution by Province"

1. Add a **Matrix visual** for geographic breakdown:

   - Rows: **dim_customers[province]**, **dim_customers[country]**
   - Columns: **dim_customers[loyalty_tier]**
   - Values: Count of **customer_key**, **Total Flights**, **Total Loyalty Points**
   - Title: "Geographic Loyalty Analysis"

1. Add a **Stacked bar chart** for Flight Activity by Loyalty Tier:

   - Axis: **dim_customers[loyalty_tier]**
   - Values: **Total Flights**, **Total Distance KM**
   - Title: "Flight Activity by Loyalty Tier"

1. Add a **Donut chart** for Transaction Status:

   - Legend: **fact_transactions[status]**
   - Values: **Total Transactions**
   - Title: "Transaction Status Distribution"

#### Page 3: Customer Segmentation Insights

1. Add a new page for customer ML segmentation analysis

1. Add a **Donut chart** for Customer Segments (if gold_customer_segments_ml exists):

   - Legend: **gold_customer_segments_ml[segment_name]**
   - Values: Count of **customer_key**
   - Title: "ML-Based Customer Segmentation"

1. Add a **Table visual** for Customer Value Analysis:

   - Columns: **kpi_customer_value[customer_key]**, **kpi_customer_value[total_flights]**, **kpi_customer_value[total_loyalty_points]**, **kpi_customer_value[total_spent]**, **kpi_customer_value[customer_status]**
   - Sort by: **total_spent** descending
   - Visual filter: Top 20
   - Title: "Top 20 Customers by Lifetime Value"

1. Add a **Clustered bar chart** for Customer Status Distribution:

   - Axis: **kpi_customer_value[customer_status]**
   - Values: Count of **customer_key**, **Total Revenue**, **Total Loyalty Points**
   - Title: "Customer Engagement Status"

### Part 4: Add Interactivity with Slicers

1. Go back to **Page 1: Sales Overview**

1. Add a **Slicer** for Year filter:

   - Field: **dim_time[year]**
   - Style: Dropdown
   - Position: Top-left corner

1. Add a **Slicer** for Region filter:

   - Field: **fact_transactions[region]**
   - Style: List
   - Position: Left side panel

1. Add a **Slicer** for Loyalty Tier:

   - Field: **dim_customers[loyalty_tier]**
   - Style: Dropdown

1. Add a **Slicer** for Customer Status:

   - Field: **kpi_customer_value[customer_status]**
   - Style: Dropdown

1. **Sync slicers** across all pages:

   - Select a slicer → **View** tab → **Sync slicers**
   - Enable sync for all relevant pages

### Part 5: Format and Polish the Dashboard

1. Apply consistent theme:

   - Go to **View** → **Themes**
   - Select a professional theme (e.g., "Executive")

1. Add report title and description:

   - Insert **Text box** at the top
   - Title: "Contoso Flight Loyalty & Customer Analytics Dashboard"
   - Subtitle: "Real-time insights from unified data platform"

1. Add last refresh timestamp:

   - Insert **Text box**
   - Add: "Data refreshed: [Current Date]"

1. Configure visual interactions:

   - Select visuals and use **Format** → **Edit interactions** to control how visuals filter each other

1. Add navigation buttons between pages:

   - Insert **Buttons** → **Navigator**
   - Configure to jump between dashboard pages

### Part 6: Publish Dashboard to Power BI Service

1. Click **File** → **Save**

   - Report name: **Contoso-Flight-Loyalty-Dashboard**

1. Click **Publish** in the Home ribbon

1. Select destination workspace: **fabric-workspace-<inject key="DeploymentID"></inject>**

   > **Note:** Your workspace is using the Fabric trial capacity, which supports all publishing features.

1. Click **Select**

1. Once published, click **Open 'Contoso-Flight-Loyalty-Dashboard' in Power BI** to view in the service

### Part 7: Configure Automatic Refresh (Optional)

1. In **Power BI Service**, navigate to the **semantic model** (not the report)

1. Go to **Settings** → **Scheduled refresh**

1. Configure refresh schedule:

   - Frequency: **Daily**
   - Time: **6:00 AM**
   - Time zone: **Your local timezone**

1. Click **Apply**

   > **Note:** Since the data is in Fabric OneLake, Power BI will automatically pick up any updates to the Gold layer tables.

### Part 8: Validate Dashboard Functionality

1. Open the published dashboard in **Power BI Service**

1. Test interactivity:

   - Click on different provinces in the map → other visuals should filter accordingly
   - Use slicers to filter by Year, Region, Loyalty Tier, Customer Status
   - Drill through from summary visuals to detailed tables

1. Verify data accuracy:

   - Compare Total Revenue in Power BI with SQL query results from Lakehouse
   - Verify Total Flights and Loyalty Points match fact_flights table
   - Confirm customer segments match data written from Databricks (if Challenge 5 was completed)

1. Share the dashboard:

   - Click **Share** button
   - Enter email addresses of stakeholders
   - Grant appropriate permissions (View only recommended)

## Success Criteria

- Semantic model created from Fabric Lakehouse Gold layer tables (fact_flights, fact_transactions, dim_customers, dim_geography, dim_time, kpi_customer_value).
- Relationships configured correctly between fact and dimension tables.
- Calculated measures created using DAX (Total Revenue, Total Flights, Total Loyalty Points, etc.).
- Multi-page interactive dashboard created with flight loyalty and transaction visualizations.
- Slicers and filters implemented for user interactivity (Year, Region, Loyalty Tier, Customer Status).
- Dashboard published to Power BI Service successfully.
- Data accuracy validated between Power BI and source Lakehouse tables.

## Additional Resources

- [Power BI and Microsoft Fabric Integration](https://learn.microsoft.com/fabric/get-started/power-bi-fabric-integration)
- [Create Reports in Power BI](https://learn.microsoft.com/power-bi/create-reports/)
- [DAX Functions Reference](https://learn.microsoft.com/dax/dax-function-reference)
- [Power BI Best Practices](https://learn.microsoft.com/power-bi/guidance/power-bi-optimization)
- [Semantic Models in Fabric](https://learn.microsoft.com/fabric/data-warehouse/semantic-models)

## Congratulations!

You have successfully built an **end-to-end unified analytics platform** using Microsoft Fabric, OneLake, Azure Databricks, and Power BI!

### Real-World Applications:

This solution enables enterprise-grade analytics across:

- **Unified Data Platform** - Single source of truth with OneLake, eliminating data silos
- **Medallion Architecture** - Structured data quality layers (Bronze → Silver → Gold)
- **Cross-Platform Analytics** - Seamless integration between Fabric and Databricks
- **Self-Service BI** - Business users empowered with governed, high-quality data
- **Scalable Architecture** - Cloud-native platform ready for enterprise-scale workloads
- **Real-Time Insights** - Direct connectivity eliminates ETL latency

### What You've Built:

**Bronze Layer**: Raw data ingestion from multiple sources  
**Silver Layer**: Cleansed, standardized, joined datasets  
**Gold Layer**: Business-ready dimensional models (Star Schema)  
**Databricks Integration**: Advanced analytics and ML workloads  
**Power BI Dashboards**: Interactive visualizations for business insights  

# Congratulations on completing this challenge!
