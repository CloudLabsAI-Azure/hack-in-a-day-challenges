# Challenge 01: Create the Financial Risk Advisor Copilot  

## Introduction
Finance teams spend significant time manually reviewing financial reports to identify risks and unusual trends.  
To simplify the process, Contoso Finance wants to implement an AI-powered Copilot that acts as a **Financial Risk Advisor**.  
This Copilot will later analyze reports, summarize trends, and flag anomalies for leadership review.

In this challenge, you will create the **Financial Risk Advisor Copilot** in Copilot Studio — serving as the foundation for the rest of the lab.

## Challenge Objectives
- Create a new Copilot in Copilot Studio.
- Configure the Copilot name, description, and industry context.
- Enable the Copilot for multiple financial analysis use cases.

## Steps to Complete
1. Open **Microsoft Copilot Studio**.
2. Select **Create a copilot**.
3. Configure the Copilot details as below:
   - **Name:** `Financial Risk Advisor Copilot`
   - **Description:** `Assists finance teams by analyzing financial reports and identifying business risks and anomalies.`
   - **Instruction:** 
     ```
     You are an autonomous Financial Risk Advisor Copilot designed to support finance teams.
     You extract information from uploaded financial documents and knowledge sources, identify trends in revenue, expenses, profitability, and cash flow, and summarize insights clearly.
     You highlight risks early — such as revenue decline, margin compression, liquidity pressure, or sudden cost spikes — and classify them as “No Risk”, “Moderate Risk”, or “High Risk” based on financial patterns.
     Always respond professionally using insight-driven analysis, not generic statements.
     If the user sentiment suggests concern or urgency, respond with a more supportive and acknowledgment-based tone.
     If multiple reports are referenced, compare performance and call out material changes.
     Format insight summaries using bullet points for clarity, and only give recommendations based on the information available in the uploaded financial documents.
     ```
4. Click **Create**.
5. Wait for the workspace to open.
6. Once created, verify:
   - The Copilot appears in your Copilot list.
   - You can access **Topics**, **Plugins**, and **Agent Flows** in the left navigation.

## Success Criteria
- The **Financial Risk Advisor Copilot** is successfully created and accessible in Copilot Studio.

## Additional Resources
- [Copilot Studio Overview](https://learn.microsoft.com/microsoft-copilot-studio/overview)
- [Create your first Copilot](https://learn.microsoft.com/microsoft-copilot-studio/authoring-create-copilot)

---

Click **Next** to continue to **Challenge 02: Upload Financial Knowledge Documents**.
