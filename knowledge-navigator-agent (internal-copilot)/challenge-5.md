# Challenge 05: Add Trigger Actions

## Introduction
Your Knowledge Navigator copilot can now answer questions with proper citations. But what if employees want to receive a policy document via email, create an IT support ticket, or send a conversation summary to their manager? In this final challenge, you'll add automated actions using Power Automate to make your copilot truly helpful.

You'll integrate three key actions: emailing documents, creating support tickets, and sending conversation summaries to Teams or email.

## Challenge Objectives
- Create a Power Automate flow to email policy documents
- Create a Power Automate flow to create IT support tickets
- Create a Power Automate flow to send conversation summaries
- Integrate flows with copilot topics
- Test all automated actions end-to-end

## Steps to Complete

### Step 1: Understand Power Automate Integration

1. In **Microsoft Copilot Studio**, click on your **Internal Knowledge Navigator** copilot.

2. In the left navigation, look for **Actions** or **Flows** (this may be under Topics → Call an action).

3. Power Automate flows can be:
   - **Triggered by the copilot** (with parameters from the conversation)
   - **Return values** back to the copilot
   - **Perform external actions** (send email, create ticket, post to Teams, etc.)

4. You'll create three flows in this challenge.

### Step 2: Connect Knowledge Request to SharePoint via Power Automate

Now we'll create a flow to save knowledge requests to SharePoint and track their status.

1. Go back to the **Knowledge Request Submission** topic you created in Challenge 3.

2. Select **Add node (1)** after the Adaptive card node, choose **Add a tool (2)**, and then select **New agent flow (3)**.

3. Select the **When an agent calls the flow (1)** action and click on **+ Add input (2)** under the **Parameters** section.

   > **Note:** If the side panel does not open automatically, click the **panel icon** on the top-right to open it.

4. Add the following input parameters one by one (click **+ Add an input** between each):

   | Parameter Name | Type |
   |----------------|------|
   | Department | Text |
   | RequestTitle | Text |
   | QuestionDetails | Text |
   | Urgency | Text |
   | EmployeeEmail | Text |

5. Select the **+ (1)** button to add an action, type **SharePoint (2)** in the search box, and select **Create item (3)**.

   > **Note:** If the side panel does not open automatically, click the **panel icon** for a clearer view.

6. Select **Sign in** and authenticate with **<inject key="AzureAdUserEmail"></inject>**.

7. If prompted, select **Allow access**.

8. On the **Create item** action, configure the following parameters:
   - **Site Address:** Select **KnowledgeHub<inject key="DeploymentID" enableCopy="false"/>** SharePoint site **(1)**
   - **List name:** Select **Knowledge_Requests_List (2)**
   - **Title:** Enter **Knowledge Request (3)**
   - Click **Show all (4)**

9. Under **Advanced parameters**, map the SharePoint list columns to the flow input parameters:
   - **Title** → {RequestTitle}
   - **Department** → {Department}
   - **Question Details** → {QuestionDetails}
   - **Urgency** → {Urgency}
   - **Employee Email** → {EmployeeEmail}
   - **Status** → "Open" (type manually)

   Use the **dynamic content** icon to select variables from Input parameters.

### Step 3: Add Conditional Logic Based on Urgency

1. Select the **+ (1)** button under the Create item action, type **Condition (2)** in the search box, and select **Condition (3)** from the control section.

2. On the Condition side screen, configure:
   - Choose a value → Select **Urgency** from input parameters **(1)**
   - Select **is equal to (2)**
   - Enter **High (3)**

3. Under the **True** branch (High urgency):
   - Select **+ (1)**, search for **Send an email (2)**, and select **Send an email (V2) (3)** from Office 365 Outlook

4. Configure the email action:
   - **To:** Your IT support team email (or use a Teams notification)
   - **Subject:** "URGENT: Knowledge Request from {EmployeeEmail}"
   - **Body:**
     ```
     A high-priority knowledge request has been submitted:
     
     Department: {Department}
     Title: {RequestTitle}
     Details: {QuestionDetails}
     From: {EmployeeEmail}
     
     Please respond as soon as possible.
     ```

