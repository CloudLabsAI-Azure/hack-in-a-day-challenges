# Challenge 05: Connect Topics to Flows

## Introduction
Now that you have created the topics and Power Automate flows, it's time to connect them together. Each topic will call the **Create IT Helpdesk Ticket** flow when escalation is needed, making the flow reusable across all support scenarios.

In this challenge, you will integrate the ticket creation flow into all 4 topics, configure the flow inputs, and test the end-to-end automation.

## Challenge Objectives
- Add the ticket creation flow as an action in each topic
- Configure flow inputs dynamically from conversation variables
- Test escalation workflow from copilot to helpdesk
- Verify tickets are created with correct information

## Steps to Complete

### Step 1: Open Password Reset Support Topic

1. In **Copilot Studio**, navigate to **Topics** in the left navigation.

2. Click on **Password Reset Support** topic to open it.

3. Review the conversation flow diagram.

### Step 2: Add Escalation Option

1. Scroll to the end of the topic's conversation flow.

2. Click **+** to add a new node.

3. Select **Ask a question**.

4. Configure the question:
   - **Message:** Type `Would you like me to create a support ticket for you?`
   - **Identify:** Select **Boolean** (Yes/No)
   - **Save response as:** Create a variable named `CreateTicket`

### Step 3: Add Condition for Ticket Creation

1. Below the question node, click **+** to add a node.

2. Select **Add a condition**.

3. Configure the condition:
   - **Select a variable:** Choose `CreateTicket`
   - **Condition:** `is equal to`
   - **Value:** `True`

### Step 4: Call the Power Automate Flow

1. In the **All other conditions** branch (when user says Yes), click **+** to add an action.

2. Select **Call an action** → **Create a flow**.

3. Wait for Power Automate to open.

4. In the list, find **Create IT Helpdesk Ticket** flow.

5. Click on the flow name to select it.

6. You'll see the flow inputs that need to be configured.

### Step 5: Configure Flow Inputs

1. Map the flow inputs to conversation variables:

   **IssueCategory:**
   - Click in the field
   - Type: `Password Reset` (or select from a variable if you collected it earlier)

   **UserEmail:**
   - Click in the field
   - Select **System.User.Email** from the variable picker (if available)
   - Or add a question earlier in the topic to collect user email and use that variable

   **IssueDescription:**
   - Click in the field
   - You can create a variable earlier in the topic that captures the user's problem description
   - For now, type a default like: `User requested password reset assistance`
   - Or concatenate multiple variables if you collected detailed information

   **Priority:**
   - Click in the field
   - Type: `Medium` (or use a variable if you're determining priority dynamically)

2. The flow action should now have all 4 inputs configured.

### Step 6: Display Ticket Confirmation

1. Below the flow action, click **+** to add a node.

2. Select **Send a message**.

3. Configure the message:
   ```
   Great! I've created a support ticket for you.
   
   Ticket ID: {x:TicketID}
   Status: {x:TicketStatus}
   
   An IT technician will contact you shortly via email.
   ```

4. Note: `{x:TicketID}` and `{x:TicketStatus}` are the outputs from your Power Automate flow.

5. Click **Save** to save the topic.

### Step 7: Add Flow to VPN Troubleshooting Topic

1. Go back to **Topics** and open **VPN Troubleshooting**.

2. Repeat steps 2-6 above:
   - Add "Would you like me to create a support ticket?" question
   - Add condition
   - Call **Create IT Helpdesk Ticket** flow
   - Configure inputs:
     - IssueCategory: `VPN Issues`
     - UserEmail: User's email variable
     - IssueDescription: VPN problem description
     - Priority: `Medium` or `High` depending on severity
   - Display confirmation message

3. Click **Save**.

### Step 8: Add Flow to Slow Laptop Performance Topic

1. Open **Slow Laptop Performance** topic.

2. Add the same escalation workflow:
   - "Create support ticket?" question
   - Condition check
   - Call **Create IT Helpdesk Ticket** flow with:
     - IssueCategory: `Slow Laptop`
     - UserEmail: User's email
     - IssueDescription: Performance issue details
     - Priority: Determined based on symptoms (e.g., disk space critical = High)
   - Confirmation message

3. Click **Save**.

### Step 9: Add Flow to Printer Support Topic

1. Open **Printer Support** topic.

2. Add the escalation workflow:
   - "Create support ticket?" question
   - Condition check
   - Call **Create IT Helpdesk Ticket** flow with:
     - IssueCategory: `Printer Issues`
     - UserEmail: User's email
     - IssueDescription: Printer problem details
     - Priority: `Low` or `Medium`
   - Confirmation message

3. Click **Save**.

### Step 10: Test End-to-End Flow

1. Open the **Test your copilot** pane.

2. Test each topic's escalation:

   **Test 1 - Password Reset:**
   - Type: "I forgot my password"
   - Follow the conversation
   - When asked about creating a ticket, respond: "Yes"
   - Verify you receive a ticket ID in the response

   **Test 2 - VPN Issues:**
   - Type: "VPN won't connect"
   - Go through troubleshooting
   - Say: "Yes, create a ticket"
   - Verify ticket creation confirmation

   **Test 3 - Slow Laptop:**
   - Type: "My computer is really slow"
   - Answer diagnostic questions
   - Escalate to ticket
   - Confirm ticket created

   **Test 4 - Printer:**
   - Type: "Printer is offline"
   - Try troubleshooting steps
   - Create ticket
   - Verify success message

### Step 11: Verify Tickets in Microsoft Lists

1. Open **Microsoft Lists** and go to **IT Helpdesk Tickets - <inject key="DeploymentID"></inject>**.

2. You should see 4 new tickets corresponding to your tests.

3. Verify each ticket has:
   - Correct Issue Category
   - Your email address
   - Appropriate Issue Description
   - Correct Priority
   - Status: New

4. If tickets appear correctly, your integration is working!

### Step 12: Test High-Priority Approval Flow

1. In the test pane, start a new conversation.

2. Type: "My C drive is completely full and I can't work"

3. When creating the ticket, ensure you set **Priority** to **High** (you may need to modify the topic to ask about urgency).

4. Check **Microsoft Teams** → **Approvals**:
   - You should see an approval request for the high-priority ticket

5. Approve or reject the ticket.

6. Verify the ticket status updates in Lists.

7. Check your email for the approval notification.

## Success Criteria
✅ All 4 topics integrated with the Create IT Helpdesk Ticket flow  
✅ Flow inputs correctly configured with topic variables  
✅ Escalation option available in each topic  
✅ Ticket creation confirmed with Ticket ID in copilot response  
✅ Tickets visible in Microsoft Lists with correct details  
✅ High-priority tickets trigger Teams approval workflow  
✅ Approval/rejection updates ticket status and sends notifications  

## Additional Resources
- [Call Power Automate flows from topics](https://learn.microsoft.com/microsoft-copilot-studio/advanced-flow)  
- [Pass variables to flows](https://learn.microsoft.com/microsoft-copilot-studio/authoring-variables)  
- [Topic authoring best practices](https://learn.microsoft.com/microsoft-copilot-studio/guidance/authoring-best-practices)

---

Now, click **Next** to continue to **Challenge 06: Deploy to Teams & Test**.
