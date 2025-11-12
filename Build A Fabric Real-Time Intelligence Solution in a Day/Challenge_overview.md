# Build a Fabric Real-Time Intelligence Solution in a Day

Welcome to the Copilot Hackathon! Today, you’ll harness **Microsoft Fabric** to build an end-to-end **Real-Time Intelligence (RTI)** solution. You’ll stream synthetic events, land and transform them with **Eventstream** and **Eventhouse**, model/query data with **KQL**, surface insights in a **Real-Time Dashboard**, and automate actions with **Data Activator**.

## Introduction

Your quest is to design a real-time analytics pipeline that ingests, processes, and visualizes streaming events for instant decision-making. Using Fabric RTI capabilities—**Workspace + Eventhouse + Eventstream + Lakehouse + KQL + Real-Time Dashboards + Data Activator**—you will simulate web events, build a lightweight medallion flow, and deliver a live dashboard with automated alerts.

## Learning Objectives

By participating in this hackathon, you will learn how to:

- **Stand up core Fabric RTI assets**: Create a Fabric **Workspace**, **Eventhouse**, and **Eventstream** for streaming ingestion.
- **Enable OneLake access & Lakehouse integration**: Expose Eventhouse data via **OneLake** and a **Lakehouse** for downstream analytics.
- **Model and query with KQL**: Define tables/functions and use **Kusto Query Language** to transform and analyze streaming data.
- **Build live analytics surfaces**: Create a **Real-Time Dashboard** with auto-refresh and KPI tiles for operational visibility.
- **Automate actions from signals**: Configure **Data Activator** (Reflex) rules to trigger alerts/actions from threshold breaches.
- **Operate in the Service**: Manage items, permissions, refresh behavior, and workspace organization for collaboration.

## Hackathon Format: Challenge-Based

This hackathon uses a challenge-based approach so you learn by building a practical solution:

- Analyze a real-time analytics scenario and required outcomes.
- Strategize ingestion, modeling, and visualization steps.
- Leverage the provided lab environment and Microsoft Fabric RTI services.

## Challenge Overview

Begin by creating a **Fabric Workspace** and provisioning an **Eventhouse** enabled for **OneLake Availability**. Set up an **Eventstream** and run a **Data Generator Notebook** to push realistic clickstream events into Eventhouse. Integrate reference data in a **Lakehouse**, then define **KQL** tables/functions to shape Bronze-to-Gold outputs for metrics like CTR and latency.

Next, build a **Real-Time Dashboard** to visualize key signals (Clicks/Impressions by time and geography, CTR, Page Load). Turn on **auto-refresh** and configure **Data Activator** to fire alerts when thresholds are exceeded (e.g., unusual spikes). By the end, you’ll have a functioning real-time pipeline—from ingestion to action—built entirely in Microsoft Fabric.

## Happy Hacking!!
