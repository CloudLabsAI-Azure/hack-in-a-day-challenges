# Manufacturing – Visual Assistant with Generative AI (GenAI)
*Build an AI-powered visual inspection assistant to detect defects, analyze images, and generate actionable insights using Azure AI Vision and Generative AI.*

**Duration:** 6 hours  

**Tags:** `Manufacturing`, `Generative AI`, `Computer Vision`, `Azure AI`, `Quality Control`

## Overview
In this lab, participants will learn how to combine **Azure AI Vision** with **Generative AI** to create a **Visual Assistant** capable of analyzing manufacturing images for defects or anomalies and generating natural-language explanations.  
You will build a lightweight workflow that processes sample images, detects issues, and uses a large language model to generate inspection summaries and corrective recommendations.

The goal is to demonstrate how GenAI can enhance human inspection tasks, improve quality control efficiency, and enable data-driven manufacturing insights.

## Problem Statement
Production lines in manufacturing frequently rely on visual inspections for defects, deviations, or maintenance issues (e.g., component misalignment, surface blemishes, missing parts). Manual visual review is time-consuming, inconsistent, and difficult to scale. Teams often struggle with using images or videos from cameras, identifying issues quickly, documenting them, and routing these insights for action. This slows throughput, increases scrap/rework, and limits real-time decision making.

## Solution Overview

Provide a beginner-friendly prototype where teams build a “visual assistant” that uses generative AI + computer-vision to assist shop-floor operators. The assistant ingests images or video frames from a manufacturing line (or sample dataset), analyses them for anomalies (defects, misalignment, missing parts), generates natural-language commentary (e.g., “Component X appears misaligned by approx 3mm; recommend repositioning”), and presents a simple UI dashboard for review and action. By combining vision models + generative AI commentary, the lab allows teams to show how manufacturing visual inspection and assistance can be automated and augmented.

## Architecture

![](./c3-arch.png)

## Learning Objectives
**Description:**  
By the end of this lab, you will learn to:

- Understand how to combine computer vision (image/frame ingestion) with generative AI to produce commentary and recommended actions.
- Pre-process visual data (images/frames), detect anomalies/defects, and use retrieval/prompting pipelines to generate natural-language insights.
- Build a simple UI or dashboard that shows visual input, detected issues, commentary and next-steps.
- Recognise challenges: camera calibration, lighting, anomaly-detection false positives, generative AI hallucination, human-in-loop review.
- Learn how to deploy a lightweight prototype using accessible Azure (or cloud) services and clean up resources.


## Challenges Overview

- **Challenge 01: Create Azure AI Vision Resource**  
Provision the Azure AI Vision service in the Azure Portal to perform image analysis on manufacturing components.

- **Challenge 02: Upload and Analyze Sample Manufacturing Images**  
Upload synthetic manufacturing images to Azure Blob Storage and analyze them using the AI Vision service to detect objects and potential anomalies.

- **Challenge 03: Deploy Azure OpenAI Service for Commentary Generation**  
Deploy the Azure OpenAI Service and use the gpt-35-turbo model to generate text-based commentary from the detected visual results.

- **Challenge 04: Generate Visual Inspection Reports**  
Combine AI Vision and Generative AI outputs to produce comprehensive visual inspection summaries highlighting detected issues and recommendations.

- **Challenge 05: Build a Visual Assistant Web Interface**  
Create a simple Streamlit-based dashboard to upload images, view AI results, and interact with Generative AI commentary in real-time.

- **Challenge 06: Clean Up Resources**  
Remove all Azure resources to prevent extra costs and complete your Visual Assistant workflow.

## Support Contact

The CloudLabs support team is available 24/7, 365 days a year, via email and live chat to ensure seamless assistance at any time. We offer dedicated support channels tailored specifically for both learners and instructors, ensuring that all your needs are promptly and efficiently addressed.

Learner Support Contacts:

- Email Support: cloudlabs-support@spektrasystems.com
- Live Chat Support: https://cloudlabs.ai/labs-support

Now, click on the **Next** from lower right corner to move on next page.

## Happy Hacking!!