# Challenge 01: Create Azure AI Custom Vision Resources  

## Introduction  
Contoso Manufacturing aims to automate defect detection by analyzing images captured from production lines.  
Azure **Custom Vision** enables you to **train your own image classification and object detection models**, allowing the system to recognize factory defects, missing components, and anomalies with high accuracy.

In this challenge, you’ll create the **Custom Vision resources** required for the Visual Assistant, including **Training** and **Prediction** endpoints, which will later be used to train and deploy defect detection models.

## Accessing the Datasets and Codefiles

Please copy the below link and paste in a new browser tab inside your LabVM to download the required datasets and codefiles for the usecase and extract it.

```
https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/c3-datasets.zip
```
> Once the file is downloaded, please extract it in any desired path in the LabVM. You will be able to see `Codefiles` and `Datasets` folders.

## Challenge Objectives  
- Create **Azure Custom Vision Training** and **Prediction** resources.  
- Note the **Endpoint** and **API Keys** for later use.  
- Understand where custom image models are trained and hosted.

## Steps to Complete  
1. In the Azure Portal, search for **Custom vision** in the search bar.

1. On the **Custom Vision** page, then click **Create**.

1. Under **Basics**, configure:

   - **Create Options:** Select **both**  
   - **Subscription:** Use your sandbox subscription.  
   - **Resource Group:** challenge-rg-<inject key="DeploymentID"></inject>.  
   - **Region:** <inject key="Region"></inject>.  

1. Scroll down to **Custom Vision Types** and ensure:  
   - **Create both Training and Prediction resources** is selected.  

1. Specify resource name:  
   - **Training Resource Name:** **cv-train-mfg-<inject key="DeploymentID"></inject>** 

1. Select **Pricing Tier**:  
   - *Free (F0)* for both training and prediction resources.

1. Click **Review + Create**, then **Create**. 
 
1. Once deployment completes, open cvtrainmfg<inject key="DeploymentID"></inject>-Prediction:  
   - Go to **Keys and Endpoint**.  
   - Copy the following and paste it in a notepad for later challenges:  
     - **Endpoint**  
     - **Key 1**

<validation step="002b996d-0b17-49eb-abd6-c85d6d6f9417" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria  
- Custom Vision Training and Prediction resources created successfully.  
- All four values recorded successfully for use in model training and inference.

## Additional Resources  
- [Azure Custom Vision Overview](https://learn.microsoft.com/azure/ai-services/custom-vision-service/overview)  
- [Quickstart: Build a Classifier with Custom Vision](https://learn.microsoft.com/azure/ai-services/custom-vision-service/getting-started-build-a-classifier)


Now, click **Next** to continue to **Challenge 02**.
