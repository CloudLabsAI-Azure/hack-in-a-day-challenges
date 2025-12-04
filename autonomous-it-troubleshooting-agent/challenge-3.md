# Challenge 03: Setup Helpdesk & Create Ticket Creation Flow

## Introduction
When the copilot cannot resolve an issue automatically, it needs to create a support ticket in your helpdesk system. Power Automate flows enable seamless integration between Copilot Studio and backend systems.

In this challenge, you will set up a Microsoft Lists-based helpdesk system and create a reusable Power Automate flow that all topics can use to create support tickets.

## Challenge Objectives
- Create a Microsoft Lists helpdesk table for ticket management
- Build a Power Automate flow to create tickets
- Configure flow inputs to capture issue details
- Test the flow independently before integration

## Steps to Complete

### Step 1: Create Helpdesk List in Microsoft Lists

1. Open **Microsoft Edge** and navigate to:

   ```
   https://www.microsoft.com/en-us/microsoft-365/microsoft-lists
   ```

2. Click **Sign in** and use your credentials:
   - **Email/Username:** <inject key="AzureAdUserEmail"></inject>
   - **Password:** <inject key="AzureAdUserPassword"></inject>

3. Click **+ New list** at the top.

4. Select **Blank list**.

5. Configure the list:
   - **Name:** `IT Helpdesk Tickets - <inject key="DeploymentID"></inject>`
   - **Description:** `Support tickets created by IT Helpdesk Copilot`
   - **Save to:** My lists (or select a specific site)

6. Click **Create**.

### Step 2: Add Custom Columns to Helpdesk List

1. Once the list is created, click **+ Add column** to add the following columns:

2. Add **Issue Category** column:
   - Type: **Choice**
   - Choices: `Password Reset`, `VPN Issues`, `Slow Laptop`, `Printer Issues`
   - Click **Save**

3. Add **User Email** column:
   - Type: **Single line of text**
   - Click **Save**

4. Add **Issue Description** column:
   - Type: **Multiple lines of text**
   - Click **Save**

5. Add **Priority** column:
   - Type: **Choice**
   - Choices: `Low`, `Medium`, `High`
   - Default: `Medium`
   - Click **Save**

6. Add **Status** column:
   - Type: **Choice**
   - Choices: `New`, `In Progress`, `Waiting for Approval`, `Resolved`, `Closed`
   - Default: `New`
   - Click **Save**

7. Add **Assigned To** column:
   - Type: **Person**
   - Allow multiple selections: No
   - Click **Save**

8. Your list should now have these columns:
   - Title (default)
   - Issue Category
   - User Email
   - Issue Description
   - Priority
   - Status
   - Assigned To

### Step 3: Navigate to Power Automate

1. Open a new tab and navigate to:

   ```
   https://make.powerautomate.com
   ```

2. Sign in with the same credentials if prompted.

3. Ensure you're in the correct environment (**Dev-<inject key="DeploymentID"></inject>** or default).

### Step 4: Create Ticket Creation Flow

1. In Power Automate, click **+ Create** in the left navigation.

2. Select **Instant cloud flow**.

3. Configure the flow:
   - **Flow name:** `Create IT Helpdesk Ticket`
   - **Choose how to trigger this flow:** Select **Power Virtual Agents** (or **Microsoft Copilot Studio**)
   - Click **Create**

### Step 5: Configure Flow Input Parameters

1. In the trigger **Power Virtual Agents**, click **+ Add an input**.

2. Add the following inputs:

   **Input 1:**
   - Type: **Text**
   - Name: `IssueCategory`
   - Description: `Category of the issue`

   **Input 2:**
   - Type: **Text**
   - Name: `UserEmail`
   - Description: `User's email address`

   **Input 3:**
   - Type: **Text**
   - Name: `IssueDescription`
   - Description: `Detailed description of the issue`

   **Input 4:**
   - Type: **Text**
   - Name: `Priority`
   - Description: `Priority level: Low, Medium, or High`

3. Your trigger should now have 4 input parameters.

### Step 6: Add Create Item Action

1. Click **+ New step**.

2. Search for **Microsoft Lists** and select **Create item**.

3. Configure the action:
   - **Site Address:** Select the SharePoint site where your list is located (or My lists)
   - **List Name:** Select `IT Helpdesk Tickets - <inject key="DeploymentID"></inject>`

4. Fill in the fields using dynamic content:
   - **Title:** Click in the field → select `IssueCategory` from dynamic content
   - **Issue Category:** Select `IssueCategory`
   - **User Email:** Select `UserEmail`
   - **Issue Description:** Select `IssueDescription`
   - **Priority:** Select `Priority`
   - **Status:** Type `New` (or leave as default)

5. Leave **Assigned To** empty for now (will be handled in the approval flow).

### Step 7: Add Response to Copilot

1. Click **+ New step**.

2. Search for **Respond to Power Virtual Agents** (or **Return value(s) to Microsoft Copilot**).

3. Select the action.

4. Click **+ Add an output**.

5. Add output:
   - Type: **Text**
   - Name: `TicketID`
   - Value: Click in the field → select **ID** from the **Create item** action's dynamic content

6. Click **+ Add an output** again.

7. Add second output:
   - Type: **Text**
   - Name: `TicketStatus`
   - Value: Type `Ticket created successfully`

### Step 8: Save and Test the Flow

1. Click **Save** in the top-right corner.

2. Wait for the flow to save successfully.

3. Click **Test** in the top-right corner.

4. Select **Manually** → **Test**.

5. Provide test values:
   - **IssueCategory:** `Password Reset`
   - **UserEmail:** `test@contoso.com`
   - **IssueDescription:** `User forgot password and cannot log in`
   - **Priority:** `Medium`

6. Click **Run flow**.

7. Wait for the flow to complete.

8. Click **Done** and verify the flow run succeeded.

### Step 9: Verify Ticket Creation

1. Go back to your **IT Helpdesk Tickets** list in Microsoft Lists.

2. Refresh the page.

3. You should see a new item with:
   - Title: Password Reset
   - Issue Category: Password Reset
   - User Email: test@contoso.com
   - Issue Description: User forgot password and cannot log in
   - Priority: Medium
   - Status: New

4. If the ticket appears correctly, your flow is working!

## Success Criteria
✅ Microsoft Lists helpdesk created with custom columns  
✅ Power Automate flow created with 4 input parameters  
✅ Flow successfully creates items in the helpdesk list  
✅ Flow returns ticket ID back to the copilot  
✅ Test run completed successfully with ticket visible in Lists  

## Additional Resources
- [Microsoft Lists overview](https://support.microsoft.com/lists)  
- [Power Automate cloud flows](https://learn.microsoft.com/power-automate/overview-cloud)  
- [Copilot Studio and Power Automate integration](https://learn.microsoft.com/microsoft-copilot-studio/advanced-flow)

---

Now, click **Next** to continue to **Challenge 04: Create Teams Approval Flow**.
