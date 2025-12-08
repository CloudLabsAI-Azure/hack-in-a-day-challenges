# Challenge 04: Create Topics Using Generative AI

## Introduction
Now that your agent flows are ready, you'll create conversational topics using generative AI in Copilot Studio. Simply describe what you want the topic to do, and AI will generate the conversation flow, trigger phrases, and responses automatically. You'll then connect these topics to your published agent flows.

In this challenge, you will create 4 topics that help employees: Document Search, Email Document, Submit Request, and New Employee Onboarding. Topics will call your published agent flows when needed.

## Challenge Objectives
- Use Copilot Studio's generative AI to create 4 topics
- Connect topics to your published agent flows
- Map topic variables to flow inputs
- Test topics with flow integration

## Steps to Complete

### Step 1: Navigate to Topics Section

- In your **Internal Knowledge Navigator** agent, click **Topics** in the left navigation pane.

- You'll see existing system topics (Conversation Start, Fallback, Error).

- Click **+ Add a topic** at the top.

- Select **Create from description with Copilot**.

### Step 2: Create Topic 1 - Document Search

- In the topic creation dialog, enter the following:

   - **Name:** `DocumentSearch`
   
   - **Description:**

   ```
   Help employees search and find information from Contoso company documents including HR handbooks, IT policies, procurement procedures, support policies, sales playbooks, and business reports. Ask the employee what information or document they are looking for and save it as a variable. Use generative answers to search the SharePoint knowledge base and retrieve relevant information from the uploaded Contoso documents. Provide clear answers with information from the documents. After sharing the information, ask if they found what they needed or if they need additional help. This topic should act as a general document search and information retrieval assistant.
   ```

- Click **Create**.

- Wait for the AI to generate the topic (15-30 seconds).

- Review the generated topic:

   - **Trigger phrases:** Verify it includes phrases like:
     - "Find a document"
     - "Search for information"
     - "What does the policy say"
     - "Company documents"
     - "Look up information"

- Review the conversation flow to ensure it searches documents and provides information.

- Click **Save**.

### Step 3: Create Topic 2 - Email Document

- Click **+ Add a topic** → **Create from description with Copilot**.

- Enter the following:

   - **Name:** `EmailDocument`
   
   - **Description:**

   ```
   Help employees who want to receive a company document via email. Ask which document they need and save it as a variable. Ask for their email address and save it as a variable. Ask them to briefly describe the document or why they need it and save that as a variable. Then call the Email Document to Employee agent flow and map the email address to EmployeeEmail input, document name to DocumentName input, and description to DocumentDescription input. After the flow completes, confirm that an email with the document information has been sent to their inbox.
   ```

- Click **Create**.

- Review the generated topic:

   - **Trigger phrases:** Verify phrases like:
     - "Email me a document"
     - "Send document to my email"
     - "I need a document emailed"
     - "Can you email the policy"

- Review the conversation flow to ensure it collects all required information.

- Click **Save**.

### Step 4: Create Topic 3 - Submit Request

- Click **+ Add a topic** → **Create from description with Copilot**.

- Enter the following:

   - **Name:** `SubmitRequest`
   
   - **Description:**

   ```
   Help employees submit requests or questions to the team via Microsoft Teams. Ask for their name and save it as a variable. Ask for their email address and save it as a variable. Ask what type of request this is using multiple choice options (IT support, HR question, Facility issue, Access request, Other) and save the selection as a variable. After capturing the selection, create a new text variable called RequestTypeText and set it to the value of the multiple choice selection to convert it to string format. Ask them to describe their request in detail and save the request details as a variable. Then call the Send Request to Teams agent flow and map the employee name to EmployeeName input, email to EmployeeEmail input, the RequestTypeText variable to RequestType input, and request details to RequestDetails input. After the flow completes, confirm that their request has been posted to the team channel in Microsoft Teams and someone will respond soon.
   ```

- Click **Create**.

- Review the generated topic:

   - **Trigger phrases:** Verify phrases like:
     - "Submit a request"
     - "Send request to team"
     - "I need help from the team"
     - "Post my question to Teams"

- Review the conversation flow to ensure it collects all necessary details.

- Click **Save**.

### Step 5: Create Topic 4 - New Employee Onboarding

- Click **+ Add a topic** → **Create from description with Copilot**.

- Enter the following:

   - **Name:** `NewEmployeeOnboarding`
   
   - **Description:**

   ```
   Assist new employees who are learning about the company. Help them understand company policies, procedures, organizational structure, benefits, workplace resources, and onboarding requirements. Use generative answers to search the SharePoint knowledge base for information from documents like the HR Handbook, Onboarding Checklist, IT Governance Policy, Employee Travel Reimbursement guidelines, and other relevant company documents. Provide comprehensive, helpful responses to help new employees get oriented and feel welcomed.
   ```

- Click **Create**.

- Review the generated topic:

   - **Trigger phrases:** Verify phrases like:
     - "I'm a new employee"
     - "New hire help"
     - "Onboarding information"
     - "First day at Contoso"
     - "What should I know as a new employee"

- Review the conversation flow to ensure it uses generative answers.

