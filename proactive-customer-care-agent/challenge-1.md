# Challenge 01: Create Proactive Customer Care Agent in Copilot Studio

## Introduction
Customer service organizations struggle with reactive support models that only address issues after they arise. Traditional helpdesk approaches lead to delayed responses, customer dissatisfaction, and missed opportunities for proactive engagement.

In this challenge, you will create an AI-powered Proactive Customer Care Agent using Microsoft Copilot Studio that will serve as your intelligent assistant to handle customer inquiries, complaints, and service requests automatically.

## Challenge Objectives
- Sign in to Microsoft Copilot Studio
- Create a new agent for customer care automation
- Configure basic agent settings and identity
- Upload knowledge base for intelligent responses

## Accessing the Datasets

Please download and extract the datasets required for this challenge from the following URL:

```
https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/proactive-dataset.zip
```

## Steps to Complete

### Step 1: Create a New Agent

1. Open **Microsoft Edge** browser in your lab VM.

1. If not already open, navigate to **Microsoft Copilot Studio** by entering the following URL in the browser:

   ```
   https://copilotstudio.microsoft.com
   ```

1. Click **Sign in**.

1. Enter the provided credentials:

   - **Email/Username: <inject key="AzureAdUserEmail"></inject>**
   - **Password: <inject key="AzureAdUserPassword"></inject>**

1. If prompted with **"Stay signed in?"**, click **No**.

1. Wait for the Copilot Studio home page to load.

1. In Copilot Studio, select **Agents** from the left navigation pane, and then click **Create blank agent** to start creating a new agent.

1. On the overview pane of the agent, click on **edit** inside the Details card to edit the agent's name and description.

1. Configure the agent details as follows:

  - **Name:** `Customer Care Copilot`
  - **Description:** `AI-powered assistant for customer service automation including order tracking, complaint management, service inquiries, and product support`

1. Click on **Save**.

1. Once done, scroll down and add the following **instructions** by clicking on **edit** inside the Instruction card.

    ```
    - You are a Proactive Customer Care Agent designed to help customers with order tracking, product returns, delivery delays, and service complaints.
    - Handle inquiries related to order status, return policies, delivery issues, and service quality concerns.
    - When answering questions:
      - Provide clear, helpful guidance to resolve customer issues quickly
      - Use friendly, professional language when explaining solutions
      - Ask clarifying questions to understand the issue better before providing solutions
    - For order tracking requests:
      - Ask for the order number
      - Provide tracking information and delivery status
      - If tracking issues persist, offer to create a support ticket with Freshdesk
    - For product return requests:
      - Ask for order number and return reason
      - Provide return policy information and instructions
      - If customer needs assistance with processing, escalate to Freshdesk ticket
    - For delivery delay issues:
      - Ask for order number and details about the delay
      - Provide information about common delays and resolution steps
      - If issue is not resolved, offer to create a priority support ticket
    - For service quality complaints:
      - Listen empathetically and ask for details about the complaint
      - Offer immediate solutions when appropriate
      - If customer is not satisfied, escalate to Freshdesk ticket for management review
    - Always be professional, empathetic, and helpful
    - When creating tickets, generate clear subject lines and detailed descriptions with all relevant information including order numbers
    ```

1. Click on **Save**.

### Step 2: Upload Knowledge Base

1. From the Copilot Studio home screen, open the **Customer Care Copilot** agent created in Step 1.

1. In the top navigation bar, select **Knowledge**.

1. Click **+ Add Knowledge**.

1. Choose **Upload files**.

1. Upload the following files from the dataset you downloaded and extracted earlier:

   - **Customer Support Ticket Dataset** (.csv)
   - **Customer-Data** (.xlsx)
   - **Employee-Data** (.xlsx)
   - **Employee-Travel-Reimbursement** (.xlsx)

1. After uploading, verify each file shows the status **Ready**.

   > **Note:** It may take up to 30 minutes for files to finish processing. You can proceed with the next challenge while the files are being processed.

<validation step="fd23ac57-641a-4da5-8f64-44bbb4ae7722" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Created a new agent named **Customer Care Copilot**
- Knowledge base files uploaded and status shows **Ready**

## Additional Resources
- [Microsoft Copilot Studio Overview](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio)
- [Add knowledge sources](https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-conversations)
- [Generative AI in Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/nlu-gpt-overview)

---

Click **Next** at the bottom of the page to proceed to the next page.

   ![](./media/pro-activ-gg-g17.png)