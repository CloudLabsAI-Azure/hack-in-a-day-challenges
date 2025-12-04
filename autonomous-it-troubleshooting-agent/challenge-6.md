# Challenge 06: Deploy to Teams & Test End-to-End

## Introduction
The final step is to deploy your IT Helpdesk Copilot to Microsoft Teams, making it accessible to all employees in your organization. Teams provides the perfect channel for IT support, with chat, notifications, and approval workflows all in one place.

In this challenge, you will publish your copilot, add it to Teams, and perform comprehensive end-to-end testing of the entire automation workflow.

## Challenge Objectives
- Publish the copilot from Copilot Studio
- Deploy the copilot to Microsoft Teams
- Test complete user journey from Teams
- Verify approval workflow in Teams
- Validate ticket management in Microsoft Lists

## Steps to Complete

### Step 1: Publish Your Copilot

1. In **Copilot Studio**, ensure you're in your **IT Helpdesk Copilot - <inject key="DeploymentID"></inject>**.

2. Click **Publish** in the top-right corner (or in the left navigation).

3. Review the pre-publish checklist:
   - Topics are configured
   - Knowledge sources are active
   - Flows are connected

4. Click **Publish** to deploy the latest version.

5. Wait for publishing to complete (this may take 1-2 minutes).

6. You'll see a success message when publishing is done.

### Step 2: Configure Teams Channel

1. After publishing, click **Channels** in the left navigation.

2. Find **Microsoft Teams** in the available channels list.

3. Click on **Microsoft Teams** to expand options.

4. Click **Turn on Teams** or **Open** (if already enabled).

5. You'll see options for Teams deployment:
   - **For you and your teammates** - Adds to your Teams
   - **For your organization** - Submits to Teams app catalog (requires admin approval)

6. Select **Availability options** → **Show to everyone in my org**.

7. Click **Submit for admin approval** (or **Add to Teams** if you have permissions).

### Step 3: Add Copilot to Your Teams

1. Open **Microsoft Teams** (desktop or web):

   ```
   https://teams.microsoft.com
   ```

2. Sign in with your credentials:
   - **Email/Username:** <inject key="AzureAdUserEmail"></inject>
   - **Password:** <inject key="AzureAdUserPassword"></inject>

3. In Teams, click **Apps** in the left sidebar.

4. Search for **IT Helpdesk Copilot** (or the name you gave it).

5. Click on your copilot in the search results.

6. Click **Add** to add it to your Teams.

7. The copilot chat will open automatically.

### Step 4: Test Password Reset Flow in Teams

1. In the copilot chat in Teams, type:
   ```
   I forgot my password
   ```

2. Follow the conversation:
   - Answer any questions the copilot asks
   - Review the self-service reset instructions
   - When asked if you want to create a ticket, respond: **Yes**

3. Provide additional information if prompted:
   - Email address
   - Problem description

4. Verify you receive a ticket ID and confirmation message.

5. Open **Microsoft Lists** in a browser:
   - Navigate to **IT Helpdesk Tickets - <inject key="DeploymentID"></inject>**
   - Find the newly created ticket
   - Verify all details are correct

### Step 5: Test VPN Issues with High Priority

1. Start a new conversation in Teams with the copilot.

2. Type:
   ```
   VPN authentication keeps failing and I can't work
   ```

3. Go through the troubleshooting steps.

4. When asked about creating a ticket:
   - Say **Yes**
   - Indicate this is **urgent** or **high priority** (if prompted)

5. The ticket should be created with **High** priority.

6. Check **Teams** → **Approvals** app:
   - Click on **Approvals** in the left Teams sidebar
   - You should see a new approval request for the VPN ticket
   - Review the ticket details

7. Click **Approve** to approve the ticket.

8. Go back to **Microsoft Lists**:
   - Refresh the helpdesk tickets list
   - Find the VPN ticket
   - Verify the status changed to **In Progress**

9. Check your email:
   - You should have received an approval confirmation email

### Step 6: Test Slow Laptop Scenario

1. Start another conversation in the copilot.

2. Type:
   ```
   My laptop is running really slow and programs keep freezing
   ```

3. Answer the diagnostic questions:
   - Symptoms, boot time, disk space, etc.

4. Follow the suggested troubleshooting steps.

5. Create a ticket if the issue persists.

6. Verify ticket creation with **Medium** priority.

7. Check Lists - the ticket should be auto-assigned (no approval needed for medium priority).