5. Under the **False** branch (Medium/Low urgency):
   - No immediate action needed - requests will be reviewed in normal queue

### Step 4: Return Response to Agent

1. After the Condition (outside both True/False branches), select **+** and add **Respond to agent** action.

2. Add output parameters:
   - **RequestCreated** (boolean) → True
   - **RequestID** (text) → Use SharePoint item ID
   - **ConfirmationMessage** (text) → "Your knowledge request has been submitted successfully"

3. Select **Publish** to save the flow.

4. Select **Go back to the agent**.

### Step 5: Map Flow Variables in Topic

1. In the **Knowledge Request Submission** topic, find the Power Automate action node.

2. Map each input parameter by clicking **ellipsis (...) (1)** and selecting the corresponding adaptive card variable **(2)**.

3. After the action node, add a **Send a message (1)** node **(2)**:

   ```
   Your knowledge request has been submitted successfully!
   
   Request ID: {RequestID}
   Department: {Department}
   
   We'll respond based on the urgency level you specified. You'll receive updates via email at {EmployeeEmail}.
   ```

4. Select **Save**.

### Step 6: Create Flow 2 - Email Policy Document

Now let's create a simpler flow for emailing policy documents:

1. From any topic (e.g., Finance - Travel Reimbursement), add a node asking if the user wants to receive the policy document via email.

2. Add a **Call an action** node → **New agent flow**.

3. Name the flow: **Email Policy Document**

4. **Trigger:** When an agent calls the flow

5. Add **Input parameters**:
   | Parameter Name | Type |
   |----------------|------|
   | RecipientEmail | Text |
   | DocumentName | Text |
   | DepartmentName | Text |

8. **Action 1: Compose Document Message**
   - Add **Compose** action
   - Inputs:
     ```
     Hello,

     As requested, here is the {DocumentName} document from the {DepartmentName} department.

     You can access this document through our internal knowledge portal or SharePoint.

     Document: {DocumentName}
     Department: {DepartmentName}

     If you have any questions, please reach out to your department representative.

     Best regards,
     Internal Knowledge Navigator
     ```

9. **Action 2: Send Email**
   - Add **Office 365 Outlook** → **Send an email (V2)** action
   - **To:** {RecipientEmail}
   - **Subject:** Your Requested Policy Document - {DocumentName}
   - **Body:** {Compose output from previous step}
   - **Importance:** Normal

10. **Action 3: Return Response to Copilot**
    - Add **Respond to Power Virtual Agents** action
    - Add output parameter:
      - **EmailSent** (boolean) - True
      - **ConfirmationMessage** (text) - "Email sent successfully to {RecipientEmail}"

11. **Save** the flow with the name: **Email Policy Document**

12. Test the flow by clicking **Test** → **Manually** → Run with sample data.

### Step 3: Integrate Email Flow with Copilot Topic

1. Return to **Copilot Studio**.

2. Open the **Finance - Travel Reimbursement** topic (or any topic where you want to offer document email).

3. Find the node where you asked: "Would you like me to send you the policy document?"

4. After the Yes response, add:
   - **Call an action** node
   - Select **Email Policy Document** flow

5. Map the input parameters:
   - **RecipientEmail:** Use variable `User.Email` or ask the user for their email
   - **DocumentName:** "Travel Reimbursement Policy"
   - **DepartmentName:** "Finance"

6. After the action completes, add:
   - **Send a message** node
   - Message: "{EmailSent.ConfirmationMessage} - Check your inbox!"

7. **Save** the topic.

8. **Test** in the copilot:
   - Trigger the Finance Travel Reimbursement topic
   - Say "Yes" when asked if you want the document emailed
   - Verify the flow executes and you receive an email

### Step 4: Create Flow 2 - Create IT Support Ticket

1. In **Power Automate**, create a new flow: **Create IT Support Ticket**

2. **Trigger:** When Copilot Studio calls a flow

