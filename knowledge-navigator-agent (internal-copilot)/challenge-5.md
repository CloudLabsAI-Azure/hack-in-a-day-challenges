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

- In **Microsoft Copilot Studio**, click on your **Internal Knowledge Navigator** copilot.

- In the left navigation, look for **Actions** or **Flows** (this may be under Topics Ã¢â€ â€™ Call an action).

- Power Automate flows can be:
   - **Triggered by the copilot** (with parameters from the conversation)
   - **Return values** back to the copilot
   - **Perform external actions** (send email, create ticket, post to Teams, etc.)

- You'll create three flows in this challenge.

### Step 2: Connect Knowledge Request to SharePoint via Power Automate

Now we'll create a flow to save knowledge requests to SharePoint and track their status.

- Go back to the **Knowledge Request Submission** topic you created in Challenge 3.

- Select **Add node ** after the Adaptive card node, choose **Add a tool **, and then select **New agent flow **.

- Select the **When an agent calls the flow ** action and click on **+ Add input ** under the **Parameters** section.

   > **Note:** If the side panel does not open automatically, click the **panel icon** on the top-right to open it.

- Add the following input parameters one by one (click **+ Add an input** between each):

   | Parameter Name | Type |
   |----------------|------|
   | Department | Text |
   | RequestTitle | Text |
   | QuestionDetails | Text |
   | Urgency | Text |
   | EmployeeEmail | Text |

- Select the **+ ** button to add an action, type **SharePoint ** in the search box, and select **Create item **.

   > **Note:** If the side panel does not open automatically, click the **panel icon** for a clearer view.

- Select **Sign in** and authenticate with **<inject key="AzureAdUserEmail"></inject>**.

- If prompted, select **Allow access**.

- On the **Create item** action, configure the following parameters:
   - **Site Address:** Select **KnowledgeHub<inject key="DeploymentID" enableCopy="false"/>** SharePoint site ****
   - **List name:** Select **Knowledge_Requests_List **
   - **Title:** Enter **Knowledge Request **
   - Click **Show all **

- Under **Advanced parameters**, map the SharePoint list columns to the flow input parameters:
   - **Title** Ã¢â€ â€™ {RequestTitle}
   - **Department** Ã¢â€ â€™ {Department}
   - **Question Details** Ã¢â€ â€™ {QuestionDetails}
   - **Urgency** Ã¢â€ â€™ {Urgency}
   - **Employee Email** Ã¢â€ â€™ {EmployeeEmail}
   - **Status** Ã¢â€ â€™ "Open" (type manually)

   Use the **dynamic content** icon to select variables from Input parameters.

### Step 3: Add Conditional Logic Based on Urgency

- Select the **+ ** button under the Create item action, type **Condition ** in the search box, and select **Condition ** from the control section.

- On the Condition side screen, configure:
   - Choose a value Ã¢â€ â€™ Select **Urgency** from input parameters ****
   - Select **is equal to **
   - Enter **High **

- Under the **True** branch (High urgency):
   - Select **+ **, search for **Send an email **, and select **Send an email (V2) ** from Office 365 Outlook

- Configure the email action:
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

- Under the **False** branch (Medium/Low urgency):
   - No immediate action needed - requests will be reviewed in normal queue

### Step 4: Return Response to Agent

- After the Condition (outside both True/False branches), select **+** and add **Respond to agent** action.

- Add output parameters:
   - **RequestCreated** (boolean) Ã¢â€ â€™ True
   - **RequestID** (text) Ã¢â€ â€™ Use SharePoint item ID
   - **ConfirmationMessage** (text) Ã¢â€ â€™ "Your knowledge request has been submitted successfully"

- Select **Publish** to save the flow.

- Select **Go back to the agent**.

### Step 5: Map Flow Variables in Topic

- In the **Knowledge Request Submission** topic, find the Power Automate action node.

- Map each input parameter by clicking **ellipsis (...) ** and selecting the corresponding adaptive card variable ****.

- After the action node, add a **Send a message ** node ****:

   ```
   Your knowledge request has been submitted successfully!
   
   Request ID: {RequestID}
   Department: {Department}
   
   We'll respond based on the urgency level you specified. You'll receive updates via email at {EmployeeEmail}.
   ```

- Select **Save**.

### Step 6: Create Flow 2 - Email Policy Document

Now let's create a simpler flow for emailing policy documents:

- From any topic (e.g., Finance - Travel Reimbursement), add a node asking if the user wants to receive the policy document via email.

- Add a **Call an action** node Ã¢â€ â€™ **New agent flow**.

