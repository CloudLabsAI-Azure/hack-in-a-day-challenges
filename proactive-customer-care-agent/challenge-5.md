# Challenge 05: Test Your Customer Care Copilot End-to-End

## Introduction
Now that you've built your Customer Care Copilot with 4 topics, a reusable Customer Service Request flow, and knowledge base integration, it's time to thoroughly test the complete solution. End-to-end testing ensures all components work together seamlessly from customer input to ticket creation in Freshdesk.

In this challenge, you will test all 4 topics comprehensively, verify Customer Service Request flow integration, confirm tickets are created in Freshdesk, and validate the entire customer experience.
 
## Challenge Objectives
 - Test all 4 topics in Copilot Studio test pane
 - Verify CustomerServiceFlow integration for each topic
 - Confirm tickets are created in Freshdesk portal
 - Validate ticket details (subject, description, priority, requester email)
 - Test knowledge base responses for common queries
 - Identify and fix any conversation flow issues

## Steps to Complete

### Step 1: Prepare Your Test Environment

1. Open your **Customer Care Copilot** in Copilot Studio.

2. Ensure all 4 topics are **enabled**:
   - OrderTrackingAssistance
   - ProductReturnProcessing
   - DeliveryDelayManagement
   - ServiceQualityComplaintHandling

3. Verify your **Customer Service Request** flow is **published** (check in Actions list).

4. Open a second browser tab or window with **Freshdesk** portal:
   ```
   https://your-account.freshdesk.com
   ```

5. Sign in to Freshdesk to monitor ticket creation in real-time.

6. Keep both windows visible for testing.

### Step 2: Test OrderTrackingAssistance Topic

1. In Copilot Studio, open the **Test your copilot** pane.

2. Start a fresh conversation by clicking **Reset** (trash icon).

3. Type a trigger phrase:
   ```
   Track my order
   ```

4. Follow the conversation flow:
   - Provide order number when asked (e.g., ORD123456)
   - Review tracking information provided
   - When asked if you need additional assistance, say: **Yes, I need help**

5. Verify the copilot:
   - Calls the Customer Service Request flow
   - Displays confirmation message
   - Shows appropriate response

6. Switch to Freshdesk portal → Go to **Tickets** section.

7. Verify the new ticket:
   - **Subject:** Should contain "Order Tracking Request - ORD123456"
   - **Description:** Should mention order number and tracking issue
   - **Priority:** Medium
   - **Requester Email:** Should match your email
   - **Status:** Open

### Step 3: Test ProductReturnProcessing Topic

1. Reset the conversation in the test pane.

2. Type:
   ```
   I want to return a product
   ```

3. Follow the conversation:
   - Provide order number (e.g., ORD789012)
   - Describe return reason (e.g., "Product is defective")
   - Request assistance with processing

4. Ensure the topic triggers correctly and provides relevant return policy information.

5. When ticket is created, verify:
   - Confirmation message is displayed
   - Ticket appears in Freshdesk

6. In **Freshdesk**, check the new ticket:
   - **Subject:** Should contain "Product Return Request - ORD789012"
   - **Description:** Should include order number and return reason
   - **Priority:** Medium
   - **Status:** Open

### Step 4: Test DeliveryDelayManagement Topic

1. Reset the test conversation.

2. Type:
   ```
   My delivery is late
   ```

3. Complete the conversation flow:
   - Provide order number (e.g., ORD345678)
   - Describe delivery issue (e.g., "Order should have arrived 3 days ago")
   - Indicate issue is not resolved

4. Verify topic provides helpful delay information before escalation.

5. Check ticket confirmation message in copilot.

6. In **Freshdesk**, verify the ticket:
   - **Subject:** Contains "Delivery Delay - ORD345678"
   - **Description:** Includes order number and delay details
   - **Priority:** Medium
   - **Status:** Open

### Step 5: Test ServiceQualityComplaintHandling Topic

1. Reset the conversation.

2. Type:
   ```
   I have a complaint about your service
   ```

