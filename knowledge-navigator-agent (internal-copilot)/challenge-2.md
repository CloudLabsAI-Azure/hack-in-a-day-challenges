# Challenge 02: Connect SharePoint Knowledge Source

## Introduction
Now that you've created your Internal Knowledge Navigator copilot and uploaded all Contoso company documents to SharePoint in Challenge 1, it's time to connect that SharePoint site to your copilot as a knowledge source. This will enable your copilot to search through all 40+ company documents and provide accurate answers to employee questions.

In this challenge, you'll connect the SharePoint site to Copilot Studio, verify the knowledge source is properly indexed, and test basic knowledge retrieval to ensure your copilot can answer questions using the Contoso documents.

## Challenge Objectives
- Connect the SharePoint site as a knowledge source in Copilot Studio
- Verify all documents are successfully indexed
- Configure knowledge source settings
- Test basic knowledge retrieval across different document types
- Ensure the copilot responds using Contoso company documents

## Prerequisites

Before starting this challenge, ensure you have:
- Created the **Internal Knowledge Navigator** agent in Challenge 1
- Created the SharePoint site `contoso-documents-<inject key="DeploymentID"></inject>` in Challenge 1
- Uploaded all 40+ Contoso documents to the SharePoint site in Challenge 1
- Saved the SharePoint site URL

## Steps to Complete

### Step 1: Add SharePoint Knowledge Source

- Open **Microsoft Copilot Studio** in your browser:

   ```
   https://copilotstudio.microsoft.com
   ```

- Ensure you're in the **ODL_User<inject key="DeploymentID"></inject>** environment (check the environment selector in the top-right).

- Select your **Internal Knowledge Navigator** agent from the agents list.

- On the **Start building your agent** page, scroll down and select **+ Add** to add knowledge sources.

- Select **SharePoint** from the **Add Knowledge** window.

- Enter the **SharePoint site URL** that you copied in Challenge 1:
   ```
   https://yourdomain.sharepoint.com/sites/contoso-documents-<inject key="DeploymentID"></inject>
   ```

   > **Tip:** If you didn't save the URL, go back to your SharePoint site in another tab and copy it from the address bar.

- Select **Add**.

   > **Note:** If the site link shows **"This item was not found in your SharePoint or OneDrive files"**, this may occur due to temporary indexing delays. Select **Add anyway** to continue.

- Select **Add to agent** to add the SharePoint knowledge source.

- Wait for the confirmation message that the SharePoint site has been added.

   > **What's happening:** Copilot Studio is now connecting to your SharePoint site and will automatically index all 40+ documents you uploaded in Challenge 1.

### Step 2: Verify Knowledge Source Connection

- After adding SharePoint, navigate to **Knowledge** in the left navigation pane.

- You should see the SharePoint site listed as a knowledge source with the name: `contoso-documents-<inject key="DeploymentID"></inject>`

- The status should show as **Processing** or **Syncing** initially.

- Wait for the status to change to **Active** or **Ready** (this may take 3-10 minutes for 40+ documents).

   > **Note:** The SharePoint connector will automatically index all documents in the Documents library. You don't need to upload individual files.

- If the status shows **Failed** or **Error**, try the following:
   - Verify the SharePoint site URL is correct
   - Check that you have access to the SharePoint site
   - Remove and re-add the knowledge source

### Step 3: Verify Knowledge Source Indexing

- In the **Knowledge** section, click on your SharePoint knowledge source to view details.

- You should see information about:
   - **Source type:** SharePoint
   - **Status:** Active (or Ready)
   - **Documents indexed:** Number of documents found and indexed
   - **Last synced:** Timestamp of last indexing

- Verify that the document count is approximately 40+ documents.

   > **Note:** The SharePoint connector automatically indexes all files in the Documents library. You'll see a single SharePoint entry, not individual files listed.

- If indexing is still in progress, wait a few more minutes and refresh the page.

### Step 4: Configure Generative AI Settings

- Click on **Settings** (gear icon) in the top-right corner.

- Navigate to the **Generative AI** section in the left panel.

- Under **Knowledge sources** or **Data sources**, verify that your SharePoint knowledge source appears and is enabled (checkbox should be checked).

