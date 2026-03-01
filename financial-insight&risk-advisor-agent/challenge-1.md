# Challenge 01: Create the Financial Risk Advisor Copilot  

## Introduction
Finance teams spend significant time manually reviewing financial reports to identify risks and unusual trends.To simplify the process, Contoso Finance wants to implement an AI-powered Copilot that acts as a **Financial Risk Advisor**. This Copilot will later analyze reports, summarize trends, and flag anomalies for leadership review.

In this challenge, you will create the **Financial Risk Advisor Copilot** in Copilot Studio, serving as the foundation for the rest of the lab.

## Accessing the Datasets

Please download and extract the datasets required for this challenge here:

```
https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/fin-datasets.zip
```

> Once the file is downloaded, please extract it in any desired path in the LabVM.

## Challenge Objectives
- Create a new Copilot in Copilot Studio.
- Configure the Copilot name, description, and industry context.
- Enable the Copilot for multiple financial analysis use cases.

## Steps to Complete

1. Open **Microsoft Copilot Studio**.

1. On the Copilot Studio pane, from left menu select **Agents** and then click on **+ Create blank agent** option to create a new agent.

1. Wait until the agent provisioning completes. This may take up to 5 minutes.

1. On the overview pane of the agent, click on **edit** inside Details card to edit agent's name and description.

1. Configure the Copilot details as below:

   - **Name:** `Financial Risk Advisor Copilot`

   - **Description:** `Assists finance teams by analyzing financial reports and identifying business risks and anomalies.`

1. Click on save.

1. Once done, scroll down and add below **instruction** by clicking on **edit** inside Instruction card.

     ```
     You are an autonomous Financial Risk Advisor Copilot designed to support finance teams.
     You extract information from uploaded financial documents and knowledge sources, identify trends in revenue, expenses, profitability, and cash flow, and summarize insights clearly.
     You highlight risks early — such as revenue decline, margin compression, liquidity pressure, or sudden cost spikes — and classify them as “No Risk”, “Moderate Risk”, or “High Risk” based on financial patterns.
     Always respond professionally using insight-driven analysis, not generic statements.
     If the user sentiment suggests concern or urgency, respond with a more supportive and acknowledgment-based tone.
     If multiple reports are referenced, compare performance and call out material changes.
     Format insight summaries using bullet points for clarity, and only give recommendations based on the information available in the uploaded financial documents.
     ```

1. Click on save.

<validation step="55d8a7b8-c53d-42fe-8aa0-2bd685c5b991" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria
- The **Financial Risk Advisor Copilot** is successfully created and accessible in Copilot Studio.

## Additional Resources
- [Copilot Studio Overview](https://learn.microsoft.com/microsoft-copilot-studio/overview)
- [Create your first Copilot](https://learn.microsoft.com/microsoft-copilot-studio/authoring-create-copilot)

Click **Next** to continue to **Challenge 02: Upload Financial Knowledge Documents**.
