# Challenge 01: Create Azure AI Vision Resource
**Estimated Time:** 30 Minutes

## Introduction
Contoso Manufacturing aims to automate defect detection by analyzing images captured from production lines.  
Azure AI Vision provides pretrained image analysis capabilities to detect objects, anomalies, and attributes in images.

In this challenge, you’ll create the Azure AI Vision resource in your subscription to enable image analysis for the Visual Assistant.

## Accessing the Azure portal

1. To access the Azure portal, click on the **Azure Portal** Microsoft edge shortcut that is created in the desktop.

1. On the Sign in to Microsoft Azure tab, you will see a login screen. Enter the following email/username, and then click on Next.

   - Email/Username: <inject key="AzureAdUserEmail"></inject>

   - Password: <inject key="AzureAdUserPassword"></inject>

1. If you see the pop-up Stay Signed in?, click No.

1. If you see the pop-up You have free Azure Advisor recommendations!, close the window to continue with the challenge.

1. If a Welcome to Microsoft Azure pop-up window appears, click Cancel to skip the tour.

## Challenge Objectives
- Create an **Azure AI Vision** (Cognitive Services) resource.  
- Note the **Endpoint** and **API Key** for later use.  
- Understand where image analysis models are hosted.

## Steps to Complete
1. In the Azure Portal, click **Create a resource**.  
2. Search for **Computer Vision** or **AI Vision**, then click **Create**.  
3. Under **Basics**, configure:
   - **Subscription:** Use your sandbox subscription.  
   - **Resource Group:** `MFG-VIS-ASSIST-RG`.  
   - **Region:** *East US* or nearest supported region.  
   - **Name:** `vision-mfg-<uniqueID>`.  
   - **Pricing Tier:** *Free (F0)* or *Standard (S0)*.  
4. Click **Review + Create**, then **Create**.  
5. Once deployment completes, go to the **Keys and Endpoint** section.  
6. Copy **Endpoint URL** and **Key 1** for later challenges.

## Success Criteria
- Azure AI Vision resource created successfully.  
- Endpoint and API Key recorded for use in image analysis.

## Additional Resources
- [Azure AI Vision Overview](https://learn.microsoft.com/azure/ai-services/computer-vision/overview)
- [Quickstart: Create Computer Vision Resource](https://learn.microsoft.com/azure/ai-services/computer-vision/quickstarts-sdk/image-analysis-client-library)

Now, click **Next** to continue to **Challenge 02: Upload and Analyze Sample Manufacturing Images**.
