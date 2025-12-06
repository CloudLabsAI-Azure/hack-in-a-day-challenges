# Challenge 04: Enable Citation Answers

## Introduction
When employees receive answers from your knowledge copilot, they need to trust the information and be able to verify it themselves. Citations show exactly which document the answer came from, building confidence and allowing employees to access the full source document for more details.

In this challenge, you'll configure your copilot to include citations with every answer, showing the document name, page number (if available), and providing links to the source documents.

## Challenge Objectives
- Enable citations in generative answers
- Configure citation display format
- Test citation functionality across all departments
- Customize citation messages and formatting
- Verify source documents are accessible via citations

## Steps to Complete

### Step 1: Access Generative AI Settings

- In **Microsoft Copilot Studio**, ensure your **Internal Knowledge Navigator** copilot is open.

- Click on **Settings** (gear icon) in the top-right corner.

- Navigate to the **Generative AI** section in the left panel.

- You'll see the configuration options for how your copilot uses AI to generate answers.

### Step 2: Enable Citation Mode

- In the Generative AI settings, look for the section about **Content moderation** or **Answer generation**.

- Find the setting: **"How should your copilot respond when it uses generative AI?"**

- Enable the following options:
   - **Include citations:** On/Enabled
   - **Allow the AI to use its own general knowledge:** Off (ensure answers only come from your documents)
   - **Content moderation:** Medium or Strict

- Look for **Citation format** or **Reference style** options:
   - **Show document names:** Enabled
   - **Show page numbers:** Enabled (if available)
   - **Make citations clickable:** Enabled

- Click **Save** to apply these changes.

### Step 3: Configure Knowledge Source Citation Settings

- Still in Settings, navigate to **Knowledge** or **Data sources** section.

- You should see your list of 12 uploaded documents.

- For each document (or select all), verify the following settings:
   - **Allow citations:** Enabled/Checked
   - **Make searchable:** Enabled
   - **Access level:** Internal users

- If available, set **Citation preference:**
   - Format: "[Document Name, Page X]"
   - Position: End of answer or inline

- Click **Save**.

### Step 4: Update Generative Answer Nodes in Topics

Now you'll update each topic to ensure citations are displayed properly.

- Go to **Topics** in the left navigation.

- Open the **HR - Leave Policy** topic.

- Find the **Create generative answers** node.

- Click to edit the node settings.

- In the generative answers configuration:
   - **Data sources:** Verify your SharePoint knowledge source or specific HR documents are selected
   - **Citations:** Enable "Show citations"
   - **Citation format:** "According to [source], ..."
   - **Link to source:** Enabled

- In the "Content" section, you can customize the prefix message:
   ```
   Based on Contoso's HR documentation:
   [AI Generated Answer with Citations]
   ```

- Click **Save** on the node.

- **Repeat this process** for the other three topics:
   - Finance - Travel Reimbursement
   - IT - Software Access
   - Procurement - Purchase Request

### Step 5: Customize Citation Message Template

- You can add a custom message after generative answers to highlight citations.

- In each topic, after the **Create generative answers** node, add:
   - **Send a message** node
   - Message: "The information above comes from our official policy documents. You can click the source links to view the full document."

- This helps users understand that clickable citations are available.

### Step 6: Configure Fallback Citations

- Navigate to **Settings** Ã¢â€ â€™ **System** Ã¢â€ â€™ **Conversational boosting**

- This is the fallback topic that triggers when no specific topic matches.

- Edit the **Conversational boosting** system topic.

- Find or add a **Create generative answers** node.

- Configure it to:
   - Search across ALL knowledge sources
   - Always show citations
   - Provide confidence scores if available

- Add a message:
   ```
   I found this information in our knowledge base:
   [Generative Answer with Citations]
   
   Tip: Click on the document references to see the full source.
   ```

- Save the topic.

### Step 7: Test Citation Display - HR Department

- Click **Test your copilot**.

- Ask: **"What's in the Contoso HR Handbook?"**

- Verify the response includes:
   - The actual answer
   - A citation at the end, like: `[Contoso_HR_Handbook.docx]` or similar
   - The citation should be clickable/tappable

- Try another: **"What are the onboarding procedures?"**

- Verify citations appear correctly referencing Contoso_HR_Onboarding_Checklist.docx.