- Click **Save**.

### Step 6: Review All Topics

- In the **Topics** list, verify you now have 4 custom topics:
   - DocumentSearch
   - EmailDocument
   - SubmitRequest
   - NewEmployeeOnboarding

- Ensure all topics are **enabled** (toggle should be on).

### Step 7: Connect Topics to Agent Flows

Only 2 topics need to be connected to agent flows: **EmailDocument** and **SubmitRequest**. The other topics use generative answers from the knowledge base only.

#### For EmailDocument Topic:

- Open **EmailDocument** topic in the editor.

- Locate the point where all information is collected (email, document name, description) and ready to send.

- Add a new node:
   - Click **+** → **Call an action** → Select **Email Document to Employee** flow.

- Map the flow inputs using the variables captured in the topic:
   - **EmployeeEmail:** Use the email variable from the topic (e.g., `Topic.EmailAddress`)
   - **DocumentName:** Use the document name variable (e.g., `Topic.DocumentName`)
   - **DocumentDescription:** Use the description variable (e.g., `Topic.DocumentDescription`)

   > **Note:** Variable names may differ based on AI generation. Use the actual variable names from your generated topic.

- After the flow action, add a **Message** node:
   - Type: `An email with the document information has been sent to your inbox.`

- Click **Save**.

#### For SubmitRequest Topic:

- Open **SubmitRequest** topic.

- Locate the point where all information is collected (name, email, request type, details) and ready to submit.

- Add a new node:
   - Click **+** → **Call an action** → Select **Send Request to Teams** flow.

- Map the flow inputs using the variables captured in the topic:
   - **EmployeeName:** Use the name variable (e.g., `Topic.EmployeeName`)
   - **EmployeeEmail:** Use the email variable (e.g., `Topic.EmailAddress`)
   - **RequestType:** Use the request type variable (e.g., `Topic.RequestType`)
   - **RequestDetails:** Use the details variable (e.g., `Topic.RequestDetails`)

   > **Note:** Use the actual variable names from your generated topic.

- After the flow action, add a **Message** node:
   - Type: `Your request has been posted to the team channel in Microsoft Teams. Someone will respond to you shortly.`

- Click **Save**.

### Step 8: Test All Topics

Open the **Test your agent** pane and test each topic.

#### Test DocumentSearch:

- Type: `Where can I find information about employee benefits?`

- Verify the agent searches the SharePoint knowledge base and provides relevant information from company documents.

- Try another query: `What are the expense reimbursement policies?`

- Verify generative answers are provided from the knowledge base without calling any flows.

#### Test EmailDocument:

- Reset the conversation (click the refresh icon).

- Type: `Email me a document`

- Provide the document name when asked (e.g., "HR Handbook").

- Provide your email address.

- Provide a brief description (e.g., "Need to review HR policies").

- Verify the flow runs and you receive the confirmation message.

- Check your email inbox (**<inject key="AzureAdUserEmail"></inject>**) to see if the email was delivered with document information.

#### Test SubmitRequest:

- Reset the conversation.

- Type: `Submit a request to the team`

- Provide your name when asked.

- Provide your email address.

- Provide a request type (e.g., "IT support" or "HR question").

- Describe your request in detail.

- Verify the flow runs and you receive the confirmation message.

- Check your Microsoft Teams to see if the request was posted to the team channel.

#### Test NewEmployeeOnboarding:

- Reset the conversation.

- Type: `I'm a new employee and need help getting started`

- Ask questions like:
  - "What benefits do I get?"
  - "What's the onboarding process?"
  - "Where can I find IT policies?"

- Verify the agent provides helpful answers from the knowledge base (HR Handbook, Onboarding Checklist, IT Governance Policy, etc.).

### Step 9: Verify Flow Execution

- Go back to **Flows** in the left navigation.

- Click on each flow (**Email Document to Employee** and **Send Request to Teams**) to view run history.

- Verify that the flows were triggered by your topic tests.

- Check that the inputs were passed correctly from the topics.

- Ensure all steps in the flows completed successfully.

## Success Criteria
- Created 4 topics using generative AI:
  - **DocumentSearch** - General document search using knowledge base
  - **EmailDocument** - Connected to Email Document to Employee flow
  - **SubmitRequest** - Connected to Send Request to Teams flow
  - **NewEmployeeOnboarding** - New employee assistance using knowledge base
- All topics have appropriate trigger phrases
- Flow-connected topics successfully call their respective agent flows
- Topic variables correctly mapped to flow inputs
- Test conversations trigger flows successfully
- Emails received for EmailDocument topic requests
- Teams messages posted for SubmitRequest topic
- Generative answers provided for DocumentSearch and NewEmployeeOnboarding topics

## Additional Resources
- [Create topics with Copilot](https://learn.microsoft.com/microsoft-copilot-studio/nlu-authoring)
- [Call flows from topics](https://learn.microsoft.com/microsoft-copilot-studio/advanced-flow)
- [Work with variables](https://learn.microsoft.com/microsoft-copilot-studio/authoring-variables)

---

Now, click **Next** to continue to **Challenge 05: Enable Citation Answers**.
