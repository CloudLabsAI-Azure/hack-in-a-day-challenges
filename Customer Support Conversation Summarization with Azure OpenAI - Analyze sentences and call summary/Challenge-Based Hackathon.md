# Challenge: Customer Support Conversation Summarization with Azure OpenAI



**Estimated Time:** 2 Hours  



---



## 🧩 Problem Statement
Modern businesses handle large volumes of customer support interactions every day. To enhance efficiency and improve customer experience, organizations must be able to automatically summarize customer-agent conversations and extract key insights.  



In this challenge, you will use **Azure OpenAI**, **Azure AI Language Studio**, and **Azure AI Speech Studio** to generate summaries from customer-agent conversations — both text and audio. This enables faster understanding, reporting, and decision-making for customer service teams.



---



## 🎯 Goals
- Generate summaries of customer-agent conversations using Azure AI Language Studio.  
- Analyze sentences and create call summaries from audio recordings using Azure AI Speech Studio.



---



## 📁 Datasets
Use the following sample datasets for this challenge:  



- **Text dataset:** Sample customer-agent conversation transcripts (provided in the lab files).  
- **Audio dataset:** Sample audio recordings of customer calls (provided in the lab files).  



Ensure that both datasets are stored in your local directory:  
`C:\LabFiles\CustomerSupport`



---



## 🧠 Challenge Objectives



---



### **Challenge 1: Summarize Customer-Agent Conversations in Azure AI Language Studio**
**Estimated Duration:** 60 minutes  



#### Objective
Use Azure AI Language Studio to summarize text-based customer-agent conversations.



#### Tasks



1. **Provision Azure AI Language Service**  
   - Deploy a new Azure AI Language resource in the Azure Portal.  
   - Select the appropriate **region** (recommended: East US or West Europe).  
   - Choose pricing tier: **S Standard**.  
   - Name your resource: `language-service`.  



2. **Summarize Customer Conversations in AI Language Studio**  
   - Access **Azure AI Language Studio**.  
   - Select the **Summarization** feature.  
   - Upload your sample customer-agent text dataset.  
   - Run the summarization model to generate concise summaries of each conversation.  
   - Review key points, sentiment, and topics extracted by the model.  



#### ✅ Validation Check
- Ensure that each conversation summary captures the main customer issue, agent response, and resolution within 2–3 concise sentences.



---



### **Challenge 2: Analyze Sentences and Generate Call Summaries in Azure AI Speech Studio**
**Estimated Duration:** 60 minutes  



#### Objective
Use Azure AI Speech Studio to analyze and summarize customer support call recordings.



#### Tasks



1. **Provision Azure AI Speech Service**  
   - In the Azure Portal, create a **Speech** resource.  
   - Select **Standard (S0)** pricing tier.  
   - Name the resource: `speech-service`.  
   - Once deployed, note the **Key** and **Endpoint** values.



2. **Analyze and Summarize Calls in AI Speech Studio**  
   - Go to **Azure AI Speech Studio**.  
   - Upload your sample audio recordings from `C:\LabFiles\CustomerSupport\audio`.  
   - Use the **Speech-to-Text** capability to transcribe audio to text.  
   - Use the **Conversation Summarization** feature to generate summaries of the transcribed text.  
   - Review the generated summaries to ensure clarity and accuracy.



#### ✅ Validation Check
- Confirm that audio files are successfully transcribed and summarized.  
- Each summary should highlight the problem discussed, actions taken, and outcome.  



---



## 🏆 Success Criteria
To successfully complete this challenge:
- The Azure AI Language resource and Azure AI Speech resource are deployed successfully.  
- Summaries are generated accurately for both text-based and audio-based customer interactions.  
- Each summary concisely presents the main issue, key details, and resolution.  
- Both validations are marked as successful.



---



## 📚 Additional Resources
- [Azure AI Language Studio Documentation](https://learn.microsoft.com/azure/ai-services/language-service/overview)  
- [Azure AI Speech Studio Documentation](https://learn.microsoft.com/azure/ai-services/speech-service/overview)  
- [Azure OpenAI Service Documentation](https://learn.microsoft.com/azure/ai-services/openai/overview)



---



## 🧭 Conclusion
In this challenge, you successfully leveraged **Azure OpenAI**, **Azure AI Language Studio**, and **Azure AI Speech Studio** to summarize customer support interactions.  



You learned how to:  
- Provision and configure Azure AI resources.  
- Generate concise conversation summaries from both text and audio data.  
- Apply summarization models to enhance support efficiency and insight extraction.  



Your work demonstrates how AI-driven summarization can significantly improve customer support quality and response times.

 
