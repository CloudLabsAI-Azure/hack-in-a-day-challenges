# Challenge 04: Create Teams Approval Flow

## Introduction
For critical or complex IT issues, tickets need approval from IT managers before they're assigned to technicians. Microsoft Teams provides a built-in approval system that integrates seamlessly with Power Automate, enabling real-time notifications and approvals.

In this challenge, you will create a reusable approval flow that sends ticket details to an IT manager in Teams, waits for their approval or rejection, and updates the ticket status accordingly.

## Challenge Objectives
- Create a Power Automate flow triggered by ticket creation
- Send approval request to IT manager via Teams
- Update ticket status based on approval decision
- Notify the user of the outcome

## Steps to Complete

### Step 1: Navigate to Power Automate

1. If not already there, navigate to:

   ```
   https://make.powerautomate.com
   ```

2. Ensure you're in the correct environment.

### Step 2: Create Approval Flow

1. Click **+ Create** in the left navigation.

2. Select **Automated cloud flow**.

3. Configure the flow:
   - **Flow name:** `IT Helpdesk Approval and Assignment`
   - **Choose your flow's trigger:** Search for **Microsoft Lists** and select **When an item is created**
   - Click **Create**

### Step 3: Configure the Trigger

1. In the **When an item is created** trigger:
   - **Site Address:** Select the SharePoint site where your helpdesk list is located
   - **List Name:** Select `IT Helpdesk Tickets - <inject key="DeploymentID"></inject>`

2. This flow will now trigger automatically whenever a new ticket is created.

### Step 4: Add Condition to Check Priority

1. Click **+ New step**.

2. Search for **Condition** and select it.

3. Configure the condition to check if the ticket needs approval:
   - Click in the first field → select **Priority** from dynamic content
   - Choose **is equal to**
   - Type: `High`

4. This ensures only high-priority tickets require manager approval.

### Step 5: Configure "Yes" Branch - Send Approval Request

1. In the **If yes** branch, click **Add an action**.

2. Search for **Approvals** and select **Start and wait for an approval**.

3. Configure the approval action:
   - **Approval type:** Select **Approve/Reject - First to respond**
   - **Title:** Type `IT Ticket Approval Required - ` then add **Title** from dynamic content
   - **Assigned to:** Enter your IT manager's email: <inject key="AzureAdUserEmail"></inject> (or another email for testing)
   - **Details:** Build a formatted message:
     ```
     A new high-priority IT ticket has been created and requires approval:
     
     Ticket ID: [Select ID from dynamic content]
     Category: [Select Issue Category]
     User: [Select User Email]
     Description: [Select Issue Description]
     Priority: [Select Priority]
     
     Please review and approve or reject this ticket.
     ```
   - **Item link:** (Optional) Enter the URL to the Lists item
   - **Item link description:** Type `View Ticket`

### Step 6: Add Condition to Check Approval Response

1. After the approval action, click **+ New step** (still in the "Yes" branch).

2. Search for **Condition** and add it.

3. Configure the nested condition:
   - Click in the first field → select **Outcome** from the approval action's dynamic content
   - Choose **is equal to**
   - Type: `Approve`

### Step 7: Handle Approved Tickets

1. In the nested **If yes** branch (approval approved), click **Add an action**.

2. Search for **Microsoft Lists** and select **Update item**.

3. Configure the update:
   - **Site Address:** Same as before
   - **List Name:** `IT Helpdesk Tickets - <inject key="DeploymentID"></inject>`
   - **Id:** Select **ID** from the trigger's dynamic content
   - **Status:** Type or select `In Progress`
   - **Assigned To Claims:** Enter an IT technician's email or leave blank

4. Click **Add an action** after the update.

5. Search for **Office 365 Outlook** and select **Send an email (V2)**.

6. Configure the email:
   - **To:** Select **User Email** from trigger dynamic content
   - **Subject:** Type `Your IT Ticket Has Been Approved`
   - **Body:** 
     ```
     Your support ticket (ID: [Select ID]) has been approved and assigned to our IT team.
     
     Category: [Select Issue Category]
     Priority: [Select Priority]
     Status: In Progress
     
     An IT technician will contact you shortly.
     ```

### Step 8: Handle Rejected Tickets

1. In the nested **If no** branch (approval rejected), click **Add an action**.

2. Search for **Microsoft Lists** and select **Update item**.

3. Configure the update:
   - **Site Address:** Same as before
   - **List Name:** `IT Helpdesk Tickets - <inject key="DeploymentID"></inject>`
   - **Id:** Select **ID** from trigger
   - **Status:** Type or select `Closed`

4. Click **Add an action**.

5. Add **Send an email (V2)** action.

6. Configure:
   - **To:** Select **User Email**
   - **Subject:** Type `Your IT Ticket Has Been Closed`
   - **Body:**
     ```
     Your support ticket (ID: [Select ID]) has been reviewed and closed.
     
     Reason: The request was not approved by IT management.
     
     If you believe this is an error, please contact IT support directly.
     ```

### Step 9: Configure "No" Branch - Auto-assign Low/Medium Priority

1. Go back to the main condition (priority check).

2. In the **If no** branch, click **Add an action**.

3. Add **Microsoft Lists** → **Update item**.

4. Configure:
   - **Site Address:** Same as before
   - **List Name:** `IT Helpdesk Tickets - <inject key="DeploymentID"></inject>`
   - **Id:** Select **ID** from trigger
   - **Status:** Type or select `In Progress`
   - **Assigned To Claims:** Enter a default IT technician email

5. Click **Add an action**.

6. Add **Send an email (V2)**.

7. Configure:
   - **To:** Select **User Email**
   - **Subject:** Type `Your IT Ticket Has Been Created`
   - **Body:**
     ```
     Your support ticket has been created and assigned to our IT team.
     
     Ticket ID: [Select ID]
     Category: [Select Issue Category]
     Priority: [Select Priority]
     Status: In Progress
     
     An IT technician will contact you shortly.
     ```

### Step 10: Save and Test the Flow

1. Click **Save** in the top-right corner.

2. Wait for the flow to save.

3. To test, go to **Power Automate** → **+ Create** → **Instant cloud flow**.

4. Or simply create a new high-priority ticket manually in your Lists:
   - Go to **IT Helpdesk Tickets** list
   - Click **+ New**
   - Fill in:
     - Title: `Test High Priority`
     - Issue Category: `VPN Issues`
     - User Email: Your email
     - Issue Description: `Test approval flow`
     - Priority: `High`
     - Status: `New`
   - Click **Save**

5. Check Microsoft Teams:
   - Open **Teams** → **Approvals** app
   - You should see a new approval request
   - Click **Approve** or **Reject** to test

6. Verify the ticket status updated in Lists.

7. Check your email for the notification.

## Success Criteria
✅ Automated flow created and triggered by new ticket creation  
✅ High-priority tickets send approval requests to Teams  
✅ Approval/rejection updates ticket status automatically  
✅ Email notifications sent to users based on approval outcome  
✅ Low/Medium priority tickets auto-assigned without approval  
✅ Flow tested successfully with both approval and rejection scenarios  

## Additional Resources
- [Approvals in Microsoft Teams](https://support.microsoft.com/office/what-is-approvals-a9a01c95-e0bf-4d20-9ada-f7be3fc283d3)  
- [Power Automate approvals](https://learn.microsoft.com/power-automate/get-started-approvals)  
- [Conditional logic in flows](https://learn.microsoft.com/power-automate/use-expressions-in-conditions)

---

Now, click **Next** to continue to **Challenge 05: Connect Topics to Flows**.
