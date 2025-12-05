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

1. In **Microsoft Copilot Studio**, ensure your **Internal Knowledge Navigator** copilot is open.

2. Click on **Settings** (gear icon) in the top-right corner.

3. Navigate to the **Generative AI** section in the left panel.

4. You'll see the configuration options for how your copilot uses AI to generate answers.

### Step 2: Enable Citation Mode

1. In the Generative AI settings, look for the section about **Content moderation** or **Answer generation**.

2. Find the setting: **"How should your copilot respond when it uses generative AI?"**

3. Enable the following options:
   - **Include citations:** On/Enabled
   - **Allow the AI to use its own general knowledge:** Off (ensure answers only come from your documents)
   - **Content moderation:** Medium or Strict

4. Look for **Citation format** or **Reference style** options:
   - **Show document names:** Enabled
   - **Show page numbers:** Enabled (if available)
   - **Make citations clickable:** Enabled

5. Click **Save** to apply these changes.

### Step 3: Configure Knowledge Source Citation Settings

1. Still in Settings, navigate to **Knowledge** or **Data sources** section.

2. You should see your list of 12 uploaded documents.

3. For each document (or select all), verify the following settings:
   - **Allow citations:** Enabled/Checked
   - **Make searchable:** Enabled
   - **Access level:** Internal users

4. If available, set **Citation preference:**
   - Format: "[Document Name, Page X]"
   - Position: End of answer or inline

5. Click **Save**.

### Step 4: Update Generative Answer Nodes in Topics

Now you'll update each topic to ensure citations are displayed properly.

1. Go to **Topics** in the left navigation.

2. Open the **HR - Leave Policy** topic.

3. Find the **Create generative answers** node.

4. Click to edit the node settings.

5. In the generative answers configuration:
   - **Data sources:** Verify HR_Leave_Policy.pdf is selected
   - **Citations:** Enable "Show citations"
   - **Citation format:** "According to [source], ..."
   - **Link to source:** Enabled

6. In the "Content" section, you can customize the prefix message:
   ```
   Based on our HR Leave Policy documentation:
   [AI Generated Answer with Citations]
   ```

7. Click **Save** on the node.

8. **Repeat this process** for the other three topics:
   - Finance - Travel Reimbursement
   - IT - Software Access
   - Procurement - Purchase Request

### Step 5: Customize Citation Message Template

1. You can add a custom message after generative answers to highlight citations.

2. In each topic, after the **Create generative answers** node, add:
   - **Send a message** node
   - Message: "The information above comes from our official policy documents. You can click the source links to view the full document."

3. This helps users understand that clickable citations are available.

### Step 6: Configure Fallback Citations

1. Navigate to **Settings** → **System** → **Conversational boosting**

2. This is the fallback topic that triggers when no specific topic matches.

3. Edit the **Conversational boosting** system topic.

4. Find or add a **Create generative answers** node.

5. Configure it to:
   - Search across ALL knowledge sources
   - Always show citations
   - Provide confidence scores if available

6. Add a message:
   ```
   I found this information in our knowledge base:
   [Generative Answer with Citations]
   
   Tip: Click on the document references to see the full source.
   ```

7. Save the topic.

### Step 7: Test Citation Display - HR Department

1. Click **Test your copilot**.

2. Ask: **"How many days of annual leave do I get?"**

3. Verify the response includes:
   - The actual answer
   - A citation at the end, like: `[HR_Leave_Policy.pdf, Page 2]`
   - The citation should be clickable/tappable

4. Try another: **"What's the sick leave policy?"**

5. Verify citations appear correctly.

### Step 8: Test Citation Display - Finance Department

1. In the test chat, ask: **"What expenses can I claim?"**

2. Check that the response cites the Finance_Expense_Policy.pdf document.

3. Ask: **"How do I submit travel receipts?"**

4. Verify it cites Finance_Travel_Reimbursement.pdf.

5. Ensure multiple citations appear if the answer draws from multiple sources.

### Step 9: Test Citation Display - IT Department

1. Ask: **"How do I reset my password?"**

2. Verify the response cites IT_Security_Policy.pdf or IT_Support_Guide.pdf.

3. Ask: **"What software can I request?"**

4. Check for citations from IT_Software_Access.pdf.

5. Test if clicking a citation opens or provides a way to access the document.

### Step 10: Test Citation Display - Procurement Department

1. Ask: **"What's the purchase approval process?"**

2. Verify citations from Procurement_Purchase_Request.pdf appear.

3. Ask: **"How do I add a new vendor?"**

4. Check for citations from Procurement_Vendor_Management.pdf.

5. Confirm citations are clear and helpful.

### Step 11: Test Multi-Source Citations

1. Ask a question that might span multiple documents:
   - "What do I need to know about business travel and expenses?"

2. Verify the copilot:
   - Provides a comprehensive answer
   - Cites MULTIPLE documents (Finance_Expense_Policy.pdf AND Finance_Travel_Reimbursement.pdf)
   - Clearly attributes which information came from which source

3. Test another cross-department question:
   - "I'm a new employee, what policies do I need to read?"

4. Check that it cites documents from HR onboarding and potentially IT security.

### Step 12: Verify Citation Accessibility

1. When citations appear in the test chat, try clicking on them.

2. Depending on your setup, citations should:
   - Open the source document (if available)
   - Show a preview of the relevant section
   - Provide a way to download or access the full document

3. If citations don't open documents yet, verify the file storage location and permissions.

4. Ensure employees will have access to the cited documents in production.

### Step 13: Refine Citation Formatting

Based on testing, you may want to adjust:

1. **Citation style:**
   - Too verbose: "[According to the HR Leave Policy document, page 3, section 2.1...]"
   - Better: "[HR_Leave_Policy.pdf, p.3]"

2. **Citation placement:**
   - End of answer (less intrusive)
   - Inline (more precise but can interrupt reading)

3. **Multiple citation handling:**
   - Numbered: [1], [2], [3] with list at end
   - Inline: [Doc1], [Doc2] within text

4. Make adjustments in Settings → Generative AI → Citation format.

5. Save and re-test.

### Step 14: Add Citation Help Topic

1. Create a quick topic to explain citations to users.

2. **New topic:** "Understanding Citations"

3. **Trigger phrases:**
   - "What are citations"
   - "How do I see sources"
   - "Where does this information come from"

4. **Message node:**
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

5. Save the topic.

## Success Criteria
- Citations are enabled in generative AI settings
- All 12 knowledge sources are configured to provide citations
- Citations appear in answers from all 4 department topics
- Citations show document name and page number (where available)
- Citations are clickable/accessible to users
- Multi-source answers show multiple citations correctly
- Citation format is clear, concise, and professional
- Test queries consistently show proper citations
- Created a help topic explaining citations to users

## Additional Resources
- [Configure generative answers](https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-node)  
- [Generative AI settings](https://learn.microsoft.com/microsoft-copilot-studio/nlu-gpt-quickstart)  
- [Knowledge source management](https://learn.microsoft.com/microsoft-copilot-studio/knowledge-manage-sources)  
- [Citation best practices](https://learn.microsoft.com/microsoft-copilot-studio/guidance/best-practices)

---

Now, click **Next** to continue to **Challenge 05: Add Trigger Actions**.
