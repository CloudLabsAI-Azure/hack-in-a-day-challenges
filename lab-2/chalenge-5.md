# Challenge 05: Add a Chat-Style Interface for Insights

## Introduction
Contoso wants operators to ask questions about data in natural language.  
In this challenge, you’ll build a simple chat-style interface using Streamlit or Flask to query the LLM for insights.

## Challenge Objectives
- Create a lightweight UI to accept user queries.  
- Send queries to Azure OpenAI model and display responses.  
- Demonstrate interactive data exploration with GenAI.

## Steps to Complete
1. Open **VS Code** or Azure Cloud Shell.  
2. Create a Python file `app.py` and paste:  
   ```python
   import openai, streamlit as st
   openai.api_key = "YOUR_API_KEY"
   endpoint = "YOUR_ENDPOINT"
   st.title("Manufacturing Data Chat Assistant")
   user_query = st.text_input("Ask about machine performance:")
   if user_query:
       prompt = f"You are a manufacturing analyst. Answer briefly based on logs. Question: {user_query}"
       response = openai.ChatCompletion.create(
           engine="gpt-35-turbo",
           messages=[{"role":"user","content":prompt}],
           temperature=0.5
       )
       st.write(response.choices[0].message["content"])
   ```
3. Run the app: streamlit run app.py and open the shown URL.

4. Ask questions such as “Which machine had maximum downtime?” or “What trend do you see in temperatures?”

## Success Criteria

- Chat interface runs locally and responds to user queries.

- Model provides relevant answers about the dataset.

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)

- [Azure OpenAI Python SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/chatgpt)

Now, click **Next** to continue to **Clean Up**.