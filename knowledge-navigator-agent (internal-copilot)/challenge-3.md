# Challenge 03: Design Department Topics

## Introduction
While your copilot can now answer general questions using the uploaded knowledge base, employees often have specific common requests that benefit from structured conversations. In this challenge, you'll create guided conversational topics organized by department to handle the most frequent employee inquiries.

These topics will help employees navigate to the right information quickly by asking clarifying questions and routing them to the appropriate resources based on their department and specific need.

## Challenge Objectives
- Create a topic for HR - Leave Policy inquiries
- Create a topic for Finance - Travel Reimbursement requests
- Create a topic for IT - Software Access requests
- Create a topic for Procurement - Purchase Request process
- Add dynamic branching logic based on user inputs
- Test each department topic thoroughly

## Steps to Complete

### Step 1: Update Conversation Start Topic

1. In **Microsoft Copilot Studio**, ensure your **Internal Knowledge Navigator** agent is open.

2. Select **Topics (1)**, select **All (2)**, then select **Conversation Start (3)**.

   ![image](./media/m-l1-26.png)

3. Keep the first sentence in the message box and update the message by entering the following text **(1)**. Then select **Save (2)**:

   ```
   I'm here to help you find information about company policies and procedures across HR, Finance, IT, and Procurement departments.
   
   You can ask me about leave policies, expense reimbursement, software access, purchase requests, and much more.
   
   I'll provide answers with citations to our official policy documents, and I can also help you with actions like emailing documents or creating support tickets.
   
   What would you like to know today?
   ```

   ![image](./media/30-9-l4-2.png)

### Step 2: Access Topics for Custom Topic Creation

1. Select **Topics (1)** again, choose **+ Add a topic (2)**, and then select **From blank (3)** or **Add from description with Copilot (3)** for faster creation.

   ![image](./media/12-9-m55.png)

### Step 3: Create Knowledge Request Topic (Using Adaptive Card)

This topic will allow employees to submit knowledge requests that get tracked in SharePoint.

1. On the **Add from description with Copilot** page:
   - **Name your topic:** `Knowledge Request Submission (1)`
   - **Create a topic to...:** `User wants to submit a knowledge request or ask about missing information (2)`
   - Then select **Create (3)**

   ![image](./media/12-9-m56.png)

2. On the newly created topic, review the **Trigger node** and **Describe what topic does** box.

   ![image](./media/m-l1-27.png)

3. Update the message node with the below text **(1)** and click **Save (2)**:

   ```
   I'd be happy to help you submit a knowledge request. Please fill out the form below with details about the information you're looking for.
   ```

   ![image](./media/m-l1-28.png)

4. Delete any auto-generated question nodes by clicking **ellipsis (...) (1)** and selecting **Delete (2)**.

   ![image](./media/m-l1-29.png)

5. Continue deleting all question nodes and the final message node until you have only the **Trigger node** and one **message node**.

   ![image](./media/m-l1-30.png)

### Step 4: Add Adaptive Card for Knowledge Request

1. Select **Add node (1)** after the message node, then click **Ask with adaptive card (2)**.

   ![image](./media/12-9-m60.png)

2. Select **Ellipsis(...) (1)** of the Adaptive card node, then select **Properties (2)**.

   ![image](./media/12-9-m61.png)

3. Select **Edit adaptive card**.

   ![image](./media/ex5img25.jpg)

4. Enter the following Adaptive Card Script into the **Card payload editor** after removing the existing script:

   ```json
   {
     "$schema": "https://adaptivecards.io/schemas/adaptive-card.json",
     "type": "AdaptiveCard",
     "version": "1.5",
     "body": [
       {
         "type": "TextBlock",
         "text": "Knowledge Request Form",
         "weight": "Bolder",
         "size": "Medium"
       },
       {
         "type": "Input.ChoiceSet",
         "id": "department",
         "label": "Department",
         "choices": [
           { "title": "HR - Human Resources", "value": "HR" },
           { "title": "Finance", "value": "Finance" },
           { "title": "IT - Information Technology", "value": "IT" },
           { "title": "Procurement", "value": "Procurement" }
         ]
       },
       {
         "type": "Input.Text",
         "id": "requestTitle",
         "placeholder": "Brief title of your request",
         "label": "Request Title"
       },
       {
         "type": "Input.Text",
         "id": "questionDetails",
         "placeholder": "Describe what information you're looking for",
         "label": "Question Details",
         "isMultiline": true
       },
       {
         "type": "Input.ChoiceSet",
         "id": "urgency",
         "label": "Urgency",
         "choices": [
           { "title": "High - Need answer today", "value": "High" },
           { "title": "Medium - Need within a week", "value": "Medium" },
           { "title": "Low - No rush", "value": "Low" }
         ]
       },
       {
         "type": "Input.Text",
         "id": "employeeEmail",
         "placeholder": "Your email address",
         "label": "Your Email"
       }
     ],
     "actions": [
       {
         "type": "Action.Submit",
         "title": "Submit Request"
       }
     ]
   }
   ```

5. After entering the script, review the form design at the top. Select **Save (1)** and then click **Close (2)**.

   ![image](./media/12-9-m62.png)

