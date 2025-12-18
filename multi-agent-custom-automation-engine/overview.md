# Visual Assistant with Generative AI (GenAI)

Welcome to the Visual Assistant Hack in a Day! Today, you’ll explore how AI can transform quality inspection by building an intelligent assistant that detects surface defects from manufacturing images and generates natural-language inspection commentary. Through this hands-on lab, you will create a Visual Inspection Assistant capable of identifying manufacturing defects, classifying severity, and producing engineer-ready insights, powered by Azure AI Custom Vision, Azure AI Foundry, and GPT-4.1-Mini.

## Scenario

A manufacturing company is receiving thousands of product images every week from its production line. Quality engineers manually inspect images for surface defects such as crazing, patches, and scratches, but high workload and fatigue cause delays and oversight. To improve efficiency and accuracy, the company decides to build a Visual Assistant that can analyze images, detect defects using Custom Vision, and generate inspection commentary using a generative AI model. This allows engineers to review defects instantly, make faster decisions, and maintain consistent product quality across every batch.

## Introduction

Your mission is to build an AI-powered **Visual Inspection Assistant** that supports quality and production teams by detecting defects and generating human-readable inspection reports. Using Azure AI Custom Vision, Azure AI Foundry, and a Python application, you will design an end-to-end solution that can:

- Classify surface defects in images using a trained Custom Vision model
- Predict the defect category with probability-based confidence scoring
- Generate professional commentary and suggestions using the GPT-4.1-Mini model
- Display predictions and insights in a user-friendly application interface

This solution reduces manual inspection time, increases defect detection accuracy, and allows quality engineers to focus on decision-making rather than repetitive visual checks.

## Learning Objectives

By participating in this Hack in a Day, you will learn how to:

- Create Azure AI Custom Vision resources for training and prediction
- Build a Custom Vision project for surface defect detection
- Upload, tag, and train datasets for supervised learning
- Publish and test a production-ready surface defect classification model
- Deploy the GPT-4.1-Mini model in Azure AI Foundry for commentary generation
- Configure and run the Streamlit-based Visual Assistant using environment variables

## Hack in a Day Format: Challenge-Based

This hands-on lab is structured into six progressive challenges that model the lifecycle of building a real-world AI visual inspection application:

- **Challenge 01: Create Azure AI Custom Vision Resources**  
  Provision Custom Vision training and prediction resources in Azure.

- **Challenge 02: Create Custom Vision Project for Surface Defect Detection**  
  Create a classification project to analyze surface defects.

- **Challenge 03: Upload and Tag Images for Surface Defect Training**  
  Upload dataset images and tag them for crazing, patches, and scratches.

- **Challenge 04: Publish and Test the Surface Defect Detection Model**  
  Train and publish the model, then test predictions with uploaded images.

- **Challenge 05: Deploy Foundry Resource and GPT-4.1-Mini Model**  
  Set up Azure AI Foundry and deploy GPT-4.1-Mini for inspection commentary.

- **Challenge 06: Configure the Application and Run the Visual Inspection Assistant**  
  Provide environment variables, run the Streamlit app, and validate end-to-end predictions and commentary.

Throughout each challenge, you will iteratively design, build, and test your Visual Assistant, from dataset preparation to model deployment and application integration.

## Challenge Overview

You will begin by provisioning Custom Vision and creating a surface defect detection project. Next, you will upload and tag image datasets and train a model capable of identifying crazing, patches, and scratches. You will then publish the model and perform live defect predictions. After that, you will deploy the GPT-4.1-Mini model in Azure AI Foundry to generate natural-language inspection reports. Finally, you will configure and run a Streamlit application to test the complete visual inspection workflow, from image upload to AI-generated inspection summary.

By the end of this Hack in a Day, you will have a fully functional **Visual Assistant** that can automatically detect surface defects, generate professional commentary, and support faster decision-making on the production line.

## Support Contact

The CloudLabs support team is available 24/7, 365 days a year via email and live chat to ensure seamless assistance throughout the lab. Dedicated support channels are available for both learners and instructors.

**Learner Support Contacts**  
- Email: cloudlabs-support@spektrasystems.com  
- Live Chat: https://cloudlabs.ai/labs-support

Click **Next** from the bottom-right corner to continue.
