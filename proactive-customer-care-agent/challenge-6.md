# Challenge 06: Publish Your Agent to Microsoft Teams

## Introduction
The final step is to deploy your Proactive Customer Care Agent to Microsoft Teams, making it accessible to customers and support teams in your organization. Teams is the perfect channel for customer service interactions where support teams already collaborate and communicate.

In this challenge, you will publish your agent, add it to Teams, test the complete customer experience, and share it with your organization.

## Challenge Objectives
- Publish your agent from Copilot Studio
- Add the agent to Microsoft Teams
- Test the complete customer journey in Teams
- Configure availability and permissions
- Share the agent with your organization

## Steps to Complete

### Step 1: Publish Your Agent

1. In **Copilot Studio**, ensure you're in your **Proactive Customer Care Agent**.

1. Click **Publish** in the top-right corner (or in the left navigation).

1. Review the pre-publish checklist:
   - Topics are configured
   - Knowledge sources are active
   - Flows are connected

1. Click **Publish** to deploy the latest version.

1. Wait for publishing to complete (this may take 1-2 minutes).

1. You'll see a success message when publishing is done.

### Step 2: Configure Teams Channel

1. After publishing, click **Channels** in the left navigation.

1. Find **Microsoft Teams** in the available channels list.

1. Click on **Microsoft Teams** to expand options.

1. Click **Turn on Teams** or **Open** (if already enabled).

1. You'll see options for Teams deployment:
   - **For you and your teammates** - Adds to your Teams
   - **For your organization** - Submits to Teams app catalog (requires admin approval)

1. Select **Availability options** → **Show to everyone in my org**.

1. Click **Submit for admin approval** (or **Add to Teams** if you have permissions).

### Step 3: Add the Agent to Your Teams

1. Open **Microsoft Teams** (desktop or web) by navigating to the following URL:

   ```
   https://teams.microsoft.com
   ```

1. Sign in with your credentials:
   - **Email/Username:** <inject key="AzureAdUserEmail"></inject>
   - **Password:** <inject key="AzureAdUserPassword"></inject>

1. In Teams, click **Apps** in the left sidebar.

1. Search for **Proactive Customer Care Agent**.

1. Click on your agent in the search results.

1. Click **Add** to add it to your Teams.

1. The agent chat will open automatically.

### Step 4: Test Your Agent in Teams

1. In the agent chat in Teams, type the following:
   ```
   Track my order
   ```

1. Follow the conversation:
   - Provide order number when asked
   - Review the tracking information provided
   - When prompted, indicate you need assistance

1. Verify you receive a helpful confirmation message that the support ticket was created.

1. Try another test by typing the following:
   ```
   I want to return a product
   ```

1. Verify the return topic triggers correctly and provides return policy information.

1. Test a knowledge base query by typing the following:
   ```
   What is your shipping policy?
   ```

1. Verify response comes from your knowledge base.

<validation step="ee184267-2451-441d-a53d-a838535aa8a6" />
 
> **Congratulations** on completing the task! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding task. If you receive a success message, you can proceed to the next task. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria
- Agent successfully published from Copilot Studio
- Agent deployed and accessible in Microsoft Teams
- All 4 topics tested successfully in Teams
- Tickets created through Teams appear in Freshdesk

## Additional Resources
- [Publish your copilot](https://learn.microsoft.com/microsoft-copilot-studio/publication-fundamentals-publish-channels)
- [Deploy to Microsoft Teams](https://learn.microsoft.com/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams)
- [Analyze copilot performance](https://learn.microsoft.com/microsoft-copilot-studio/analytics-overview)
- [Share your copilot](https://learn.microsoft.com/microsoft-copilot-studio/admin-share-bots)

## Congratulations!

You have successfully built an **AI-powered Proactive Customer Care Agent** using Microsoft Copilot Studio!

### Real-World Applications:
This solution can transform customer service across:
- **E-commerce & Retail** - Order tracking, returns, delivery issues, product inquiries
- **Telecommunications** - Service quality complaints, billing questions, technical support
- **Banking & Finance** - Account inquiries, transaction disputes, card services
- **Travel & Hospitality** - Booking assistance, cancellations, itinerary changes
- **Healthcare** - Appointment scheduling, insurance claims, patient inquiries
- **SaaS & Technology** - Subscription management, product support, feature requests

Congratulations on completing this challenge!