3. Add **Input parameters**:
   - **EmployeeName** (text)
   - **EmployeeEmail** (text)
   - **IssueType** (text) - e.g., "Software Access"
   - **IssueDescription** (text)
   - **Priority** (text) - Low, Medium, High

4. **Action 1: Create Ticket Data**
   - Add **Compose** action
   - Create JSON for the ticket:
     ```json
     {
       "requester": "{EmployeeEmail}",
       "subject": "{IssueType} - Request from {EmployeeName}",
       "description": "{IssueDescription}",
       "priority": "{Priority}",
       "status": "Open",
       "category": "IT Support"
     }
     ```

5. **Action 2: Send to Ticketing System**
   
   **Option A: If you have Freshdesk from earlier challenges:**
   - Add **HTTP** action
   - Method: POST
   - URI: `https://your-domain.freshdesk.com/api/v2/tickets`
   - Headers: 
     - Authorization: Basic {YourAPIKey}
     - Content-Type: application/json
   - Body: {Compose output}

   **Option B: Send to Teams instead:**
   - Add **Microsoft Teams** → **Post message in a chat or channel**
   - Team: Select your team
   - Channel: IT Support channel
   - Message:
     ```
     **New IT Support Ticket**
     
     **From:** {EmployeeName} ({EmployeeEmail})
     **Issue:** {IssueType}
     **Description:** {IssueDescription}
     **Priority:** {Priority}
     
     Please assign and respond to this request.
     ```

6. **Action 3: Return Response**
   - Add **Respond to Copilot Studio** action
   - Output parameters:
     - **TicketCreated** (boolean) - True
     - **TicketID** (text) - Generate or use "TKT-" + utcNow()
     - **ConfirmationMessage** (text) - "Your IT support ticket {TicketID} has been created"

7. **Save** the flow.

8. Test the flow manually.

### Step 5: Integrate Ticket Creation with IT Topic

1. Return to **Copilot Studio**.

2. Open the **IT - Software Access** topic.

3. Find where you asked: "Would you like me to help you create a ticket now?"

4. After the Yes response:
   
   **Node 1: Get Employee Details**
   - If not already captured, use `User.DisplayName` and `User.Email`
   - Or ask: "Please confirm your email address for the ticket"

   **Node 2: Confirm Details**
   - **Send message:** "I'll create a ticket for {SoftwareName} access request."

   **Node 3: Call Action**
   - Add **Call an action** node
   - Select **Create IT Support Ticket** flow
   - Map parameters:
     - EmployeeName: {User.DisplayName}
     - EmployeeEmail: {User.Email}
     - IssueType: "Software Access Request"
     - IssueDescription: "Request for {SoftwareName} - {SoftwareType}"
     - Priority: "Medium"

   **Node 4: Confirmation**
   - **Send message:** "{TicketCreated.ConfirmationMessage}"
   - Add: "You'll receive email updates as your request is processed. Typical response time is 1-2 business days."

5. **Save** the topic.

6. **Test** the ticket creation flow end-to-end.

### Step 6: Create Flow 3 - Send Conversation Summary

1. In **Power Automate**, create a new flow: **Send Conversation Summary**

2. **Trigger:** When Copilot Studio calls a flow

3. Add **Input parameters**:
   - **EmployeeName** (text)
   - **EmployeeEmail** (text)
   - **ConversationTopic** (text) - e.g., "Leave Policy"
   - **ConversationSummary** (text) - Key points discussed
   - **SendTo** (text) - "Manager" or "Self"
   - **ManagerEmail** (text) - Optional, if sending to manager

4. **Action 1: Compose Summary Message**
   - Add **Compose** action
   - Inputs:
     ```
     **Conversation Summary from Knowledge Navigator**
     
     **Employee:** {EmployeeName}
     **Topic Discussed:** {ConversationTopic}
     **Date:** {utcNow()}
     
     **Summary:**
     {ConversationSummary}
     
     **Key Documents Referenced:**
     - [Citations from the conversation]
     
     This summary was automatically generated by the Internal Knowledge Navigator.
     
     For questions, contact HR, Finance, IT, or Procurement directly.
     ```