### Step 8: Test Citation Display - Finance/Travel Department

- In the test chat, ask: **"How does travel reimbursement work at Contoso?"**

- Check that the response cites the Employee-Travel-Reimbursement.xlsx document.

- Ask: **"What's the process for expense reimbursement?"**

- Verify it cites Finance_Travel_Reimbursement.pdf.

- Ensure multiple citations appear if the answer draws from multiple sources.

### Step 9: Test Citation Display - IT Department

- Ask: **"What are the IT governance policies?"**

- Verify the response cites Contoso-Corp-IT-Governance&Compliance-Policy.docx.

- Ask: **"What's the SLA for support?"**

- Check for citations from Contos_Corp_SLA.docx.

- Test if clicking a citation opens or provides a way to access the document.

### Step 10: Test Citation Display - Procurement Department

- Ask: **"What's the procurement process at Contoso?"**

- Verify citations from Contoso_Procurement_Data_With_Policies.docx appear.

- Ask: **"How does contract management work?"**

- Check for citations from Procurement_Contracts_Repository_List.xlsx.

- Confirm citations are clear and helpful.

### Step 11: Test Multi-Source Citations

- Ask a question that might span multiple documents:
   - "What do I need to know about Contoso's business operations?"

- Verify the copilot:
   - Provides a comprehensive answer
   - May cite MULTIPLE documents (Contoso_Corp_Business_Performance_Report.docx, Contoso_Sales_Playbook.docx, etc.)
   - Clearly attributes which information came from which source

- Test another cross-department question:
   - "I'm a new employee, what policies do I need to read?"

- Check that it cites documents from HR onboarding (Contoso_HR_Onboarding_Checklist.docx) and potentially IT governance.

### Step 12: Verify Citation Accessibility

- When citations appear in the test chat, try clicking on them.

- Depending on your setup, citations should:
   - Open the source document (if available)
   - Show a preview of the relevant section
   - Provide a way to download or access the full document

- If citations don't open documents yet, verify the file storage location and permissions.

- Ensure employees will have access to the cited documents in production.

### Step 13: Refine Citation Formatting

Based on testing, you may want to adjust:

- **Citation style:**
   - Too verbose: "[According to the Contoso HR Handbook document, page 3, section 2.1...]"
   - Better: "[Contoso_HR_Handbook.docx]"

- **Citation placement:**
   - End of answer (less intrusive)
   - Inline (more precise but can interrupt reading)

- **Multiple citation handling:**
   - Numbered: [1], [2], [3] with list at end
   - Inline: [Doc1], [Doc2] within text

- Make adjustments in Settings Ã¢â€ â€™ Generative AI Ã¢â€ â€™ Citation format.

- Save and re-test.

### Step 14: Add Citation Help Topic

- Create a quick topic to explain citations to users.

- **New topic:** "Understanding Citations"

- **Trigger phrases:**
   - "What are citations"
   - "How do I see sources"
   - "Where does this information come from"

- **Message node:**
   ```
   **About Citations and Sources**
   
   When I provide answers, I always include citations that show exactly where the information came from. 
   
   Citations appear like this: [Document_Name.pdf, Page X]
   
   You can click on citations to:
   - View the original document
   - See the full context
   - Verify the information
   
   This helps you trust the information and access more details when needed!
   
   All information comes from official company policy documents maintained by HR, Finance, IT, and Procurement departments.
   ```

- Save the topic.

## Success Criteria
- Citations are enabled in generative AI settings
- SharePoint knowledge source is configured to provide citations
- Citations appear in answers from all department topics
- Citations show document name (and page number where available)
- Citations are clickable/accessible to users
- Multi-source answers show multiple citations correctly
- Citation format is clear, concise, and professional
- Test queries consistently show proper citations from Contoso documents
- Created a help topic explaining citations to users

## Additional Resources
- [Configure generative answers](https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-node)  
- [Generative AI settings](https://learn.microsoft.com/microsoft-copilot-studio/nlu-gpt-quickstart)  
- [Knowledge source management](https://learn.microsoft.com/microsoft-copilot-studio/knowledge-manage-sources)  
- [Citation best practices](https://learn.microsoft.com/microsoft-copilot-studio/guidance/best-practices)

---

Now, click **Next** to continue to **Challenge 05: Add Trigger Actions**.
