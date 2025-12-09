# Challenge 04: Create Topics Using Generative AI

## Introduction
Instead of manually building conversation flows from scratch, Microsoft Copilot Studio allows you to create topics using generative AI. Simply describe what you want the topic to do, and AI will generate the conversation flow, trigger phrases, and responses automatically. You'll then connect these topics to your Freshdesk flow for ticket escalation.

In this challenge, you will create 3 essential IT support topics using generative AI: CredentialResetSupport, VPNConnectivitySupport, and HardwareSupportAssistant. Each topic will call your published Freshdesk flow when escalation is needed.

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

### Step 2: Create Topic 1 - CredentialResetSupport

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

6. **Important:** Check variable scope settings:
   - Click on each variable in the topic
   - If you see an error about "limited scope" or variables not being accessible
   - Enable the checkbox for **"Can be used by other topics"** or **"Receive values from other topics"**

7. Click **Save** to keep this topic.

<validation step="40ad233d-94ef-47d9-93c7-9232dca6bdc2" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

### Step 3: Create Topic 2 - VPNConnectivitySupport

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

6. **Important:** Check variable scope settings:
   - Click on each variable in the topic
   - If you see an error about "limited scope" or variables not being accessible
   - Enable the checkbox for **"Can be used by other topics"** or **"Receive values from other topics"**

7. Click **Save**.

### Step 4: Create Topic 3 - HardwareSupportAssistant

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

6. **Important:** Check variable scope settings:
   - Click on each variable in the topic
   - If you see an error about "limited scope" or variables not being accessible
   - Enable the checkbox for **"Can be used by other topics"** or **"Receive values from other topics"**

7. Click **Save**.

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

3. At that escalation point, you'll see a message node. Click the **three dots (...)** menu on the message node and select **Delete** to remove it.

4. Click the **+** button below where the message was, then select **Add a tool**.

5. In the **Add a tool** pane that opens on the right:
   - Search for **Freshdesk** in the search box
   - Select **Freshdesk** from the list (it should show as "Updated" with your flow description)

6. The **Action** node will be added with your Freshdesk flow's input parameters.

7. Configure the flow inputs by mapping the variables captured in the topic:
   
   - For **Subject** field:
   - Click on the **Subject** input field
   - Click the **{x}** icon to open variable selector
   - Select the appropriate variable from your generated topic
   
   - For **Description** field:
   - Click on the **Description** input field
   - Click the **{x}** icon to open variable selector
   - Select the relevant variables that capture the issue details

   > **Note:** If your topic doesn't have all the required variables, you may need to add additional **Question** nodes in your topic to collect missing information before calling the flow.

8. After configuring the flow inputs, click the **+** button below the Action node.

9. Select **Send a message** to add a **Message** node.

10. In the message field, type:
    ```
    I've created a support ticket for your password reset request. Our IT team will contact you shortly.
    ```

11. Click **Save** at the top to save the topic.

#### For VPNConnectivitySupport Topic:

1. Open **VPNConnectivitySupport** topic in the editor.

2. Locate the point where the user indicates the issue is NOT resolved (after troubleshooting).

3. Delete any existing message node at the escalation point by clicking **three dots (...)** → **Delete**.

4. Click the **+** button, then select **Add a tool**.

5. Search for and select **Freshdesk** from the tool list.

6. Configure the flow inputs:
   
   - For **Subject** field:
   - Click the input field and then the **{x}** icon
   - Select the appropriate variable from your topic
   
   - For **Description** field:
   - Click the input field and then the **{x}** icon
   - Select the relevant variables that capture the connectivity issue details

   > **Note:** If your topic doesn't capture all necessary information, add **Question** nodes to collect missing details before calling the flow.

7. Click **+** below the Action node and select **Send a message**.

8. Type the message:
   ```
   I've created a support ticket for your connectivity issue. Our IT team will contact you shortly.
   ```

9. Click **Save** to save the topic.

#### For HardwareSupportAssistant Topic:

1. Open **HardwareSupportAssistant** topic in the editor.

2. Locate the point where the user indicates the issue is NOT resolved (after troubleshooting).

3. Delete any existing message node at the escalation point by clicking **three dots (...)** → **Delete**.

4. Click the **+** button, then select **Add a tool**.

5. Search for and select **Freshdesk** from the tool list.

6. Configure the flow inputs:
   
   - For **Subject** field:
   - Click the input field and then the **{x}** icon
   - Select the device type variable from your topic
   
   - For **Description** field:
   - Click the input field and then the **{x}** icon
   - Select the variables that describe the hardware problem

   > **Note:** If your topic doesn't have the necessary variables, add **Question** nodes to gather the required information before calling the flow.

7. Click **+** below the Action node and select **Send a message**.

8. Type the message:
   ```
   I've created a support ticket for your hardware issue. Our IT team will contact you shortly.
   ```

9. Click **Save** to save the topic.

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
