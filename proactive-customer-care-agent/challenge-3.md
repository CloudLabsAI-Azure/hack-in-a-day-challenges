# Challenge 03: Create CustomerServiceFlow

## Introduction
Now that your Freshdesk account is ready, you'll create a reusable flow in Copilot Studio that connects to Freshdesk. This flow will be called by your topics to create support tickets automatically when customers need assistance beyond self-service troubleshooting.

In this challenge, you will create an agent flow with the Freshdesk connector that automates ticket creation based on customer input, streamlining the process for handling service requests.

## Challenge Objectives

- Navigate to Actions in Copilot Studio
- Configure the Flow
- Publish the Flow
- Rename the Flow

## Steps to Complete

### Step 1: Navigate to Actions in Copilot Studio

1. In **Copilot Studio**, with your **Customer Care Copilot Agent** open, click **Flows** in the left navigation.

1. Click on **+ New agent flow**

1. This will open the flow designer.

### Step 2: Configure the Flow

1. In the **Add a trigger** pane, search for **When an agent calls the flow**, and then select **When an agent calls the flow** under **Skills**.

1. You'll now add input parameters that topics will pass to this flow.

1. In the trigger node, click **+ Add an input**.

1. Select **Text** as the datatype.

1. Provide `Subject` as the **Input name**.

1. Add one more input:

   **Input 2:**
   - Type: **Text**
   - Name: `Description`

1. Your trigger should now have 2 text input parameters.

   > **Note:** These are reference variables. Topics will pass actual values when calling this flow. Email, Priority, and Status will be preset in the flow.

1. Below the trigger node, click on (**+**) to add a new step.

1. Search for **Freshdesk** in the connector search box.

1. From the list, select the action **Create a ticket**.

1. In the **Create a ticket** action pane, you'll be prompted to create a new connection.

1. Click **Create new** (or **+ New connection**).

1. Provide the following connection details:
   - **Connection name:** `customerservice`
   - **Account URL:** Paste the Account URL you copied in Challenge 02 (e.g., `https://your-account.freshdesk.com`)
   - **Email or API key:** Paste the **API Key** you copied in Challenge 02
   - **Password:** Enter **<inject key="AzureAdUserPassword"></inject>**.

1. Click **Create** to establish the connection.

1. Wait for the connection to be validated.

### Step 2: Map Flow Inputs to Freshdesk Fields

1. Once the connection is created, configure the **Create a ticket** action fields:

1. **Subject** parameter:
   - Click in the **Subject** field
   - Click **Dynamic content** option
   - Select **Subject** from the trigger's input variables

1. **Description** parameter:
   - Click in the **Description** field
   - Click **Dynamic content**
   - Select **Description** variable

1. In the **Email** parameter field, select the dropdown and choose one option from the list.

   > **Note:** If the options do not load, select **Enter custom value**, and then enter **<inject key="AzureAdUserEmail"></inject>** in the **Email** field.

1. **Priority** parameter:
   - Select **Medium** from the dropdown

1. **Status** parameter:
   - Select **Open** from the dropdown

1. Select **Publish** to publish the flow.

1. Below the **Create a ticket** action, click on **(+)**.

1. In **Add an action**, search for **Respond to the agent**, and then select **Respond to the agent** under **Skills**.

1. Click **+ Add an output**.

1. Configure output as follows:
   - Type: **Text**
   - Name: `TicketStatus`
   - Value: Type `Ticket created successfully`

### Step 3: Publish the Flow

1. Click **Save draft** in the top-right corner of the flow designer.

1. The flow will be saved with a default name initially.

1. Wait for the flow to save successfully.

1. Now click **Publish** in the top-right corner.

3. Wait for the flow to be published.

1. You'll see a confirmation message: "Your flow has been published."

1. Click **Flow** to return to Copilot Studio.

### Step 4: Rename the Flow

1. In Flow page, select the **Overview** tab to view the flow details.

1. Find your newly published flow in the list.

1. In the **Overview** tab, select **Edit** to modify the flow details.

1. In the flow designer, click on the flow name at the top (it will have a default name).

1. Change the name to the following:
   ```
   CustomerServiceFlow
   ```

1. Click **Save** to save the renamed flow.

<validation step="79f81fd7-cb7b-41f4-b1a4-031172834963" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria

- Navigate to Actions in Copilot Studio
- Configure the Flow
- Publish the Flow
- Rename the Flow

## Additional Resources
- [Create flows in Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/advanced-flow)
- [Freshdesk connector documentation](https://learn.microsoft.com/connectors/freshdesk/)
- [Flow inputs and outputs](https://learn.microsoft.com/microsoft-copilot-studio/authoring-variables)

---

Click **Next** at the bottom of the page to proceed to the next page.

   ![](./media/pro-activ-gg-g19.png)
