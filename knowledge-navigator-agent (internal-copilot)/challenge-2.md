# Challenge 02: Upload Department Documents

## Introduction
Now that you've created your Internal Knowledge Navigator copilot, it's time to add the knowledge base that will power its responses. In this challenge, you'll upload policy and procedure documents from four key departments: HR, Finance, IT, and Procurement.

By organizing knowledge sources by department, your copilot will be able to provide accurate, cited answers to employee questions across all major business functions.

## Challenge Objectives
- Access and review the department knowledge base documents
- Upload HR policies and procedures to the copilot
- Upload Finance policies and procedures
- Upload IT support and access procedures
- Upload Procurement request procedures
- Verify all knowledge sources are successfully indexed

## Accessing the Datasets

The datasets required for this challenge are provided in the attached folder:

```
c:\Users\GirishR\OneDrive - Spektra Systems LLC\Documents\GitHub\hack-in-a-day-challenges\knowledge-navigator-agent (internal-copilot)\datasets\
```

Alternatively, you can download them here - [Datasets](https://github.com/CloudLabsAI-Azure/hack-in-a-day-challenges/archive/refs/heads/knowledge-navigator-datasets.zip)

## Steps to Complete

### Step 1: Review Available Knowledge Documents

1. Open **File Explorer** in your lab VM.

2. Navigate to the datasets folder:
   ```
   c:\Users\GirishR\OneDrive - Spektra Systems LLC\Documents\GitHub\hack-in-a-day-challenges\knowledge-navigator-agent (internal-copilot)\datasets\
   ```

3. Review the available department documents:
   
   **HR Department (Human Resources)**
   - `HR_Leave_Policy.pdf` - Annual leave, sick leave, and time-off procedures
   - `HR_Onboarding_Guide.pdf` - New employee onboarding checklist and procedures
   - `HR_Benefits_Guide.pdf` - Health insurance, retirement, and benefits information
   
   **Finance Department**
   - `Finance_Expense_Policy.pdf` - Business expense guidelines and approval limits
   - `Finance_Travel_Reimbursement.pdf` - Travel booking and reimbursement procedures
   - `Finance_Budget_Request.pdf` - Department budget request process
   
   **IT Department**
   - `IT_Software_Access.pdf` - Software installation and access request procedures
   - `IT_Support_Guide.pdf` - Common IT issues and troubleshooting steps
   - `IT_Security_Policy.pdf` - Password policies and security best practices
   
   **Procurement Department**
   - `Procurement_Purchase_Request.pdf` - Purchase order and approval workflow
   - `Procurement_Vendor_Management.pdf` - Vendor onboarding and management procedures
   - `Procurement_Contract_Process.pdf` - Contract review and signature process

### Step 2: Add SharePoint Knowledge Source

1. Return to the **Microsoft Copilot Studio** browser tab with your **Internal Knowledge Navigator** agent open.

2. Scroll down on the **Start building your agent** page and select **+ Add (1)** to add knowledge sources.

3. Select **SharePoint** from the **Add Knowledge** window.

4. Enter the **SharePoint site KnowledgeHub link (1)** that you copied in Challenge 1, then select **Add (2)**.

   > **Note:** If the site link shows **"This item was not found in your SharePoint or OneDrive files"**, this may occur due to temporary indexing delays. Select **Add anyway** to continue.

5. Select **Add to agent** to add the SharePoint knowledge source.

6. The SharePoint site will now be indexed for knowledge retrieval.

### Step 3: Access Knowledge Section for Document Upload

1. After adding SharePoint, navigate to **Knowledge** in the left navigation pane.

2. You should see the SharePoint site listed as a knowledge source.

3. Now you'll add individual department documents as additional knowledge sources.

### Step 3: Upload HR Department Documents

1. Click **+ Add knowledge** or **+ Upload files** button.

2. Select **Upload files** if prompted to choose a source type.

3. Click **Browse** or drag and drop files.

4. Navigate to the datasets folder and select all three HR documents:
   - `HR_Leave_Policy.pdf`
   - `HR_Onboarding_Guide.pdf`
   - `HR_Benefits_Guide.pdf`

5. Click **Open** to upload.

6. Wait for the files to upload and begin processing (you'll see a progress indicator).

7. Once uploaded, you should see these documents listed with a status of **Processing** or **Indexing**.

### Step 4: Upload Finance Department Documents

1. Click **+ Add knowledge** or **+ Upload files** again.

2. Navigate to the datasets folder and select all three Finance documents:
   - `Finance_Expense_Policy.pdf`
   - `Finance_Travel_Reimbursement.pdf`
   - `Finance_Budget_Request.pdf`

3. Click **Open** to upload.

4. Wait for the upload to complete.

### Step 5: Upload IT Department Documents

1. Click **+ Add knowledge** or **+ Upload files** again.

2. Navigate to the datasets folder and select all three IT documents:
   - `IT_Software_Access.pdf`
   - `IT_Support_Guide.pdf`
   - `IT_Security_Policy.pdf`

3. Click **Open** to upload.

4. Wait for the upload to complete.

### Step 6: Upload Procurement Department Documents

1. Click **+ Add knowledge** or **+ Upload files** again.

2. Navigate to the datasets folder and select all three Procurement documents:
   - `Procurement_Purchase_Request.pdf`
   - `Procurement_Vendor_Management.pdf`
   - `Procurement_Contract_Process.pdf`

3. Click **Open** to upload.

4. Wait for the upload to complete.

### Step 7: Verify Knowledge Source Indexing

1. On the Knowledge sources page, verify that all 12 documents are listed.

2. Wait for all documents to show a status of **Active** or **Ready** (this may take 2-5 minutes total).

   > **Note:** If any document shows **Failed** status, try re-uploading that specific file.

3. The documents should be organized or tagged by department for easier management.

### Step 8: Configure Knowledge Source Settings

1. Click on **Settings** (gear icon) in the top navigation.

2. Navigate to **Generative AI** section.

3. Under **Data sources**, verify that all 12 uploaded documents are listed and enabled (checkboxes should be checked).

4. Set the following options:
   - **Content moderation:** Medium
   - **Allow the AI to use its own general knowledge:** Off (to ensure responses come only from uploaded documents)

5. Click **Save**.

### Step 9: Test Basic Knowledge Retrieval

1. Click **Test your copilot** button in the top-right corner.

2. Try the following department-specific questions:

   **HR Questions:**
   - "How many days of annual leave do I get?"
   - "What do I need to do on my first day at work?"
   - "What health benefits are available?"

   **Finance Questions:**
   - "What's the expense approval limit?"
   - "How do I request travel reimbursement?"
   - "What's the budget request process?"

   **IT Questions:**
   - "How do I request software access?"
   - "My laptop is running slow, what should I do?"
   - "What's the password policy?"

   **Procurement Questions:**
   - "How do I submit a purchase request?"
   - "What's the vendor onboarding process?"
   - "How do I get a contract reviewed?"

3. Verify that the copilot responds with relevant information from the uploaded documents.

4. If responses are too generic or say "I don't have information," wait a bit longer for indexing to complete.

### Step 10: Review Response Quality

1. When testing, pay attention to whether responses:
   - Are accurate and relevant to the question
   - Come from the correct department's documents
   - Are clear and easy to understand

2. Note: In Challenge 4, you'll enable citations so users can see exactly which document the answer came from.

## Success Criteria
- Successfully uploaded all 12 department documents (3 per department)
- All knowledge sources show **Active** or **Ready** status
- Verified documents are indexed and enabled in settings
- Test queries return relevant responses from the knowledge base
- Copilot can answer questions across all four departments (HR, Finance, IT, Procurement)

## Additional Resources
- [Add knowledge sources to your copilot](https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-conversations)  
- [Generative answers with uploaded files](https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-node)  
- [Manage knowledge sources](https://learn.microsoft.com/microsoft-copilot-studio/knowledge-manage-sources)

---

Now, click **Next** to continue to **Challenge 03: Design Department Topics**.