3. Complete the conversation:
   - Describe complaint details (e.g., "The product quality is poor and customer service was rude")
   - Provide order number if asked (e.g., ORD901234)
   - Indicate not satisfied with proposed solutions

4. Verify topic provides empathetic response and resolution options.

5. Check ticket confirmation message.

6. In **Freshdesk**, verify the ticket:
   - **Subject:** Contains "Service Quality Complaint - ORD901234"
   - **Description:** Includes complaint details and order information
   - **Priority:** Medium
   - **Status:** Open

### Step 6: Test Knowledge Base Integration

Test if your copilot can answer questions directly from the knowledge base without creating tickets.

1. Reset the conversation.

2. Ask a general customer service question:
   ```
   What is your return policy?
   ```

3. Verify the copilot:
   - Provides a direct answer from knowledge base
   - Does NOT trigger a topic unnecessarily
   - Offers helpful policy information

4. Try another knowledge base query:
   ```
   How long does shipping take?
   ```

5. Check if the response comes from the uploaded knowledge base.

6. If responses are generic, verify:
   - Knowledge sources are enabled in **Settings** → **Generative AI**
   - All four PDF files are uploaded and indexed

### Step 7: Test Multiple Tickets in Sequence

1. Create 4 tickets in quick succession to test flow reliability:
   - Order tracking ticket
   - Product return ticket
   - Delivery delay ticket
   - Service complaint ticket

2. Verify all 4 tickets appear in Freshdesk.

3. Ensure no duplicate tickets are created.

### Step 8: Test Edge Cases and Error Handling

1. Test what happens if customer provides incomplete information:
   - Start order tracking topic
   - Skip order number when asked
   - See how copilot handles it

2. Test fallback behavior:
   - Type something unrelated: "What's the weather today?"
   - Verify copilot uses fallback topic appropriately

3. Test error handling if API fails:
   - If possible, temporarily disconnect Freshdesk connection
   - Try creating a ticket
   - Verify copilot provides graceful error message

4. Reconnect Freshdesk connection after testing.

### Step 9: Verify Ticket Details in Freshdesk

1. In **Freshdesk**, go to **Tickets** → View all open tickets.

2. For each test ticket, verify:
   - All required fields are populated correctly
   - No missing or null values
   - Priority levels match flow configuration (Medium)
   - Description provides enough context for customer service team

3. Check if tickets are assigned to any agent or group (optional based on your Freshdesk setup).

### Step 10: Test Conversation Flow Quality

1. Evaluate each topic for conversation quality:
   - Are questions clear and relevant?
   - Are responses helpful and accurate?
   - Is the tone appropriate for customer service?
   - Are transitions smooth?

2. If any topic feels generic or unhelpful:
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

2. Note any issues encountered during testing.

3. Document any required fixes or improvements.

### Step 12: Fix Issues (If Any)

If you encounter issues during testing:

1. **Topic not triggering:**
   - Go to **Topics** → Open the topic
   - Add more trigger phrases
   - Save and retest

2. **Flow not being called:**
   - Verify "Call an action" node is correctly configured
   - Check flow is published
   - Verify flow input mappings

3. **Ticket not appearing in Freshdesk:**
   - Check Freshdesk connection in Copilot Studio
   - Verify API Key and Account URL are correct
   - Test flow independently in Actions

4. **Incorrect ticket details:**
   - Review variable mappings in "Call an action" node
   - Ensure variables are captured in topic conversation
   - Update mappings and retest

### Step 13: Final Verification

1. Complete one final end-to-end test for each topic.

2. Verify in Freshdesk:
   - All tickets are created successfully
   - Ticket details are accurate
   - No errors in ticket creation

3. Check copilot behavior:
   - All topics trigger correctly
   - Conversation flows are smooth
   - Ticket confirmations are displayed

4. Your copilot is now ready for deployment.

## Success Criteria
- All 4 topics tested successfully in Copilot Studio
- Each topic correctly triggers from appropriate phrases
- Customer Service Request flow is called from each topic without errors
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

Now, click **Next** to continue to **Challenge 06: Publish Your Copilot to Microsoft Teams**.
