# Challenge 01: Create Internal Knowledge Copilot in Copilot Studio

## Introduction
Employees across organizations waste valuable time searching for internal policies, procedures, and guidelines scattered across different departments. Traditional document repositories and file shares make it difficult to find relevant information quickly, leading to repeated questions to managers and colleagues.

In this challenge, you will create an AI-powered Internal Knowledge Copilot using Microsoft Copilot Studio that will serve as your intelligent assistant to help employees access information from HR, Finance, IT, and Procurement departments.

## Challenge Objectives
- Sign in to Microsoft Copilot Studio
- Create a new Copilot for internal knowledge navigation
- Configure basic copilot settings and identity
- Prepare for knowledge base upload in the next challenge

## Steps to Complete

### Step 1: Get SharePoint Site URL

- In the **Lab VM**, click on **Microsoft Edge** browser icon on the desktop.

- Navigate to the **Microsoft 365** portal:

   ```
   https://www.office.com
   ```

- Sign in with the provided credentials:
   - **Email/Username:** <inject key="AzureAdUserEmail"></inject>
   - **Password:** <inject key="AzureAdUserPassword"></inject>

- If prompted with **"Stay signed in?"**, click **No**.

- From the Microsoft 365 apps, select **SharePoint**.

- Click on **My Sites** and then select **KnowledgeHub<inject key="DeploymentID" enableCopy="false"/>**.

   > **Note:** This SharePoint site will store employee knowledge queries and department document metadata.

- **Copy the SharePoint site URL** from the browser address bar and paste it into **Notepad** for use in upcoming steps.

   Example format: `https://yourdomain.sharepoint.com/sites/KnowledgeHub<inject key="DeploymentID" enableCopy="false"/>`

### Step 2: Sign in to Microsoft Copilot Studio

- Open a new browser tab and navigate to **Microsoft Copilot Studio**:

   ```
   https://copilotstudio.microsoft.com
   ```

- Sign in using the same credentials if prompted.

- Wait for the Copilot Studio home page to load.

### Step 3: Create a New Agent

- On **Copilot Studio**, select **+ Create**, and then select **+ New agent**.

- On **Start building your agent** page, select **Configure**.

- Provide the following details:
   - **Name:** `Internal Knowledge Navigator (2)`
   - **Description (3):**
     ```
     This agent helps employees quickly find policies, procedures, and guidelines across HR, Finance, IT, and Procurement departments. It provides accurate answers with document citations, guides users through common processes, and can trigger helpful actions like emailing documents or creating support tickets.
     ```
   - **Instructions (4):**
     ```
     - Respond only to queries related to internal company policies, procedures, and department-specific guidelines.
     - Retrieve knowledge from uploaded department documents (HR, Finance, IT, Procurement).
     - When answering questions:
       - Provide clear, accurate information based strictly on official policy documents
       - Always cite the source document name and section
       - Use professional, helpful language
       - If information isn't in the knowledge base, direct users to the appropriate department contact
     - For common scenarios, guide users through step-by-step processes
     - Offer to email policy documents or create IT tickets when appropriate
     - Maintain employee privacy and confidentiality at all times
     ```

- Click **Create** to initialize your agent.

- Wait for the agent to be created (this may take 30-60 seconds).

### Step 4: Customize Copilot Icon and Identity

- Once the copilot is created, you'll see the authoring canvas.

- Click on **Settings** (gear icon) in the top-right corner.

- Navigate to **Details** section.

- Under **Icon** or **Avatar**, select an appropriate icon for internal knowledge (e.g., book, search, or information icon).

- Optionally, customize the following:
   - **Welcome message:** "Hello! I'm your Internal Knowledge Navigator. I can help you find information about HR policies, Finance procedures, IT support, and Procurement processes. What would you like to know?"
   - **Color theme:** Choose a professional color that matches your organization

- Click **Save** to apply changes.

### Step 5: Review Default Topics

- In the left navigation pane, click on **Topics**.

- Review the default system topics:
   - **Greeting** - Welcome message for users
   - **Conversational boosting** - Fallback for unmatched queries
   - **End of conversation** - Closing message

- These default topics will be enhanced in later challenges.

### Step 6: Verify Copilot Environment

- Click **Settings** (gear icon) again.

- Navigate to **Generative AI** section.

- Verify that the following settings are available:
   - **How should your copilot interact with people?** - Set to **Generative**
   - **How strictly should your copilot match the knowledge sources?** - Set to **Medium**

- Do NOT make changes yet - you'll configure these in Challenge 4.

- Click **Cancel** or navigate back.

### Step 7: Test Basic Copilot Greeting

- Click **Test your copilot** button (usually in the top-right corner).

- In the test pane, the copilot should greet you with the welcome message.

- Try typing a simple question like:
   - "Hello"
   - "What can you help me with?"

- Verify that the copilot responds appropriately with the greeting.

- Note that specific knowledge questions won't work yet - you'll add knowledge sources in the next challenge.

### Step 8: Save Your Progress

- Ensure all settings are saved.

- Keep the Copilot Studio browser tab open for the next challenge.

- Take note of your copilot name: **Internal Knowledge Navigator**

## Success Criteria
- Successfully signed in to Microsoft Copilot Studio
- Created a new copilot named **Internal Knowledge Navigator**
- Configured copilot with appropriate description and icon
- Verified basic greeting functionality
- Ready to proceed with knowledge base upload

## Additional Resources
- [Microsoft Copilot Studio Overview](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-what-is-copilot-studio)  
- [Create your first copilot](https://learn.microsoft.com/microsoft-copilot-studio/fundamentals-get-started)  
- [Copilot Studio best practices](https://learn.microsoft.com/microsoft-copilot-studio/guidance/best-practices)

---

Now, click **Next** to continue to **Challenge 02: Upload Department Documents**.
