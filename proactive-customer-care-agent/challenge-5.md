# Challenge 05: Test Your Proactive Customer Care Agent End-to-End

## Introduction
Now that you've built your Proactive Customer Care Agent with 4 topics and a reusable CustomerServiceFlow, it's time to thoroughly test the complete solution. End-to-end testing ensures all components work together seamlessly from customer input to ticket creation in Freshdesk.

In this challenge, you will test all 4 topics comprehensively, verify CustomerServiceFlow integration, confirm tickets are created in Freshdesk, and validate the entire customer experience.
 
## Challenge Objectives
- Prepare Your Test Environment
- Test 1 Customer Care Copilot Agent
- Test 2 Customer Care Copilot Agent
- Test 3 Knowledge Base Integration
- Verify Ticket Details in Freshdesk

## Steps to Complete

### Step 1: Prepare Your Test Environment

1. Open your **Customer Care Copilot Agent** in Copilot Studio.

1. Click on **Publish**.

1. In the **Publish this agent** pane, click on **Publish**.

1. Wait for the **Customer Care Copilot Agent** to be **published**.

1. In a separate browser tab, navigate back to the **Freshdesk** portal.

1. Keep both windows visible for testing.

### Step 2: Test 1 Customer Care Copilot Agent

1. Click the **Test** button to open the test panel on the right side.

1. Type the following trigger phrase:
   ```
   Track my order
   ```

1. Follow the conversation flow:
   - Provide order number when asked (e.g., ORD123456)
   - Review tracking information provided
   - When asked if you need additional assistance, say: **Yes, I need help**

1. Verify the agent:
   - Calls the CustomerServiceFlow
   - Displays confirmation message
   - Shows appropriate response

1. Switch to Freshdesk portal → Go to **Tickets** section.

1. Verify the new ticket:
   - **Subject:** Should contain "Order Tracking Request - ORD123456"
   - **Description:** Should mention order number and tracking issue
   - **Priority:** Medium
   - **Requester Email:** Should match your email
   - **Status:** Open

### Step 3: Test 2 Customer Care Copilot Agent

1. Reset the conversation in the test pane.

1. Type the following:
   ```
   I want to return a product
   ```

1. Follow the conversation:
   - Provide order number (e.g., ORD789012)
   - Describe return reason (e.g., "Product is defective")
   - Request assistance with processing

1. Ensure the topic triggers correctly and provides relevant return policy information.

1. When ticket is created, verify:
   - Confirmation message is displayed
   - Ticket appears in Freshdesk

1. In **Freshdesk**, check the new ticket:
   - **Subject:** Should contain "Product Return Request - ORD789012"
   - **Description:** Should include order number and return reason
   - **Priority:** Medium
   - **Status:** Open

### Step 4: Test 3 Knowledge Base Integration

Test if your agent can answer questions directly from the knowledge base without creating tickets.

1. Reset the conversation.

1. Ask a general customer service question by typing the following:
   ```
   What is your return policy?
   ```

1. Verify the agent:
   - Provides a direct answer from knowledge base
   - Does NOT trigger a topic unnecessarily
   - Offers helpful policy information

1. Try another knowledge base query by typing the following:
   ```
   How long does shipping take?
   ```

1. Check if the response comes from the uploaded knowledge base.

1. If responses are generic, verify:
   - Knowledge sources are enabled in **Settings** → **Generative AI**
   - All four files are uploaded and indexed

### Step 5: Verify Ticket Details in Freshdesk

1. In **Freshdesk**, go to **Tickets** → View all open tickets.

1. Review the newly created tickets.

## Success Criteria
- Prepare Your Test Environment
- Test 1 Customer Care Copilot Agent
- Test 2 Customer Care Copilot Agent
- Test 3 Knowledge Base Integration
- Verify Ticket Details in Freshdesk

## Additional Resources
- [Test your copilot](https://learn.microsoft.com/microsoft-copilot-studio/authoring-test-bot)
- [Debug topic flows](https://learn.microsoft.com/microsoft-copilot-studio/authoring-create-edit-topics)
- [Freshdesk API troubleshooting](https://developers.freshdesk.com/api/)

---

Click **Next** at the bottom of the page to proceed to the next page.

   ![](./media/pro-activ-gg-g21.png)