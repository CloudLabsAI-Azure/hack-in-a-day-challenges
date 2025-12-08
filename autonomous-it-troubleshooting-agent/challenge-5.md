# Challenge 05: Test Your IT Helpdesk Copilot End-to-End

## Introduction
Now that you've built your IT Helpdesk Copilot with 3 topics, a reusable Freshdesk flow, and knowledge base integration, it's time to thoroughly test the complete solution. End-to-end testing ensures all components work together seamlessly—from user input to ticket creation in Freshdesk.

In this challenge, you will test all 3 topics comprehensively, verify Freshdesk flow integration, confirm tickets are created in Freshdesk, and validate the entire user experience.

## Challenge Objectives
- Test all 3 topics in Copilot Studio test pane
- Verify Freshdesk flow integration for each topic
- Confirm tickets are created in Freshdesk portal
- Validate ticket details (subject, description, priority, requester email)
- Test knowledge base responses for common queries
- Identify and fix any conversation flow issues

## Steps to Complete

### Step 1: Prepare Your Test Environment

1. Open your **IT Support Copilot** in Copilot Studio.

2. Ensure all 3 topics are **enabled**:
   - CredentialResetSupport
   - VPNConnectivitySupport
   - HardwareSupportAssistant

3. Verify your **Freshdesk** flow is **published** (check in Actions list).

4. Open a second browser tab or window with **Freshdesk** portal:
   ```
   https://your-account.freshdesk.com
   ```

5. Sign in to Freshdesk to monitor ticket creation in real-time.

6. Keep both windows visible for testing.

### Step 2: Test CredentialResetSupport Topic

1. In Copilot Studio, open the **Test your copilot** pane.

2. Start a fresh conversation by clicking **Reset** (trash icon).

3. Type a trigger phrase:
   ```
   I forgot my password
   ```

4. Follow the conversation flow:
   - Answer questions about username
   - Respond to reset instructions
   - When asked if you need to escalate, say: **Yes, create a ticket**

5. Verify the copilot:
   - Calls the Freshdesk flow
   - Displays confirmation message
   - Shows appropriate response

6. **Switch to Freshdesk portal** → Go to **Tickets** section.

7. Verify the new ticket:
   - **Subject:** Should contain "Password Reset Assistance"
   - **Description:** Should mention username and issue details
   - **Priority:** Medium
   - **Requester Email:** Should match your email
   - **Status:** Open

### Step 3: Test VPNConnectivitySupport Topic

1. Reset the conversation in the test pane.

2. Type:
   ```
   VPN won't connect
   ```

3. Follow the conversation:
   - Provide error details
   - Answer troubleshooting questions
   - Request ticket creation

4. Ensure the topic triggers correctly and provides relevant troubleshooting steps.

5. When ticket is created, verify:
   - Confirmation message is displayed
   - Ticket appears in Freshdesk

6. In **Freshdesk**, check the new ticket:
   - **Subject:** Should contain "Connectivity Issue" with location
   - **Description:** Should include error message and location details
   - **Priority:** Medium
   - **Status:** Open

### Step 4: Test HardwareSupportAssistant Topic

1. Reset the test conversation.

2. Type:
   ```
   My laptop is slow
   ```

3. Complete the conversation flow:
   - Describe symptoms (freezing, slow boot, etc.)
   - Follow diagnostic suggestions
   - Escalate to ticket creation

4. Verify topic provides helpful diagnostic steps before escalation.

5. Check ticket confirmation message in copilot.

6. In **Freshdesk**, verify the ticket:
   - **Subject:** Contains "Hardware Issue" with device type
   - **Description:** Includes device type and issue description
   - **Priority:** Medium
   - **Status:** Open

### Step 5: Test Knowledge Base Integration

Test if your copilot can answer questions directly from the **IT_Support_QA.pdf** knowledge base without creating tickets.

1. Reset the conversation.

2. Ask a general IT question:
   ```
   How do I clear my browser cache?
   ```

