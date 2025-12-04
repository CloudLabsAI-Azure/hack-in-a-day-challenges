# Challenge 03: Build Financial Analysis Topics  
**Estimated Time:** 50 Minutes

## Introduction
With the financial datasets and knowledge documents uploaded, the Financial Risk Advisor Copilot can now reference business data to extract meaningful insights.  
In this challenge, you will design two key financial analysis topics that not only summarize trends but also classify the level of business risk using an AI-reasoning prompt:
• Revenue Trend & Growth Drivers  
• Cash Flow Stability & Liquidity Outlook  

These topics form the analytical core of the Copilot.

## Challenge Objectives
- Create two professional finance analysis topics.
- Provide topic descriptions instead of trigger phrases (new Copilot Studio interface).
- Configure instructions to summarize insights **and assign a risk score**.

---

## Steps to Complete

### Topic 1 — Revenue Trend & Growth Drivers
1. Open the Financial Risk Advisor Copilot in Copilot Studio.
2. From the top navigation, select **Topics**, then click **New topic**.
3. Set the **Topic name:** Revenue Trend & Growth Drivers
4. Set the **Topic description:**  
   Identifies whether revenue is increasing or decreasing across reporting periods. Highlights spikes or declines and explains business drivers impacting revenue performance.
5. Add a **Prompt** action and paste these instructions:  
   Extract revenue values from the uploaded financial statements. Analyze whether revenue is trending up or down across the available reporting periods. Identify major spikes or declines and explain root causes mentioned in the reports. Based on this trend, classify the financial risk as: No Risk, Moderate Risk, or High Risk. Provide the output in bullet points with clear numbers and the final risk level.
6. Add a **Message** action and enable **Respond using generative answers (with knowledge)**.
7. Click **Save**.

---

### Topic 2 — Cash Flow Stability & Liquidity Outlook
1. Still inside **Topics**, click **New topic** again.
2. Set the **Topic name:** Cash Flow Stability & Liquidity Outlook
3. Set the **Topic description:**  
   Evaluates whether the business is generating or burning cash. Detects liquidity pressure, instability, and signals of financial stress from cash flow reports.
4. Add a **Prompt** action and paste these instructions:  
   Review the cash flow and liquidity data from the uploaded financial documents. Determine whether the business is generating or burning cash, and identify any periods of significant cash pressure or volatility. Describe causes where available (operational, staffing, supply chain, seasonal, etc.). Based on the analysis, classify the financial risk as: No Risk, Moderate Risk, or High Risk. Provide the summary in bullet points with specific values and the final risk level.
5. Add a **Message** action and enable **Respond using generative answers (with knowledge)**.
6. Click **Save**.

---

### Test Both Topics
1. Ensure all uploaded files under **Knowledge** show status **Ready**.
2. Click **Test** (top right).
3. Ask sample questions such as:  
   • How is our revenue trending?  
   • What is the current cash flow situation?  
4. Confirm that the Copilot:
   • References real values from the documents  
   • Provides bullet-point summaries  
   • Assigns the correct risk level (No / Moderate / High)

---

## Success Criteria
- Two topics are created successfully:
  1) Revenue Trend & Growth Drivers  
  2) Cash Flow Stability & Liquidity Outlook
- Responses reference uploaded financial content, not generic or templated answers.
- The Copilot outputs a risk classification clearly in each topic.

## Additional Resources
- https://learn.microsoft.com/microsoft-copilot-studio/topics
- https://learn.microsoft.com/microsoft-copilot-studio/knowledge#use-knowledge-in-topics

---
