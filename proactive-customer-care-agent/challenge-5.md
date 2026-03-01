# Challenge 05: Test Your Proactive Customer Care Agent End-to-End

## Introduction
Now that you've built your Proactive Customer Care Agent with 4 topics and a reusable CustomerServiceFlow, it's time to thoroughly test the complete solution. End-to-end testing ensures all components work together seamlessly from customer input to ticket creation in Freshdesk.

In this challenge, you will test all 4 topics comprehensively, verify CustomerServiceFlow integration, confirm tickets are created in Freshdesk, and validate the entire customer experience.
 
## Challenge Objectives
 - Test all 4 topics in Copilot Studio test pane
 - Verify CustomerServiceFlow integration for each topic
 - Confirm tickets are created in Freshdesk portal
 - Validate ticket details (subject, description, priority, requester email)
 - Test knowledge base responses for common queries
 - Identify and fix any conversation flow issues

## Steps to Complete

### Step 1: Prepare Your Test Environment

1. Open your **Customer Care Copilot Agent** in Copilot Studio.

1. Ensure all 4 topics are **enabled**:
   - OrderTrackingAssistance
   - ProductReturnProcessing
   - DeliveryDelayManagement
   - ServiceQualityComplaintHandling

1. Verify your **CustomerServiceFlow** is **published** (check in Actions list).

1. Open a second browser tab or window with the **Freshdesk** portal by navigating to the following URL:
   ```
   https://your-account.freshdesk.com
   ```

1. Sign in to Freshdesk to monitor ticket creation in real-time.

1. Keep both windows visible for testing.

### Step 2: Test OrderTrackingAssistance Topic

1. In Copilot Studio, open the **Test your copilot** pane.

1. Start a fresh conversation by clicking **Reset** (trash icon).

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

### Step 3: Test ProductReturnProcessing Topic

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

### Step 4: Test DeliveryDelayManagement Topic

1. Reset the test conversation.

1. Type the following:
   ```
   My delivery is late
   ```

1. Complete the conversation flow:
   - Provide order number (e.g., ORD345678)
   - Describe delivery issue (e.g., "Order should have arrived 3 days ago")
   - Indicate issue is not resolved

1. Verify topic provides helpful delay information before escalation.

1. Check ticket confirmation message in the agent.

1. In **Freshdesk**, verify the ticket:
   - **Subject:** Contains "Delivery Delay - ORD345678"
   - **Description:** Includes order number and delay details
   - **Priority:** Medium
   - **Status:** Open

### Step 5: Test ServiceQualityComplaintHandling Topic

1. Reset the conversation.

1. Type the following:
   ```
   I have a complaint about your service
   ```

1. Complete the conversation:
   - Describe complaint details (e.g., "The product quality is poor and customer service was rude")
   - Provide order number if asked (e.g., ORD901234)
   - Indicate not satisfied with proposed solutions

1. Verify topic provides empathetic response and resolution options.

1. Check ticket confirmation message.

1. In **Freshdesk**, verify the ticket:
   - **Subject:** Contains "Service Quality Complaint - ORD901234"
   - **Description:** Includes complaint details and order information
   - **Priority:** Medium
   - **Status:** Open

### Step 6: Test Knowledge Base Integration

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
   - All four PDF files are uploaded and indexed

### Step 7: Test Multiple Tickets in Sequence

1. Create 4 tickets in quick succession to test flow reliability:
   - Order tracking ticket
   - Product return ticket
   - Delivery delay ticket
   - Service complaint ticket

1. Verify all 4 tickets appear in Freshdesk.

1. Ensure no duplicate tickets are created.

### Step 8: Test Edge Cases and Error Handling

1. Test what happens if customer provides incomplete information:
   - Start order tracking topic
   - Skip order number when asked
   - See how the agent handles it

1. Test fallback behavior:
   - Type something unrelated: "What's the weather today?"
   - Verify the agent uses the fallback topic appropriately

1. Test error handling if API fails:
   - If possible, temporarily disconnect Freshdesk connection
   - Try creating a ticket
   - Verify the agent provides a graceful error message

1. Reconnect Freshdesk connection after testing.

### Step 9: Verify Ticket Details in Freshdesk

1. In **Freshdesk**, go to **Tickets** → View all open tickets.

1. For each test ticket, verify:
   - All required fields are populated correctly
   - No missing or null values
   - Priority levels match flow configuration (Medium)
   - Description provides enough context for the customer service team

1. Check if tickets are assigned to any agent or group (optional based on your Freshdesk setup).

### Step 10: Test Conversation Flow Quality

1. Evaluate each topic for conversation quality:
   - Are questions clear and relevant?
   - Are responses helpful and accurate?
   - Is the tone appropriate for customer service?
   - Are transitions smooth?

1. If any topic feels generic or unhelpful:
   - Go to **Topics** → Open the specific topic
   - Edit message nodes to improve clarity
   - Add more context or instructions
   - Save and retest

### Step 11: Document Test Results

1. Create a simple test results log:

   | Topic | Trigger Phrase | Ticket Created | Priority | Status |
   |-------|----------------|----------------|----------|--------|
   | OrderTrackingAssistance | Track my order | Yes | Medium | Pass |
   | ProductReturnProcessing | Return a product | Yes | Medium | Pass |
   | DeliveryDelayManagement | Delivery is late | Yes | Medium | Pass |
   | ServiceQualityComplaintHandling | Have a complaint | Yes | Medium | Pass |
   | Knowledge Base | Return policy | N/A | N/A | Pass |

1. Note any issues encountered during testing.

1. Document any required fixes or improvements.

### Step 12: Fix Issues (If Any)

If you encounter issues during testing:

1. **Topic not triggering:**
   - Go to **Topics** → Open the topic
   - Add more trigger phrases
   - Save and retest

1. **Flow not being called:**
   - Verify "Call an action" node is correctly configured
   - Check flow is published
   - Verify flow input mappings

1. **Ticket not appearing in Freshdesk:**
   - Check Freshdesk connection in Copilot Studio
   - Verify API Key and Account URL are correct
   - Test flow independently in Actions

1. **Incorrect ticket details:**
   - Review variable mappings in "Call an action" node
   - Ensure variables are captured in topic conversation
   - Update mappings and retest

### Step 13: Final Verification

1. Complete one final end-to-end test for each topic.

1. Verify in Freshdesk:
   - All tickets are created successfully
   - Ticket details are accurate
   - No errors in ticket creation

1. Check agent behavior:
   - All topics trigger correctly
   - Conversation flows are smooth
   - Ticket confirmations are displayed

1. Your agent is now ready for deployment.

## Success Criteria
- All 4 topics tested successfully in Copilot Studio
- Each topic correctly triggers from appropriate phrases
- CustomerServiceFlow is called from each topic without errors
- Tickets appear in Freshdesk portal with correct details
- Confirmation messages are displayed to customers
- Knowledge base queries return accurate responses
- Edge cases and error scenarios handled gracefully
- Conversation flows are clear and helpful
- Test results documented

## Additional Resources
- [Test your copilot](https://learn.microsoft.com/microsoft-copilot-studio/authoring-test-bot)
- [Debug topic flows](https://learn.microsoft.com/microsoft-copilot-studio/authoring-create-edit-topics)
- [Freshdesk API troubleshooting](https://developers.freshdesk.com/api/)

---

Click **Next** at the bottom of the page to proceed to the next page.

   ![](./media/pro-activ-gg-g21.png)