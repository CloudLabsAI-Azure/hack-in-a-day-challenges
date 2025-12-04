# Challenge 06: Publish Your Copilot to Microsoft Teams

## Introduction
The final step is to deploy your Customer Care Copilot to Microsoft Teams, making it accessible to customers and support teams in your organization. Teams is the perfect channel for customer service interactions where support teams already collaborate and communicate.

In this challenge, you will publish your copilot, add it to Teams, test the complete customer experience, and share it with your organization.

## Challenge Objectives
- Publish your copilot from Copilot Studio
- Add the copilot to Microsoft Teams
- Test the complete customer journey in Teams
- Configure availability and permissions
- Share the copilot with your organization

## Steps to Complete

### Step 1: Publish Your Copilot

1. In **Copilot Studio**, ensure you're in your **Customer Care Copilot**.

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

4. Search for **Customer Care Copilot**.

5. Click on your copilot in the search results.

6. Click **Add** to add it to your Teams.

7. The copilot chat will open automatically.

### Step 4: Test Your Copilot in Teams

1. In the copilot chat in Teams, type:
   ```
   Track my order
   ```

2. Follow the conversation:
   - Provide order number when asked
   - Review the tracking information provided
   - When prompted, indicate you need assistance

3. Verify you receive a helpful confirmation message that the support ticket was created.

4. Try another test:
   ```
   I want to return a product
   ```

5. Verify the return topic triggers correctly and provides return policy information.

6. Test knowledge base query:
   ```
   What is your shipping policy?
   ```

7. Verify response comes from your knowledge base.

### Step 5: Configure Copilot Availability

1. Go back to **Copilot Studio** → **Channels** → **Microsoft Teams**.

2. Review availability settings:
   - **Show to everyone in my org** - Recommended for organization-wide access
   - **Show to users or groups** - For limited rollout
   - **Hide from others** - For testing only

3. Select **Show to everyone in my org** (or appropriate option).

4. Click **Save**.

### Step 6: Share Copilot with Your Team

1. In **Teams**, with your copilot open, click **Share** (if available).

2. Alternatively, copy the copilot link from Copilot Studio:
   - Go to **Channels** → **Microsoft Teams**
   - Click **Availability options**
   - Copy the **Share link**

3. Share this link via:
   - Email to your team
   - Teams channel announcement
   - Company intranet

4. Example message to share:
   ```
   New Customer Care Copilot Available

   Get instant customer service support directly in Teams. Our new copilot can help with:
   - Order tracking
   - Product returns
   - Delivery delays
   - Service complaints

   Click here to start chatting: [Copilot Link]
   ```

### Step 7: Pin Copilot in Teams (Optional)

1. In **Teams**, right-click on your copilot in the left sidebar.

2. Select **Pin** to keep it easily accessible.

3. You can also add it to a specific team or channel:
   - Go to a team → Click **+** to add a tab
   - Search for your copilot
   - Add it as a tab for easy access

### Step 8: Test from Customer Perspective (Optional)

If you have access to a test account:

1. Sign in to Teams with a different user account.

2. Search for your Customer Care Copilot in Teams Apps.

3. Add it and test:
   - Trigger a topic
   - Create a test ticket
   - Verify it appears in Freshdesk

4. This validates the end-customer experience.

### Step 9: Configure Bot Settings (Optional)

1. In **Copilot Studio**, go to **Settings** → **General**.

2. Review and configure:
   - **Icon:** Upload a custom icon for your copilot
   - **Color:** Set brand colors
   - **Description:** Add helpful description for users

3. Update **Conversation Start** topic:
   - Go to **Topics** → **Conversation Start**
   - Customize welcome message:
     ```
     Welcome to Customer Care Support

     I can help you with:
     - Order tracking and delivery status
     - Product returns and exchanges
     - Delivery delays and issues
     - Service complaints and feedback

     Or ask me any customer service question.

     How may I assist you today?
     ```

4. Save and republish.

### Step 10: Monitor Usage and Performance

1. In **Copilot Studio**, go to **Analytics** in the left navigation.

2. Review metrics:
   - **Total sessions:** How many conversations
   - **Engagement rate:** Customer interaction level
   - **Resolution rate:** Topics successfully completed
   - **Escalation rate:** How often tickets are created

3. Identify improvement opportunities:
   - Topics with low resolution
   - Common fallback triggers
   - Frequently asked questions

4. Iterate and improve based on analytics.

### Step 11: Review All Tickets in Freshdesk

1. Open **Freshdesk portal** in a browser.

2. Go to **Tickets** → View all open tickets.

3. Review tickets created from Teams:
   - Verify all tickets from your testing appear
   - Check ticket details are accurate
   - Confirm all tickets have Medium priority and Open status

4. Test ticket management in Freshdesk:
   - Assign a ticket to yourself
   - Add a note or comment
   - Update ticket status to "In Progress"

5. This validates the complete integration flow.

## Success Criteria
- Copilot successfully published from Copilot Studio
- Copilot deployed and accessible in Microsoft Teams
- All 4 topics tested successfully in Teams
- Tickets created through Teams appear in Freshdesk
- Confirmation messages are displayed to customers in Teams
- Knowledge base queries work correctly in Teams
- Copilot availability configured appropriately
- Share link created and distributed
- Analytics reviewed for usage insights
- Complete solution working end-to-end

## Additional Resources
- [Publish your copilot](https://learn.microsoft.com/microsoft-copilot-studio/publication-fundamentals-publish-channels)
- [Deploy to Microsoft Teams](https://learn.microsoft.com/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams)
- [Analyze copilot performance](https://learn.microsoft.com/microsoft-copilot-studio/analytics-overview)
- [Share your copilot](https://learn.microsoft.com/microsoft-copilot-studio/admin-share-bots)

---

## Congratulations

You have successfully built an **AI-powered Customer Care Copilot** using Microsoft Copilot Studio and Power Automate.

### What You Accomplished:
- Created an intelligent Customer Care Copilot with knowledge base
- Built 4 automated customer service topics using generative AI
- Created reusable Customer Service Request flow in Copilot Studio
- Integrated Freshdesk API for ticket management
- Deployed to Microsoft Teams for organization-wide access
- Reduced manual customer service workload through automation
- Built the entire solution with Copilot Studio agent flows

### Next Steps:
- Monitor analytics to identify improvement opportunities
- Add more topics for additional service scenarios
- Customize Freshdesk ticket fields for your needs
- Add priority-based routing in Freshdesk
- Create automation rules in Freshdesk for ticket assignment
- Expand knowledge base with more customer service documentation
- Configure SLA policies in Freshdesk for response times

### Business Impact:
- **Faster Response Times** - 24/7 instant customer service
- **Reduced Ticket Volume** - Self-service resolution via knowledge base
- **Improved Customer Satisfaction** - Quick issue resolution in Teams
- **Better Ticket Management** - Centralized customer service in Freshdesk
- **Cost Savings** - Reduced manual support workload and automated repetitive tasks
- **Better Insights** - Data-driven customer service improvements

Great work on completing this challenge.
