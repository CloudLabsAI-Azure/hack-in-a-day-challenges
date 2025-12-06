# Challenge 04: Create Topics Using Generative AI

## Introduction
Instead of manually building conversation flows from scratch, Microsoft Copilot Studio allows you to create topics using generative AI. Simply describe what you want the topic to do, and AI will generate the conversation flow, trigger phrases, and responses automatically. You'll then connect these topics to your Freshdesk flow for ticket escalation.

In this challenge, you will create 3 essential IT helpdesk topics using generative AI: Credential Reset Support, VPN Connectivity Support, and Hardware Support Assistant. Each topic will call your published Freshdesk flow when escalation is needed.

## Challenge Objectives
- Use Copilot Studio's generative AI to create 3 topics
- Connect each topic to your published Freshdesk flow
- Map topic variables to flow inputs
- Test topics with flow integration

## Steps to Complete

### Step 1: Navigate to Topics Section

1. In your **IT Support Copilot**, click **Topics** in the left navigation pane.

2. You'll see existing system topics (Conversation Start, Fallback, Error).

3. Click **+ Add** or **+ New topic** at the top.

4. Select **Create from description with Copilot** (or similar option for AI-generated topics).

### Step 2: Create Topic 1 - Credential Reset Support

1. In the topic creation dialog, enter the following:

    - **Name:** `CredentialResetSupport`
    - **Description:**

    ```
    Help users who need password reset assistance when they forget their password or their account becomes locked. Ask the user for their username and save it as a variable. Use generative answers to provide self-service reset instructions by referring to the uploaded knowledge sources whenever possible. After sharing the steps, ask the user whether they were able to reset their password successfully. If not, offer to create a support ticket. When creating the ticket, generate a subject line such as "Password Reset Assistance – <username>" and create a detailed description that includes the username and the reason they were unable to reset the password. Map these values to the Freshdesk Power Automate flow inputs for Subject and Description so the flow receives the correct variables. This topic should act as a guided password-reset helper that uses the knowledge base first, and escalates to ticket creation only when needed.
    ```

2. Click **Create** or **Generate**.

3. Wait for the AI to generate the topic (15-30 seconds).

4. Review the generated topic:

   - **Trigger phrases:** Verify it includes phrases like:
     - "I forgot my password"
     - "Reset my password"
     - "Account locked"
     - "Can't log in"
     - "Password reset"

5. Review the conversation flow:
   - Should ask for username and save as variable
   - Should provide self-service reset instructions using knowledge base
   - Should ask if issue is resolved
   - Should offer escalation to ticket creation

6. Click **Save** to keep this topic.

### Step 3: Create Topic 2 - VPN Connectivity Support

1. Click **+ Add** → **Create from description with Copilot**.

2. Enter the following:

    - **Name:** `VPNConnectivitySupport`
    - **Description:**

        ```
        Assist users experiencing VPN or general internet connectivity issues. Ask the user what exact problem or error message they are seeing and save that response as a variable. Ask where the user is working from, such as home, office, or another location, and save that as another variable. Provide basic troubleshooting steps including checking internet connection, verifying Wi-Fi status, restarting the VPN client, checking login credentials, reconnecting to the network, and any other basic connectivity checks. After giving these steps, ask the user whether the issue is resolved. If the user says no, offer to create a support ticket. When creating the ticket, generate a subject line using the location variable, for example "Connectivity Issue – <location>," and generate a detailed description that includes the user's reported error message and the location information. Map these values to the Freshdesk Power Automate flow inputs for Subject and Description so the flow receives the correct variables. This topic should handle all VPN and internet issues but exclude hardware problems, as those are handled in another topic.
        ```

3. Click **Create** or **Generate**.

4. Review and customize:

   - **Trigger phrases:** Verify phrases like:
     - "VPN not connecting"
     - "VPN authentication failed"
     - "Can't connect to VPN"
     - "Internet not working"
     - "Connectivity issues"
     - "Network problems"

5. Review the conversation flow:
   - Should ask about error message and save as variable
   - Should ask about location (home/office) and save as variable
   - Should provide troubleshooting steps
   - Should ask if issue is resolved
   - Should offer ticket creation with location in subject

6. Click **Save**.

### Step 4: Create Topic 3 - Hardware Support Assistant

1. Click **+ Add** → **Create from description with Copilot**.

2. Enter the following:

    - **Name:** `HardwareSupportAssistant`
    - **Description:**

        ```
        Create a hardware support topic that handles all common device issues, including laptops, mice, keyboards, monitors, printers, headphones, docking stations, network adapters, and any other device. Begin by asking the user which device they are having trouble with and save this selection as a variable, then ask them to describe the issue in their own words and save that as another variable. Provide troubleshooting steps based on the selected device: for laptops, include steps for slow performance, freezing, overheating, slow boot, high CPU or memory usage, updates, restart, disk cleanup, and malware checks; for printers, include steps for offline issues, paper jams, blank pages, print queue problems, restarting the spooler, reconnecting cables, reloading paper, and power cycling; for mice and keyboards, include USB or Bluetooth checks, battery checks, driver checks, cleaning stuck keys, and re-pairing; for monitors, include steps for no display, flickering, resolution problems, cable or port checks, brightness and power checks; for headphones and microphones, include audio settings, mic testing, Bluetooth reconnecting, resetting, and driver updates; and for docking stations or network adapters, include cable checks, restarting the dock, firmware checks, and adapter resets. For any "other device," provide general troubleshooting such as checking cables, restarting the device, and verifying drivers. After the troubleshooting steps, ask the user whether the issue is resolved. If not, offer to create a support ticket. When creating the ticket, generate a subject like "Hardware Issue – <device>" and a description that includes the user's reported issue details and device type, and map these values to the Freshdesk Power Automate flow as the Subject and Description inputs.
        ```

