# Challenge: Build a Fabric Real-Time Intelligence Solution

**Estimated Time:** 4 Hours  

**Industry Focus:** Cross-Industry (Operations, Digital, Commerce)

## Problem Statement
Organizations need instant insights from streaming events but lack an end-to-end pipeline for ingesting, modeling, visualizing, and automating actions in real time. Disconnected tools slow response times, limit visibility into key metrics (CTR/latency), and make alerting and reactive workflows difficult to implement.

In this challenge, you will build a **complete Fabric Real-Time Intelligence (RTI) solution** using Microsoft Fabric to stream synthetic events, land and process them with Eventstream and Eventhouse, model and query data using KQL, expose data via OneLake and Lakehouse, visualize with Real-Time Dashboards, and trigger actions via Data Activator (Reflex).

## Goals
By the end of this challenge, you will deliver a **live, auto-refreshing dashboard with threshold-based alerts** including:

- Stand up Fabric Workspace, Eventhouse, and Eventstream for real-time data ingestion
- Enable OneLake and Lakehouse integration for unified data access  
- Create KQL tables and functions (Bronze → Silver → Gold data layers)
- Build a Real-Time Dashboard with auto-refresh and KPI tiles
- Configure Data Activator alerts for threshold monitoring
- Operate effectively in the Fabric Service (items, permissions, refresh capabilities)

## Prerequisites
- **Skill Level:** Basic familiarity with KQL and streaming concepts
- **Audience:** Data engineers, BI developers, analytics engineers, operations teams
- **Technology Stack:** Microsoft Fabric (Workspace, Eventhouse, Eventstream, OneLake/Lakehouse, KQL Database, Real-Time Dashboards, Data Activator/Reflex)

## Datasets
Use the following sample datasets provided in lab files:  

- **Synthetic Event Data:** Generated via Python Notebook (`Generate_synthetic_web_events.ipynb`) for Click and Impression events
- **Reference Data:** `products.csv` and `productcategory.csv` for Lakehouse tables  

Ensure all datasets are stored in your local directory: `C:\LabFiles\FabricRTI`

## Challenge Objectives

### **Challenge 1: Foundation - Set Up Fabric Workspace and Eventhouse**
**Estimated Duration:** 30 Minutes  

#### Objective
Establish the foundational components for real-time data ingestion and storage.

#### Tasks
1. Create a Fabric Workspace named `RTI_<uniqueID>` for collaborative development
2. Create an Eventhouse `WebEvents_EH` within the workspace for event storage  
3. Enable OneLake Availability to expose Eventhouse data across the Fabric ecosystem
4. Verify workspace permissions and access controls

#### Validation Check
- Workspace and Eventhouse are successfully created
- OneLake Availability is enabled and accessible
- Workspace is ready for collaborative development

### **Challenge 2: Data Ingestion - Stream Events with Eventstream**
**Estimated Duration:** 60 Minutes  

#### Objective
Implement real-time event streaming to simulate customer web interactions and establish data flow patterns.

#### Tasks
1. Create an Eventstream `WebEventsStream_ES` to handle real-time Click and Impression events
2. Import and execute the `Generate_synthetic_web_events.ipynb` notebook to generate synthetic web events
3. Configure Eventstream topology with proper routing:
   - **Click Events** → `BronzeClicks` table in Eventhouse
   - **Impression Events** → `BronzeImpressions` table in Eventhouse  
4. Monitor event flow and verify data ingestion rates
5. Test event stream resilience and error handling

#### Validation Check
- Eventstream topology is active and processing events
- Eventhouse tables (`BronzeClicks`, `BronzeImpressions`) receive streaming data
- Event flow rates are consistent and measurable

### **Challenge 3: Data Integration - Build KQL Database Schema and Lakehouse Integration**
**Estimated Duration:** 60 Minutes  

#### Objective
Create a unified data architecture with KQL-based data transformations and Lakehouse integration for analytics.

#### Tasks
1. Create a Lakehouse named `WebSalesData_LH` for unified data access
2. Upload reference CSV files (`products.csv`, `productcategory.csv`) and create Delta tables
3. Create shortcuts in Lakehouse to connect Eventhouse tables (`BronzeClicks` and `BronzeImpressions`)
4. Execute `createAll.kql` script to build data transformation layers:
   - **Bronze Layer:** Raw event data from Eventstream
   - **Silver Layer:** Cleaned and enriched data with business rules
   - **Gold Layer:** Aggregated metrics and KPIs for analytics
