# Challenge 03: Create Agent Flows for Actions

## Introduction
Your copilot can answer questions using the Contoso knowledge base, but what if employees want to receive a document via email or submit a request to their team? In this challenge, you'll create two agent flows that enable your copilot to take actions beyond just answering questions.

These flows will be created first so they're ready to use when you build conversational topics in Challenge 4.

## Challenge Objectives
- Create an agent flow to email documents to employees
- Create an agent flow to send requests to Microsoft Teams
- Verify both flows are configured correctly
- Prepare flows for integration with copilot topics in the next challenge

## Steps to Complete

### Step 1: Access Agent Flows in Copilot Studio

- In **Microsoft Copilot Studio**, ensure your **Internal Knowledge Navigator** agent is open.

- In the left navigation pane, select **Flows** (or **Agent flows**).

- You will see the **Agent flows** page with options to create new flows.

### Step 2: Create Flow 1 - Email Document to Employee

- On the **Agent flows** page, click **+ New agent flow** button.

- A new flow canvas will open.

- The flow will have a default name initially.

### Step 3: Add Trigger - When an Agent Calls the Flow

- On the flow canvas, click **Add a trigger**.

- Search for and select **When an agent calls the flow** (or **When Copilot Studio calls a flow**).

- The trigger will be added to the canvas.

### Step 4: Add Input Parameters for Email Flow

- In the **When an agent calls the flow** trigger, click **Add an input**.

- Select **Text** as the input type.

- Enter **EmployeeEmail** as the input name and press Enter.

- Click **Add an input** again and add:
   - Type: **Text**
   - Name: **DocumentName**

- Click **Add an input** one more time and add:
   - Type: **Text**
   - Name: **DocumentDescription**

- You should now have 3 input parameters: EmployeeEmail, DocumentName, and DocumentDescription.

### Step 5: Add Email Action

- Click the **+** icon below the trigger to add a new step.

- In the search box, type **Send an email** and select **Send an email (V2)** from **Office 365 Outlook**.

- If prompted to sign in, use your credentials: **<inject key="AzureAdUserEmail"></inject>**

- Configure the email action:

   - **To:** Enter **<inject key="AzureAdUserEmail"></inject>**
   
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

- The flow is now saved with a default name. You'll rename it shortly.

### Step 6: Create Flow 2 - Send Request to Teams

- Navigate back to the **Flows** page by clicking the back arrow.

- Click **+ New agent flow** button again.

- A new flow canvas will open.

- The flow will have a default name initially.

### Step 7: Add Trigger - When an Agent Calls the Flow

- On the flow canvas, click **Add a trigger**.

- Search for and select **When an agent calls the flow** (or **When Copilot Studio calls a flow**).

- The trigger will be added to the canvas.

### Step 8: Add Input Parameters for Teams Flow

- In the **When an agent calls the flow** trigger, click **Add an input**.

- Select **Text** as the input type.

- Add the following input parameters one by one:

   1. **EmployeeName** (Text)
   2. **EmployeeEmail** (Text)
   3. **RequestType** (Text)
   4. **RequestDetails** (Text)

- You should now have 4 input parameters defined.

### Step 9: Add Teams Action

- Click the **+** icon below the trigger to add a new step.

- In the search box, type **Post message** and select **Post message in a chat or channel** from **Microsoft Teams**.

- If prompted to sign in, use your credentials: **<inject key="AzureAdUserEmail"></inject>**

- Configure the Teams action:

   - **Post as:** Flow bot
   
   - **Post in:** Channel

   - **Team:** Select Exisitng

   - **Channel:** Document Request
   
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

- The flow is now saved with a default name. You'll rename it next.

### Step 10: Rename Flow 1 - Email Document to Employee

- Navigate back to the **Flows** page by clicking the back arrow or selecting **Flows** from the left navigation.

- Find your first flow in the list and click on it to open the **Flow overview** page.

- Click **Edit** in the top-right corner.

- In the flow designer, click on the flow name at the top (it will have a default name).

- Change the name to:
   ```
   Email Document to Employee
   ```

- Click **Save** to save the renamed flow.

- Click the back arrow to return to the **Flows** page.

### Step 11: Rename Flow 2 - Send Request to Teams

- On the **Flows** page, find your second flow and click on it to open the **Flow overview** page.

- Click **Edit** in the top-right corner.

- In the flow designer, click on the flow name at the top.

- Change the name to:
   ```
   Send Request to Teams
   ```

- Click **Save** to save the renamed flow.

- Click the back arrow to return to the **Flows** page.

### Step 12: Verify Both Flows are Created and Renamed

- On the **Flows** page, you should now see both agent flows listed with their correct names:
   - Email Document to Employee
   - Send Request to Teams

- Both flows should show as **On** or **Active** status.

   > **Note:** These flows are now ready to be used in your agent topics in Challenge 4.

<validation step="718fdc4b-852f-46bb-883c-5a5c8ae52fef" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria
- Created **Email Document to Employee** agent flow
- Created **Send Request to Teams** agent flow
- Both flows have the correct input parameters configured
- Both flows are saved and active in Copilot Studio
- Flows are ready to be used in conversational topics in Challenge 4

## Additional Resources
- [Create flows for Microsoft Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/advanced-flow)
- [Use flows in Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/authoring-create-edit-flows)
- [Office 365 Outlook connector](https://learn.microsoft.com/connectors/office365/)
- [Microsoft Teams connector](https://learn.microsoft.com/connectors/teams/)

---

Now, click **Next** to continue to **Challenge 04: Design Topics and Integrate Flows**.
