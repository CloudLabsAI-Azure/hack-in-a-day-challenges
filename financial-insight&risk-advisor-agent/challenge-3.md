# Challenge 03: Build Financial Analysis Topics  

## Introduction

The Copilot now has access to financial datasets and documents.  
In this challenge, you will create two interactive financial analysis topics.  
When each topic is triggered, the Copilot will:
1) Ask a clarifying question  
2) Use the user's answer to locate and interpret the correct values in the uploaded documents  
3) Provide insights + assign a risk level: **No Risk / Moderate Risk / High Risk**

This makes the agent conversational and context-aware.

## Challenge Objectives

- Create two interactive financial analysis topics.
- Ask for user input before performing analysis.
- Generate insights using the knowledge base + user input.
- Include a clear risk classification in responses.

## Steps to Complete

### Topic 1: Revenue Trend & Growth Drivers

1. Open the Financial Risk Advisor Copilot in Copilot Studio.

1. From the top navigation bar, select **topics** and click on **+ Add a topic** and select **From Blank** to create a new topic.

1. Configure: 
   - **Describe what topic does:** Analyze revenue patterns across reporting periods using financial documents. Ask the user which period or report to analyze, then evaluate the revenue trend, identify drivers behind changes, and assign a risk level (No Risk / Moderate Risk / High Risk) with clear reasoning.

1. In the topic flow editor, Add a new **ask a question** node and add the below question:
     ```
     Which reporting period or document would you like me to analyze for revenue performance? 
     ```
1. Under **identify** select type as **User's Entire Response**.

1. Once added, add one more node, select **Advanced** from list and click on **Generative answers**.

1. In **Generative answers** node, select the **Variable** `Var1` by clicking on **...** option.

1. Under data sources, click on **edit** and in the configuration pane, under **Knowledge Sources**, enable **search only selected resources** and select all the documents uploaded.

1. once done, in the same pane, scroll down and disable **allow ai to use its own general knowledge**.

1. Now, to Save the topic, click on save from top right corner and provide the name for the topic as `Revenue Trend & Growth Driver`.

### Topic 2: Cash Flow Stability & Liquidity Outlook

1. On the **Topics** page, click **New topic** again.

1. Configure:

   - **Describe what topic does:** Evaluate cash flow and liquidity using financial documents. Ask the user which period or report to examine, then assess whether the business is generating or burning cash, identify liquidity stress factors, and assign a risk level (No Risk / Moderate Risk / High Risk) with justification.

1. In the topic flow editor, Add a new **ask a question** node and add the below question:

   ```
   Which period or document should I examine to evaluate cash flow and liquidity?
   ```
1. Under **identify** select type as **User's Entire Response**.

1. Once added, add one more node, select **Advanced** from list and click on **Generative answers**.

1. In **Generative answers** node, select the **Variable** `Var2` by clicking on **...** option.

1. Under data sources, click on **edit** and in the configuration pane, under **Knowledge Sources**, enable **search only selected resources** and select all the documents uploaded.

1. once done, in the same pane, scroll down and disable **allow ai to use its own general knowledge**.

1. Now, to Save the topic, click on save from top right corner and provide the name for the topic as `Cash Flow Stability & Liquidity Driver`.

### Test Both Topics

1. Confirm uploaded files under **Knowledge** show status **Ready**.

1. Click **Test** from top right corner.

1. Ask the Copilot:

   ```
   Analyse revenue performance
   ```
1. When the Agent asks for period, add any one of the follwoing as answer: 

  - Q1-2024
  - Q2-2024
  - Q3-2024
  - Q1-2025
  - Q2-2025

1. Again ask the Copilot:

   ```
   How is our cash flow ?
   ```
1. When the Agent asks for period, add any one of the follwoing as answer: 

  - Q1-2024
  - Q2-2024
  - Q3-2024
  - Q1-2025
  - Q2-2025

1. Copilot should

   - Ask follow-up question (period/document)  
   - Use user’s reply to reference the correct dataset  
   - Produce bullet-point insights.

## Success Criteria

- Both topics are created successfully and request clarification from the user.
- Copilot references uploaded financial data based on user input (not generic advice).
- Responses include:
  - Numeric insights in bullet points  
  - A final, clearly stated risk level  

## Additional Resources
- https://learn.microsoft.com/microsoft-copilot-studio/topics  
- https://learn.microsoft.com/microsoft-copilot-studio/knowledge

