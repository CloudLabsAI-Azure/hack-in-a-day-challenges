# Challenge 03: Design Department Topics Using Generative AI

## Introduction
While your copilot can now answer general questions using the uploaded knowledge base, employees often have specific common requests that benefit from structured conversations. Instead of manually building conversation flows from scratch, Microsoft Copilot Studio allows you to create topics using generative AI. Simply describe what you want the topic to do, and AI will generate the conversation flow, trigger phrases, and responses automatically.

In this challenge, you'll create one custom topic with an Adaptive Card for knowledge requests, plus four department-specific topics using AI generation to handle the most frequent employee inquiries across HR, Finance, IT, and Procurement.

## Challenge Objectives
- Update the Conversation Start topic with a welcoming message
- Create a custom Knowledge Request Submission topic using Adaptive Cards
- Use generative AI to create 4 department topics:
  - HR - Leave Policy Assistance
  - Finance - Travel Reimbursement
  - IT - Software Access Requests
  - Procurement - Purchase Requests
- Test each AI-generated topic thoroughly
- Verify topics use knowledge sources effectively

## Steps to Complete

### Step 1: Update Conversation Start Topic

1. In **Microsoft Copilot Studio**, ensure your **Internal Knowledge Navigator** agent is open.

2. Select **Topics (1)**, select **All (2)**, then select **Conversation Start (3)**.

3. Keep the first sentence in the message box and update the message by entering the following text **(1)**. Then select **Save (2)**:

   ```
   I'm here to help you find information about company policies and procedures across HR, Finance, IT, and Procurement departments.
   
   You can ask me about leave policies, expense reimbursement, software access, purchase requests, and much more.
   
   I'll provide answers with citations to our official policy documents, and I can also help you with actions like emailing documents or creating support tickets.
   
   What would you like to know today?
   ```

### Step 2: Access Topics for Custom Topic Creation

1. Select **Topics (1)** again, choose **+ Add a topic (2)**, and then select **From blank (3)** or **Add from description with Copilot (3)** for faster creation.

### Step 3: Create Knowledge Request Topic (Using Adaptive Card)

This topic will allow employees to submit knowledge requests that get tracked in SharePoint.

1. On the **Add from description with Copilot** page:
   - **Name your topic:** `Knowledge Request Submission (1)`
   - **Create a topic to...:** `User wants to submit a knowledge request or ask about missing information (2)`
   - Then select **Create (3)**

2. On the newly created topic, review the **Trigger node** and **Describe what topic does** box.

3. Update the message node with the below text **(1)** and click **Save (2)**:

   ```
   I'd be happy to help you submit a knowledge request. Please fill out the form below with details about the information you're looking for.
   ```

4. Delete any auto-generated question nodes by clicking **ellipsis (...) (1)** and selecting **Delete (2)**.

5. Continue deleting all question nodes and the final message node until you have only the **Trigger node** and one **message node**.

### Step 4: Add Adaptive Card for Knowledge Request

1. Select **Add node (1)** after the message node, then click **Ask with adaptive card (2)**.

2. Select **Ellipsis(...) (1)** of the Adaptive card node, then select **Properties (2)**.

3. Select **Edit adaptive card**.

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

6. **Close** the **Adaptive card node properties** window.

7. Expand the **Output** section of the Adaptive card and make all variables **Global** by selecting each variable **(1)** and choosing **Global (2)** from the properties window.

8. Select **Save**.

### Step 5: Create Topic 1 - HR Leave Policy Assistance

1. Select **Topics**, choose **+ Add a topic**, and select **Create from description with Copilot**.

2. On the **Create from description with Copilot** page, enter the following:

   - **Name your topic:** `HR - Leave Policy Assistance`
   - **Create a topic to...:**

   ```
   Help employees understand leave policies including annual leave, sick leave, personal leave, and time-off procedures. Ask the employee what type of leave information they need and save it as a variable. Use generative answers to retrieve policy details from the uploaded HR knowledge sources whenever possible. Provide information about leave accrual, approval processes, request procedures, and contact information. After sharing the information, ask the employee whether they need additional assistance with leave policies. If the employee requests the full policy document by email or has questions requiring HR review, offer helpful next steps. This topic should act as a comprehensive self-service leave policy assistant that provides accurate information directly from the HR Leave Policy document and guides employees through common leave-related questions.
   ```

