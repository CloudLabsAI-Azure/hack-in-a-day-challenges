# Challenge 05: Publish Your Agent to Microsoft Teams

## Introduction
The final step is to deploy your Internal Knowledge Navigator agent to Microsoft Teams, making it accessible to employees in your organization. Teams is the perfect channel for knowledge sharing—employees can get help directly where they already collaborate and communicate.

In this challenge, you will publish your agent, add it to Teams, test the complete user experience, and share it with your organization.

## Challenge Objectives
- Publish your agent from Copilot Studio
- Add the agent to Microsoft Teams
- Test all topics and flows in Teams
- Configure availability and permissions
- Share the agent with your organization

## Steps to Complete

### Step 1: Publish Your Agent

1. In **Copilot Studio**, ensure you're in your **Internal Knowledge Navigator** agent.

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

### Step 3: Add Agent to Your Teams

1. Open **Microsoft Teams** (desktop or web):

   ```
   https://teams.microsoft.com
   ```

2. Sign in with your credentials:
   - **Email/Username:** <inject key="AzureAdUserEmail"></inject>
   - **Password:** <inject key="AzureAdUserPassword"></inject>

3. In Teams, click **Apps** in the left sidebar.

4. Search for **Internal Knowledge Navigator**.

5. Click on your agent in the search results.

6. Click **Add** to add it to your Teams.

7. The agent chat will open automatically.

### Step 4: Test Your Agent in Teams

Test all 4 topics you created in Challenge 4:

#### Test DocumentSearch Topic:

1. In the agent chat in Teams, type:
   ```
   Where can I find information about employee benefits?
   ```

2. Verify the agent searches the SharePoint knowledge base and provides relevant information.

3. Try another query:
   ```
   What are the expense reimbursement policies?
   ```

4. Verify generative answers are provided from the knowledge base.

#### Test EmailDocument Topic:

1. Reset the conversation (click the refresh icon or start a new chat).

2. Type:
   ```
   Email me a document
   ```

3. Follow the conversation:
   - Provide the document name (e.g., "HR Handbook")
   - Provide your email address
   - Provide a brief description

4. Verify the flow runs and you receive the confirmation message.

5. Check your email inbox (**<inject key="AzureAdUserEmail"></inject>**) to see if the email was delivered.

#### Test SubmitRequest Topic:

1. Reset the conversation.

2. Type:
   ```
   Submit a request to the team
   ```

3. Follow the conversation:
   - Provide your name
   - Provide your email address
   - Select request type from options
   - Describe your request

4. Verify the flow runs and you receive the confirmation message.

5. Check your Microsoft Teams **Document Request** channel to see if the request was posted.

#### Test NewEmployeeOnboarding Topic:

1. Reset the conversation.

2. Type:
   ```
   I'm a new employee and need help getting started
   ```

3. Ask questions like:
   - "What benefits do I get?"
   - "What's the onboarding process?"
   - "Where can I find IT policies?"

4. Verify the agent provides helpful answers from the knowledge base.

### Step 5: Configure Agent Availability

1. Go back to **Copilot Studio** → **Channels** → **Microsoft Teams**.

2. Review availability settings:
   - **Show to everyone in my org** - Recommended for company-wide access
   - **Show to users or groups** - For limited rollout
   - **Hide from others** - For testing only

3. Select **Show to everyone in my org** (or appropriate option).

4. Click **Save**.

### Step 6: Share Agent with Your Team

1. In **Teams**, with your agent open, click **Share** (if available).

2. Alternatively, copy the agent link from Copilot Studio:
   - Go to **Channels** → **Microsoft Teams**
   - Click **Availability options**
   - Copy the **Share link**

3. Share this link via:
   - Email to your team
   - Teams channel announcement
   - Company intranet

4. Example message to share:
   ```
   New Internal Knowledge Navigator Available!

   Get instant access to company information directly in Teams. Our new agent can help with:
   - Searching company documents
   - Emailing documents to you
   - Submitting requests to the team
   - New employee onboarding

   Click here to start chatting: [Agent Link]
   ```

### Step 7: Pin Agent in Teams (Optional)

1. In **Teams**, right-click on your agent in the left sidebar.

2. Select **Pin** to keep it easily accessible.

3. You can also add it to a specific team or channel:
   - Go to a team → Click **+** to add a tab
   - Search for your agent
   - Add it as a tab for easy access

### Step 8: Verify Flow Execution

1. Go back to **Copilot Studio**.

2. Click **Flows** in the left navigation.

3. Click on each flow (**Email Document to Employee** and **Send Request to Teams**) to view run history.

4. Verify that the flows were triggered by your Teams tests.

5. Check that the inputs were passed correctly.

6. Ensure all steps in the flows completed successfully.

### Step 9: Monitor Usage and Performance

1. In **Copilot Studio**, go to **Analytics** in the left navigation.

2. Review metrics:
   - **Total sessions:** How many conversations
   - **Engagement rate:** User interaction level
   - **Resolution rate:** Topics successfully completed
   - **Escalation rate:** How often flows are called

3. Identify improvement opportunities:
   - Topics with low resolution
   - Common fallback triggers
   - Frequently asked questions

4. Iterate and improve based on analytics.

## Success Criteria
- Agent successfully published from Copilot Studio
- Agent deployed and accessible in Microsoft Teams
- All 4 topics tested successfully in Teams:
  - DocumentSearch works with generative answers
  - EmailDocument flow sends emails successfully
  - SubmitRequest flow posts to Teams channel
  - NewEmployeeOnboarding provides helpful responses
- Flows execute successfully and appear in run history
- Agent availability configured appropriately
- Share link created and ready to distribute
- Analytics reviewed for usage insights
- Complete solution working end-to-end

## Additional Resources
- [Publish your agent](https://learn.microsoft.com/microsoft-copilot-studio/publication-fundamentals-publish-channels)  
- [Deploy to Microsoft Teams](https://learn.microsoft.com/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams)  
- [Analyze agent performance](https://learn.microsoft.com/microsoft-copilot-studio/analytics-overview)  
- [Share your agent](https://learn.microsoft.com/microsoft-copilot-studio/admin-share-bots)

---

## Congratulations! 🎉

You have successfully built an **AI-powered Internal Knowledge Navigator Agent** using Microsoft Copilot Studio!

### What You Built:
- **Agent with SharePoint Knowledge Source** - Connected 40+ Contoso company documents for intelligent search
- **4 AI-Generated Conversational Topics** - Document search, email delivery, request submission, and employee onboarding
- **2 Agent Flows** - Automated email and Teams channel notifications created entirely in Copilot Studio
- **Teams Deployment** - Organization-wide access through Microsoft Teams integration

### Real-World Applications:
This solution can transform knowledge management across:
- **HR & Employee Services** - Onboarding, policies, benefits inquiries
- **IT Support** - Self-service help desk, documentation access
- **Compliance & Training** - Policy distribution, procedure guidance
- **Sales Enablement** - Playbooks, product information, pricing guidelines
- **Operations** - Process documentation, vendor management, procurement workflows

### Next Steps & Enhancements:
- **Expand Knowledge Base** - Add more departments and document types
- **Advanced Analytics** - Track top queries and identify knowledge gaps
- **Multi-Language Support** - Serve global teams with localized content
- **Integration** - Connect to CRM, ticketing systems, or HR platforms
- **Proactive Notifications** - Send policy updates or reminders through the agent
- **Voice & Mobile** - Enable voice interactions and mobile app access

Great work on completing this challenge! 🚀 
