# Challenge 01: Create IT Support Copilot in Copilot Studio

## Introduction
IT departments frequently face overwhelming volumes of repetitive support requests password resets, VPN connectivity issues, hardware problems, and printer troubleshooting. Traditional manual helpdesk processes lead to delayed responses, inconsistent resolutions, and poor visibility into support trends.

In this challenge, you will create an AI-powered IT Support Copilot using Microsoft Copilot Studio that will serve as your intelligent assistant to handle common IT support requests automatically.

## Challenge Objectives
- Sign in to Microsoft Copilot Studio
- Create a new Copilot for IT support automation
- Configure basic copilot settings and identity
- Upload IT_Support_QA.pdf knowledge base for intelligent responses

## Accessing the Datasets

Please download and extract the datasets required for this challenge here:

```
https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/it-support-dataset.zip
```

## Steps to Complete

### Step 1: Create a New Copilot

1. Open **Microsoft Copilot Studio**.

1. On the Copilot Studio pane, from left menu select **Create** and then click on **+New Agent** option to create a new agent.

1. If any error shows up like `There was a problem creating your agent.`, then please click on **Create a blank agent**.

1. On the overview pane of the agent, click on **edit** inside Details card to edit agent's name and description.

1. Configure the Copilot details as below:

   - **Name:** `IT Support Copilot`

   - **Description:** `AI-powered assistant for IT support automation including password resets, VPN issues, laptop troubleshooting, and printer support.`

1. Click on save.

1. Once done, scroll down and add below **instructions** by clicking on **edit** inside Instruction card.

     ```
     - You are an IT Support Copilot designed to help employees resolve common IT issues quickly and efficiently.
     - Handle inquiries related to password resets, account lockouts, VPN connectivity, slow device performance, and printer problems.
     - When answering questions:
       - First, check the uploaded IT support knowledge base (IT_Support_QA.pdf) for documented solutions
       - Provide clear, step-by-step troubleshooting guidance
       - Use simple, non-technical language when explaining solutions
       - Ask clarifying questions to understand the issue better before providing solutions
     - For password reset requests:
       - Collect the username
       - Provide self-service reset instructions from the knowledge base
       - If unsuccessful, offer to create a support ticket with Freshdesk
     - For VPN and connectivity issues:
       - Guide users through common troubleshooting steps
       - Check if the issue is resolved after each step
       - Escalate to Freshdesk ticket if unresolved
     - For hardware/performance issues:
       - Gather details about the problem (slow startup, applications, etc.)
       - Suggest troubleshooting steps from the knowledge base
       - Create a ticket if the issue persists
     - Always be professional, patient, and helpful
     - When creating tickets, generate clear subject lines and detailed descriptions with all relevant information
     ```

1. Click on save.

### Step 2: Upload Knowledge Base

1. From the Copilot Studio home screen, open the **IT Support Copilot** you just created.

1. In top navigation bar, select **Knowledge**.

1. Click **+ Add knowledge** or **+ Add a knowledge source**.

1. Choose **Upload files** or **Files**.

1. Click **Browse** and navigate to the extracted dataset folder from Step 1.

1. Upload the files.

1. After uploading, verify the file shows the status **Ready** or **Synced**.

   > **Note:** The knowledge base may take 15-25 minutes to process and index. You can proceed to the next challenge while the knowledge base finishes processing.

<validation step="0e6f0182-dd4d-402d-b9fc-b85a2a89e95d" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria
- Successfully signed in to Microsoft Copilot Studio
- Created a new agent named **IT Support Copilot**
- Configured agent with appropriate description and instructions for IT support scenarios
- Downloaded and extracted IT support dataset
- Uploaded **IT_Support_QA.pdf** as knowledge source
- Verified knowledge base is processing (status will show **Ready** after 2-5 minutes)
- Knowledge base is now available for use in topics

## Additional Resources
- [Microsoft Copilot Studio Overview](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio)  
- [Add knowledge sources](https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-conversations)  
- [Generative AI in Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/nlu-gpt-overview)

---

Now, click **Next** to continue to **Challenge 02: Setup Freshdesk & Get API Credentials**.
