# Challenge 05: Add Teams Notifications with Adaptive Cards

## Introduction
For high-priority tickets or when IT manager approval is needed, you want to send rich, interactive notifications directly to Microsoft Teams. Copilot Studio supports sending adaptive cards to Teams channels, allowing IT managers to view ticket details and take action without leaving Teams.

In this challenge, you'll add Teams notifications with adaptive cards for high-priority tickets, all within Copilot Studio without external Power Automate flows.

## Challenge Objectives
- Add conditional logic to detect high-priority tickets
- Send adaptive cards to Teams channel for manager review
- Include ticket details in interactive cards
- Test notifications in Microsoft Teams

## Steps to Complete

### Step 1: Create Teams Channel for IT Notifications

1. Open **Microsoft Teams** (desktop or web):

   ```
   https://teams.microsoft.com
   ```

2. Sign in with your credentials:
   - **Email/Username:** <inject key="AzureAdUserEmail"></inject>
   - **Password:** <inject key="AzureAdUserPassword"></inject>

3. Create a new team or use an existing one:
   - Click **Teams** in the left sidebar
   - Click **Join or create a team**
   - Click **Create team**
   - Select **From scratch**
   - Select **Private**
   - Name: `IT Support Team - <inject key="DeploymentID"></inject>`
   - Click **Create**

4. Add a channel for tickets:
   - In your team, click **...** next to the team name
   - Select **Add channel**
   - Name: `High Priority Tickets`
   - Privacy: **Standard**
   - Click **Add**

5. Note the team and channel names for later use.

### Step 2: Get Teams Channel ID

1. In the **High Priority Tickets** channel, click **...** (More options) at the top.

2. Select **Get link to channel**.

3. Copy the link - it contains the team and channel IDs you'll need.

4. The URL format is:
   ```
   https://teams.microsoft.com/l/channel/CHANNEL_ID/channel-name?groupId=TEAM_ID
   ```

5. Save both IDs for later (or you can use the channel name in Copilot Studio).

### Step 3: Modify VPN Topic for High-Priority Detection

1. Go back to **Copilot Studio** → **Topics** → **VPN Troubleshooting**.

2. Find the "Create a record" action you added in Challenge 04.

3. After the ticket creation action, click **+** to add a new node.

4. Select **Add a condition**.

5. Configure the condition to check priority:
   - **Variable:** (Create or select a variable that holds priority, e.g., `TicketPriority`)
   - **Operator:** `is equal to`
   - **Value:** `High`

### Step 4: Add Teams Message Action

1. In the **Condition is met** branch (High priority), click **+**.

2. Select **Call an action** → **Send a message to Teams**.

3. If this action isn't available, you may need to:
   - Click **Call an action** → **Create a flow**
   - Select **Post a message to Teams** template
   - Or use a simpler message node and manually configure later

4. Configure the Teams message:
   - **Team:** Select or enter `IT Support Team - <inject key="DeploymentID"></inject>`
   - **Channel:** Select or enter `High Priority Tickets`
   - **Message:** Use an adaptive card JSON (see Step 5)

### Step 5: Create Adaptive Card JSON

1. For the message content, use this adaptive card template:

```json
{
  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
  "type": "AdaptiveCard",
  "version": "1.4",
  "body": [
    {
      "type": "TextBlock",
      "text": "🚨 High Priority IT Ticket",
      "weight": "Bolder",
      "size": "Large",
      "color": "Attention"
    },
    {
      "type": "FactSet",
      "facts": [
        {
          "title": "Ticket ID:",
          "value": "${TicketID}"
        },
        {
          "title": "Category:",
          "value": "${IssueCategory}"
        },
        {
          "title": "User:",
          "value": "${UserEmail}"
        },
        {
          "title": "Priority:",
          "value": "High"
        },
        {
          "title": "Status:",
          "value": "New"
        }
      ]
    },
    {
      "type": "TextBlock",
      "text": "Description:",
      "weight": "Bolder"
    },
    {
      "type": "TextBlock",
      "text": "${IssueDescription}",
      "wrap": true
    }
  ],
  "actions": [
    {
      "type": "Action.OpenUrl",
      "title": "View in Power Apps",
      "url": "https://make.powerapps.com"
    }
  ]
}
```

