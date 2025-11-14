# Challenge: Autonomous IT Troubleshooting Agent

**Estimated Time:** 4 Hours  

**Industry Focus:** IT Operations, Enterprise Support, Infrastructure Management  

## Problem Statement

IT teams spend significant time manually resolving common infrastructure issues like CPU overuse, service restarts, and user access errors. Manual diagnosis slows response time, clutters ticket queues, and diverts engineers from strategic work.

In this challenge, you will build an **autonomous troubleshooting agent** that uses an LLM-powered reasoning loop (for example, Azure OpenAI or Azure AI Foundry) to analyze issue descriptions and logs, query knowledge bases, and trigger corrective actions using Power Automate or APIs. The agent will also decide when to escalate complex or sensitive cases to humans via Microsoft Teams.

## Goals

By the end of this challenge, you will deliver an **LLM-driven IT agent** capable of:

- Interpreting incident descriptions and basic log data.
- Classifying common issues (e.g., CPU alerts, service down, access denied).
- Invoking remediation tools using Power Automate flows or APIs.
- Logging actions and decisions in Dataverse or another store.
- Escalating complex cases with context to IT engineers in Microsoft Teams.

## Expected Outcomes

You will have:

- A working agent capable of identifying and resolving simple IT incidents automatically.  
- Reduced average resolution time for repetitive support tasks (simulated in the lab).  
- A demonstrated reasoning and self-correction loop for IT troubleshooting.  
- Integration with Microsoft Teams for alerts and escalation.

## Prerequisites

- **Skill Level:** Basic Azure & M365 familiarity, plus introductory Power Automate skills.  
- **Audience:** IT operations engineers, support engineers, automation specialists, and solution architects.  
- **Technology Stack:**  
  - Azure AI Foundry / Azure OpenAI  
  - Power Automate  
  - Microsoft Teams  
  - Microsoft Dataverse  
  - Azure (for APIs / Functions and integration)

## Learning Objectives

By completing this challenge, you will:

- Understand agent loops and planning in agentic architectures.  
- Implement tool invocation using Power Automate or APIs.  
- Learn basic prompt-based reasoning and escalation logic.  
- Configure Copilot Studio or Foundry to surface the agent to end users.

## Datasets

Use the following sample assets provided in the lab files (or created as part of the lab):

- **Incident Samples:** A CSV or JSON file containing common incident records (issue type, severity, description, affected system).  
- **Knowledge Base Articles:** A simple table or dataset (for example, in Dataverse or a CSV) mapping common problems to recommended remediation steps.  
- **Action Logs:** A Dataverse table or equivalent used to store agent decisions, actions taken, and escalation history.

Ensure all datasets are stored under your local lab path (for example):  
`C:\LabFiles\AutonomousITAgent`

## Challenge Objectives

### **Challenge 1: Foundation – Set Up Environment and Knowledge Base**

**Estimated Duration:** 45 Minutes  

#### Objective

Establish the foundational components for the autonomous IT troubleshooting agent, including AI resources, data storage, and a simple knowledge base.

#### Tasks

1. Create or validate access to:
   - An Azure AI Foundry / Azure OpenAI resource.
   - A Power Automate environment.
   - A Microsoft Teams team/channel for IT alerts (e.g., `#it-operations`).
2. Create a Dataverse table (or equivalent) to store:
   - Incident samples (input).
   - Known fix patterns or remediation steps.
3. Import sample incident and knowledge base data into Dataverse or your chosen store.
4. Define a simple schema for:
   - **Incident**: Id, Title, Description, Category, Severity, Status.
   - **Remediation Pattern**: IssueType, Conditions, RecommendedAction, Script/Runbook link.
5. Verify that you can query this data from Power Automate or your API layer.

#### Validation Check

- Azure AI and Power Automate resources are accessible.
- Teams channel exists for receiving alerts.
- Dataverse (or equivalent) tables are created and populated with sample data.
- You can retrieve incidents and remediation patterns via a test flow or query.

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