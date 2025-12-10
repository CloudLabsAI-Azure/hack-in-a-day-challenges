# Challenge 02: Create Custom Vision Project for Surface Defect Detection  

## Introduction
Contoso’s production line generates images for every manufactured component.  
To enable automated defect detection, you will now create a **Custom Vision project** that will be used later to train a model for identifying surface defects in manufactured parts.

## Challenge Objectives
- Sign in to the **Custom Vision Portal**.  
- Create a new **Custom Vision Project** for defect detection.  
- Configure correct project type, classification type, and domain.

## Steps to Complete
1. Open the Custom Vision Portal:
   ```
   https://www.customvision.ai/projects  
   ```
2. Sign in using the same credentials you used to deploy Azure resources.  
3. On the **Projects** page, click **+ New Project**.  
4. Fill in the project details:  
   - **Name:** `surface-detection-project`  
   - **Description:** `Surface defect detection for manufacturing components`  
   - **Project Type:** `Classification`  
   - **Classification Type:** `Multiclass (Single tag per image)`  
   - **Domain:** `General [A2]`  
5. Click **Create Project**.  
6. Wait for the workspace to load, you should now see the **Training Images** page where images can later be uploaded and tagged.

## Success Criteria
- Custom Vision project named **surface-detection-project** created successfully.  
- Project type correctly set to **Classification (Multiclass)** using **General [A2]** domain.

## Additional Resources
- [Custom Vision Portal](https://www.customvision.ai)  
- [Classification Models with Custom Vision](https://learn.microsoft.com/azure/ai-services/custom-vision-service/getting-started-build-a-classifier)

Now, click **Next** to continue to **Challenge 03**.