6. **Close** the **Adaptive card node properties** window.

7. Expand the **Output** section of the Adaptive card and make all variables **Global** by selecting each variable **(1)** and choosing **Global (2)** from the properties window.

   ![image](./media/12-9-m63.png)

8. Select **Save**.

   ![image](./media/12-9-m64.png)

### Step 5: Create HR Leave Policy Topic

For quicker setup, let's use Copilot to generate this topic:

1. Select **Topics**, choose **+ Add a topic**, and select **Add from description with Copilot**.

2. On the **Add from description with Copilot** page:
   - **Name your topic:** `HR - Leave Policy`
   - **Create a topic to...:** `Help employees understand leave policies including annual leave, sick leave, and time-off procedures. Ask what type of leave they want to know about and provide information from HR documents.`
   - Then select **Create**

3. Review the auto-generated conversation flow and trigger phrases.

4. Now build or refine the conversation flow:

   **Node 1: Ask Leave Type**
   - Click **+ Add node** → **Ask a question**
   - **Question:** "What type of leave would you like to know about?"
   - **Identify:** Multiple choice options
   - **Options:**
     - Annual Leave
     - Sick Leave
     - Personal Leave
     - Other
   - **Save response as:** LeaveType

   **Node 2: Ask Specific Question**
   - Click **+** → **Ask a question**
   - **Question:** "What would you like to know about {LeaveType}?"
   - **Identify:** Multiple choice options
   - **Options:**
     - How much leave do I get?
     - How do I request it?
     - What's the approval process?
     - Who do I contact?
   - **Save response as:** LeaveQuestion

   **Node 3: Provide Answer**
   - Click **+** → **Send a message**
   - **Message:** "Let me find that information for you about {LeaveType} - {LeaveQuestion}."
   
   - Click **+** → **Create generative answers**
   - This will use your uploaded HR_Leave_Policy.pdf to answer
   - Configure:
     - **Data sources:** Select HR_Leave_Policy.pdf
     - **How should sources be used:** Search only selected sources

   **Node 4: Offer Further Help**
   - Click **+** → **Ask a question**
   - **Question:** "Would you like to know anything else about leave policies or other HR topics?"
   - **Identify:** Boolean (Yes/No)
   - **Save response as:** NeedMoreHelp
   
   - If Yes → Loop back to ask what else they need
   - If No → End the conversation with a message: "Great! If you need anything else, just ask. Have a great day!"

5. Click **Save** to save the topic.

### Step 3: Create Finance Travel Reimbursement Topic

1. Click **+ New topic** → **From blank**

2. Configure the new topic:
   - **Name:** `Finance - Travel Reimbursement`
   - **Description:** `Guides employees through travel booking and reimbursement process`

3. Add trigger phrases:
   - "I need to book travel"
   - "Travel reimbursement"
   - "How do I get reimbursed for travel"
   - "Business trip expenses"
   - "Travel expense policy"
   - "Submit travel receipts"

4. Build the conversation flow:

   **Node 1: Ask Travel Stage**
   - **Ask a question:** "What stage of the travel process are you in?"
   - **Identify:** Multiple choice
   - **Options:**
     - Planning a trip (pre-approval)
     - Already traveled (reimbursement)
     - General policy questions
   - **Save as:** TravelStage

   **Node 2: Conditional Branching**
   - Add **Condition** node
   - Create separate paths for each TravelStage option

   **Branch 1: Planning a trip**
   - **Send message:** "Great! Let me help you with the pre-approval process."
   - **Create generative answers** from Finance_Travel_Reimbursement.pdf
   - Focus on: booking procedures, approval requirements

   **Branch 2: Already traveled**
   - **Ask question:** "Do you have all your receipts ready?"
   - **Identify:** Boolean
   - If Yes: Provide reimbursement submission instructions
   - If No: Explain what receipts are needed
   - **Create generative answers** from Finance_Travel_Reimbursement.pdf

   **Branch 3: General policy**
   - **Create generative answers** from Finance_Travel_Reimbursement.pdf
   - Allow open-ended questions about the policy

   **Node 3: Offer Document Email**
   - **Send message:** "I can email you the complete Travel Reimbursement policy document if you'd like to review it in detail."
   - **Ask question:** "Would you like me to send you the policy document?"
   - **Identify:** Boolean
   - Note: We'll implement the actual email action in Challenge 5

5. Click **Save**.

### Step 4: Create IT Software Access Topic

1. Click **+ New topic** → **From blank**

2. Configure:
   - **Name:** `IT - Software Access`
   - **Description:** `Helps employees request software installations and access permissions`

3. Add trigger phrases:
   - "I need software access"
   - "How do I install software"
   - "Request software"
   - "I need a license for"
   - "Software installation"
   - "Application access"

