# Challenge 02: Upload and Analyze Sample Manufacturing Images
**Estimated Time:** 45 Minutes

## Introduction
Contoso’s production line generates product images for every component batch.  
You will now upload synthetic manufacturing images to Azure Blob Storage and analyze them with your Vision resource to detect objects and anomalies.

## Challenge Objectives
- Upload sample manufacturing images to Azure Blob Storage.  
- Analyze images using Azure AI Vision service.  
- Review detected objects and anomaly details.

## Steps to Complete
1. In the Azure Portal, create or open your **Storage Account**.  
2. Select **Containers** → click **+ Container** → name it `mfg-vision-input`.  
3. Set **Access Level:** Private.  
4. Upload the sample images provided in the lab (`gear_part_1.jpg`, `gear_part_2_defect.jpg`, etc.).  
5. Navigate to your **AI Vision** resource → select **Try in Vision Studio**.  
6. Under **Image Analysis**, choose **Object Detection**.  
7. Upload one of your images from the `mfg-vision-input` container.  
8. Review the detected tags, objects, and confidence scores displayed on the right.

## Success Criteria
- Images successfully analyzed using Vision Studio.  
- Object tags and anomaly labels visible with confidence percentages.

## Additional Resources
- [Vision Studio](https://portal.vision.cognitive.azure.com)
- [Object Detection with Azure AI Vision](https://learn.microsoft.com/azure/ai-services/computer-vision/concept-object-detection)

Now, click **Next** to continue to **Challenge 03: Deploy Azure OpenAI Service for Commentary Generation**.