2. Replace `${TicketID}`, `${IssueCategory}`, etc. with actual variables from your topic using the `{x:VariableName}` syntax in Copilot Studio.

### Step 6: Alternative - Use Simple Teams Message

If adaptive cards are complex, use a simpler approach:

1. Instead of "Send adaptive card", use **Send a message** or **Post to Teams channel**.

2. Compose a formatted message:
   ```
   🚨 **High Priority IT Ticket Created**
   
   **Ticket ID:** {x:System.CreatedRecordId}
   **Category:** VPN Issues
   **User:** {x:UserEmail}
   **Priority:** High
   **Status:** New
   
   **Description:**
   {x:IssueDescription}
   
   Please review and assign this ticket to an IT technician.
   ```

3. Select the Teams channel where this message should be posted.

4. Click **Save**.

### Step 7: Test High-Priority Ticket with Teams Notification

1. Open the **Test your copilot** pane in Copilot Studio.

2. Start a new conversation.

3. Type: `VPN authentication keeps failing and I can't access any company resources`

4. Go through the troubleshooting steps.

5. When asked to create a ticket, say **Yes**.

6. Ensure the priority is set to **High** (you may need to adjust topic logic to automatically set VPN issues as High priority).

7. Complete the ticket creation.

### Step 8: Verify Teams Notification

1. Go to **Microsoft Teams** → **IT Support Team** → **High Priority Tickets** channel.

2. You should see a new message with the ticket details.

3. If using an adaptive card, verify all fields are populated correctly.

4. If not, check the topic flow and variable mappings.

### Step 9: Add Teams Notification to Other High-Priority Scenarios

1. Go to **Topics** → **Slow Laptop Performance**.

2. Find the section where you determine if disk space is critical (C drive is red).

3. If this indicates high priority, add the same Teams notification logic:
   - Condition: Priority is High
   - Action: Send Teams message with ticket details

4. Repeat for any other scenarios that warrant manager notification.

5. Click **Save** on each topic.

### Step 10: Optional - Add Approval Buttons to Adaptive Card

If you want managers to approve/reject directly from Teams:

1. Modify the adaptive card JSON to include action buttons:

```json
"actions": [
  {
    "type": "Action.Submit",
    "title": "Approve",
    "style": "positive",
    "data": {
      "action": "approve",
      "ticketId": "${TicketID}"
    }
  },
  {
    "type": "Action.Submit",
    "title": "Reject",
    "style": "destructive",
    "data": {
      "action": "reject",
      "ticketId": "${TicketID}"
    }
  },
  {
    "type": "Action.OpenUrl",
    "title": "View Ticket",
    "url": "https://make.powerapps.com"
  }
]
```

2. Note: Handling button clicks requires additional Power Automate logic or a webhook, which goes beyond pure Copilot Studio.

3. For this challenge, displaying information is sufficient.

### Step 11: Test Multiple Scenarios

1. Create several high-priority tickets:
   - VPN issue (High)
   - Critical disk space (High)
   - General password reset (Medium - should NOT notify Teams)

2. Verify:
   - High-priority tickets appear in Teams channel
   - Medium/Low priority tickets do NOT spam the channel
   - All ticket details are accurate

### Step 12: Configure Channel Notifications

1. In Teams, in the **High Priority Tickets** channel, click **...** → **Channel notifications settings**.

2. Set notifications to:
   - **All new posts**
   - **Banner and feed**

3. This ensures IT managers get immediate alerts for high-priority tickets.

4. Click **Save**.

## Success Criteria
✅ Teams channel created for IT notifications  
✅ High-priority ticket detection logic added to topics  
✅ Teams messages or adaptive cards sent for high-priority tickets  
✅ Ticket details correctly displayed in Teams channel  
✅ Medium/Low priority tickets do not trigger Teams notifications  
✅ Test high-priority ticket successfully posted to Teams  
✅ All notifications contain accurate ticket information  

## Additional Resources
- [Adaptive Cards overview](https://adaptivecards.io/)  
- [Post messages to Teams from Copilot](https://learn.microsoft.com/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams)  
- [Conditional branching in topics](https://learn.microsoft.com/microsoft-copilot-studio/authoring-create-edit-topics)

---

Now, click **Next** to continue to **Challenge 06: Deploy to Teams & Test End-to-End**.
