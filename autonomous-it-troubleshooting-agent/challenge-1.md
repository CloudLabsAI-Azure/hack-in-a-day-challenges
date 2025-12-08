# Challenge 01: Create IT Helpdesk Copilot in Copilot Studio

## Introduction
IT departments frequently face overwhelming volumes of repetitive support requests—password resets, software access, connectivity issues, or device setup queries. Traditional manual helpdesk processes lead to delayed responses, inconsistent resolutions, and poor visibility into support trends.

In this challenge, you will create an AI-powered IT Helpdesk Copilot using Microsoft Copilot Studio that will serve as your intelligent assistant to handle common IT support requests automatically.

## Challenge Objectives
- Sign in to Microsoft Copilot Studio
- Create a new Copilot for IT Helpdesk automation
- Configure basic copilot settings and identity
- Upload knowledge base (it-support.pdf) for intelligent responses

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

1. Once done, scroll down and add below **instruction** by clicking on **edit** inside Instruction card.

     ```

     ```

1. Click on save.

### Step 2: Upload Knowledge Base

1. From the Copilot Studio home screen, open the **HR Interview Copilot** created previously.

1. In top navigation bar, select **Knowledge**.

1. Click **+ Add a knowledge source**.

1. Choose **Upload files**.

1. Upload the Job Description and Resume documents provided, which you downloaded and extracted earlier.

1. After uploading, verify each file shows the status **Ready**.

   > Note: It may take up to 30 minutes for files to finish processing. You may continue to the next challenge while processing completes.

## Success Criteria
- Successfully signed in to Microsoft Copilot Studio
- Created a new copilot named **IT Support Copilot**
- Configured copilot with appropriate description and icon
- Uploaded **it-support.pdf** as knowledge source
- Verified knowledge base is active and indexed
- Test queries return relevant responses from the knowledge base  

## Additional Resources
- [Microsoft Copilot Studio Overview](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio)  
- [Add knowledge sources](https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-conversations)  
- [Generative AI in Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/nlu-gpt-overview)

Now, click **Next** to continue to **Challenge 02: Create Topics Using Generative AI**.