3. Click **Create** or **Generate**.

4. Wait for the AI to generate the topic (15-30 seconds).

5. Review the generated topic:

   - **Trigger phrases:** Verify it includes phrases like:
     - "Leave policy"
     - "How do I request leave"
     - "Annual leave"
     - "Sick leave"
     - "Time off procedures"

6. Review the conversation flow to ensure it:
   - Asks what type of leave information is needed
   - Uses generative answers from HR knowledge sources
   - Offers additional assistance

7. Click **Save** to save the topic.

### Step 6: Create Topic 2 - Finance Travel Reimbursement

1. Click **+ Add a topic** → **Create from description with Copilot**.

2. Enter the following:

   - **Name your topic:** `Finance - Travel Reimbursement`
   - **Create a topic to...:**

   ```
   Assist employees with travel booking and reimbursement procedures. Ask the employee what stage of the travel process they are in and save it as a variable - whether they are planning a trip (pre-approval), have already traveled (reimbursement), or have general policy questions. Use generative answers to provide detailed information about travel booking procedures, approval requirements, reimbursement submission steps, receipt requirements, reimbursement timelines, and expense policies by referring to the uploaded Finance knowledge sources. For employees planning trips, provide pre-approval guidance and booking procedures. For employees seeking reimbursement, explain the submission process, required documentation, and expected timelines. After sharing the information, ask whether they need additional assistance or would like the full policy document emailed to them. This topic should serve as a comprehensive travel and expense assistant that uses the Finance Travel Reimbursement Policy document to answer all travel-related questions and guide employees through the complete travel expense cycle.
   ```

3. Click **Create** or **Generate**.

4. Review the generated topic:

   - **Trigger phrases:** Verify it includes phrases like:
     - "Travel reimbursement"
     - "Book business travel"
     - "Submit travel expenses"
     - "Travel expense policy"
     - "Business trip reimbursement"

5. Review the conversation flow to ensure it:
   - Asks about the travel stage (planning, reimbursement, or policy questions)
   - Uses generative answers from Finance knowledge sources
   - Offers to email the policy document

6. Click **Save**.

### Step 7: Create Topic 3 - IT Software Access Requests

1. Click **+ Add a topic** → **Create from description with Copilot**.

2. Enter the following:

   - **Name your topic:** `IT - Software Access Requests`
   - **Create a topic to...:**

   ```
   Help employees request software installations and access permissions. Ask the employee what type of software access they need and save it as a variable, then ask them to specify which software or application they require and save that as another variable. Use generative answers to provide detailed instructions about the software request process, approval requirements, installation procedures, license availability, and access request workflows by referring to the uploaded IT knowledge sources. Provide step-by-step guidance for submitting software access requests through the IT portal or ticket system. After sharing the instructions, ask the employee whether they understand the process or need help creating an IT support ticket. If the employee requests assistance with submitting the ticket, offer to help them initiate the ticket creation process (note: actual ticket creation will be implemented in Challenge 5). This topic should serve as a comprehensive software access assistant that uses the IT Software Access Request document to guide employees through all software request procedures and provide clear next steps.
   ```

3. Click **Create** or **Generate**.

4. Review the generated topic:

   - **Trigger phrases:** Verify it includes phrases like:
     - "Software access request"
     - "Install software"
     - "Need software license"
     - "Application access"
     - "Request software"

5. Review the conversation flow to ensure it:
   - Asks about software type and specific application name
   - Uses generative answers from IT knowledge sources
   - Offers to help create an IT support ticket

6. Click **Save**.

### Step 8: Create Topic 4 - Procurement Purchase Requests

1. Click **+ Add a topic** → **Create from description with Copilot**.