3. Click **Create** or **Generate**.

4. Review and customize:
   - **Trigger phrases:** Verify phrases like:
     - "My laptop is slow"
     - "Printer not working"
     - "Mouse not responding"
     - "Keyboard issue"
     - "Monitor problems"
     - "Hardware issue"
     - "Device not working"

5. Review the conversation flow:
   - Should ask which device and save as variable
   - Should ask to describe the issue and save as variable
   - Should provide device-specific troubleshooting steps
   - Should ask if issue is resolved
   - Should offer ticket creation with device type in subject

6. Click **Save**.

### Step 5: Review All Topics

1. In the **Topics** list, verify you now have 3 custom topics:
   - CredentialResetSupport
   - VPNConnectivitySupport
   - HardwareSupportAssistant

2. Ensure all topics are **enabled** (toggle should be on).

### Step 6: Connect Topics to Freshdesk Flow

Now connect each topic to your published **Freshdesk** flow. The AI-generated topics should already have the conversation flow with variables captured. You'll add the action to call the Freshdesk flow when escalation is needed.

#### For CredentialResetSupport Topic:

1. Open **CredentialResetSupport** topic in the editor.

2. Locate the point in the conversation where the user indicates the issue is NOT resolved (after troubleshooting).

3. At that escalation point, add a new node:
   - Click **+** → **Call an action** → Select **Freshdesk** flow.

4. Map the flow inputs using the variables captured in the topic:
   - **Subject:** `"Password Reset Assistance - " & Topic.Username`
   - **Description:** `"User unable to reset password. Username: " & Topic.Username & ". Additional details: " & Topic.IssueReason`

   > **Note:** Variable names may differ based on AI generation. Use the actual variable names from your generated topic (e.g., `Topic.username`, `Topic.UserName`, etc.).

5. After the flow action, add a **Message** node:
   - Type: `"I've created a support ticket for your password reset request. Our IT team will contact you shortly."`

6. Save the topic.

#### For VPNConnectivitySupport Topic:

1. Open **VPNConnectivitySupport** topic.

2. Locate the point where the user indicates the issue is NOT resolved (after troubleshooting).

3. Add **Call an action** node at the escalation point → Select **Freshdesk** flow.

4. Map inputs using the variables captured in the topic:
   - **Subject:** `"Connectivity Issue - " & Topic.Location`
   - **Description:** `"User experiencing connectivity problems. Location: " & Topic.Location & ". Error/Issue: " & Topic.ErrorMessage`

   > **Note:** Use the actual variable names from your generated topic for location and error message.

5. Add a **Message** node:
   - Type: `"I've created a support ticket for your connectivity issue. Our IT team will contact you shortly."`

6. Save the topic.

#### For HardwareSupportAssistant Topic:

1. Open **HardwareSupportAssistant** topic.

2. Locate the point where the user indicates the issue is NOT resolved (after troubleshooting).

3. Add **Call an action** node → Select **Freshdesk** flow.

4. Map inputs using the variables captured in the topic:
   - **Subject:** `"Hardware Issue - " & Topic.Device`
   - **Description:** `"User experiencing hardware problems. Device: " & Topic.Device & ". Issue description: " & Topic.IssueDescription`

   > **Note:** Use the actual variable names from your generated topic for device type and issue description.

5. Add a **Message** node:
   - Type: `"I've created a support ticket for your hardware issue. Our IT team will contact you shortly."`

6. Save the topic.

### Step 7: Test Topics with Flow Integration

1. Open the **Test your copilot** pane.

2. Test **CredentialResetSupport** topic:
   - Type: "I forgot my password"
   - Provide username when asked
   - Review the self-service instructions
   - Indicate issue is not resolved
   - Verify ticket creation confirmation message

3. Test **VPNConnectivitySupport** topic:
   - Type: "VPN won't connect"
   - Describe the error message
   - Provide location (home/office)
   - Follow troubleshooting steps
   - Indicate issue is not resolved
   - Verify ticket is created with location in subject

4. Test **HardwareSupportAssistant** topic:
   - Type: "My laptop is slow" or "Printer not working"
   - Select device type when asked
   - Describe the issue
   - Follow troubleshooting steps
   - Indicate issue is not resolved
   - Verify ticket is created with device type in subject

5. For each test, ensure:
   - Topic triggers correctly
   - Variables are captured properly
   - Troubleshooting steps are provided
   - Flow is called with proper inputs when escalated
   - Confirmation message is displayed

## Success Criteria
- Created 3 topics using generative AI (CredentialResetSupport, VPNConnectivitySupport, HardwareSupportAssistant)
- All topics have relevant trigger phrases configured
- Topics capture user input in variables (username, location, device, error messages, etc.)
- Connected each topic to your Freshdesk flow via "Call an action"
- Mapped flow inputs (Subject and Description) correctly using topic variables
- Test pane successfully creates tickets through topics with dynamic subject lines
- Confirmation messages are displayed to users  

## Additional Resources
- [Create topics with Copilot](https://learn.microsoft.com/microsoft-copilot-studio/authoring-create-edit-topics)  
- [Use generative AI for topic creation](https://learn.microsoft.com/microsoft-copilot-studio/nlu-authoring)  
- [Call flows from topics](https://learn.microsoft.com/microsoft-copilot-studio/authoring-call-action)

Now, click **Next** to continue to **Challenge 05: Test Your IT Helpdesk Copilot End-to-End**.
