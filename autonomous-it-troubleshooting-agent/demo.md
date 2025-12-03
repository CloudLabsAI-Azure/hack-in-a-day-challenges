# Challenge: IT Support Copilot with Microsoft Copilot Studio

**Estimated Time:** 4 Hours  

**Industry Focus:** IT Helpdesk, Employee Support, Service Management  

## Problem Statement

IT support teams are overwhelmed with repetitive helpdesk tickets: password resets, VPN connection issues, slow laptop complaints, and printer problems. These common issues consume 60-70% of support time, leading to long wait times and frustrated employees.

In this challenge, you will build an **IT Support Copilot** using Microsoft Copilot Studio that provides instant, intelligent assistance for common IT issues. The copilot will use uploaded knowledge base documents (SOPs and FAQs) to answer questions, guide users through troubleshooting steps with conversational topics, and use generative AI to handle unknown scenarios. When appropriate, it will send resolution summaries via Microsoft Teams or email.

## Goals

By the end of this challenge, you will deliver an **IT Support Copilot** capable of:

- Answering common IT support questions using uploaded knowledge base documents (PDFs).
- Guiding users through structured troubleshooting flows for popular issues (slow laptop, VPN, printer).
- Using Generative AI to handle unknown or complex questions by summarizing relevant information from documents.
- Collecting user information through conversational interactions.
- Sending resolution summaries and escalation notifications via Microsoft Teams or email.

## Expected Outcomes

You will have:

- A fully functional IT Support Copilot deployed in Copilot Studio.
- Multiple troubleshooting topics (password reset, VPN issues, slow laptop, printer problems).
- Generative AI fallback handling for questions not covered by structured topics.
- Integration with Microsoft Teams for sending resolution summaries and escalations.
- A realistic knowledge base of IT support SOPs and FAQs.

## Prerequisites

- **Skill Level:** Basic Microsoft 365 familiarity, no coding required.  
- **Audience:** IT support professionals, helpdesk managers, IT administrators, and business analysts.  
- **Technology Stack:**  
  - Microsoft Copilot Studio (with Generative AI capabilities)
  - Power Automate (for sending notifications)
  - Microsoft Teams (for collaboration and notifications)
  - Microsoft Dataverse (for data storage - optional)
  - Access to Microsoft 365 tenant with appropriate licenses

## Learning Objectives

By completing this challenge, you will:

- Create and configure a copilot in Microsoft Copilot Studio from scratch.
- Upload and manage knowledge base documents for generative answers.
- Design conversational topics with branching logic and question nodes.
- Configure Generative AI for handling unknown questions using document context.
- Integrate Power Automate flows for sending notifications via Teams and email.
- Test and iterate on copilot responses to improve user experience.

## Datasets and Knowledge Base

The following datasets and knowledge base documents are provided in the lab files under the `datasets` folder:

### Knowledge Base Documents (PDF/Word format):
1. **IT_Support_FAQ_Password_Reset.pdf** - Comprehensive guide for password reset procedures
2. **IT_Support_SOP_VPN_Issues.pdf** - Standard operating procedures for VPN troubleshooting
3. **IT_Support_SOP_Slow_Laptop.pdf** - Step-by-step troubleshooting for slow laptop performance
4. **IT_Support_SOP_Printer_Issues.pdf** - Printer connectivity and common issue resolution guide

### Test Scenarios:
- **IT_Support_Test_Scenarios.csv** - Sample user questions and expected responses for testing your copilot

All datasets are available in:  
`C:\LabFiles\AutonomousITAgent\datasets`

You will upload these documents to your Copilot Studio knowledge base in Challenge 2.

---

## Challenge Objectives

### **Challenge 1: Create Your IT Support Copilot in Copilot Studio**

**Estimated Duration:** 40 Minutes  

#### Objective

Create a new copilot in Microsoft Copilot Studio and configure its basic identity and capabilities as an IT Support Assistant.

#### Tasks

