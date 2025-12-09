# Challenge 06: Publish Your Copilot to Microsoft Teams

## Introduction
The final step is to deploy your IT Helpdesk Copilot to Microsoft Teams, making it accessible to employees in your organization. Teams is the perfect channel for IT support—employees can get help directly where they already collaborate and communicate.

In this challenge, you will publish your copilot, add it to Teams, test the complete user experience, and share it with your organization.

## Challenge Objectives
- Publish your copilot from Copilot Studio
- Add the copilot to Microsoft Teams
- Test the complete user journey in Teams
- Configure availability and permissions
- Share the copilot with your organization

## Steps to Complete

### Step 1: Publish Your Copilot

1. In **Copilot Studio**, ensure you're in your **IT Support Copilot**.

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

4. Search for **IT Support Copilot**.

5. Click on your copilot in the search results.

6. Click **Add** to add it to your Teams.

7. The copilot chat will open automatically.

### Step 4: Test Your Copilot in Teams

1. In the copilot chat in Teams, type:
   ```
   I forgot my password
   ```

2. Follow the conversation:
   - Provide your username when asked
   - Review the self-service reset instructions from knowledge base
   - When asked if issue is resolved, say: **No**
   - Confirm you want to create a ticket

3. Verify you receive a confirmation message that the support ticket was created.

4. Try another test:
   ```
   VPN won't connect
   ```

5. Verify the VPNConnectivitySupport topic triggers, provides troubleshooting steps, and creates a ticket when escalated.

6. Test hardware topic:
   ```
   My laptop is slow
   ```

7. Verify HardwareSupportAssistant topic provides device-specific troubleshooting.

8. Test knowledge base query:
   ```
   What are the password reset steps?
   ```

9. Verify response comes from your IT_Support_QA.pdf knowledge base.

### Step 5: Configure Copilot Availability

1. Go back to **Copilot Studio** → **Channels** → **Microsoft Teams**.

2. Review availability settings:
   - **Show to everyone in my org** - Recommended for company-wide access
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
   New IT Support Copilot Available!

   Get instant IT support directly in Teams. Our new copilot can help with:
   - Credential resets and account lockouts
   - VPN and connectivity issues
   - Hardware troubleshooting (laptops, printers, monitors, keyboards)
   - And more!

   Click here to start chatting: [Copilot Link]
   ```

### Step 7: Pin Copilot in Teams (Optional)

1. In **Teams**, right-click on your copilot in the left sidebar.

2. Select **Pin** to keep it easily accessible.

3. You can also add it to a specific team or channel:
   - Go to a team → Click **+** to add a tab
   - Search for your copilot
   - Add it as a tab for easy access

### Step 8: Test from Another User's Perspective (Optional)

If you have access to a test account:

1. Sign in to Teams with a different user account.

2. Search for your IT Support Copilot in Teams Apps.

3. Add it and test:
   - Trigger a topic (CredentialResetSupport, VPNConnectivitySupport, or HardwareSupportAssistant)
   - Create a test ticket
   - Verify it appears in Freshdesk

4. This validates the end-user experience.

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
     Welcome to IT Support Copilot!

     I can help you with:
     - Credential resets and account lockouts
     - VPN and connectivity issues  
     - Hardware problems (laptops, printers, monitors, keyboards, etc.)

     Or ask me any IT support question!

     What can I help you with today?
     ```

4. Save and republish.

### Step 10: Monitor Usage and Performance

1. In **Copilot Studio**, go to **Analytics** in the left navigation.

2. Review metrics:
   - **Total sessions:** How many conversations
   - **Engagement rate:** User interaction level
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

<validation step="6d77e727-80a0-4147-8484-e70b51cd78e3" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria
- Copilot successfully published from Copilot Studio
- Copilot deployed and accessible in Microsoft Teams
- All 3 topics tested successfully in Teams (CredentialResetSupport, VPNConnectivitySupport, HardwareSupportAssistant)
- Tickets created through Teams appear in Freshdesk with correct subject lines and descriptions
- Confirmation messages are displayed to users in Teams after ticket creation
- Knowledge base queries return responses from IT_Support_QA.pdf
- Copilot availability configured appropriately for organization
- Share link created and distributed to team
- Analytics reviewed for usage insights
- Complete end-to-end solution working from Teams to Freshdesk  

## Additional Resources
- [Publish your copilot](https://learn.microsoft.com/microsoft-copilot-studio/publication-fundamentals-publish-channels)  
- [Deploy to Microsoft Teams](https://learn.microsoft.com/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams)  
- [Analyze copilot performance](https://learn.microsoft.com/microsoft-copilot-studio/analytics-overview)  
- [Share your copilot](https://learn.microsoft.com/microsoft-copilot-studio/admin-share-bots)

## Congratulations!

You have successfully built an **AI-powered IT Helpdesk Automation Copilot** using Microsoft Copilot Studio!

### Real-World Applications:
This solution can transform IT operations across:
- **IT Support & Helpdesk** - Password resets, VPN issues, hardware troubleshooting
- **Employee Onboarding** - Equipment setup, account provisioning, access requests
- **Service Desk Automation** - Ticket triage, incident management, self-service support
- **Infrastructure Management** - Network diagnostics, system monitoring alerts
- **Software Support** - Application troubleshooting, license management, update assistance
- **Security & Compliance** - Access reviews, security incident reporting, policy enforcement

Congratulations on completing this challenge!
