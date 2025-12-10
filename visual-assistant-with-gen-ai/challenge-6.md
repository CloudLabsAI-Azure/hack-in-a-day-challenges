# Challenge 06: Configure the Application and Run the Visual Inspection Assistant  

## Introduction

Now that all AI services are deployed and configured, Contoso will integrate them into the sample application.  
In this challenge, you will configure the environment variables, install dependencies, and run the Visual Inspection Assistant locally to perform real-time surface defect inspection.

## Challenge Objectives

- Configure the `.env` file with Custom Vision and Foundry model credentials.  
- Install required Python dependencies.  
- Run the Streamlit application and test image inspection.

## Steps to Complete

1. Open **Visual Studio Code**.

1. From VS Code, select **File → Open Folder** and open the `Codefiles` folder extracted earlier.

1. Ensure the folder contains the following files:  

   - `app.py`  
   - `.env.example`  
   - `requirements.txt`

1. Open the VS Code terminal.

1. Run the following command to create the `.env` file from the example template:

   ```
   Copy-Item .env.example .env
   ```

1. In the created .env file, add the following values as mentioned below: 

1. Get these values from your Custom Vision resource in the Azure portal

   - CUSTOM_VISION_ENDPOINT=https://xxxxx-prediction.cognitiveservices.azure.com/
   - CUSTOM_VISION_KEY=<your_custom_vision_prediction_key>
   - CUSTOM_VISION_PROJECT_ID=<your_project_id_here>
   - CUSTOM_VISION_PUBLISHED_MODEL_NAME=surface-detection-v1

   > **Tip to extract Project ID:** 

   > From an example prediction URL:  

   > `https://xxx-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/f63d1b26-0a6e-4970-b30f-0c5053c9c7fe/classify/iterations/surface-detection-v1/image`  
   > Then the **Project ID** is: `f63d1b26-0a6e-4970-b30f-0c5053c9c7fe`

1. Azure OpenAI Configuration
   - AZURE_OPENAI_ENDPOINT=<foundry_endpoint_value>
   - AZURE_OPENAI_KEY=<foundry_key_value>
   - AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4.1-mini

1. Save the `.env` file.

1. In the terminal, install dependencies by running this command: 

   ```
   pip install -r requirements.txt
   ```

1. After installation completes, run the application:

   ```
   stramlit run app.py
   ```

1. Once the Streamlit application launches in a browser, upload any manufacturing test image.

1. Review the output:  

   - Predicted defect category & confidence score  
   - AI-generated inspection commentary

 <validation step="56bca8de-b1ad-4ce2-a404-ca37e30617d8" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Environment variables populated correctly.  
- Streamlit application runs successfully.  
- Uploading an image triggers both prediction and commentary generation.

## Additional Resources

- [Working with Environment Variables in Python](https://code.visualstudio.com/docs/python/tutorial-env-file)  
- [Streamlit Documentation](https://docs.streamlit.io)

## Congratulations!

You have successfully built an **AI-powered Visual Inspection Assistant** using Azure AI Custom Vision + Azure OpenAI!

### Real-World Applications:

This solution can transform manufacturing operations across:

- **Quality Control** - Surface defect detection, visual inspection automation, compliance monitoring
- **Manufacturing Inspection** - Product quality assurance, defect classification, process optimization
- **Maintenance & Reliability** - Equipment surface monitoring, wear detection, preventive maintenance
- **Safety & Compliance** - Hazard identification, regulatory compliance, risk assessment
- **Operational Efficiency** - Automated inspection workflows, reduced manual labor, faster defect identification
- **Data-Driven Decision Making** - Inspection analytics, trend analysis, continuous improvement

# Congratulations on completing this challenge!


