# Challenge 03: Upload and Tag Images for Surface Defect Training  

## Introduction
With the Custom Vision project created, Contoso will now prepare the defect detection model by uploading labeled training images.  
The model will learn to identify surface anomalies based on three defect categories: **crazing**, **patches**, and **scratches**.

In this challenge, you will upload images to the existing project, assign the correct tags to each image, and trigger model training.

## Challenge Objectives
- Upload sample manufacturing images to the Custom Vision project.  
- Tag images according to the correct defect category.  
- Train the initial defect-detection model.

## Steps to Complete
1. On the **Training Images** page, click **Add images**.
1. From the downloaded dataset folder, extract the ZIP file if not already extracted.
1. Navigate to the `Datasets/train` directory which you have extracted earlier, inside it you will find three folders representing defect categories:  
   - `crazing`  
   - `patches`  
   - `scratches`
1. Upload images category-wise:  
   - Open the `crazing` folder → select all images → click **Open** → apply the tag `crazing`.  
   - Open the `patches` folder → select all images → click **Open** → apply the tag `patches`.  
   - Open the `scratches` folder → select all images → click **Open** → apply the tag `scratches`.
1. After all images are uploaded and tagged, click **Train** (top right).
1. Select **Quick training** and confirm.  
1. Wait for the training run to complete.
   > **Note:** Training may take up to **30 minutes**, depending on compute availability.

## Success Criteria
- All training images uploaded and correctly tagged across **three defect categories**.  
- Initial training completed and a performance summary (Precision / Recall / mAP) is displayed.

## Additional Resources
- [Upload and Tag Images in Custom Vision](https://learn.microsoft.com/azure/ai-services/custom-vision-service/getting-started-build-a-classifier#upload-and-tag-images)  
- [Train and Evaluate Custom Vision Models](https://learn.microsoft.com/azure/ai-services/custom-vision-service/getting-started-build-a-classifier#train-the-classifier)

Now, click **Next** to continue to **Challenge 04: Publish and Test the Surface Defect Detection Model**.