2. Enter the following:

   - **Name your topic:** `Procurement - Purchase Requests`
   - **Create a topic to...:**

   ```
   Guide employees through the purchase order and approval workflow. Ask the employee what the approximate purchase amount is and save it as a variable to determine the appropriate approval path. Use generative answers to provide detailed information about purchase request procedures, approval requirements based on amount thresholds, purchase order processes, vendor selection guidelines, and procurement policies by referring to the uploaded Procurement knowledge sources. For different purchase amounts, explain the specific approval levels required - manager approval for small purchases, department head approval for medium purchases, and finance review for large purchases. Also ask whether this is from an existing approved vendor and save that response, then provide guidance on vendor management and onboarding procedures if needed. After sharing the procurement process, provide a clear summary of next steps including required forms, approval chain, and submission procedures. This topic should serve as a comprehensive procurement assistant that uses the Procurement Purchase Order Process and Vendor Management Policy documents to guide employees through all purchasing procedures based on their specific purchase amount and vendor status.
   ```

3. Click **Create** or **Generate**.

4. Review the generated topic:

   - **Trigger phrases:** Verify it includes phrases like:
     - "Purchase request"
     - "Buy equipment"
     - "Procurement process"
     - "Purchase order"
     - "Make a purchase"

5. Review the conversation flow to ensure it:
   - Asks about purchase amount and provides amount-based guidance
   - Asks about vendor status (existing or new)
   - Uses generative answers from Procurement knowledge sources
   - Provides clear next steps for submission

6. Click **Save**.

### Step 9: Test Each Generated Topic

1. Click **Test your copilot** button in the top-right corner.

2. **Test HR Leave Policy Assistance topic:**
   - Type: "I need to take leave"
   - Follow the AI-generated conversation flow
   - Verify the copilot asks about leave type
   - Check that generative answers provide relevant information from HR documents
   - Confirm the copilot offers additional assistance

3. **Test Finance Travel Reimbursement topic:**
   - Type: "How do I get travel reimbursement"
   - Verify the copilot asks about travel stage (planning, reimbursement, or policy)
   - Check that responses include relevant Finance policy information
   - Test different branches to ensure proper routing

4. **Test IT Software Access Requests topic:**
   - Type: "I need Microsoft Project access"
   - Verify the copilot asks for software type and name
   - Check that instructions are relevant from IT documents
   - Confirm it offers to help create a support ticket

5. **Test Procurement Purchase Requests topic:**
   - Type: "I need to make a purchase"
   - Provide a purchase amount when asked
   - Verify approval path information matches the amount
   - Check vendor-related questions appear
   - Confirm next steps are clear

### Step 10: Refine Generated Topics (If Needed)

1. If any generated topic needs improvement:
   - Open the topic in edit mode
   - Review the AI-generated nodes
   - Add more trigger phrases manually if needed
   - Adjust any message wording for clarity
   - Ensure generative answers are connected to correct knowledge sources

2. Click **Save** after each refinement.

3. Test again to verify improvements.

### Step 11: Organize Topics

1. In the Topics list view, you should now see:
   - System topics (Conversation Start, Fallback, etc.)
   - Your Knowledge Request Submission topic (from Step 3)
   - Four new department topics (HR, Finance, IT, Procurement)

2. Verify all topics are **enabled** and **active**.

3. You can organize topics by:
   - Department (HR, Finance, IT, Procurement)
   - Priority for triggering
   - Status (enabled/disabled)

## Success Criteria
- Created 5 topics total:
  - 1 Knowledge Request Submission topic (with Adaptive Card)
  - 4 AI-generated department topics:
    - HR - Leave Policy Assistance
    - Finance - Travel Reimbursement
    - IT - Software Access Requests
    - Procurement - Purchase Requests
- Each AI-generated topic created using **Create from description with Copilot**
- Topics automatically include:
  - Relevant trigger phrases (generated by AI)
  - Dynamic conversation flows based on AI understanding
  - Generative answers connected to appropriate knowledge sources
  - Clear next steps and helpful guidance
- All topics tested and responding correctly to user queries
- Topics provide accurate information from uploaded department documents
- Conversation flows feel natural and helpful

## Additional Resources
- [Create and edit topics](https://learn.microsoft.com/microsoft-copilot-studio/authoring-create-edit-topics)  
- [Use conditions in topics](https://learn.microsoft.com/microsoft-copilot-studio/authoring-using-conditions)  
- [Ask questions in topics](https://learn.microsoft.com/microsoft-copilot-studio/authoring-ask-a-question)  
- [Generative answers node](https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-node)

---

Now, click **Next** to continue to **Challenge 04: Enable Citation Answers**.