- Name the flow: **Email Policy Document**

- **Trigger:** When an agent calls the flow

- Add **Input parameters**:
   | Parameter Name | Type |
   |----------------|------|
   | RecipientEmail | Text |
   | DocumentName | Text |
   | DepartmentName | Text |

- **Action 1: Compose Document Message**
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

- **Action 2: Send Email**
   - Add **Office 365 Outlook** Ã¢â€ â€™ **Send an email (V2)** action
   - **To:** {RecipientEmail}
   - **Subject:** Your Requested Policy Document - {DocumentName}
   - **Body:** {Compose output from previous step}
   - **Importance:** Normal

- **Action 3: Return Response to Copilot**
    - Add **Respond to Power Virtual Agents** action
    - Add output parameter:
      - **EmailSent** (boolean) - True
      - **ConfirmationMessage** (text) - "Email sent successfully to {RecipientEmail}"

- **Save** the flow with the name: **Email Policy Document**

- Test the flow by clicking **Test** Ã¢â€ â€™ **Manually** Ã¢â€ â€™ Run with sample data.

### Step 3: Integrate Email Flow with Copilot Topic

- Return to **Copilot Studio**.

- Open the **Finance - Travel Reimbursement** topic (or any topic where you want to offer document email).

- Find the node where you asked: "Would you like me to send you the policy document?"

- After the Yes response, add:
   - **Call an action** node
   - Select **Email Policy Document** flow

- Map the input parameters:
   - **RecipientEmail:** Use variable `User.Email` or ask the user for their email
   - **DocumentName:** "Travel Reimbursement Policy"
   - **DepartmentName:** "Finance"

- After the action completes, add:
   - **Send a message** node
   - Message: "{EmailSent.ConfirmationMessage} - Check your inbox!"

- **Save** the topic.

- **Test** in the copilot:
   - Trigger the Finance Travel Reimbursement topic
   - Say "Yes" when asked if you want the document emailed
   - Verify the flow executes and you receive an email

### Step 4: Create Flow 2 - Create IT Support Ticket

- In **Power Automate**, create a new flow: **Create IT Support Ticket**

- **Trigger:** When Copilot Studio calls a flow

- Add **Input parameters**:
   - **EmployeeName** (text)
   - **EmployeeEmail** (text)
   - **IssueType** (text) - e.g., "Software Access"
   - **IssueDescription** (text)
   - **Priority** (text) - Low, Medium, High

- **Action 1: Create Ticket Data**
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

- **Action 2: Send to Ticketing System**
   
   **Option A: If you have Freshdesk from earlier challenges:**
   - Add **HTTP** action
   - Method: POST
   - URI: `https://your-domain.freshdesk.com/api/v2/tickets`
   - Headers: 
     - Authorization: Basic {YourAPIKey}
     - Content-Type: application/json
   - Body: {Compose output}

   **Option B: Send to Teams instead:**
   - Add **Microsoft Teams** Ã¢â€ â€™ **Post message in a chat or channel**
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

- **Action 3: Return Response**
   - Add **Respond to Copilot Studio** action
   - Output parameters:
     - **TicketCreated** (boolean) - True
     - **TicketID** (text) - Generate or use "TKT-" + utcNow()
     - **ConfirmationMessage** (text) - "Your IT support ticket {TicketID} has been created"

- **Save** the flow.

- Test the flow manually.

### Step 5: Integrate Ticket Creation with IT Topic

- Return to **Copilot Studio**.

- Open the **IT - Software Access** topic.

- Find where you asked: "Would you like me to help you create a ticket now?"

- After the Yes response:
   
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

- **Save** the topic.

- **Test** the ticket creation flow end-to-end.

### Step 6: Create Flow 3 - Send Conversation Summary

- In **Power Automate**, create a new flow: **Send Conversation Summary**

- **Trigger:** When Copilot Studio calls a flow

- Add **Input parameters**:
   - **EmployeeName** (text)
   - **EmployeeEmail** (text)
   - **ConversationTopic** (text) - e.g., "Leave Policy"
   - **ConversationSummary** (text) - Key points discussed
   - **SendTo** (text) - "Manager" or "Self"
   - **ManagerEmail** (text) - Optional, if sending to manager

- **Action 1: Compose Summary Message**
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

- **Action 2: Determine Recipient**
   - Add **Condition** action
   - If SendTo equals "Manager"
     - Send email to {ManagerEmail}
   - Else
     - Send email to {EmployeeEmail}

