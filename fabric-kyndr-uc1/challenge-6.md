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

1. In your **Microsoft Fabric workspace**, navigate to:

   - Workspace: **fabric-workspace-<inject key="DeploymentID"></inject>**

1. Open your Lakehouse: **contoso-lakehouse-<inject key="DeploymentID"></inject>**

1. From the Lakehouse, click on **SQL analytics endpoint** in the top-right corner.

   > **Note:** This provides a T-SQL interface to your Delta Lake tables for Power BI connectivity.

1. Click **New semantic model** (formerly known as Dataset):

   - Name: **Contoso-Sales-Analytics-Model**
   - Select the following Gold layer tables:
     - ✅ gold_fact_sales
     - ✅ gold_dim_customer
     - ✅ gold_dim_product
     - ✅ gold_dim_date
     - ✅ gold_sales_summary
     - ✅ gold_customer_segments (from Databricks integration)

1. Click **Confirm** to create the semantic model.

### Part 2: Configure Relationships in Semantic Model

1. Once the semantic model opens, you'll see the **Model view**.

1. Create relationships between tables by dragging between fields:

   - **gold_fact_sales[CustomerKey]** → **gold_dim_customer[CustomerKey]**  
     Cardinality: Many-to-One (*)
   
   - **gold_fact_sales[ProductKey]** → **gold_dim_product[ProductKey]**  
     Cardinality: Many-to-One (*)
   
   - **gold_fact_sales[DateKey]** → **gold_dim_date[DateKey]**  
     Cardinality: Many-to-One (*)

1. Verify that all relationships are **active** and have the correct **cross-filter direction**:

   - Set cross-filter direction to **Single** for all relationships (default)

1. Add calculated measures to the **gold_fact_sales** table:

   - Right-click **gold_fact_sales** → **New measure**
   
   ```DAX
   Total Sales = SUM(gold_fact_sales[SalesAmount])
   ```
   
   ```DAX
   Total Profit = SUM(gold_fact_sales[Profit])
   ```
   
   ```DAX
   Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0) * 100
   ```
   
   ```DAX
   Total Orders = COUNTROWS(gold_fact_sales)
   ```
   
   ```DAX
   Average Order Value = DIVIDE([Total Sales], [Total Orders], 0)
   ```

1. **Save** the semantic model.

### Part 3: Create Power BI Report

1. From the semantic model, click **Create report** in the top ribbon.

1. The Power BI report canvas will open with your data model connected.

#### Page 1: Sales Overview Dashboard

1. Add a **Card visual** for Total Sales:

   - Drag **Total Sales** measure to the canvas
   - Format: Currency, no decimals
   - Title: "Total Revenue"

1. Add three more **Card visuals** for KPIs:

   - **Total Profit**
   - **Total Orders**
   - **Average Order Value**

1. Add a **Line chart** for Sales Trend over Time:

   - Axis: **gold_dim_date[Year]** and **gold_dim_date[Month]**
   - Values: **Total Sales**
   - Title: "Monthly Sales Trend"

1. Add a **Clustered column chart** for Sales by Region:

   - Axis: **gold_fact_sales[Region]**
   - Values: **Total Sales**, **Total Profit**
   - Title: "Sales & Profit by Region"

1. Add a **Pie chart** for Sales by Product Category:

   - Legend: **gold_dim_product[Category]**
   - Values: **Total Sales**
   - Title: "Sales Distribution by Category"

1. Add a **Table visual** for Top 10 Products:

   - Columns: **gold_dim_product[ProductName]**, **Total Sales**, **Total Profit**
   - Add visual-level filter: Top 10 by **Total Sales**
   - Title: "Top 10 Products by Revenue"

#### Page 2: Regional Performance Analysis

1. Add a new page: Click **+ Add page** at the bottom

1. Add a **Map visual** for Regional Sales:

   - Location: **gold_fact_sales[Region]**
   - Bubble size: **Total Sales**
   - Title: "Sales by Region Map"

