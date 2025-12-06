# Challenge 03: Create Power Automate Flows for Actions

## Introduction
Your copilot can answer questions using the Contoso knowledge base, but what if employees want to receive a document via email or submit a request to their team? In this challenge, you'll create two Power Automate flows that enable your copilot to take actions beyond just answering questions.

These flows will be created first so they're ready to use when you build conversational topics in Challenge 4.

## Challenge Objectives
- Create a Power Automate flow to email documents to employees
- Create a Power Automate flow to send requests to Microsoft Teams
- Test both flows to ensure they work correctly
- Prepare flows for integration with copilot topics in the next challenge

## Steps to Complete

### Step 1: Access Agent Flows in Copilot Studio

- In **Microsoft Copilot Studio**, ensure your **Internal Knowledge Navigator** agent is open.

- In the left navigation pane, select **Flows** (or **Agent flows**).

- You will see the **Agent flows** page with options to create new flows.

### Step 2: Create Flow 1 - Email Document to Employee

- On the **Agent flows** page, click **+ New agent flow** button.

- In the text box that appears, describe what the flow should do:

   ```
   Send an email to an employee with information about a requested document
   ```

- Click the arrow or press **Enter** to generate the flow.

- Wait for Copilot Studio to generate the flow structure.

- Once the flow designer opens, you'll see the flow canvas.

- At the top, rename the flow to: **Email Document to Employee**

- The flow should have the **Run a flow from Copilot** trigger already added.

### Step 3: Add Input Parameters for Email Flow

- Click on the **Run a flow from Copilot** trigger node to expand it.

- Under **Inputs**, click **+ Add an input**.

- Select **Text** as the input type.

- Enter the following for the first parameter:
   - **Input name:** EmployeeEmail
   - Click outside or press Enter to save

- Click **+ Add an input** again and add:
   - **Input type:** Text
   - **Input name:** DocumentName

- Click **+ Add an input** one more time and add:
   - **Input type:** Text  
   - **Input name:** DocumentDescription

- You should now have 3 input parameters defined.

### Step 4: Add Email Action

- Click **+ (plus icon)** below the trigger to add a new step.

- In the search box, type **Send an email** and select **Send an email (V2)** from **Office 365 Outlook**.

- If prompted to sign in, use your credentials: **<inject key="AzureAdUserEmail"></inject>**

- Configure the email action:

   - **To:** Click in the field and select **EmployeeEmail** from the dynamic content (the parameter you created).
   
   - **Subject:** Type: `Your Requested Document - ` and then select **DocumentName** from dynamic content.
   
   - **Body:** Enter the following text and add dynamic content where indicated:

   ```
   Hello,

   As requested, here is information about the document you requested.

   Document: [Click and add DocumentName dynamic content]
   Description: [Click and add DocumentDescription dynamic content]

   You can access this document through the Contoso SharePoint site or contact your department for more details.

   Best regards,
   Internal Knowledge Navigator
   ```

- Click **Save** in the top-right corner to save the flow.

- The flow is now saved and ready to use in your agent.

### Step 5: Create Flow 2 - Send Request to Teams

- Click the back arrow or navigate back to the **Flows** page in Copilot Studio.

- Click **+ New agent flow** button again.

- In the text box, describe the second flow:

   ```
   Send a request notification to Microsoft Teams with employee details
   ```

- Click the arrow or press **Enter** to generate the flow.

- Once the flow designer opens, rename the flow to: **Send Request to Teams**

- The **Run a flow from Copilot** trigger should already be present.

### Step 6: Add Input Parameters for Teams Flow

- Click on the **Run a flow from Copilot** trigger to expand it.

- Click **+ Add an input** and select **Text**.

- Add the following input parameters one by one:

   1. **EmployeeName** (Text)
   2. **EmployeeEmail** (Text)
   3. **RequestType** (Text)
   4. **RequestDetails** (Text)

- You should now have 4 input parameters defined.

### Step 7: Add Teams Action

- Click **+ (plus icon)** below the trigger to add a new step.

- In the search box, type **Post message** and select **Post message in a chat or channel** from **Microsoft Teams**.

- If prompted to sign in, use your credentials: **<inject key="AzureAdUserEmail"></inject>**

- Configure the Teams action:

   - **Post as:** Flow bot
   
   - **Post in:** Chat with Flow bot
   
   - **Recipient:** Click in the field and enter **<inject key="AzureAdUserEmail"></inject>** (this will send to your own Teams account so you can see the request).
   
   - **Message:** Enter the following text and add dynamic content:

   ```
   New Employee Request Submitted

   Employee: [Add EmployeeName dynamic content]
   Email: [Add EmployeeEmail dynamic content]
   Request Type: [Add RequestType dynamic content]

   Details:
   [Add RequestDetails dynamic content]

   Please review and respond to this request.
   ```

- Click **Save** to save the flow.

- The flow is now saved and ready to use in your agent.

### Step 8: Verify Both Flows are Created

- Navigate back to the **Flows** page by clicking the back arrow or selecting **Flows** from the left navigation.

- You should now see both agent flows listed:
   - Email Document to Employee
   - Send Request to Teams

- Both flows should show as **On** or **Active** status.

   > **Note:** These flows are now ready to be used in your agent topics in Challenge 4.

## Success Criteria
- Created **Email Document to Employee** flow in Power Automate
- Created **Send Request to Teams** flow in Power Automate
- Both flows have the correct input parameters configured
- Both flows are published and available in Copilot Studio Actions
- Flows are ready to be used in conversational topics in Challenge 4

## Additional Resources
- [Create flows for Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/advanced-flow)
- [Power Automate documentation](https://learn.microsoft.com/power-automate/)
- [Office 365 Outlook connector](https://learn.microsoft.com/connectors/office365/)
- [Microsoft Teams connector](https://learn.microsoft.com/connectors/teams/)

---

Now, click **Next** to continue to **Challenge 04: Design Topics and Integrate Flows**.
