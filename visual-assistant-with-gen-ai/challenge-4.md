# Challenge 04: Publish and Test the Surface Defect Detection Model  

## Introduction
After the model has completed training, Contoso now needs to make the model available for real-time predictions.  
Publishing the trained model connects it to the **Prediction resource**, enabling applications and operators to send new images for defect detection.

In this challenge, you will publish the trained model and test it using sample images to verify prediction accuracy.

## Challenge Objectives
- Publish the trained Custom Vision model to the Prediction resource.  
- Run a **Quick Test** using sample manufacturing images.  
- Validate the model’s ability to identify defect categories with confidence scores.

## Steps to Complete

1. From the **surface-detection-project** workspace, navigate to the **Performance** tab.  
1. Locate the trained iteration (model) created in the previous challenge.
1. Click **Publish**.
1. In the Publish dialog:
   - **Model Name:** keep the default or enter a version name such as `surface-detection-v1`.  
   - **Prediction Resource:** select the available **Prediction** resource created earlier.
1. Click **Publish** to enable the Prediction API.
1. click on **Prediction URL** from top beside publish option to get the URL, from the list copy the second URL which will be under `If you have an image file:` section which is known as image_file_url.Paste it safely for later use.
1. After publishing, click **Quick Test** (top right).
1. From the downloaded dataset, navigate to the `Datasets/test` folder.
1. Upload any sample test image (for example, an image from *crazing*, *patches*, or *scratches* category).
1. Review prediction results displayed in the Quick Test panel:
   - Predicted defect category  
   - Confidence score for each category (probablity)

## Success Criteria
- The model is published successfully to the Prediction resource.  
- Quick Test displays a predicted defect label with probability scores, confirming correct model behavior.

## Additional Resources
- [Publish and Test Custom Vision Models](https://learn.microsoft.com/azure/ai-services/custom-vision-service/use-predictions-from-custom-vision)  
- [Quick Test in Custom Vision Portal](https://learn.microsoft.com/azure/ai-services/custom-vision-service/getting-started-build-a-classifier#test-your-model)

---

Now, click **Next** to continue to **Challenge 05: Generate AI-Based Inspection Commentary**.
