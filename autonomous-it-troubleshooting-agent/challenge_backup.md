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

### **Challenge 2: Reasoning & Diagnosis – Design the Agent Loop**

**Estimated Duration:** 60 Minutes  

#### Objective

Design the reasoning and planning loop for the agent so it can interpret incidents, propose next steps, and decide whether an issue is auto-resolvable or requires escalation.

#### Tasks

1. In Azure AI Foundry or Copilot Studio, define an **Agent / Copilot** with:
   - A clear system prompt describing its role as an IT troubleshooting agent.
   - Guidance on using knowledge base entries and tools instead of guessing.
2. Implement a **reasoning loop** that:
   - Takes an incident description and available context (severity, category).
   - Asks itself clarifying questions (internally) using chain-of-thought-style planning.
   - Decides whether the issue matches a known remediation pattern.
3. Add logic/prompting for:
   - **Confidence thresholds** (when the agent is “confident enough” to act).
   - **Escalation criteria** (high severity, unknown pattern, multiple failed attempts).
4. Test the agent with sample incidents:
   - CPU threshold exceeded on a VM.
   - Web service not responding.
   - User access denied to an application.

#### Validation Check

- Agent successfully classifies sample incidents into known categories.
- Agent generates clear reasoning and a proposed remediation plan.
- Escalation vs auto-resolution decisions follow your defined rules.

---

### **Challenge 3: Tools & Actions – Connect Remediation Workflows**

**Estimated Duration:** 75 Minutes  

#### Objective

Connect the agent to concrete tools that can execute remediation steps, such as Power Automate flows or Azure Functions.

#### Tasks

1. Create one or more **Power Automate flows** (or APIs) that can:
   - Update an incident record in Dataverse.
   - Simulate a restart action (e.g., a dummy HTTP trigger or a logged “restart service” action).
   - Reset a user access flag or permissions in a test table.
2. Expose these flows or APIs as **tools/actions** to the agent (via Copilot Studio, Azure AI Foundry, or function calling).
3. Update the agent prompt/logic so that:
   - For known fixable issues (e.g., non-critical CPU alerts, minor service issues), it invokes the appropriate tool.
   - It logs each decision and action in the Action Logs dataset.
4. Implement basic **self-correction**:
   - If a tool returns an error or a “no-op” response, the agent should either retry, choose an alternative action, or escalate.
5. Test end-to-end:
   - Trigger an incident.
   - Observe the agent’s reasoning.
   - Confirm that the correct Power Automate flow or API is invoked.

#### Validation Check

- Tools are correctly wired and callable from the agent.
- Actions taken by the agent are logged.
- Failed actions are handled through retry or escalation logic.

---

### **Challenge 4: Orchestration & Escalation – Teams Integration and End-to-End Flow**

**Estimated Duration:** 60 Minutes  

#### Objective

Finalize the solution by integrating with Microsoft Teams, configuring escalation workflows, and validating the complete troubleshooting lifecycle.

#### Tasks

1. Configure a **Teams notification** mechanism (via Power Automate or API) that:
   - Posts a message to the IT operations channel when:
     - An incident is escalated.
     - An automated resolution is completed for a high-visibility incident.
2. Ensure that escalation messages include:
   - Incident details (Title, Severity, Description).
   - Actions the agent already attempted.
   - Suggested next steps for the human engineer.
3. Implement a simple **feedback loop**:
   - Allow an engineer in Teams to approve/deny a recommended action or mark the resolution as correct.
   - Capture this feedback back into Dataverse or your log store.
4. Run an **end-to-end scenario**:
   - Create a new incident.
   - Let the agent process, diagnose, and either auto-resolve or escalate.
   - Confirm Teams notification, agent actions, and logs.
5. Document any limitations or future improvements (e.g., additional tools, more granular escalation rules).

#### Validation Check

- Teams notifications are sent for escalations and key automated resolutions.
- Human engineers receive enough context to continue investigation.
- Feedback from engineers is captured and can inform future improvements.
- End-to-end flow from incident creation → agent reasoning → actions → escalation works as expected.

---

## Success Criteria

**You will have successfully completed this challenge when you deliver:**

An **Autonomous IT Troubleshooting Agent** that can:

- Interpret and categorize incoming incidents.
- Use knowledge base patterns to propose and execute remediation steps.
- Trigger Power Automate flows or APIs for common fixes.
- Escalate complex or sensitive issues to humans in Microsoft Teams with full context.
- Log actions and decisions for transparency and future learning.

### Technical Deliverables

- **Foundation:** Azure AI / OpenAI resource, Power Automate environment, Teams channel, and Dataverse tables configured.  
- **Agent Logic:** Reasoning and planning loop implemented with clear prompting and escalation rules.  
- **Tooling:** Power Automate flows or APIs integrated as tools for remediation actions.  
- **Data & Logs:** Incident, knowledge base, and action logs stored and queryable.  
- **Orchestration:** Teams integration for alerts, escalation, and feedback loop.

### Business Outcomes

- **Reduced Manual Effort:** Simple, repetitive incidents are handled automatically.  
- **Faster Resolution:** Shorter response and resolution times for common IT issues.  
- **Better Visibility:** Clear logging and notifications for both automated and escalated incidents.  
- **Scalable Pattern:** A reusable blueprint for expanding agent-based troubleshooting to more services and teams.

## Additional Resources

- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/)  
- [Azure OpenAI Service Documentation](https://learn.microsoft.com/azure/ai-services/openai/)  
- [Power Automate Documentation](https://learn.microsoft.com/power-automate/)  
- [Microsoft Dataverse Documentation](https://learn.microsoft.com/power-apps/maker/data-platform-overview)  
- [Microsoft Teams Developer Documentation](https://learn.microsoft.com/microsoftteams/platform/)  

## Conclusion

By completing this challenge, you have built an **end-to-end autonomous IT troubleshooting agent** on the Microsoft cloud.

You learned how to:

- Set up core AI, automation, and collaboration resources.  
- Design an LLM-based reasoning loop for IT incidents.  
- Integrate the agent with Power Automate, Dataverse, and APIs for remediation.  
- Connect the agent to Microsoft Teams for alerts, escalation, and feedback.

This lab demonstrates how agentic AI patterns can transform IT operations by enabling **faster, more consistent, and more autonomous incident resolution**.