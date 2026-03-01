# Challenge 03: Create CustomerServiceFlow

## Introduction
Now that your Freshdesk account is ready, you'll create a reusable flow in Copilot Studio that connects to Freshdesk. This flow will be called by your topics to create support tickets automatically when customers need assistance beyond self-service troubleshooting.

In this challenge, you will create an agent flow with the Freshdesk connector that automates ticket creation based on customer input, streamlining the process for handling service requests.

## Challenge Objectives
- Create an agent flow in Copilot Studio
- Add Freshdesk connector to the flow
- Configure connection with API credentials
- Define flow inputs (Subject and Description)
- Test the flow independently
- Publish the flow for use in topics

## Steps to Complete

### Step 1: Navigate to Actions in Copilot Studio

1. In **Copilot Studio**, with your **Proactive Customer Care Agent** open, click **Actions** (or **Flows**) in the left navigation.

2. Click **+ Add an action** at the top.

3. Select **Create a new flow** (or **Create from blank**).

4. This will open the flow designer.

### Step 2: Configure Flow Trigger

1. The flow will start with a trigger node: **When an agent calls the flow** (or **Power Virtual Agents**).

2. Click on the trigger node to expand it.

3. You'll now add input parameters that topics will pass to this flow.

### Step 3: Add Input Parameters

1. In the trigger node, click **+ Add an input**.

2. Select **Text** as the datatype.

3. Provide `Subject` as the **Input name**.

4. Add one more input:

   **Input 2:**
   - Type: **Text**
   - Name: `Description`

5. Your trigger should now have 2 text input parameters.

   > **Note:** These are reference variables. Topics will pass actual values when calling this flow. Email, Priority, and Status will be preset in the flow.

### Step 4: Add Freshdesk Connector

1. Below the trigger node, click **+ New step** (or **+**).

2. Search for **Freshdesk** in the connector search box.

3. From the list, select **Freshdesk** connector.

4. Select the action **Create a ticket**.

### Step 5: Configure Freshdesk Connection

1. In the **Create a ticket** action pane, you'll be prompted to create a new connection.

2. Click **Create new** (or **+ New connection**).

3. Provide the following connection details:
   - **Connection name:** `customerservice`
   - **Account URL:** Paste the Account URL you copied in Challenge 02 (e.g., `https://your-account.freshdesk.com`)
   - **Email or API key:** Paste the **API Key** you copied in Challenge 02
   - **Password:** Since you're using an API Key, enter any random value (e.g., `X`) as it's a required field

4. Click **Create** to establish the connection.

5. Wait for the connection to be validated.

### Step 6: Map Flow Inputs to Freshdesk Fields

1. Once the connection is created, configure the **Create a ticket** action fields:

2. **Subject** parameter:
   - Click in the **Subject** field
   - Click **Dynamic content** option
   - Select **Subject** from the trigger's input variables

3. **Description** parameter:
   - Click in the **Description** field
   - Click **Dynamic content**
   - Select **Description** variable

4. **Email** parameter:
   - Enter your email address: **<inject key="AzureAdUserEmail"></inject>**

5. **Priority** parameter:
   - Select **Medium** from the dropdown

6. **Status** parameter:
   - Select **Open** from the dropdown

7. Leave other optional fields blank.

### Step 7: Add Return Values to Agent

1. Below the **Create a ticket** action, click **+ New step**.

2. Search for **Return value(s) to Microsoft Copilot** (or **Respond to Power Virtual Agents**).

3. Select this action.

4. Click **+ Add an output**.

5. Configure output as follows:
   - Type: **Text**
   - Name: `TicketStatus`
   - Value: Type `Ticket created successfully`

6. Optionally, you can add another output for Ticket ID if Freshdesk returns it in the response.

### Step 8: Save the Flow

1. Click **Save** in the top-right corner of the flow designer.

2. The flow will be saved with a default name initially.

3. Wait for the flow to save successfully.

### Step 9: Test the Flow Independently

1. Click **Test** in the top-right corner of the flow designer.

2. Select **Manually** → **Test**.

3. Provide test values for the input parameters:
   - **Subject:** `Test Ticket - Flow Validation`
   - **Description:** `Testing the customer service flow before connecting to topics`

4. Click **Run flow**.

5. Wait for the flow to execute.

6. Review the flow run history to ensure all steps completed successfully.

7. You should see a green checkmark on each action.

### Step 10: Verify Ticket in Freshdesk

1. Open a new tab and navigate to your **Freshdesk portal** by entering the following URL:
   ```
   https://your-account.freshdesk.com
   ```

2. Sign in if prompted.

3. Click on **Tickets** in the left navigation.

4. You should see a new ticket with:
   - **Subject:** Test Ticket - Flow Validation
   - **Description:** Testing the customer service flow before connecting to topics
   - **Priority:** Medium
   - **Status:** Open
   - **Requester:** Your email address

5. Click on the ticket to view full details.

6. Verify all information is correctly populated.

7. If the ticket appears correctly, your flow is working.

### Step 11: Publish the Flow

1. Go back to the flow designer in Copilot Studio.

2. Click **Publish** in the top-right corner.

3. Wait for the flow to be published.

4. You'll see a confirmation message: "Your flow has been published."

5. Click **Go back to agent** to return to Copilot Studio.

### Step 12: Rename the Flow

1. In Copilot Studio, click **Actions** in the left navigation.

2. Find your newly published flow in the list.

3. Click on the flow to open the **Flow overview** page.

4. Click **Edit** in the top-right corner.

5. In the flow designer, click on the flow name at the top (it will have a default name).

6. Change the name to the following:
   ```
   CustomerServiceFlow
   ```

7. Click **Save** to save the renamed flow.

8. Click **Publish** again to publish the updated flow name.

9. Click **Go back to agent** to return to Copilot Studio.

### Step 13: Verify Flow is Available in Actions

1. In Copilot Studio, go back to **Actions** in the left navigation.

2. You should see your flow listed:
   - **Name:** CustomerServiceFlow
   - **Status:** Published

3. This flow is now ready to be called from any topic.

<validation step="79f81fd7-cb7b-41f4-b1a4-031172834963" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria
- Agent flow created successfully in Copilot Studio
- Flow trigger configured with 2 input parameters (Subject, Description)
- Freshdesk connector added and connection established
- Freshdesk "Create a ticket" action configured with dynamic inputs and preset values
- Return value added to send status back to agent
- Flow saved and tested independently with manual test inputs
- Test ticket created successfully in Freshdesk portal
- Flow published successfully
- Flow renamed to "CustomerServiceFlow" after initial publish
- Flow available in Actions list with correct name

## Additional Resources
- [Create flows in Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/advanced-flow)
- [Freshdesk connector documentation](https://learn.microsoft.com/connectors/freshdesk/)
- [Flow inputs and outputs](https://learn.microsoft.com/microsoft-copilot-studio/authoring-variables)

---

Click **Next** at the bottom of the page to proceed to the next page.

   ![](./media/pro-activ-gg-g19.png)
