# Challenge 05: Add a Chat-Style Interface for Insights

## Introduction

Contoso wants operators to ask questions about data in natural language.  
In this challenge, you’ll build a simple chat-style interface using Streamlit or Flask to query the LLM for insights.

## Challenge Objectives

- Create a lightweight UI to accept user queries.  
    - Send queries to the Foundry LLM and display responses.  
- Demonstrate interactive data exploration with GenAI.

## Steps to Complete

1. Open **VS Code** or Azure Cloud Shell.  
2. Create a Python file `app.py` and paste a lightweight example (pseudocode) that calls the Foundry/LLM endpoint via your preferred client library. Replace the `YOUR_API_KEY` and `YOUR_ENDPOINT` placeholders with values from your Foundry project:

   ```python
   # PSEUDOCODE: replace with Foundry SDK or REST call
   import requests
   import streamlit as st

   API_KEY = "YOUR_API_KEY"
   ENDPOINT = "YOUR_ENDPOINT"

   st.title("Manufacturing Data Chat Assistant")
   user_query = st.text_input("Ask about machine performance:")
   if user_query:
       payload = {"model": "gpt-4.1-mini", "prompt": user_query, "temperature": 0.5}
       headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
       r = requests.post(ENDPOINT, json=payload, headers=headers)
       st.write(r.json().get("output", "No response"))
   ```
3. Run the app: streamlit run app.py and open the shown URL.

4. Ask questions such as “Which machine had maximum downtime?” or “What trend do you see in temperatures?”

<validation step="2ea74b2b-34e6-4ae2-84eb-be669c59f8a9" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.


## Success Criteria

- Chat interface runs locally and responds to user queries.

- Model provides relevant answers about the dataset.

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)

- Foundry/LLM docs and SDKs: https://learn.microsoft.com/azure/ai-foundry/

Now, click **Next** to continue to **Clean Up**.