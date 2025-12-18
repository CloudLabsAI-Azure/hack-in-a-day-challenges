# Unified Data Foundation with Fabric

Welcome to the Unified Data Foundation with Fabric Hack in a Day! Today, you'll explore how to build an enterprise-grade data lakehouse using Microsoft Fabric's unified analytics platform. Through hands-on challenges, you will implement the Medallion architecture (Bronze-Silver-Gold layers), perform data quality transformations, create dimensional models, and integrate with Azure Databricks for advanced machine learning analytics.

## Scenario

A large airline operates a flight loyalty program with millions of members worldwide. The program tracks customer demographics, flight history, loyalty tier progression, and transaction data. The data team needs to build a unified data lakehouse that can:

- Ingest raw data from multiple sources (CSV files, JSON transactions)
- Clean and standardize data with quality checks
- Create dimensional models for analytics
- Perform customer segmentation using machine learning
- Enable self-service analytics for business users

Using Microsoft Fabric OneLake and the Medallion architecture, you will build a complete data engineering solution that handles real-world data quality issues, implements best practices for data organization, and creates analytics-ready datasets for reporting and ML workloads.

## Introduction

Your mission is to build a **Data Lakehouse Solution** using Microsoft Fabric OneLake that enables the airline to analyze flight loyalty program data and transaction patterns. Using Microsoft Fabric, Azure Databricks, and Power BI, you will design an end-to-end solution that can:

- Create a Fabric Lakehouse with Bronze, Silver, and Gold folder structure
- Ingest dirty datasets with missing values, duplicates, and inconsistent formatting
- Transform data using PySpark notebooks for data cleansing and standardization
- Implement dimensional modeling with star schema (facts and dimensions)
- Integrate Azure Databricks for customer segmentation using K-Means clustering
- Build Power BI dashboards for business intelligence and reporting

This solution enables data-driven decision making, reduces manual data processing, and provides a scalable foundation for advanced analytics and machine learning.

## Learning Objectives

By participating in this Hack in a Day, you will learn how to:

- Create Microsoft Fabric workspaces with Trial capacity
- Build OneLake Lakehouses with folder structures for Medallion architecture
- Upload and manage datasets in OneLake (CSV and JSON files)
- Write PySpark transformations in Fabric Notebooks for data quality and cleansing
- Implement Silver layer transformations to handle missing values and standardize data
- Create Gold layer dimensional models with fact and dimension tables
- Integrate Azure Databricks with Fabric OneLake for seamless data access
- Perform machine learning customer segmentation using K-Means clustering
- Write enriched ML data back to Fabric from Databricks
- Build Power BI dashboards connected to Gold layer tables

## Hack in a Day Format: Challenge-Based

This hands-on lab is structured into six progressive challenges that model the lifecycle of building a real-world data lakehouse solution:

- **Challenge 1: Set Up Microsoft Fabric Workspace and OneLake Lakehouse**  
  Create a Fabric workspace using Trial capacity, build a Lakehouse with Bronze/Silver/Gold folders, and download the flight and transaction datasets.

- **Challenge 2: Ingest Raw Data to Bronze Layer**  
  Upload flight loyalty data (62,988 records) and customer transaction data (JSON format) to the Bronze layer, preview the data to identify quality issues.

- **Challenge 3: Transform and Cleanse Data for Silver Layer**  
  Use PySpark notebooks to clean data, handle missing values, standardize inconsistent values, remove duplicates, and write to Silver layer Delta tables.

- **Challenge 4: Build Gold Layer - Dimensional Modeling**  
  Create dimension tables (customers, geography, time) and fact tables (flight activity, transactions), implement business KPIs, and write analytics queries.

- **Challenge 5: Integrate Azure Databricks for Advanced Analytics**  
  Configure OneLake access from Databricks, load Gold layer tables, perform customer segmentation with K-Means ML clustering, and write enriched data back to Fabric.

- **Challenge 6: Build Power BI Dashboard**  
  Connect Power BI to Fabric Lakehouse, create semantic models, build visualizations for loyalty program insights, and publish interactive dashboards.

Throughout each challenge, you will iteratively design, build, and test your data lakehouse, from raw data ingestion to business intelligence reporting.

## Challenge Overview

You will begin by creating a Microsoft Fabric workspace and Lakehouse with a Medallion architecture folder structure. Next, you will upload dirty flight and transaction datasets to the Bronze layer. Then, you will write PySpark transformations to cleanse data and create Silver layer tables. After that, you will build Gold layer dimensional models with star schema design. You will then integrate Azure Databricks to perform ML-based customer segmentation and write results back to Fabric. Finally, you will create Power BI dashboards to visualize loyalty program metrics and customer insights.

By the end of this Hack in a Day, you will have a fully functional **Data Lakehouse Solution** with Bronze-Silver-Gold layers, ML-enriched customer segments, and interactive Power BI dashboards for business analytics.

## Support Contact

The CloudLabs support team is available 24/7, 365 days a year via email and live chat to ensure seamless assistance throughout the lab. Dedicated support channels are available for both learners and instructors.

**Learner Support Contacts**  
- Email: cloudlabs-support@spektrasystems.com  
- Live Chat: https://cloudlabs.ai/labs-support

Click **Next** from the bottom-right corner to continue.