1. Add a **Matrix visual** for detailed regional breakdown:

   - Rows: **gold_fact_sales[Region]**
   - Columns: **gold_dim_date[Year]**
   - Values: **Total Sales**, **Total Profit**, **Profit Margin %**
   - Title: "Regional Performance Matrix"

1. Add a **Stacked bar chart** for Status by Region:

   - Axis: **gold_fact_sales[Region]**
   - Legend: **gold_fact_sales[Status]**
   - Values: **Total Orders**
   - Title: "Order Status Distribution by Region"

#### Page 3: Customer Insights

1. Add a new page for customer analysis

1. Add a **Donut chart** for Customer Segments:

   - Legend: **gold_customer_segments[Segment]**
   - Values: Count of **CustomerName**
   - Title: "Customer Segmentation"

1. Add a **Table visual** for Top Customers:

   - Columns: **gold_dim_customer[CustomerName]**, **gold_customer_segments[TotalSpent]**, **gold_customer_segments[TotalOrders]**, **gold_customer_segments[Segment]**
   - Sort by: **TotalSpent** descending
   - Visual filter: Top 15
   - Title: "Top 15 Customers"

1. Add a **Clustered bar chart** for Customer Segment Revenue:

   - Axis: **gold_customer_segments[Segment]**
   - Values: **gold_customer_segments[TotalSpent]**
   - Title: "Revenue by Customer Segment"

### Part 4: Add Interactivity with Slicers

1. Go back to **Page 1: Sales Overview**

1. Add a **Slicer** for Year filter:

   - Field: **gold_dim_date[Year]**
   - Style: Dropdown
   - Position: Top-left corner

1. Add a **Slicer** for Region filter:

   - Field: **gold_fact_sales[Region]**
   - Style: List
   - Position: Left side panel

1. Add a **Slicer** for Product Category:

   - Field: **gold_dim_product[Category]**
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
   - Title: "Contoso Sales Analytics Dashboard"
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

   - Report name: **Contoso-Sales-Dashboard**

1. Click **Publish** in the Home ribbon

1. Select destination workspace: **fabric-workspace-<inject key="DeploymentID"></inject>**

1. Click **Select**

1. Once published, click **Open 'Contoso-Sales-Dashboard' in Power BI** to view in the service

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

   - Click on different regions in the map → other visuals should filter accordingly
   - Use slicers to filter by Year, Region, Category
   - Drill through from summary visuals to detailed tables

1. Verify data accuracy:

   - Compare Total Sales in Power BI with SQL query results from Lakehouse
   - Confirm customer segments match data written from Databricks

1. Share the dashboard:

   - Click **Share** button
   - Enter email addresses of stakeholders
   - Grant appropriate permissions (View only recommended)

<validation step="f6a7b8c9-d0e1-4f2a-3b4c-5d6e7f8a9b0c" />

> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Semantic model created from Fabric Lakehouse Gold layer tables.
- Relationships configured correctly between fact and dimension tables.
- Calculated measures created using DAX (Total Sales, Profit Margin, etc.).
- Multi-page interactive dashboard created with various visualizations.
- Slicers and filters implemented for user interactivity.
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

- **Unified Data Platform** - Single source of truth with OneLake eliminating data silos
- **Medallion Architecture** - Structured data quality layers (Bronze → Silver → Gold)
- **Cross-Platform Analytics** - Seamless integration between Fabric and Databricks
- **Self-Service BI** - Business users empowered with governed, high-quality data
- **Scalable Architecture** - Cloud-native platform ready for enterprise-scale workloads
- **Real-Time Insights** - Direct connectivity eliminates ETL latency

### What You've Built:

✅ **Bronze Layer**: Raw data ingestion from multiple sources  
✅ **Silver Layer**: Cleansed, standardized, joined datasets  
✅ **Gold Layer**: Business-ready dimensional models (Star Schema)  
✅ **Databricks Integration**: Advanced analytics and ML workloads  
✅ **Power BI Dashboards**: Interactive visualizations for business insights  

# Congratulations on completing this challenge!