- Configure the following options:

   - **Content moderation:** Set to **Medium** (balances safety and response flexibility)
   
   - **Allow the AI to use its own general knowledge:** Toggle **Off** 
     > **Important:** This ensures responses come ONLY from your Contoso documents, not from the AI's general knowledge.

- Review other settings:
   - **Response length:** Medium (recommended)
   - **Response format:** Professional

- Click **Save** to apply the changes.

### Step 5: Test Basic Knowledge Retrieval

- Click the **Test your copilot** button in the top-right corner to open the test pane.

- Wait for the copilot to load and display the welcome message.

- Try the following questions to test different Contoso documents:

   **HR Questions:**
   - Type: `"What's in the Contoso HR handbook?"`
   - Expected: Information from Contoso_HR_Handbook.docx
   
   - Type: `"What are the onboarding procedures for new employees?"`
   - Expected: Information from Contoso_HR_Onboarding_Checklist.docx
   
   - Type: `"Tell me about employee travel reimbursement"`
   - Expected: Information from Employee-Travel-Reimbursement.xlsx

   **IT & Governance Questions:**
   - Type: `"What are Contoso's IT governance policies?"`
   - Expected: Information from Contoso-Corp-IT-Governance&Compliance-Policy.docx
   
   - Type: `"What is the SLA for support?"`
   - Expected: Information from Contos_Corp_SLA.docx
   
   - Type: `"Tell me about the data governance framework"`
   - Expected: Information from Data_Governance_Framework.docx

   **Procurement Questions:**
   - Type: `"What are Contoso's procurement policies?"`
   - Expected: Information from Contoso_Procurement_Data_With_Policies.docx
   
   - Type: `"How does contract management work?"`
   - Expected: Information from Procurement_Contracts_Repository_List.xlsx

   **Support & Operations Questions:**
   - Type: `"What's the support policy?"`
   - Expected: Information from Contoso_Support_Policy.docx
   
   - Type: `"Tell me about the sales playbook"`
   - Expected: Information from Contoso_Sales_Playbook.docx

- **Verify each response:**
   - Contains specific information from Contoso documents (not generic answers)
   - Is relevant and accurate to the question asked
   - References company-specific information

> **Troubleshooting:** If responses say "I don't have that information" or are too generic:
> - Wait 5-10 more minutes for full indexing to complete
> - Refresh the test pane
> - Check that the SharePoint knowledge source shows **Active** status
> - Verify "Allow AI to use its own general knowledge" is turned **Off**

### Step 6: Test Multi-Department Knowledge

- Test that the copilot can answer questions across different departments in a single conversation:

   1. Ask: `"What's the HR onboarding process?"`
   2. Then ask: `"What about the IT governance policies?"`
   3. Then ask: `"How do procurement contracts work?"`

- Verify that the copilot:
   - Maintains context throughout the conversation
   - Answers each question accurately using the appropriate Contoso document
   - Doesn't confuse information between departments

### Step 7: Review Response Quality

- When reviewing all test responses, verify that they:
   - **Are accurate:** Information matches what's in the actual documents
   - **Are specific:** Contains company-specific details, not generic information
   - **Are relevant:** Directly answers the question asked
   - **Are clear:** Easy to understand and well-formatted

- Take note of any questions that don't work well - you may need to wait longer for indexing.

   > **Note:** In Challenge 4, you'll enable citations so users can see exactly which document each answer came from. For now, focus on verifying that the copilot is finding and using the Contoso documents.

## Success Criteria
- SharePoint knowledge source is connected to Copilot Studio
- SharePoint knowledge source shows **Active** or **Ready** status
- Knowledge source has indexed 40+ Contoso documents
- Generative AI settings configured (general knowledge turned OFF)
- Test queries return relevant, specific responses from Contoso documents
- Copilot can answer questions across all departments (HR, IT, Procurement, Finance, Support, Sales)
- Responses contain company-specific information, not generic answers

## Additional Resources
- [Add knowledge sources to your copilot](https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-conversations)  
- [Generative answers with uploaded files](https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-node)  
- [Manage knowledge sources](https://learn.microsoft.com/microsoft-copilot-studio/knowledge-manage-sources)

---

Now, click **Next** to continue to **Challenge 03: Design Department Topics**.
