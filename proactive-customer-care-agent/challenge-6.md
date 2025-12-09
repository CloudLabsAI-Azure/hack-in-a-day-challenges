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

<validation step="ee184267-2451-441d-a53d-a838535aa8a6" />
 
> **Congratulations** on completing the task! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding task. If you receive a success message, you can proceed to the next task. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria
- Copilot successfully published from Copilot Studio
- Copilot deployed and accessible in Microsoft Teams
- All 4 topics tested successfully in Teams
- Tickets created through Teams appear in Freshdesk

## Additional Resources
- [Publish your copilot](https://learn.microsoft.com/microsoft-copilot-studio/publication-fundamentals-publish-channels)
- [Deploy to Microsoft Teams](https://learn.microsoft.com/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams)
- [Analyze copilot performance](https://learn.microsoft.com/microsoft-copilot-studio/analytics-overview)
- [Share your copilot](https://learn.microsoft.com/microsoft-copilot-studio/admin-share-bots)

## Congratulations!

You have successfully built an **AI-powered Customer Care Copilot** using Microsoft Copilot Studio!

### Real-World Applications:
This solution can transform customer service across:
- **E-commerce & Retail** - Order tracking, returns, delivery issues, product inquiries
- **Telecommunications** - Service quality complaints, billing questions, technical support
- **Banking & Finance** - Account inquiries, transaction disputes, card services
- **Travel & Hospitality** - Booking assistance, cancellations, itinerary changes
- **Healthcare** - Appointment scheduling, insurance claims, patient inquiries
- **SaaS & Technology** - Subscription management, product support, feature requests

Congratulations on completing this challenge!