3. Verify the copilot:
   - Provides a direct answer from knowledge base
   - Does NOT trigger a topic unnecessarily
   - Offers helpful instructions

4. Try another knowledge base query:
   ```
   What are the system requirements for our VPN client?
   ```

5. Check if the response comes from the uploaded knowledge base.

6. If responses are generic, verify:
   - Knowledge source is enabled in **Settings** → **Generative AI**
   - **IT_Support_QA.pdf** is uploaded and indexed with status **Ready**

### Step 6: Test Multiple Tickets in Sequence

1. Create 3 tickets in quick succession to test flow reliability:
   - Credential reset ticket (CredentialResetSupport)
   - VPN connectivity ticket (VPNConnectivitySupport)
   - Hardware issue ticket (HardwareSupportAssistant)

2. Verify all 3 tickets appear in Freshdesk.

3. Ensure no duplicate tickets are created.

### Step 7: Test Edge Cases and Error Handling

1. Test what happens if user provides incomplete information:
   - Start CredentialResetSupport topic
   - Skip username when asked
   - See how copilot handles it

2. Test fallback behavior:
   - Type something unrelated: `What's the weather today?`
   - Verify copilot uses fallback topic appropriately

3. Test error handling (if API fails):
   - If possible, temporarily disconnect Freshdesk connection
   - Try creating a ticket
   - Verify copilot provides graceful error message

4. Reconnect Freshdesk connection after testing.

### Step 8: Verify Ticket Details in Freshdesk

1. In **Freshdesk**, go to **Tickets** → View all open tickets.

2. For each test ticket, verify:
   - All required fields are populated correctly
   - No missing or null values
   - Priority levels match topic configuration
   - Description provides enough context for IT team

3. Check if tickets are assigned to any agent or group (optional based on your Freshdesk setup).

### Step 9: Test Conversation Flow Quality

1. Evaluate each topic for conversation quality:
   - Are questions clear and relevant?
   - Are responses helpful and accurate?
   - Is the tone appropriate for IT helpdesk?
   - Are transitions smooth?

2. If any topic feels generic or unhelpful:
   - Go to **Topics** → Open the specific topic
   - Edit message nodes to improve clarity
   - Add more context or instructions
   - Save and retest

### Step 10: Document Test Results

1. Create a simple test results log:

   | Topic | Trigger Phrase | Ticket Created | Priority | Status |
   |-------|----------------|----------------|----------|--------|
   | CredentialResetSupport | I forgot my password | Yes | Medium | Pass |
   | VPNConnectivitySupport | VPN won't connect | Yes | Medium | Pass |
   | HardwareSupportAssistant | My laptop is slow | Yes | Medium | Pass |
   | Knowledge Base | Password reset steps | N/A | N/A | Pass |

2. Note any issues encountered during testing.

3. Document any required fixes or improvements.

### Step 11: Fix Issues (If Any)

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

### Step 12: Final Verification

1. Complete one final end-to-end test for each topic.

2. Verify in Freshdesk:
   - All tickets are created successfully
   - Ticket details are accurate
   - No errors in ticket creation

3. Check copilot behavior:
   - All topics trigger correctly
   - Conversation flows are smooth
   - Ticket confirmations are displayed

4. Your copilot is now ready for deployment!

## Success Criteria
- All 3 topics tested successfully in Copilot Studio
- Each topic correctly triggers from appropriate phrases
- Freshdesk flow is called from each topic without errors
- Tickets appear in Freshdesk portal with correct details
- Confirmation messages are displayed to users
- Knowledge base queries return accurate responses
- Edge cases and error scenarios handled gracefully
- Conversation flows are clear and helpful
- Test results documented  

## Additional Resources
- [Test your copilot](https://learn.microsoft.com/microsoft-copilot-studio/authoring-test-bot)  
- [Debug topic flows](https://learn.microsoft.com/microsoft-copilot-studio/authoring-create-edit-topics)  
- [Freshdesk API troubleshooting](https://developers.freshdesk.com/api/)

Now, click **Next** to continue to **Challenge 06: Publish Your Copilot to Microsoft Teams**.
