# Challenge 05: Run the Clinical Research Intelligence Assistant

## Introduction

With all Azure services configured and validated, the final step is to run the Clinical Research Intelligence Assistant application.

In this challenge, you will configure environment variables, install required dependencies, and launch a Streamlit-based chat application that allows clinical researchers to query indexed medical literature using natural language.

## Challenge Objectives

- Configure environment variables for Foundry and Azure AI Search  
- Install required Python dependencies  
- Run the Streamlit application  
- Validate clinical research queries end-to-end  

## Steps to Complete

1. Open **Visual Studio Code**.

1. From VS Code, select **File → Open Folder** and open the extracted **Codefiles** folder.

1. Ensure the folder contains the following files:
   - `app.py`
   - `.env.example`
   - `requirements.txt`

1. In the File Explorer, right-click **.env.example** and rename it to **.env**.

1. Open the **.env** file and update it with the following values:
   - Foundry endpoint
   - Foundry API key
   - Azure AI Search endpoint
   - Azure AI Search admin key
   - Azure AI Search index name

1. Save the file.

1. Open a new terminal in VS Code (**Terminal → New Terminal**).

1. Install the required dependencies by running:

   ```
   pip install -r requirements.txt
   ```

1. After installation completes, start the Streamlit application:

   ```
   streamlit run app.py
   ```

1. When the browser opens, test the assistant with prompts such as:

   ```
   What are the latest treatments for glioblastoma in patients over 60?
   ```

   ```
   Compare chemotherapy and immunotherapy outcomes
   ```

1. Review the AI-generated, grounded responses.

## Success Criteria

- Streamlit application runs successfully  
- User can submit clinical research queries  
- Responses are grounded in indexed medical literature  

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [Environment Variables in Python](https://code.visualstudio.com/docs/python/tutorial-env-file)

## Congratulations!

You have successfully built an **AI-powered Clinical Research Intelligence Assistant** that accelerates literature review and supports evidence-based healthcare research.

Click **Finish** to complete the lab.