1. Navigate to **Microsoft Copilot Studio** (https://copilotstudio.microsoft.com)
2. Sign in with your Microsoft 365 credentials provided in the lab environment
3. Create a new copilot:
   - Name: **"IT Support Copilot"**
   - Description: **"Your intelligent assistant for common IT support issues including password resets, VPN problems, slow laptop troubleshooting, and printer issues"**
   - Language: English
   - Select an appropriate environment for your tenant
4. Configure the copilot settings:
   - **Icon/Avatar:** Choose an appropriate IT support icon
   - **Conversation starters:** Add these suggested phrases:
     - "I forgot my password"
     - "VPN not connecting"
     - "My laptop is running slow"
     - "Printer not working"
5. Review the default system topics:
   - Understand how Conversation Start, Fallback, and Error topics work
   - Keep these enabled for now
6. Test the copilot in the Test pane:
   - Type "Hello" to verify basic conversation flow
   - Try "What can you help me with?" to see conversation starters

#### Validation Check

- ✅ Copilot Studio is accessible and a new copilot is created
- ✅ Copilot has an appropriate name, description, and icon
- ✅ Four conversation starters are configured
- ✅ Test pane shows the copilot responding to basic greetings
- ✅ Default system topics (Conversation Start, Fallback) are present

---

### **Challenge 2: Upload IT Support Knowledge Base Documents**

**Estimated Duration:** 30 Minutes  

#### Objective

Upload IT support Standard Operating Procedures (SOPs) and FAQ documents to your copilot's knowledge base to enable it to provide accurate, document-based answers.

#### Tasks

1. In Copilot Studio, navigate to your **IT Support Copilot**
2. Go to **Knowledge** section in the left navigation menu
3. Click **+ Add knowledge** and select **Files**
4. Upload the following documents from `C:\LabFiles\AutonomousITAgent\datasets`:
   - **IT_Support_FAQ_Password_Reset.pdf**
   - **IT_Support_SOP_VPN_Issues.pdf**
   - **IT_Support_SOP_Slow_Laptop.pdf**
   - **IT_Support_SOP_Printer_Issues.pdf**
5. Wait for the documents to be processed (indexing status should show "Ready")
6. Enable **Generative answers** capability:
   - Go to **Settings** → **Generative AI**
   - Toggle on **Generative answers**
   - Select **Search only selected sources**
   - Ensure all four uploaded documents are selected as knowledge sources
7. Configure the Generative AI instructions:
   - Add instruction: **"You are an IT support assistant. Always provide step-by-step instructions. If you don't know the answer, say so and suggest contacting the IT helpdesk."**
   - Set Content moderation to **Medium**
8. Test the knowledge base:
   - In the Test pane, ask: "How do I reset my password?"
   - Ask: "My VPN won't connect, what should I do?"
   - Verify that responses include information from the uploaded documents

#### Validation Check

- ✅ All four IT support documents are uploaded and indexed
- ✅ Generative answers feature is enabled
- ✅ Documents are selected as knowledge sources
- ✅ Generative AI instructions are configured
- ✅ Test queries return relevant answers citing the uploaded documents
- ✅ Copilot can answer questions about passwords, VPN, slow laptops, and printers

---

### **Challenge 3: Design Conversational Topics for Popular IT Issues**

**Estimated Duration:** 75 Minutes  

#### Objective

Create structured conversational topics for the most common IT support scenarios. These topics will guide users through troubleshooting with dynamic questions and provide step-by-step resolution guidance.

#### Tasks

#### Part 1: Create "Slow Laptop" Troubleshooting Topic (25 minutes)

1. In Copilot Studio, go to **Topics** → **+ Add a topic** → **From blank**
2. Name the topic: **"Slow Laptop Troubleshooting"**
3. Add trigger phrases:
   - "My laptop is slow"
   - "Computer running slow"
   - "Laptop performance issues"
   - "PC is lagging"
4. Design the conversation flow:
   - **Message node:** "I can help you troubleshoot your slow laptop. Let me ask a few questions."
   - **Question node:** "How long has your laptop been running slow?" (Multiple choice: Less than a day, Few days, More than a week)
   - **Question node:** "Are you running any specific applications when it slows down?" (User's entire response)
   - **Condition node:** Check if duration is "More than a week"
     - If YES: Show message with steps to check for Windows updates, disk cleanup, and suggest running antivirus scan
     - If NO: Show message to restart laptop and close unnecessary applications
   - **Question node:** "Did these steps help resolve the issue?" (Yes/No)
   - **Condition node:** If No → Transfer to escalation topic; If Yes → Show success message

#### Part 2: Create "VPN Connection Issues" Topic (25 minutes)

1. Create a new topic: **"VPN Connection Issues"**
2. Add trigger phrases:
   - "VPN not working"
   - "Can't connect to VPN"
   - "VPN connection failed"
   - "VPN issue"
3. Design the conversation flow:
   - **Message node:** "Let me help you with your VPN connection."
   - **Question node:** "What error message are you seeing?" (User's entire response)
   - **Question node:** "Are you working from home or office?" (Multiple choice: Home, Office, Other location)
   - **Message node:** "Please try these steps: 1. Check your internet connection 2. Restart VPN client 3. Try disconnecting and reconnecting"
   - **Question node:** "Can you connect now?" (Yes/No)
   - **Condition node:** 
     - If YES: "Great! Your VPN is connected. Remember to disconnect when you're done working."
     - If NO: "Let me check if your VPN account is active..." → Call Power Automate flow (we'll add this in Challenge 4)

#### Part 3: Create "Printer Issues" Topic (25 minutes)

1. Create a new topic: **"Printer Troubleshooting"**
2. Add trigger phrases:
   - "Printer not working"
   - "Can't print"
   - "Printer offline"
   - "Print job stuck"
3. Design the conversation flow:
   - **Message node:** "I'll help you fix your printer issue."
   - **Question node:** "What type of printer are you using?" (Multiple choice: Network printer, USB printer, Wireless printer)
   - **Question node:** "What's happening with your printer?" (Multiple choice: Not printing at all, Printing blank pages, Paper jam, Printer offline)
   - **Condition nodes:** Branch based on the issue type:
     - **Not printing:** Check if printer is on, check connections, restart print spooler
     - **Blank pages:** Check ink/toner levels, run print head cleaning
     - **Paper jam:** Provide steps to safely remove jammed paper
     - **Offline:** Check network connection, set printer as default
   - **Message node:** Provide relevant troubleshooting steps based on the issue
   - **Question node:** "Is your printer working now?" (Yes/No)

#### Validation Check

- ✅ Three custom topics created (Slow Laptop, VPN Issues, Printer Issues)
- ✅ Each topic has at least 4 trigger phrases
- ✅ Topics use Question nodes to collect information from users
- ✅ Topics use Condition nodes to provide different paths based on user responses
- ✅ Each topic ends with a confirmation question
- ✅ Test each topic in the Test pane and verify the conversation flows correctly

---

### **Challenge 4: Add Generative AI Fallback for Unknown Issues**

**Estimated Duration:** 35 Minutes  

#### Objective

Configure the copilot to use Generative AI to handle questions that don't match any predefined topics. This ensures users always get helpful responses even for unexpected questions.

#### Tasks

1. In Copilot Studio, navigate to **Settings** → **Generative AI**
2. Configure the **System fallback topic**:
   - Enable "Generative answers"
   - Ensure it's set to use your uploaded knowledge base documents
3. Customize the **Fallback topic**:
   - Go to **Topics** → Find the **Fallback** system topic
   - Edit the topic to improve the user experience
   - Add a message node: "I don't have a specific guide for that, but let me search my knowledge base to help you."
   - Add a **Generative answers** node configured to:
     - Search uploaded IT support documents
     - Provide a conversational, step-by-step response
     - Cite sources from the documents
4. Add an escalation option:
   - After the generative answer, add a Question node: "Did this answer help?" (Yes/No)
   - If No → Add a message: "I'll connect you with a live support agent" and add a **Transfer to agent** node (or create an escalation topic)
5. Test the fallback with questions not covered by your topics:
   - "How do I set up two-factor authentication?"
   - "My keyboard keys are not working"
   - "How do I access the company intranet?"
6. Review the answers:
   - Verify the copilot provides relevant information from your knowledge base
   - Check that source citations are included
   - Ensure the escalation option works when users need more help

#### Validation Check

- ✅ Generative answers are enabled for the fallback topic
- ✅ Fallback topic includes a user-friendly message before searching knowledge base
- ✅ Generative answers node is configured to search uploaded documents
- ✅ Escalation option is available when generative answers don't help
- ✅ Test queries for unknown topics return helpful, document-based answers
- ✅ Source citations are visible in the responses

---

### **Challenge 5: Send Resolution Summary via Teams or Email**

**Estimated Duration:** 60 Minutes  

#### Objective

Integrate Power Automate to send resolution summaries to users via Microsoft Teams or email when an IT issue is resolved by the copilot.

#### Tasks

#### Part 1: Create Power Automate Flow for Teams Notification (30 minutes)

1. Open **Power Automate** (https://make.powerautomate.com)
2. Create a new **Instant cloud flow**:
   - Flow name: **"Send IT Resolution Summary to Teams"**
   - Trigger: **"When Power Virtual Agents calls a flow"** (or "Copilot Studio")
3. Add input parameters:
   - **UserName** (Text) - User who reported the issue
   - **IssueType** (Text) - Type of IT issue (e.g., "Slow Laptop", "VPN Issue")
   - **Resolution** (Text) - Summary of steps taken
   - **Resolved** (Yes/No) - Whether issue was resolved
4. Add action: **"Post message in a chat or channel"** (Microsoft Teams)
   - Team: Select your IT Support team
   - Channel: Select #it-support or #general
   - Message: Use dynamic content to format:
     ```
     🎫 IT Support Resolution Summary
     
     👤 User: [UserName]
     📋 Issue Type: [IssueType]
     ✅ Status: [Resolved]
     
     📝 Resolution Steps:
     [Resolution]
     
     Generated by IT Support Copilot
     ```
5. **Save** the flow and test it manually with sample data
6. Copy the **Flow URL/ID** (you'll need this in Copilot Studio)

#### Part 2: Create Power Automate Flow for Email Notification (15 minutes)

1. Create another **Instant cloud flow**:
   - Flow name: **"Send IT Resolution Email"**
   - Same trigger and input parameters as above
2. Add action: **"Send an email (V2)"** (Office 365 Outlook)
   - To: [UserEmail] (add this as an input parameter)
   - Subject: "Your IT Support Issue - Resolution Summary"
   - Body: Format with HTML:
     ```html
     <h2>IT Support Resolution Summary</h2>
     <p><strong>Issue Type:</strong> [IssueType]</p>
     <p><strong>Status:</strong> [Resolved]</p>
     <h3>Resolution Steps:</h3>
     <p>[Resolution]</p>
     <hr>
     <p><em>This is an automated message from IT Support Copilot</em></p>
     ```
3. **Save** the flow

#### Part 3: Integrate Flows with Copilot Topics (15 minutes)

1. Go back to **Copilot Studio**
2. Open one of your topics (e.g., "Slow Laptop Troubleshooting")
3. At the end of the topic (after user confirms resolution):
   - Add a **Call an action** node
   - Select **Power Automate** → Choose "Send IT Resolution Summary to Teams"
   - Map the input parameters:
     - UserName: Use a variable that captures user's name (or use System.User.DisplayName)
     - IssueType: "Slow Laptop"
     - Resolution: Create a variable that concatenates the steps discussed
     - Resolved: Map to the user's Yes/No answer
4. Add a confirmation message: "I've sent a summary of this session to our IT support team."
5. Repeat this integration for your other topics (VPN, Printer)
6. **Publish** your copilot

#### Part 4: Test End-to-End (10 minutes)

1. Test the complete flow:
   - Start a conversation in the Test pane
   - Go through a troubleshooting topic (e.g., Slow Laptop)
   - Answer all questions
   - Confirm resolution
   - Verify that a Teams message is posted to your IT support channel
2. Test with the email flow:
   - Update one topic to call the email flow instead
   - Provide a test email address
   - Verify email is received

#### Validation Check

- ✅ Power Automate flow created for Teams notifications
- ✅ Power Automate flow created for email notifications
- ✅ Flows successfully test with sample data
- ✅ At least one copilot topic is integrated with a Power Automate flow
- ✅ Flow is triggered when topic reaches resolution point
- ✅ Teams message or email contains accurate resolution summary
- ✅ Copilot is published and accessible for testing

---

## Success Criteria

**You will have successfully completed this challenge when you deliver:**

An **IT Support Copilot** that can:

- Greet users and offer help with common IT issues
- Answer questions about password resets, VPN, slow laptops, and printers using knowledge base documents
- Guide users through structured troubleshooting conversations with intelligent branching
- Handle unexpected questions using Generative AI with document citations
- Automatically send resolution summaries to Microsoft Teams or email
- Provide escalation options when issues cannot be resolved

### Technical Deliverables

- **Copilot Foundation:** A fully configured copilot in Copilot Studio with appropriate branding and conversation starters
- **Knowledge Base:** Four IT support documents uploaded and indexed for generative answers
- **Conversational Topics:** Three custom topics (Slow Laptop, VPN, Printer) with dynamic question flows
- **Generative AI Fallback:** Configured fallback topic that searches knowledge base for unknown questions
- **Power Automate Integration:** Flows for sending resolution summaries via Teams and/or email
- **Published Copilot:** Deployed and accessible for end-user testing

### Business Outcomes

- **Reduced Support Workload:** Common IT issues are resolved through self-service, reducing ticket volume by an estimated 40-50%
- **Faster Resolution Times:** Users get immediate help 24/7 without waiting for support agents
- **Improved Documentation:** Structured knowledge base ensures consistent, accurate responses
- **Better User Experience:** Conversational interface is more intuitive than searching through KB articles
- **Scalable Solution:** Easy to add new topics and expand knowledge base as needs evolve

---

## Additional Resources

- [Microsoft Copilot Studio Documentation](https://learn.microsoft.com/microsoft-copilot-studio/)
- [Generative Answers in Copilot Studio](https://learn.microsoft.com/microsoft-copilot-studio/nlu-boost-conversations)
- [Power Automate Documentation](https://learn.microsoft.com/power-automate/)
- [Microsoft Teams Integration](https://learn.microsoft.com/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams)
- [Best Practices for Copilot Design](https://learn.microsoft.com/microsoft-copilot-studio/guidance/design-overview)

---

## Bonus Challenges (If Time Permits)

If you complete all challenges with time remaining, try these enhancements:

### Bonus 1: Add Authentication
- Configure authentication in Copilot Studio
- Make the copilot recognize returning users
- Personalize greetings with user names

### Bonus 2: Analytics Dashboard
- Go to **Analytics** in Copilot Studio
- Review conversation transcripts
- Identify common questions not yet covered
- Create new topics based on analytics insights

### Bonus 3: Deploy to Multiple Channels
- Publish copilot to Microsoft Teams as an app
- Add the copilot to your organization's SharePoint site
- Create a mobile-friendly web chat widget

### Bonus 4: Advanced Escalation Workflow
- Create a Dataverse table to log all escalations
- Build a Power App for support agents to view escalated issues
- Add priority levels based on issue severity

### Bonus 5: Multilingual Support
- Create a second copilot for another language (Spanish, French, etc.)
- Translate your knowledge base documents
- Test the multilingual user experience

---

## Conclusion

Congratulations! You have successfully built an **IT Support Copilot** using Microsoft Copilot Studio that can:

- Provide instant, accurate answers from your IT knowledge base
- Guide users through interactive troubleshooting conversations
- Handle unexpected questions with Generative AI
- Automatically notify support teams of resolutions and escalations

This solution demonstrates how modern conversational AI can transform IT support operations by:
- **Reducing manual support workload** through intelligent self-service
- **Improving employee satisfaction** with 24/7 instant assistance
- **Ensuring consistent, accurate responses** based on approved documentation
- **Scaling support capacity** without adding headcount

The patterns and skills you've learned in this challenge can be applied to many other business scenarios:
- HR support copilots for onboarding and benefits questions
- Finance copilots for expense and invoice inquiries
- Customer service copilots for product support
- Sales copilots for product information and quote generation

**Well done on completing this Hack in a Day challenge!**
