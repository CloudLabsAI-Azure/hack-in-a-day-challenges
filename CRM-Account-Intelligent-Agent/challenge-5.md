# Challenge 05: Run the B2B Account Intelligence Assistant

## Introduction

All backend services are now configured and validated. In this final challenge, you will run the B2B Account Intelligence Assistant and interact with it using a Streamlit-based UI.

The application allows sales teams to query account intelligence conversationally and receive contextual, AI-generated briefings.

## Challenge Objectives

- Configure environment variables for the AI services  
- Install Python dependencies  
- Run the Streamlit-based account intelligence application  
- Validate sales-focused queries  

## Steps to Complete

1. Open **Visual Studio Code**.

1. Select **File → Open Folder** and open the **Codefiles** directory.

1. Verify the following files are present:
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

1. Open the VS Code terminal.

1. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

1. After installation completes, start the Streamlit application:

   ```
   streamlit run app.py
   ```

1. In the browser, test prompts such as:

   ```
   What risks exist for Horizon Bank?
   ```

   ```
   Any recent changes at GlobalRetail Group?
   ```

1. Review the generated account insights.

<validation step="1150cf48-cc24-45fd-81e3-263abb8126cc" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. When it asks for AppURL, please provide the localhost url where your webapp is running.
> - If succeeded, you have successfully completed the challenges!
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Streamlit app launches successfully  
- Account intelligence queries return contextual insights  
- Responses are grounded in indexed account data  

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [RAG for Business Applications](https://learn.microsoft.com/azure/architecture/ai-ml/guide/rag)

## Congratulations!

You have successfully built an **AI-powered B2B Account Intelligence Assistant** that enhances sales preparation and customer engagement.

Click **Finish** to complete the lab.
