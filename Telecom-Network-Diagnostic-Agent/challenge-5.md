# Challenge 05: Run the Network Diagnostics & Optimization Assistant

## Introduction

With all infrastructure and AI services in place, the final step is to run the Network Diagnostics and Optimization Assistant.

In this challenge, you will launch a Streamlit application that allows telecom engineers to query network telemetry and incident data conversationally and receive AI-driven diagnostics and recommendations.

## Challenge Objectives

- Configure environment variables for AI services  
- Install required dependencies  
- Run the Streamlit diagnostics application  
- Validate network diagnostics queries  

## Steps to Complete

1. Open **Visual Studio Code**.

1. Open the **Codefiles** folder using **File → Open Folder**.

1. Confirm the following files exist:
   - `app.py`
   - `.env.example`
   - `requirements.txt`

1. Rename **.env.example** to **.env**.

1. Open the **.env** file and update it with the following values:
   - Foundry endpoint
   - Foundry API key
   - Azure AI Search endpoint
   - Azure AI Search query key
   - Azure AI Search index name

1. Save the file.

1. Open a new terminal in VS Code.

1. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

1. After installation completes, start the Streamlit application:

   ```
   streamlit run app.py
   ```

1. When the browser opens, test the assistant with prompts such as:

   ```
   Why is network latency high in Beverly hills?
   ```

   ```
   What remediation actions are recommended for congestion?
   ```

1. Review the diagnostics explanations and recommendations.

<validation step="d9175e14-5167-48fb-971a-6a885fd1184f" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. When it asks for AppURL, please provide the localhost url where your webapp is running.
> - If succeeded, you have successfully completed the challenges!
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Streamlit application runs successfully  
- Network diagnostics queries return explainable insights  
- Recommendations are grounded in indexed telemetry data  

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [AI for Telecom Operations](https://learn.microsoft.com/azure/architecture/industries/telecommunications/)

## Congratulations!

You have successfully built an **AI-powered Network Diagnostics & Optimization Assistant** that transforms reactive telecom operations into a proactive model.
