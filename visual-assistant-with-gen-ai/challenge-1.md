# Challenge 01: Create Azure AI Custom Vision Resources  

## Introduction  
Contoso Manufacturing aims to automate defect detection by analyzing images captured from production lines.  
Azure **Custom Vision** enables you to **train your own image classification and object detection models**, allowing the system to recognize factory defects, missing components, and anomalies with high accuracy.

In this challenge, you’ll create the **Custom Vision resources** required for the Visual Assistant — including **Training** and **Prediction** endpoints — which will later be used to train and deploy defect detection models.

## Challenge Objectives  
- Create **Azure Custom Vision Training** and **Prediction** resources.  
- Note the **Endpoint** and **API Keys** for later use.  
- Understand where custom image models are trained and hosted.

## Steps to Complete  
1. In the Azure Portal, click **Create a resource**.  
2. Search for **Custom Vision**, then click **Create**.  
3. Under **Basics**, configure:  
   - **Subscription:** Use your sandbox subscription.  
   - **Resource Group:** ODL-demolab-<inject key="DeploymentID"></inject>.  
   - **Region:** <inject key="Region"></inject>.  
4. Scroll down to **Custom Vision Types** and ensure:  
   - **Create both Training and Prediction resources** is selected.  
5. Specify resource names:  
   - **Training Resource Name:** `cv-train-mfg-<uniqueID>`  
   - **Prediction Resource Name:** `cv-pred-mfg-<uniqueID>`  
6. Select **Pricing Tier**:  
   - *Free (F0)* if available — or *Standard (S0)*.  
7. Click **Review + Create**, then **Create**.  
8. Once deployment completes, open each resource:  
   - Go to **Keys and Endpoint**.  
   - Copy the following for later challenges:  
     - **Training Endpoint**  
     - **Training Key**  
     - **Prediction Endpoint**  
     - **Prediction Key**

## Success Criteria  
- Custom Vision Training and Prediction resources created successfully.  
- All four values recorded successfully for use in model training and inference.

## Additional Resources  
- [Azure Custom Vision Overview](https://learn.microsoft.com/azure/ai-services/custom-vision-service/overview)  
- [Quickstart: Build a Classifier with Custom Vision](https://learn.microsoft.com/azure/ai-services/custom-vision-service/getting-started-build-a-classifier)

---

Now, click **Next** to continue to **Challenge 02: Upload and Analyze Sample Manufacturing Images**.
