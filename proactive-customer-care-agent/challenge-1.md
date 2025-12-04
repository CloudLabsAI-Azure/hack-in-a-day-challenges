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
   - **Name:** `Customer Care Copilot`
   - **Description:** `AI-powered assistant for customer service automation including order tracking, complaint management, service inquiries, and product support`
   - **Language:** English
   - **Environment:** Select the default environment or **Dev-<inject key="DeploymentID"></inject>** if available

2. Click **Create** to initialize your copilot.

3. Wait for the copilot to be created (this may take 30-60 seconds).

### Step 4: Customize Copilot Icon and Identity

1. Once the copilot is created, you'll see the authoring canvas.

2. Click on **Settings** (gear icon) in the top-right corner.

3. Navigate to **Details** section.

4. Under **Icon** or **Avatar**, select an appropriate icon for customer service (e.g., support, chat, or service icon).

5. Click **Save** to apply changes.

### Step 5: Upload Knowledge Base

1. In the left navigation pane, click on **Knowledge** (or **Generative AI** section).

2. Click **+ Add knowledge** or **Upload**.

3. Select **Upload files**.

4. Navigate to and select the knowledge base files from:
   ```
   c:\Users\GirishR\OneDrive - Spektra Systems LLC\Documents\GitHub\hack-in-a-day-challenges\proactive-customer-care-agent\datasets\
   ```

5. Upload all four PDF files:
   - customer-care-ecommerce.pdf
   - customer-care-food-delivery.pdf
   - customer-care-retail.pdf
   - customer-care-telecom.pdf

6. Click **Open** to upload.

7. Wait for the files to be processed and indexed (this may take 2-3 minutes).

8. Verify all knowledge sources appear in your list with status **Active** or **Ready**.

### Step 6: Configure Generative AI Settings

1. In the **Settings** → **Generative AI** section, ensure the following are enabled:
   - **Generative answers**: On
   - **Content moderation**: Medium
   - **Classic fallback**: On (for graceful degradation)

2. Under **Data sources**, verify that all four PDF files are listed and enabled.

3. Click **Save**.

### Step 7: Test Basic Knowledge Retrieval

1. Click **Test your copilot** button (usually in the top-right or bottom-right corner).

2. In the test pane, try these questions:
   - "How do I track my order?"
   - "I want to return a product"
   - "My delivery is delayed"
   - "I need to speak with customer service"

3. Verify that the copilot responds with relevant information from the knowledge base.

4. If responses are generic or unhelpful, wait a bit longer for indexing to complete and test again.

## Success Criteria
- Successfully signed in to Microsoft Copilot Studio
- Created a new copilot named **Customer Care Copilot**
- Configured copilot with appropriate description and icon
- Uploaded all four knowledge base files as sources
- Verified knowledge bases are active and indexed
- Test queries return relevant responses from the knowledge base

## Additional Resources
- [Microsoft Copilot Studio Overview](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio)
- [Add knowledge sources](https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-conversations)
- [Generative AI in Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/nlu-gpt-overview)

---

Now, click **Next** to continue to **Challenge 02: Setup Freshdesk & Get API Credentials**.
