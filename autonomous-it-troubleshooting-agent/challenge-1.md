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

Please download and extract the datasets required for this challenge here - [Datasets](https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/c1-datasets.zip)

   ```
   https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/c1-datasets.zip/
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
   - **Email/Username:** <inject key="AzureAdUserEmail"></inject>
   - **Password:** <inject key="AzureAdUserPassword"></inject>

5. If prompted with **"Stay signed in?"**, click **No**.

6. Wait for the Copilot Studio home page to load.

### Step 2: Create a New Copilot

1. On the Copilot Studio home page, click **+ Create** in the left navigation pane.

2. Select **New copilot** from the options.

3. In the creation dialog, choose **Skip to configure** or **Create from blank** to manually configure.

### Step 3: Configure Basic Copilot Settings

1. In the copilot configuration screen, provide the following details:
   - **Name:** `IT Helpdesk Copilot - <inject key="DeploymentID"></inject>`
   - **Description:** `AI-powered assistant for IT support automation including password resets, VPN issues, laptop troubleshooting, and printer support`
   - **Language:** English
   - **Environment:** Select the default environment or **Dev-<inject key="DeploymentID"></inject>** if available

2. Click **Create** to initialize your copilot.

3. Wait for the copilot to be created (this may take 30-60 seconds).

### Step 4: Customize Copilot Icon and Identity

1. Once the copilot is created, you'll see the authoring canvas.

2. Click on **Settings** (gear icon) in the top-right corner.

3. Navigate to **Details** section.

4. Under **Icon** or **Avatar**, select an appropriate icon for IT helpdesk (e.g., headset, support, or computer icon).

5. Click **Save** to apply changes.

### Step 5: Upload Knowledge Base

1. In the left navigation pane, click on **Knowledge** (or **Generative AI** section).

2. Click **+ Add knowledge** or **Upload**.

3. Select **Upload files**.

4. Navigate to and select the **it-support.pdf** file from:
   ```
   c:\Users\GirishR\OneDrive - Spektra Systems LLC\Documents\GitHub\hack-in-a-day-challenges\autonomous-it-troubleshooting-agent\datasets\it-support.pdf
   ```

5. Click **Open** to upload.

6. Wait for the file to be processed and indexed (this may take 1-2 minutes).

7. Verify the knowledge source appears in your list with status **Active** or **Ready**.

### Step 6: Configure Generative AI Settings

1. In the **Settings** → **Generative AI** section, ensure the following are enabled:
   - **Generative answers**: On
   - **Content moderation**: Medium
   - **Classic fallback**: On (for graceful degradation)

2. Under **Data sources**, verify that **it-support.pdf** is listed and enabled.

3. Click **Save**.

### Step 7: Test Basic Knowledge Retrieval

1. Click **Test your copilot** button (usually in the top-right or bottom-right corner).

2. In the test pane, try these questions:
   - "I forgot my password"
   - "VPN not connecting"
   - "My laptop is running slow"

3. Verify that the copilot responds with relevant information from the knowledge base.

4. If responses are generic or unhelpful, wait a bit longer for indexing to complete and test again.

## Success Criteria
✅ Successfully signed in to Microsoft Copilot Studio  
✅ Created a new copilot named **IT Helpdesk Copilot - <inject key="DeploymentID"></inject>**  
✅ Configured copilot with appropriate description and icon  
✅ Uploaded **it-support.pdf** as knowledge source  
✅ Verified knowledge base is active and indexed  
✅ Test queries return relevant responses from the knowledge base  

## Additional Resources
- [Microsoft Copilot Studio Overview](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio)  
- [Add knowledge sources](https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-conversations)  
- [Generative AI in Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/nlu-gpt-overview)

---

Now, click **Next** to continue to **Challenge 02: Create Topics Using Generative AI**.
