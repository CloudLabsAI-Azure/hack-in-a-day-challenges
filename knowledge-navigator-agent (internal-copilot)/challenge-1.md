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

### Step 1: Verify Local Documents Folder

- In the **Lab VM**, open **File Explorer**.

- Navigate to the documents folder to verify all company documents are present:

   ```
   c:\Users\GirishR\OneDrive - Spektra Systems LLC\Documents\GitHub\hack-in-a-day-challenges\knowledge-navigator-agent (internal-copilot)\documents\
   ```

- Verify you can see multiple Contoso company documents (40+ files) including:
   - Contoso_HR_Handbook.docx
   - Contoso_Procurement_Data_With_Policies.docx
   - Contoso-Corp-IT-Governance&Compliance-Policy.docx
   - Employee-Travel-Reimbursement.xlsx
   - And many more...

- Keep this folder location accessible for uploading in Challenge 2.

### Step 2: Create SharePoint Site

- Navigate to the **Microsoft 365** portal:

   ```
   https://www.office.com
   ```

- Sign in with the provided credentials:
   - **Email/Username:** <inject key="AzureAdUserEmail"></inject>
   - **Password:** <inject key="AzureAdUserPassword"></inject>

- If prompted with **"Stay signed in?"**, click **No**.

- From the Microsoft 365 apps, select **SharePoint**.

- Click on **+ Create site** and select **Team site**.

- Configure the new site:
   - **Site name:** `contoso-documents-<inject key="DeploymentID"></inject>`
   - **Site description:** "Internal knowledge base for company policies and procedures"
   - **Privacy settings:** Set to **Public** (anyone in the organization can access)

- Click **Next** and add any additional owners if needed, then click **Finish**.

- Once the site is created, navigate to the **Documents** section.

- You can upload files now or in Challenge 2. To upload now, click **Upload** > **Files** and select all documents from:
   ```
   c:\Users\GirishR\OneDrive - Spektra Systems LLC\Documents\GitHub\hack-in-a-day-challenges\knowledge-navigator-agent (internal-copilot)\documents\
   ```

- Wait for all files to upload successfully (this may take several minutes for 40+ documents).

- **Copy the SharePoint site URL** from the browser address bar and paste it into **Notepad** for use in upcoming steps.

   Example format: `https://yourdomain.sharepoint.com/sites/contoso-documents-<inject key="DeploymentID"></inject>`

- Navigate to **Microsoft Copilot Studio**:

   ```
   https://copilotstudio.microsoft.com
   ```

- Ensure the environment is **ODL_User<inject key="DeploymentID"></inject>**.

### Step 3: Create a New Agent

- On **Copilot Studio**, select **+ Create**, and then select **+ New agent**.

- On **Start building your agent** page, select **Configure**.

- Provide the following details:
   - **Name:** `Internal Knowledge Navigator`
   - **Description:**
     ```
     This agent helps employees quickly find Contoso company policies, procedures, and guidelines across all departments including HR, IT, Procurement, Finance, Sales, and Operations. It provides accurate answers with document citations from official company documents, guides users through common processes, and can trigger helpful actions like emailing documents or creating support tickets.
     ```
   - **Instructions:**
     ```
     - Respond only to queries related to Contoso internal company policies, procedures, business operations, and department-specific guidelines.
     - Retrieve knowledge from the uploaded Contoso company documents stored in SharePoint, including HR handbooks, IT governance policies, procurement procedures, support policies, sales playbooks, business reports, and operational data.
     - When answering questions:
       - Provide clear, accurate information based strictly on official Contoso documents
       - Always cite the source document name (e.g., Contoso_HR_Handbook.docx)
       - Use professional, helpful language appropriate for internal employees
       - If information isn't in the knowledge base, direct users to the appropriate department contact
     - For common scenarios, guide users through step-by-step processes based on documented procedures
     - Offer to email policy documents or create support tickets when appropriate
     - Maintain employee privacy and confidentiality at all times
     - Focus on providing information from official Contoso documents rather than general knowledge
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

### Step 5: Test Basic Copilot Greeting

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
