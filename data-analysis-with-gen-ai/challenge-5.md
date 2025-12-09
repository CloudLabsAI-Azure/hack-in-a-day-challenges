# Challenge 05: Configure the Application and Run the Manufacturing Data Analysis Assistant

## Introduction

Now that all AI services are deployed and configured, Contoso will integrate them into the sample application.  
In this challenge, you will configure the environment variables, install dependencies, and run the Manufacturing Data Analysis Assistant locally to perform real-time data analysis using RAG (Retrieval-Augmented Generation).

## Challenge Objectives

- Configure the `.env` file with Azure OpenAI and Azure AI Search credentials.  
- Install required Python dependencies.  
- Run the Streamlit application and test interactive data analysis.

## Steps to Complete

1. Open **Visual Studio Code**.

1. From VS Code, select **File → Open Folder** and open the `Codefiles` folder extracted in Challenge-1.

1. Ensure the folder contains the following files: 

   - `app.py`  
   - `.env.example`  
   - `requirements.txt`

1. In VS Code File Explorer, right-click on `.env.example` file and select **Rename**, then rename it to `.env`.

1. Open the `.env` file and add the values and **save**.

1. Open the VS Code terminal (Terminal → New Terminal).

1. In the terminal, install dependencies by running this command:

   ```
   pip install -r requirements.txt
   ```

1. After installation completes, run the application:

   ```
   streamlit run app.py
   ```

1. Once the Streamlit application launches in a browser, try asking questions such as:
   - Which machine had the most downtime this week?
   - Show me all machines with RUNNING status
   - What is the average temperature for MACHINE_001?
   - Find machines with high vibration levels
   - Which machines are currently in maintenance?
   - Analyze temperature trends across all machines

1. Review the output:  
   - AI-generated insights based on retrieved data  
   - Retrieved data from Azure AI Search  
   - Chat-style interface for interactive analysis

<validation step="2ea74b2b-34e6-4ae2-84eb-be669c59f8a9" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Environment variables populated correctly.  
- Streamlit application runs successfully.  
- User can ask questions and receive AI-generated insights based on manufacturing data.

## Additional Resources

- [Working with Environment Variables in Python](https://code.visualstudio.com/docs/python/tutorial-env-file)  
- [Streamlit Documentation](https://docs.streamlit.io)
- [Azure AI Search Documentation](https://learn.microsoft.com/azure/search/)
- [Azure OpenAI Documentation](https://learn.microsoft.com/azure/ai-services/openai/)

### **Congratulations — you have now completed the Manufacturing Data Analysis Assistant application!**

You have successfully combined **Azure AI Search + Azure OpenAI** to create an intelligent manufacturing data analysis solution using RAG (Retrieval-Augmented Generation).