### Step 7: Test Printer Support

1. Start a new conversation.

2. Type:
   ```
   The office printer keeps showing as offline
   ```

3. Go through printer troubleshooting:
   - Check printer status
   - Restart print spooler
   - Clear print queue

4. If unresolved, create a ticket.

5. Verify ticket creation in Lists with appropriate category.

### Step 8: Test Knowledge Base Responses

1. Test questions that should be answered from the knowledge base without ticket creation:

   - "What are the password requirements?"
   - "What's the VPN server address?"
   - "How do I check Task Manager?"
   - "How do I add a printer?"

2. Verify the copilot provides helpful responses from the it-support.pdf knowledge base.

3. Ensure responses are accurate and contextual.

### Step 9: Test Approval Rejection Flow

1. Create another high-priority ticket in Teams.

2. Go to **Teams** → **Approvals**.

3. This time, click **Reject** on the approval request.

4. Add a rejection comment: "Please try standard troubleshooting first"

5. Go to **Microsoft Lists**:
   - Find the rejected ticket
   - Verify status is **Closed**

6. Check your email for the rejection notification.

### Step 10: Review Analytics and Insights

1. Go back to **Copilot Studio**.

2. Click **Analytics** in the left navigation.

3. Review the dashboard:
   - **Total sessions** - Number of conversations
   - **Engagement rate** - User interaction level
   - **Resolution rate** - How often issues were resolved
   - **Escalation rate** - How often tickets were created

4. Click **Topics** to see which topics are used most frequently.

5. Identify any topics with high abandonment rates that may need improvement.

### Step 11: Share Copilot with Team Members

1. In Teams, go to your copilot chat.

2. Click the **...** (More options) at the top.

3. Select **Share**.

4. Choose how to share:
   - **Copy link** - Share the link with colleagues
   - **Add to a team** - Make it available in a specific Teams channel
   - **Add to a chat** - Add to group conversations

5. Share with at least one colleague for testing (if available).

### Step 12: Document Your Solution

1. Create a quick reference guide that includes:
   - How to access the IT Helpdesk Copilot in Teams
   - What types of issues it can help with
   - How to escalate issues
   - Expected response times

2. Share this guide with your team.

## Success Criteria
✅ Copilot successfully published from Copilot Studio  
✅ Copilot deployed and accessible in Microsoft Teams  
✅ All 4 topic scenarios tested end-to-end in Teams  
✅ Tickets created successfully with correct information in Lists  
✅ High-priority tickets trigger approval workflow in Teams  
✅ Approval and rejection flows work correctly  
✅ Email notifications sent at appropriate stages  
✅ Knowledge base provides accurate responses without escalation  
✅ Analytics show conversation metrics and topic usage  
✅ Copilot shared with team members for broader access  

## Additional Resources
- [Publish your copilot](https://learn.microsoft.com/microsoft-copilot-studio/publication-fundamentals-publish-channels)  
- [Deploy to Microsoft Teams](https://learn.microsoft.com/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams)  
- [Analyze copilot performance](https://learn.microsoft.com/microsoft-copilot-studio/analytics-overview)  
- [Share your copilot](https://learn.microsoft.com/microsoft-copilot-studio/admin-share-bots)

---

## 🎉 Congratulations!

You have successfully built an **AI-powered IT Helpdesk Automation Copilot** using Microsoft Copilot Studio and Power Automate!

### What You Accomplished:
✅ Created an intelligent conversational assistant with knowledge base  
✅ Built 4 automated support topics using generative AI  
✅ Integrated Power Automate flows for ticket creation  
✅ Implemented Teams approval workflow for critical issues  
✅ Deployed to Microsoft Teams for organization-wide access  
✅ Reduced manual helpdesk workload through automation  

### Next Steps:
- Monitor analytics to identify improvement opportunities
- Add more topics for additional support scenarios
- Integrate with other systems (ServiceNow, Jira, etc.)
- Customize responses based on user feedback
- Expand knowledge base with more documentation

### Business Impact:
- ⚡ **Faster Response Times** - 24/7 instant support
- 📉 **Reduced Ticket Volume** - Self-service resolution
- 😊 **Improved User Satisfaction** - Quick issue resolution
- 💰 **Cost Savings** - Automated repetitive tasks
- 📊 **Better Insights** - Data-driven support improvements

Great work on completing this challenge! 🚀