5. **Action 2: Determine Recipient**
   - Add **Condition** action
   - If SendTo equals "Manager"
     - Send email to {ManagerEmail}
   - Else
     - Send email to {EmployeeEmail}

6. **Action 3: Send Email**
   - Add **Office 365 Outlook** → **Send an email**
   - **To:** {Determined from condition}
   - **Subject:** Knowledge Navigator Conversation Summary - {ConversationTopic}
   - **Body:** {Compose output}

7. **Action 4: Post to Teams (Optional)**
   - Add **Microsoft Teams** → **Post message in chat**
   - **Recipient:** {EmployeeEmail}
   - **Message:** "I've sent a summary of our conversation to {SendTo}. Check your email!"

8. **Action 5: Return Response**
   - Add **Respond to Copilot Studio** action
   - Output:
     - **SummarySent** (boolean) - True
     - **Message** (text) - "Summary sent successfully"

9. **Save** the flow.

### Step 7: Add Summary Option to Multiple Topics

1. In **Copilot Studio**, you can add this to any topic.

2. For example, in **HR - Leave Policy** topic:

3. At the end of the conversation, before "Would you like to know anything else?":

   **Node: Offer Summary**
   - **Ask question:** "Would you like me to send a summary of this conversation to your email or manager?"
   - **Identify:** Multiple choice
   - **Options:**
     - Yes, email me a summary
     - Yes, send to my manager
     - No thanks
   - **Save as:** SummaryOption

   **Node: Conditional Summary**
   - If "Yes, email me":
     - Call **Send Conversation Summary** flow
     - SendTo: "Self"
   
   - If "Yes, send to my manager":
     - Ask: "What's your manager's email?"
     - Call **Send Conversation Summary** flow
     - SendTo: "Manager"
   
   - If "No thanks":
     - Continue to end

4. **Save** the topic.

5. Repeat for other topics (Finance, IT, Procurement).

### Step 8: Publish and Deploy Agent

1. After creating all topics and flows, click **Save** on all open topics.

2. Select **Publish** from the top navigation.

3. Click **Publish** again to confirm.

4. Select **Channels (1)**, then select **Teams and Microsoft 365 Copilot (2)**.

5. Make sure the checkbox **Make agent available in Microsoft 365 Copilot (1)** is enabled, then select **Add Channel (2)**.

6. **Close** the page.

7. Select **Publish** again to deploy the agent to Microsoft 365 Copilot.

8. Click **Publish** to confirm.

### Step 9: Access Agent in Microsoft 365 Copilot

1. Navigate back to **Channels (1)**, then select **Teams and Microsoft 365 Copilot (2)**.

2. Select the **See agent in Microsoft 365** option.

3. Select **Add** to deploy it in Microsoft 365 Copilot.

4. **Your Internal Knowledge Navigator agent is now available in Microsoft 365 Copilot!**

5. Open the **Microsoft 365 desktop app**, and from the left panel, select **Internal Knowledge Navigator** under **Agents**.

   > **Note:** After adding the agent, if it opens in a browser, **open the Microsoft 365 desktop app** to access the deployed agent. If you don't see the newly created agent, **sign out** and **sign back in** using your credentials.

### Step 10: Test Knowledge Request Submission

1. In the **Microsoft 365 Copilot** app, navigate to your **Internal Knowledge Navigator** agent.

2. Type one of the trigger phrases to activate the Knowledge Request topic:
   ```
   I need to submit a knowledge request
   ```
   or
   ```
   Submit knowledge request
   ```

3. Fill out the adaptive card form:
   - **Department:** Select "IT"
   - **Request Title:** "How to access SAP system"
   - **Question Details:** "I need instructions on requesting access to SAP for my role"
   - **Urgency:** Select "High"
   - **Your Email:** Your lab email address

4. Click **Submit Request**.

5. Verify you receive the confirmation message with a Request ID.