5. Create KQL functions for key metrics (CTR calculations, latency analysis)
6. Verify data lineage and transformation logic

#### Validation Check
- Lakehouse contains Delta tables and active Eventhouse shortcuts
- KQL Silver and Gold tables/functions are successfully created and populated
- Data transformations produce accurate business metrics
- OneLake integration enables cross-service data access

### **Challenge 4: Visualization & Automation - Real-Time Dashboard and Alerting**
**Estimated Duration:** 90 Minutes  

#### Objective
Create an interactive, auto-refreshing dashboard with intelligent alerting to enable real-time monitoring and automated responses.

#### Tasks
1. **Build Real-Time Dashboard** `Web Events Dashboard` with comprehensive KPI tiles:
   - **Traffic Metrics:** Clicks by hour, Impressions by hour
   - **Geographic Analysis:** Impressions by location/region  
   - **Performance KPIs:** CTR (Click-Through Rate) metrics
   - **Technical Metrics:** Average Page Load Time trends
   - **Business Insights:** Conversion funnel and user engagement patterns

2. **Configure Dashboard Features:**
   - Enable Auto-refresh (Continuous) for real-time updates
   - Set appropriate refresh intervals for optimal performance
   - Implement interactive filters and drill-down capabilities
   - Add time-series visualizations for trend analysis

3. **Implement Data Activator (Reflex) Alerts:**
   - Configure threshold-based alerts for critical metrics
   - Set up automated notifications for anomaly detection
   - Create escalation workflows for different alert severity levels
   - Test alert triggering and response mechanisms

4. **Optimize for Collaboration:**
   - Configure dashboard sharing and permissions
   - Set up workspace collaboration features
   - Implement dashboard embedding capabilities

#### Validation Check
- Dashboard visuals update automatically with live data
- All KPI tiles display accurate, real-time metrics
- Data Activator triggers alerts correctly when thresholds are exceeded
- Dashboard is responsive, interactive, and ready for production use
- Collaboration features are properly configured

## Success Criteria
**You will have successfully completed this challenge when you deliver:**

A **functioning real-time pipeline** where events stream into Eventhouse, are curated via KQL into Silver/Gold layers, surfaced in an interactive Real-Time Dashboard with continuous refresh, and monitored by automated alerts via Data Activator - all ready for collaboration in a Fabric workspace.

### **Technical Deliverables:**
- **Foundation:** Fabric Workspace and Eventhouse properly configured with OneLake integration
- **Data Flow:** Real-time event streaming pipeline operational with consistent data ingestion  
- **Data Architecture:** Lakehouse integration with reference data and Eventhouse shortcuts established
- **Data Transformation:** KQL Silver/Gold tables and functions producing accurate business metrics
- **Visualization:** Interactive Real-Time Dashboard with auto-refresh and comprehensive KPIs
- **Automation:** Data Activator alerts configured and tested for threshold monitoring
- **Collaboration:** Workspace permissions and sharing capabilities ready for team collaboration

### **Business Outcomes:**
- **Instant Visibility:** Real-time insights into key performance indicators (CTR, latency, engagement)
- **Automated Response:** Threshold-based alerting enables immediate reaction to anomalies  
- **Unified Platform:** End-to-end pipeline eliminates disconnected tools and improves response times
- **Scalable Solution:** Architecture ready for production deployment and team collaboration

## Additional Resources
- [Microsoft Fabric Overview](https://learn.microsoft.com/fabric/overview)  
- [Eventhouse Documentation](https://learn.microsoft.com/fabric/eventhouse)  
- [Eventstream Documentation](https://learn.microsoft.com/fabric/eventstream)  
- [KQL Reference](https://learn.microsoft.com/azure/data-explorer/kusto/query/)  
- [Data Activator Documentation](https://learn.microsoft.com/fabric/data-activator)

## Conclusion
By completing this challenge, you will have built an **end-to-end real-time analytics pipeline** in Microsoft Fabric.  

You learned how to:  
- Set up a collaborative Fabric Workspace and Eventhouse.  
- Stream and process synthetic events in real time.  
- Integrate Eventhouse with Lakehouse and build structured KQL databases.  
- Create an interactive real-time dashboard with automated alerts.  

This lab demonstrates how Microsoft Fabric enables **timely, data-driven decision making** through real-time analytics and automation.