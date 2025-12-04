# Challenge 02: Create Topics Using Generative AI

## Introduction
Instead of manually building conversation flows from scratch, Microsoft Copilot Studio allows you to create topics using generative AI. Simply describe what you want the topic to do, and AI will generate the conversation flow, trigger phrases, and responses automatically.

In this challenge, you will create 4 essential IT helpdesk topics using generative AI: Password Reset, VPN Issues, Slow Laptop, and Printer Issues.

## Challenge Objectives
- Use Copilot Studio's generative AI to create topics
- Create 4 automated support topics
- Review and customize AI-generated conversation flows
- Test each topic with sample user queries

## Steps to Complete

### Step 1: Navigate to Topics Section

1. In your **IT Helpdesk Copilot - <inject key="DeploymentID"></inject>**, click **Topics** in the left navigation pane.

2. You'll see existing system topics (Conversation Start, Fallback, Error).

3. Click **+ Add** or **+ New topic** at the top.

4. Select **Create from description with Copilot** (or similar option for AI-generated topics).

### Step 2: Create Topic 1 - Password Reset

1. In the topic creation dialog, enter the following 

    - **Name:** Rename to `Password Reset Support`
    - **description:**

    ```
    Help users reset their password when they forget it or their account is locked. Ask for their username, provide self-service reset instructions, and offer to create a ticket if they need additional help.
    ```

2. Click **Create** or **Generate**.

3. Wait for the AI to generate the topic (15-30 seconds).

4. Review the generated topic:

   - **Trigger phrases:** Verify it includes phrases like:
     - "I forgot my password"
     - "Reset my password"
     - "Account locked"
     - "Can't log in"

5. Review the conversation flow:
   - Should ask for username or email
   - Should provide reset instructions
   - Should offer escalation option

6. Click **Save** to keep this topic.

### Step 3: Create Topic 2 - VPN Issues

1. Click **+ Add** → **Create from description with Copilot**.


2. **Name:** Rename to `VPN Troubleshooting`
    - Enter the description:

        ```
        Assist users experiencing VPN connection problems. Ask what error they're seeing, provide troubleshooting steps like checking internet connection and credentials, and offer to escalate if the issue persists.
        ```

3. Click **Create** or **Generate**.

4. Review and customize:

   - **Trigger phrases:** Verify phrases like:
     - "VPN not connecting"
     - "VPN authentication failed"
     - "Can't connect to VPN"
     - "VPN disconnects"

5. Review the flow for troubleshooting steps and escalation path.

6. Click **Save**.

### Step 4: Create Topic 3 - Slow Laptop

1. Click **+ Add** → **Create from description with Copilot**.

2. Enter the description:

   ```
   Help users diagnose and fix slow laptop performance. Ask about symptoms like freezing or slow boot time, suggest checking Task Manager for high CPU or memory usage, recommend disk cleanup, and offer to create a support ticket for hardware issues.
   ```

3. Click **Create** or **Generate**.

4. Review and customize:
   - **Name:** Rename to `Slow Laptop Performance`
   - **Trigger phrases:** Verify phrases like:
     - "My laptop is slow"
     - "Computer running slow"
     - "Laptop freezing"
     - "System lagging"

5. Review the diagnostic flow and recommendations.

6. Click **Save**.

### Step 5: Create Topic 4 - Printer Issues

1. Click **+ Add** → **Create from description with Copilot**.

2. Enter the description:

   ```
   Assist users with printer problems. Ask what issue they're experiencing like offline status, paper jams, or blank pages. Provide troubleshooting steps such as checking printer status, restarting print spooler, and clearing print queue. Offer to escalate if unresolved.
   ```

3. Click **Create** or **Generate**.

4. Review and customize:
   - **Name:** Rename to `Printer Support`
   - **Trigger phrases:** Verify phrases like:
     - "Printer not working"
     - "Printer offline"
     - "Print job stuck"
     - "Printer paper jam"

5. Review the troubleshooting flow.

6. Click **Save**.

### Step 6: Review All Topics

1. In the **Topics** list, verify you now have 4 custom topics:
   - Password Reset Support
   - VPN Troubleshooting
   - Slow Laptop Performance
   - Printer Support

2. Ensure all topics are **enabled** (toggle should be on).

3. Click on each topic to review the conversation flow diagram and make minor adjustments if needed.

### Step 7: Test Topics in Test Pane

1. Open the **Test your copilot** pane.

2. Test each topic with trigger phrases:
   - Type: "I forgot my password" → Should trigger Password Reset Support
   - Type: "VPN won't connect" → Should trigger VPN Troubleshooting
   - Type: "My computer is slow" → Should trigger Slow Laptop Performance
   - Type: "Printer is offline" → Should trigger Printer Support

3. Go through at least one complete conversation flow for each topic.

4. Verify the copilot asks relevant questions and provides appropriate responses.

### Step 8: Refine Topic Responses (Optional)

1. If any response feels generic, click **Edit** on that message node.

2. You can:
   - Add more detailed instructions
   - Include links to internal documentation
   - Add conditional branching for different scenarios

3. Click **Save** after each refinement.

## Success Criteria
✅ Created 4 topics using generative AI in Copilot Studio  
✅ All topics have relevant trigger phrases configured  
✅ Each topic includes conversation flow with questions and responses  
✅ All topics are enabled and functional  
✅ Test pane correctly identifies and triggers each topic  
✅ Conversation flows provide helpful responses from knowledge base  

## Additional Resources
- [Create topics with Copilot](https://learn.microsoft.com/microsoft-copilot-studio/authoring-create-edit-topics)  
- [Use generative AI for topic creation](https://learn.microsoft.com/microsoft-copilot-studio/nlu-authoring)  
- [Trigger phrases best practices](https://learn.microsoft.com/microsoft-copilot-studio/authoring-trigger-phrases)

---

Now, click **Next** to continue to **Challenge 03: Setup Helpdesk & Create Ticket Creation Flow**.
