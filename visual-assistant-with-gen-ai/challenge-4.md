# Challenge 04: Generate Visual Inspection Reports

## Introduction
After detecting visual anomalies, Contoso wants to automatically generate descriptive inspection reports summarizing what was found.  
You will combine AI Vision output with Azure OpenAI commentary to produce readable reports.

## Challenge Objectives
- Combine vision detection data and LLM commentary.  
- Generate inspection summaries for each analyzed image.  
- Save the results as text or JSON files.

## Steps to Complete
1. Open **Vision Studio** → select your analyzed image.  
2. Copy detected tags and confidence data (e.g., “Bolt missing,” “Surface scratch detected”).  
3. Go to **Azure AI Studio / OpenAI Playground** → select your deployed model `gpt-35-turbo`.  
4. Use a prompt like:  

   - You are a manufacturing quality assistant.Based on these findings, generate a short inspection report with recommendations:[Paste object detection output]

5. Observe the generated summary.  
6. Save the generated text to a `.txt` or `.json` file for later display.

## Success Criteria
- AI-generated inspection summary successfully created.  
- File saved for visualization in the next challenge.

## Additional Resources
- [Azure AI Studio](https://oai.azure.com/portal)
- [Prompt Engineering Examples](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering)

Now, click **Next** to continue to **Challenge 05: Build a Visual Assistant Web Interface**.

