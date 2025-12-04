# Challenge 04: Connect Copilot Studio to Freshdesk

## Introduction
Now that your Freshdesk account is ready, you'll connect Copilot Studio to Freshdesk using the Freshdesk connector. This integration allows your copilot to automatically create support tickets when users need assistance beyond self-service troubleshooting.

In this challenge, you will add the Freshdesk connector to one topic, configure ticket creation with user inputs, and test the end-to-end flow within Copilot Studio.

## Challenge Objectives
- Add Freshdesk connector to Password Reset Support topic
- Configure connection with API credentials
- Collect Subject and Description from users
- Create tickets in Freshdesk with appropriate priority
- Display ticket confirmation to users

## Steps to Complete

### Step 1: Open Password Reset Support Topic

1. In **Copilot Studio**, navigate to **Topics** in the left navigation.

2. Click on **Password Reset Support** topic to open it.

3. Review the existing conversation flow created by generative AI.

### Step 2: Add Escalation Question

1. Scroll to the end of the conversation flow.

2. Click **+** to add a node.

3. Select **Ask a question**.

4. Configure:
   - **Message:** `Would you like me to create a support ticket for you?`
   - **Identify:** Select **Boolean** (Yes/No)
   - **Save response as:** `CreateTicket`

5. Click **Save**.

### Step 3: Add Condition for Ticket Creation

1. Below the question, click **+** to add a node.

2. Select **Add a condition**.

3. Configure the condition:
   - **Variable:** Select `CreateTicket`
   - **Operator:** `is equal to`
   - **Value:** `true` (Yes)

### Step 4: Collect Ticket Subject

1. In the **Condition is met** branch (when user says Yes), click **+**.

2. Select **Ask a question**.

3. Configure:
   - **Message:** `Please provide a brief subject for your ticket`
   - **Identify:** Select **User's entire response**
   - **Save response as:** Create variable `Subject`

4. Click **Save**.

### Step 5: Collect Ticket Description

1. Below the Subject question, click **+**.

2. Select **Ask a question**.

3. Configure:
   - **Message:** `Please describe the issue in detail`
   - **Identify:** Select **User's entire response**
   - **Save response as:** Create variable `Description`

4. Click **Save**.

### Step 6: Add Freshdesk Connector Action

1. Below the Description question, click **+**.

2. Select **Call an action** → **Create a flow**.

   > **Note:** This opens the connector library where you can add Freshdesk.

3. In the search box, type **Freshdesk**.

4. From the list, select **Freshdesk** connector.

5. Select the action **Create a ticket**.

### Step 7: Configure Freshdesk Connection

1. In the **Create a ticket** configuration pane, you'll be prompted to create a new connection.

2. Click **Create new** (or **+ New connection**).

3. Provide the following connection details:
   - **Connection name:** `helpdesk`
   - **Account URL:** Paste the Account URL you copied in Challenge 03 (e.g., `https://your-account.freshdesk.com`)
   - **Email or API key:** Paste the **API Key** you copied in Challenge 03
   - **Password:** Since you're using an API Key, the password field is not important, but it's required. Enter any random value (e.g., `X`)

4. Click **Create** to establish the connection.

5. Wait for the connection to be validated and established.

### Step 8: Map Variables to Freshdesk Fields

1. Once the connection is created, you'll see the **Create a ticket** action with input fields.

2. Configure the **Subject** parameter:
   - Click in the **Subject** field
   - Click **Insert dynamic content** (lightning bolt icon or **{x}** button)
   - Select **Subject** variable from the list

3. Configure the **Description** parameter:
   - Click in the **Description** field
   - Click **Insert dynamic content**
   - Select **Description** variable

4. Configure the **Email** parameter:
   - Click **Enter custom value**
   - Type: `<inject key="AzureAdUserEmail"></inject>` (or use `System.User.Email` if available)

5. Configure the **Priority** parameter:
   - From the dropdown, select **Medium** (or use a variable if you're determining priority dynamically)

6. Configure the **Status** parameter:
   - From the dropdown, select **Open**

7. Leave other optional fields blank for now.

8. Click **Save** on the action.

### Step 9: Display Success Message

1. Below the Freshdesk action, click **+**.

2. Select **Send a message**.

3. Configure the message:
   ```
   ✅ Great! I've created a support ticket for you in Freshdesk.
   
   Your ticket has been submitted successfully and our IT team will contact you shortly.
   ```

4. Click **Save**.

### Step 10: Add Message for "No" Response

1. Go back to the **Else** branch of the condition (when user says No to creating a ticket).

2. Click **+** → **Send a message**.

3. Type:
   ```
   No problem! Feel free to reach out if you need help later. You can also contact IT support directly at support@company.com
   ```

4. Click **Save** on the topic.

### Step 11: Test the Password Reset Topic with Freshdesk

1. Click **Save** to save all changes to the topic.

2. Open the **Test your copilot** pane on the right side.

3. Type: `I want to create a ticket` and press Enter.

4. The copilot should respond and trigger the Password Reset Support topic.

5. When asked if you want to create a support ticket, respond: **Yes**

6. When asked for the subject, type:
   ```
   Password Reset Request
   ```

7. When asked for the description, type:
   ```
   I forgot my password and need assistance resetting it. I've tried the self-service portal but encountered errors.
   ```

8. Wait for the confirmation message indicating the ticket was created successfully.

### Step 12: Verify Ticket in Freshdesk

1. Open a new tab and navigate to your **Freshdesk portal**:
   ```
   https://your-account.freshdesk.com
   ```

2. Sign in if prompted.

3. Click on **Tickets** in the left navigation.

4. You should see a new ticket with:
   - **Subject:** Password Reset Request
   - **Description:** The description you provided
   - **Priority:** Medium
   - **Status:** Open
   - **Requester:** Your email address

5. Click on the ticket to view full details.

6. Verify all information is correctly populated.

### Step 13: Test Again with Different Inputs

1. Go back to Copilot Studio's test pane.

2. Click **Restart** to start a fresh conversation.

3. Type: `I forgot my password`

4. Go through the topic flow.

5. When creating a ticket, provide different details:
   - **Subject:** `Account Locked Out`
   - **Description:** `My account is locked after multiple failed login attempts`

6. Verify the ticket is created.

7. Check Freshdesk again to see the second ticket appears.

## Success Criteria
✅ Freshdesk connector successfully added to Password Reset Support topic  
✅ Connection established using API Key and Account URL  
✅ Subject and Description variables collected from users  
✅ Freshdesk "Create a ticket" action configured with dynamic variables  
✅ Ticket priority and status set appropriately  
✅ Test tickets created successfully in Copilot Studio  
✅ Tickets visible in Freshdesk portal with correct information  
✅ All ticket fields populated accurately  

## Additional Resources
- [Freshdesk connector in Power Platform](https://learn.microsoft.com/connectors/freshdesk/)  
- [Use connectors in Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/advanced-flow)  
- [Freshdesk API documentation](https://developers.freshdesk.com/api/)

---

Now, click **Next** to continue to **Challenge 05: Add Freshdesk Connector to Remaining Topics**.