6. Navigate to the **KnowledgeHub<inject key="DeploymentID" enableCopy="false"/>** SharePoint site.

7. Click **Site contents** and select **Knowledge_Requests_List**.

8. Verify your request appears in the list with all the details filled in.

9. If urgency was "High", check if the notification email was sent.

### Step 11: Test Department Knowledge Queries

1. In the agent chat, try department-specific queries:

   **HR Questions:**
   ```
   How many days of annual leave do I get?
   ```
   ```
   What's the onboarding process for new employees?
   ```

   **Finance Questions:**
   ```
   What expenses can I claim for business travel?
   ```
   ```
   How do I submit travel receipts?
   ```

   **IT Questions:**
   ```
   How do I request Microsoft Project access?
   ```
   ```
   What's the password reset procedure?
   ```

   **Procurement Questions:**
   ```
   What's the approval process for a $10,000 purchase?
   ```
   ```
   How do I add a new vendor?
   ```

2. Verify each response:
   - Provides accurate information from the correct department document
   - Includes citations showing document name
   - Uses professional, helpful language

### Step 12: Test in Microsoft Teams

1. Open **Microsoft Teams** desktop app.

2. Click on **Chat** or **Apps** in the left sidebar.

3. Search for **Internal Knowledge Navigator**.

4. Start a conversation with the agent:
   ```
   Hello! Can you help me understand the travel reimbursement policy?
   ```

5. Test the same queries you tested in Microsoft 365 Copilot.

6. Verify the agent responds correctly in the Teams environment.

### Step 13: Monitor and Review Analytics

1. Return to **Copilot Studio**.

2. Select your **Internal Knowledge Navigator** agent.

3. Navigate to **Analytics** in the left navigation.

4. Review the following metrics:
   - **Total sessions** - How many conversations
   - **Engagement rate** - User interaction levels
   - **Resolution rate** - Successfully answered questions
   - **Escalation rate** - When agent couldn't help
   - **Top topics** - Most frequently triggered topics

5. Use these insights to improve your agent:
   - Add more trigger phrases to popular topics
   - Update knowledge sources with missing information
   - Refine conversational flows based on user behavior

### Step 14: Validate Deployment

> **Congratulations** on completing the task! Now, it's time to validate it. Here are the steps:
> - If you receive a success message, you can proceed to the next section.
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help you out.

<validation step="knowledge-navigator-deployment" />

## Success Criteria
- Created 3 Power Automate flows:
  - Email Policy Document
  - Create IT Support Ticket
  - Send Conversation Summary
- All flows successfully connected to Copilot Studio
- Integrated actions into relevant department topics
- Tested all actions end-to-end:
  - Policy documents are emailed successfully
  - IT tickets are created in Teams or ticketing system
  - Conversation summaries are sent via email
- Added error handling to flows
- Created help topic documenting available actions
- All actions work reliably and provide user confirmation

## Additional Resources
- [Create flows for copilots](https://learn.microsoft.com/microsoft-copilot-studio/advanced-flow)  
- [Call Power Automate flows](https://learn.microsoft.com/microsoft-copilot-studio/advanced-use-flow)  
- [Power Automate connectors](https://learn.microsoft.com/connectors/connector-reference/)  
- [Send email with Office 365](https://learn.microsoft.com/connectors/office365/)  
- [Microsoft Teams actions](https://learn.microsoft.com/connectors/teams/)

---

## Congratulations

You have successfully built a complete **Internal Knowledge Navigator** agent with:
- Multi-department knowledge base (HR, Finance, IT, Procurement)
- Intelligent conversational topics with branching logic
- Citation-based answers showing document sources
- Automated actions (email documents, create tickets, send summaries)

Your agent is now ready to help employees find information efficiently across your organization.

### Next Steps:
1. Publish your agent to make it available to employees
2. Share the agent or embed it in Teams, SharePoint, or your intranet
3. Monitor usage analytics to see which topics and actions are most popular
4. Gather feedback and continuously improve the agent
5. Add more departments and documents as needed

**Thank you for completing this Hack in a Day.**