- **Action 3: Send Email**
   - Add **Office 365 Outlook** Ã¢â€ â€™ **Send an email**
   - **To:** {Determined from condition}
   - **Subject:** Knowledge Navigator Conversation Summary - {ConversationTopic}
   - **Body:** {Compose output}

- **Action 4: Post to Teams (Optional)**
   - Add **Microsoft Teams** Ã¢â€ â€™ **Post message in chat**
   - **Recipient:** {EmployeeEmail}
   - **Message:** "I've sent a summary of our conversation to {SendTo}. Check your email!"

- **Action 5: Return Response**
   - Add **Respond to Copilot Studio** action
   - Output:
     - **SummarySent** (boolean) - True
     - **Message** (text) - "Summary sent successfully"

- **Save** the flow.

### Step 7: Add Summary Option to Multiple Topics

- In **Copilot Studio**, you can add this to any topic.

- For example, in **HR - Leave Policy** topic:

- At the end of the conversation, before "Would you like to know anything else?":

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

- **Save** the topic.

- Repeat for other topics (Finance, IT, Procurement).

### Step 8: Publish and Deploy Agent

- After creating all topics and flows, click **Save** on all open topics.

- Select **Publish** from the top navigation.

- Click **Publish** again to confirm.

- Select **Channels **, then select **Teams and Microsoft 365 Copilot **.

- Make sure the checkbox **Make agent available in Microsoft 365 Copilot ** is enabled, then select **Add Channel **.

- **Close** the page.

- Select **Publish** again to deploy the agent to Microsoft 365 Copilot.

- Click **Publish** to confirm.

### Step 9: Access Agent in Microsoft 365 Copilot

- Navigate back to **Channels **, then select **Teams and Microsoft 365 Copilot **.

- Select the **See agent in Microsoft 365** option.

- Select **Add** to deploy it in Microsoft 365 Copilot.

- **Your Internal Knowledge Navigator agent is now available in Microsoft 365 Copilot!**

- Open the **Microsoft 365 desktop app**, and from the left panel, select **Internal Knowledge Navigator** under **Agents**.

   > **Note:** After adding the agent, if it opens in a browser, **open the Microsoft 365 desktop app** to access the deployed agent. If you don't see the newly created agent, **sign out** and **sign back in** using your credentials.

### Step 10: Test Knowledge Request Submission

- In the **Microsoft 365 Copilot** app, navigate to your **Internal Knowledge Navigator** agent.

- Type one of the trigger phrases to activate the Knowledge Request topic:
   ```
   I need to submit a knowledge request
   ```
   or
   ```
   Submit knowledge request
   ```

- Fill out the adaptive card form:
   - **Department:** Select "IT"
   - **Request Title:** "How to access SAP system"
   - **Question Details:** "I need instructions on requesting access to SAP for my role"
   - **Urgency:** Select "High"
   - **Your Email:** Your lab email address

- Click **Submit Request**.

- Verify you receive the confirmation message with a Request ID.

- Navigate to the **KnowledgeHub<inject key="DeploymentID" enableCopy="false"/>** SharePoint site.

- Click **Site contents** and select **Knowledge_Requests_List**.

- Verify your request appears in the list with all the details filled in.

- If urgency was "High", check if the notification email was sent.

### Step 11: Test Department Knowledge Queries

- In the agent chat, try department-specific queries:

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

- Verify each response:
   - Provides accurate information from the correct department document
   - Includes citations showing document name
   - Uses professional, helpful language

### Step 12: Test in Microsoft Teams

- Open **Microsoft Teams** desktop app.

- Click on **Chat** or **Apps** in the left sidebar.

- Search for **Internal Knowledge Navigator**.

- Start a conversation with the agent:
   ```
   Hello! Can you help me understand the travel reimbursement policy?
   ```

- Test the same queries you tested in Microsoft 365 Copilot.

- Verify the agent responds correctly in the Teams environment.

### Step 13: Monitor and Review Analytics

- Return to **Copilot Studio**.

- Select your **Internal Knowledge Navigator** agent.

- Navigate to **Analytics** in the left navigation.

- Review the following metrics:
   - **Total sessions** - How many conversations
   - **Engagement rate** - User interaction levels
   - **Resolution rate** - Successfully answered questions
   - **Escalation rate** - When agent couldn't help
   - **Top topics** - Most frequently triggered topics

- Use these insights to improve your agent:
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
- Publish your agent to make it available to employees
- Share the agent or embed it in Teams, SharePoint, or your intranet
- Monitor usage analytics to see which topics and actions are most popular
- Gather feedback and continuously improve the agent
- Add more departments and documents as needed

**Thank you for completing this Hack in a Day.**