4. Build the conversation flow:

   **Node 1: Identify Software Type**
   - **Ask question:** "What type of software access do you need?"
   - **Identify:** Multiple choice
   - **Options:**
     - Standard business software (Office, Teams, etc.)
     - Specialized department software
     - Development tools
     - Other/Not sure
   - **Save as:** SoftwareType

   **Node 2: Ask Software Name**
   - **Ask question:** "Which specific software or application do you need?"
   - **Identify:** Free text
   - **Save as:** SoftwareName

   **Node 3: Provide Instructions**
   - **Send message:** "Let me find the access request process for {SoftwareName}."
   - **Create generative answers** from IT_Software_Access.pdf
   
   **Node 4: Offer to Create Ticket**
   - **Send message:** "For software access requests, you typically need to create an IT ticket."
   - **Ask question:** "Would you like me to help you create a ticket now?"
   - **Identify:** Boolean
   - **Save as:** CreateTicket
   - Note: Ticket creation will be implemented in Challenge 5

   **Node 5: Next Steps**
   - If CreateTicket = Yes: "I'll help you create that ticket in just a moment."
   - If CreateTicket = No: "No problem! You can submit a ticket through the IT portal whenever you're ready. The link has been shared above."

5. Click **Save**.

### Step 5: Create Procurement Purchase Request Topic

1. Click **+ New topic** → **From blank**

2. Configure:
   - **Name:** `Procurement - Purchase Request`
   - **Description:** `Guides employees through the purchase order and approval workflow`

3. Add trigger phrases:
   - "I need to make a purchase"
   - "How do I buy something"
   - "Purchase request"
   - "Purchase order"
   - "Buy equipment"
   - "Procurement process"
   - "Vendor purchase"

4. Build the conversation flow:

   **Node 1: Ask Purchase Amount**
   - **Send message:** "I'll help you with the purchase request process."
   - **Ask question:** "What is the approximate amount of this purchase?"
   - **Identify:** Multiple choice
   - **Options:**
     - Under $500
     - $500 - $5,000
     - $5,000 - $25,000
     - Over $25,000
   - **Save as:** PurchaseAmount

   **Node 2: Conditional Approval Path**
   - Add **Condition** based on PurchaseAmount
   - Different approval levels for different amounts

   **Branch 1: Under $500**
   - **Send message:** "For purchases under $500, you typically need only your manager's approval."
   - **Create generative answers** from Procurement_Purchase_Request.pdf

   **Branch 2: $500 - $5,000**
   - **Send message:** "For purchases in this range, you'll need manager and department head approval."
   - **Create generative answers** from Procurement_Purchase_Request.pdf

   **Branch 3: $5,000+**
   - **Send message:** "For larger purchases, additional approvals are required, including finance review."
   - **Create generative answers** from Procurement_Purchase_Request.pdf

   **Node 3: Ask if Vendor Exists**
   - **Ask question:** "Is this from an existing approved vendor?"
   - **Identify:** Boolean
   - If No: Mention vendor onboarding requirements
   - **Create generative answers** from Procurement_Vendor_Management.pdf

   **Node 4: Provide Next Steps**
   - **Send message:** "Here's a summary of what you need to do next to submit your purchase request."
   - Include relevant forms and approval chain info

5. Click **Save**.

### Step 6: Test Each Topic

1. Click **Test your copilot** button.

2. **Test HR Leave Policy topic:**
   - Type: "I need to take leave"
   - Follow the conversation flow
   - Try different options
   - Verify answers are relevant

3. **Test Finance Travel Reimbursement topic:**
   - Type: "Travel reimbursement"
   - Test each branch (planning, already traveled, policy)
   - Verify proper routing

4. **Test IT Software Access topic:**
   - Type: "I need software access"
   - Provide a software name
   - Check that instructions are relevant

5. **Test Procurement Purchase Request topic:**
   - Type: "I need to make a purchase"
   - Try different purchase amounts
   - Verify approval paths are correct

### Step 7: Refine and Improve Topics

1. Based on your testing, make improvements:
   - Add more trigger phrases if needed
   - Clarify question wording
   - Adjust branching logic
   - Add helpful links or references

2. Click **Save** after each refinement.

### Step 8: Organize Topics

1. In the Topics list view, you can:
   - Use folders or labels to organize by department
   - Enable/disable topics as needed
   - Set topic priority if multiple topics match

2. Verify all four new topics are enabled and active.

## Success Criteria
- Created 4 department-specific topics:
  - HR - Leave Policy
  - Finance - Travel Reimbursement
  - IT - Software Access
  - Procurement - Purchase Request
- Each topic has relevant trigger phrases (at least 5 per topic)
- Conversational flows include:
  - Dynamic questions based on user input
  - Conditional branching logic
  - Generative answers from appropriate knowledge sources
  - Clear next steps or closing messages
- All topics tested and working correctly
- Topics are organized and easy to maintain

## Additional Resources
- [Create and edit topics](https://learn.microsoft.com/microsoft-copilot-studio/authoring-create-edit-topics)  
- [Use conditions in topics](https://learn.microsoft.com/microsoft-copilot-studio/authoring-using-conditions)  
- [Ask questions in topics](https://learn.microsoft.com/microsoft-copilot-studio/authoring-ask-a-question)  
- [Generative answers node](https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-node)

---

Now, click **Next** to continue to **Challenge 04: Enable Citation Answers**.
