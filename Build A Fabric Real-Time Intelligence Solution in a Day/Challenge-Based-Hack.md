# Challenge: Build a Fabric Real-Time Intelligence Solution

**Estimated Time:** 4 Hours  

---

## Problem Statement
Organizations today need real-time insights from streaming data to make timely decisions. Microsoft Fabric provides tools to ingest, process, and visualize streaming events for analytics and automation.  

In this challenge, you will build a **Fabric Real-Time Intelligence solution**, including workspace setup, event streaming, Lakehouse integration, KQL database schema creation, and a real-time dashboard with automated alerts.

---

## Goals
- Set up a Fabric Workspace and Eventhouse for real-time data ingestion.  
- Stream synthetic events using Eventstream and Python Notebook.  
- Integrate Eventhouse data with a Lakehouse and create KQL tables/functions.  
- Build a Real-Time Dashboard with auto-refresh and automated alerts using Data Activator.

---

## Datasets
Use the following sample datasets provided in lab files:  

- **Synthetic Event Data:** Generated via Python Notebook (`Generate_synthetic_web_events.ipynb`).  
- **Reference Data:** `products.csv` and `productcategory.csv` for Lakehouse tables.  

Ensure all datasets are stored in your local directory:  
`C:\LabFiles\FabricRTI`

---

## Challenge Objectives

---

### **Challenge 1: Create a Fabric Workspace and Eventhouse**
**Estimated Duration:** 30 Minutes  

#### Objective
Enable real-time data ingestion and storage using Fabric Workspace and Eventhouse.

#### Tasks
1. Create a Fabric Workspace named `RTI_`.  
2. Create an Eventhouse `WebEvents_EH` in the workspace.  
3. Enable OneLake Availability for the Eventhouse.

#### Validation Check
- Workspace and Eventhouse exist.  
- OneLake Availability is enabled.

---

### **Challenge 2: Stream Data using Eventstream and Notebook**
**Estimated Duration:** 60 Minutes  

#### Objective
Simulate real-time customer events using Eventstream and Python Notebook.

#### Tasks
1. Create an Eventstream `WebEventsStream_ES` to handle Click and Impression events.  
2. Import and run the `Generate_synthetic_web_events.ipynb` notebook to send events to Eventstream.  
3. Define Eventstream topology to route:
   - Clicks → BronzeClicks  
   - Impressions → BronzeImpressions  

#### Validation Check
- Eventstream topology is active.  
- Eventhouse tables receive streaming data.

---

### **Challenge 3: Integrate Eventhouse with Lakehouse**
**Estimated Duration:** 60 Minutes  

#### Objective
Make Eventhouse data accessible via Lakehouse and build KQL database schema.

#### Tasks
1. Create a Lakehouse named `WebSalesData_LH`.  
2. Upload reference CSV files (`products.csv`, `productcategory.csv`) and create Delta tables.  
3. Create shortcuts in Lakehouse to Eventhouse tables (`BronzeClicks` and `BronzeImpressions`).  
4. Execute `createAll.kql` to build Silver and Gold tables/functions.

#### Validation Check
- Lakehouse contains Delta tables and Eventhouse shortcuts.  
- Silver and Gold tables/functions are successfully created.

---

### **Challenge 4: Build Real-Time Dashboard with Automation**
**Estimated Duration:** 90 Minutes  

#### Objective
Visualize live streaming data and automate alerts using Data Activator.

#### Tasks
1. Create a Real-Time Dashboard `Web Events Dashboard` with tiles for:
   - Clicks by hour  
   - Impressions by hour  
   - Impressions by location  
   - CTR metrics  
   - Average Page Load Time  
2. Enable Auto-refresh (Continuous).  
3. Configure a Data Activator (Reflex Alert) for events exceeding a threshold.

#### Validation Check
- Dashboard visuals update automatically.  
- Data Activator triggers alerts correctly.

---

## Success Criteria
To successfully complete this challenge:
- Fabric Workspace and Eventhouse are set up.  
- Real-time data streams into Eventhouse correctly.  
- Lakehouse contains reference data and Eventhouse shortcuts.  
- KQL Silver/Gold tables and functions are correctly created.  
- Real-Time Dashboard is interactive, auto-refreshing, and alerts are active.

---

## Additional Resources
- [Microsoft Fabric Overview](https://learn.microsoft.com/fabric/overview)  
- [Eventhouse Documentation](https://learn.microsoft.com/fabric/eventhouse)  
- [Eventstream Documentation](https://learn.microsoft.com/fabric/eventstream)  
- [KQL Reference](https://learn.microsoft.com/azure/data-explorer/kusto/query/)  
- [Data Activator Documentation](https://learn.microsoft.com/fabric/data-activator)

---

## Conclusion
By completing this challenge, you will have built an **end-to-end real-time analytics pipeline** in Microsoft Fabric.  

You learned how to:  
- Set up a collaborative Fabric Workspace and Eventhouse.  
- Stream and process synthetic events in real time.  
- Integrate Eventhouse with Lakehouse and build structured KQL databases.  
- Create an interactive real-time dashboard with automated alerts.  

This lab demonstrates how Microsoft Fabric enables **timely, data-driven decision making** through real-time analytics and automation.
 
