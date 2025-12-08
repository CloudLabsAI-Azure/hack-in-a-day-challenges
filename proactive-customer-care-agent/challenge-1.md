# Challenge 01: Create Customer Care Copilot in Copilot Studio

## Introduction
Customer service organizations struggle with reactive support models that only address issues after they arise. Traditional helpdesk approaches lead to delayed responses, customer dissatisfaction, and missed opportunities for proactive engagement.

In this challenge, you will create an AI-powered Customer Care Copilot using Microsoft Copilot Studio that will serve as your intelligent assistant to handle customer inquiries, complaints, and service requests automatically.

## Challenge Objectives
- Sign in to Microsoft Copilot Studio
- Create a new Copilot for customer care automation
- Configure basic copilot settings and identity
- Upload knowledge base for intelligent responses

## Accessing the Datasets

Please download and extract the datasets required for this challenge here - [Datasets](https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/proactive-dataset.zip)

   ```
   https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/proactive-dataset.zip
   ```

## Steps to Complete

### Step 1: Sign in to Microsoft Copilot Studio

1. Open **Microsoft Edge** browser in your lab VM.

2. Navigate to **Microsoft Copilot Studio**:

   ```
   https://copilotstudio.microsoft.com
   ```

3. Click **Sign in**.

4. Enter the provided credentials:
   - **Email/Username: <inject key="AzureAdUserEmail"></inject>**
   - **Password: <inject key="AzureAdUserPassword"></inject>**

5. If prompted with **"Stay signed in?"**, click **No**.

6. Wait for the Copilot Studio home page to load.

### Step 2: Create a New Copilot

1. On the Copilot Studio pane, from left menu select **Create** and then click on **+New Agent** option to create a new agent.

2. If any error shows up like `There was a problem creating your agent.`, then please click on **Create a blank agent**.

3. On the overview pane of the agent, click on **edit** inside Details card to edit agent's name and description.

4. Configure the Copilot details as below:

   - **Name:** `Customer Care Copilot`

   - **Description:** `AI-powered assistant for customer service automation including order tracking, complaint management, service inquiries, and product support`

5. Click on save.

6. Once done, scroll down and add below **instructions** by clicking on **edit** inside Instruction card.

     ```
     - You are a Customer Care Copilot designed to help customers with order tracking, product returns, delivery delays, and service complaints.
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

7. Click on save.

<validation step="fd23ac57-641a-4da5-8f64-44bbb4ae7722" />
 
> **Congratulations** on completing the task! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding task. If you receive a success message, you can proceed to the next task. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria
- Successfully signed in to Microsoft Copilot Studio
- Created a new agent named **Customer Care Copilot**
- Configured agent with appropriate description and instructions for customer service scenarios
- Agent instructions configured with proper customer service behavior guidelines
- Copilot ready for Freshdesk integration in next challenges

## Additional Resources
- [Microsoft Copilot Studio Overview](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio)
- [Add knowledge sources](https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-conversations)
- [Generative AI in Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/nlu-gpt-overview)

---

Now, click **Next** to continue to **Challenge 02: Setup Freshdesk & Get API Credentials**.
