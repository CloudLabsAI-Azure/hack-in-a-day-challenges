# Challenge-Based Learning: Internal Knowledge Navigator

**Estimated Time:** 4 Hours  

**Industry Focus:** Internal Knowledge Management, Employee Productivity  

## Problem Statement

Employees waste time searching for policies and procedures across different departments. Information is scattered in various document repositories, leading to repeated questions, inconsistent answers, and decreased productivity. HR, Finance, IT, and Procurement teams spend hours answering the same basic questions.

In this challenge, you will build an **Internal Knowledge Navigator** copilot using Microsoft Copilot Studio that helps employees quickly find information across departments with AI-powered search, citation-based answers, and automated actions.

## Goals

By the end of this challenge, you will deliver a **conversational knowledge assistant** capable of:

- Answering employee questions across HR, Finance, IT, and Procurement departments
- Providing responses with citations showing document sources
- Guiding employees through common processes with conversational topics
- Emailing policy documents on request
- Creating IT support tickets automatically
- Sending conversation summaries to employees or managers

## Expected Outcomes

You will have:

- An Internal Knowledge Navigator copilot accessible via web or Teams
- Knowledge base with 12 department documents (HR, Finance, IT, Procurement)
- 4 department-specific conversational topics with smart routing
- Citation-based answers showing document sources
- 3 automated actions (email documents, create tickets, send summaries)
- Production-ready solution helping employees find information 10x faster

## Prerequisites

- **Skill Level:** Beginner to Intermediate
- **Audience:** IT teams, business analysts, department coordinators, employee experience managers
- **Technology Stack:**  
  - Microsoft Copilot Studio (no-code platform)
  - Power Automate
  - Microsoft 365 (Teams, Outlook)
  - Optional: Freshdesk or other ticketing system

## Learning Objectives

By completing this challenge, you will:

- Create and configure copilots in Microsoft Copilot Studio
- Upload and manage multi-department knowledge bases
- Design conversational topics with branching logic
- Enable AI-powered answers with proper citations
- Integrate Power Automate flows for automated actions
- Test and deploy enterprise knowledge assistants

## Datasets / Content Sources

This challenge uses 12 internal policy documents across 4 departments:

**HR Department (3 documents):**
- Leave Policy (annual, sick, personal leave)
- Onboarding Guide (first day checklist, orientation)
- Benefits Guide (health insurance, retirement, wellness)

**Finance Department (3 documents):**
- Expense Policy (business expenses, approval limits)
- Travel Reimbursement (booking, per diem, receipts)
- Budget Request (annual planning, approval workflow)

**IT Department (3 documents):**
- Software Access (request process, licenses)
- Support Guide (common issues, troubleshooting)
- Security Policy (passwords, MFA, data protection)

**Procurement Department (3 documents):**
- Purchase Request (approval thresholds, PO process)
- Vendor Management (onboarding, performance)
- Contract Process (legal review, signatures)

All documents should be in PDF format. See the `datasets/` folder for detailed document specifications and creation guidelines.

## Challenge Objectives

### **Challenge 1: Create Your Internal Knowledge Copilot**

**Estimated Duration:** 30 Minutes  

#### Objective

Set up Microsoft Copilot Studio and create your first Internal Knowledge Navigator copilot with basic configuration.

#### What You'll Do

1. Sign in to Microsoft Copilot Studio
2. Create a new copilot named "Internal Knowledge Navigator"
3. Configure copilot settings and identity
4. Customize welcome message and icon
5. Verify environment setup

#### Success Criteria
- Copilot created and configured
- Basic greeting functionality working
- Ready for knowledge base upload

---

### **Challenge 2: Upload Department Documents**

**Estimated Duration:** 45 Minutes  

#### Objective

Upload policy and procedure documents from HR, Finance, IT, and Procurement departments to create a comprehensive knowledge base.

#### What You'll Do

1. Access the 12 department PDF documents
2. Upload HR documents (Leave Policy, Onboarding, Benefits)
3. Upload Finance documents (Expense, Travel, Budget)
4. Upload IT documents (Software Access, Support, Security)
5. Upload Procurement documents (Purchase Request, Vendor, Contract)
6. Verify all knowledge sources are indexed
7. Test basic knowledge retrieval

#### Success Criteria
- All 12 documents uploaded successfully
- Knowledge sources show "Active" status
- Test queries return relevant information from documents

---

### **Challenge 3: Design Department Topics**

**Estimated Duration:** 60 Minutes  

#### Objective

Create guided conversational topics organized by department to handle common employee inquiries with smart routing and branching logic.

#### What You'll Do

1. Create HR Leave Policy topic with trigger phrases and conversation flow
2. Create Finance Travel Reimbursement topic with conditional branching
3. Create IT Software Access topic with ticket creation option
4. Create Procurement Purchase Request topic with approval paths
5. Add dynamic questions and user input handling
6. Connect topics to relevant knowledge sources
7. Test each department topic thoroughly

#### Success Criteria
- 4 department topics created with appropriate trigger phrases
- Conversational flows include branching logic
- Generative answers pull from correct department documents
- All topics tested and working correctly

---

### **Challenge 4: Enable Citation Answers**

**Estimated Duration:** 45 Minutes  

#### Objective

Configure your copilot to provide answers with proper citations showing document sources, building trust and transparency.

#### What You'll Do

1. Enable citations in generative AI settings
2. Configure citation display format
3. Update generative answer nodes in topics to show citations
4. Test citation display across all departments
5. Verify citations are clickable and accessible
6. Test multi-source citations
7. Create a help topic explaining citations

#### Success Criteria
- Citations enabled and displayed in all answers
- Citations show document name and page number
- Citations are clear and professionally formatted
- Multi-source answers show multiple citations
- Users can access source documents via citations

---

### **Challenge 5: Add Trigger Actions**

**Estimated Duration:** 60 Minutes  

#### Objective

Integrate Power Automate flows to enable automated actions: emailing documents, creating support tickets, and sending conversation summaries.

#### What You'll Do
   - An **Azure AI Foundry** (or Azure OpenAI) resource.  
   - An **Azure AI Search** service.
2. Create a **search index** to store enterprise content with fields such as:
   - Id, Title, Content, SourceType (SharePoint, Teams, FAQ), URL, Tags.
3. Upload or ingest a small set of sample internal documents into the index (via sample script, import wizard, or indexer).
4. Verify that you can query the index using basic keyword or semantic search.

#### Validation Check

- Azure AI Foundry and AI Search resources are accessible.  
- A search index is created and populated with sample enterprise content.  
- Test queries return relevant documents and metadata.

---

### **Challenge 2: Data Connectors & Indexing – Connect Enterprise Data**

**Estimated Duration:** 60 Minutes  

#### Objective

Extend the index with multiple content types and configure connectors / indexing pipelines to represent a realistic enterprise knowledge landscape.

#### Tasks

1. Define one or more **data sources** in Azure AI Search (or simulate them) such as:
   - SharePoint site/document library.
   - File storage with markdown/PDF files.
   - FAQ/KB dataset (e.g., CSV/JSON).
2. Configure or simulate **indexers** that:
   - Pull content from each data source.
   - Normalize fields into the common index schema (Title, Content, SourceType, URL, Tags).
3. Add basic **filters and facets**:
   - For example, filter by SourceType or Tag.
4. Test queries that:
   - Retrieve results from multiple content types.
   - Demonstrate that the index includes diverse enterprise content.

#### Validation Check

- Indexers successfully ingest content from defined data sources.  
- The unified index can be filtered and searched across all sources.  
- Documents are labeled with sufficient metadata to support downstream reasoning.

---

### **Challenge 3: Reasoning & RAG – Build the Knowledge Navigator Agent**

**Estimated Duration:** 60 Minutes  

#### Objective

Use Azure AI Foundry and Azure OpenAI to implement a RAG-based reasoning workflow that autonomously selects, retrieves, and summarizes content with citations.

#### Tasks

1. In Azure AI Foundry, create a **Knowledge Navigator Agent** (or orchestration flow) that:
   - Receives a user question in natural language.
   - Determines what kind of content is likely needed (policy, project, FAQ, etc.).
   - Issues a retrieval request to Azure AI Search with appropriate query parameters.
2. Implement a **RAG pipeline**:
   - Use search results as context for the LLM.
   - Generate an answer that:
     - Is grounded strictly in retrieved content.
     - Includes inline or end-of-answer citations (e.g., “Source: Project Charter Doc”).
3. Add **autonomous selection logic**:
   - Vary query types (keyword vs semantic) or filters based on the user’s question.
   - For example, route “How do I apply for leave?” to HR policy content, but “What is the design of Project X?” to project documents.
4. Test the agent on several queries:
   - “Where can I find the onboarding checklist?”  
   - “What are the key milestones for Project Alpha?”  
   - “Summarize the latest release notes for the CRM app.”

#### Validation Check

- Agent retrieves relevant content from the unified index.  
- Answers are grounded, coherent, and contain citations to underlying documents.  
- Different query types lead to appropriate source selections.

---

### **Challenge 4: Copilot Experience & Actions – Integrate with Copilot Studio and Power Automate**

**Estimated Duration:** 60 Minutes  

#### Objective

Expose the Knowledge Navigator Agent as an internal copilot in Copilot Studio and enable contextual actions using Power Automate.

#### Tasks

1. In **Microsoft Copilot Studio**, create a copilot that:
   - Connects to the Knowledge Navigator Agent backend (e.g., via API or AI Foundry endpoint).
   - Presents a chat-based interface for users to ask questions.
2. Configure **conversation flows**:
   - Pass user questions to the agent.
   - Display answers, including citations and relevant document links.
3. Add **contextual actions** using Power Automate:
   - For example:
     - A command like “Send me this summary in Teams” triggers a flow to post the answer in a Teams chat/channel.
     - A command like “Email this to my manager” triggers an email with the summary and links.
4. Implement basic **session context**:
   - Allow follow-up questions (e.g., “Show me more details” or “Filter to 2024 documents”) to reuse previous results context.
5. Run an **end-to-end scenario**:
   - Ask a multi-step question (e.g., “Summarize the latest project status for Project Alpha and send me a summary in Teams.”).
   - Confirm retrieval, reasoning, and action execution.

#### Validation Check

- Copilot Studio provides a functional chat interface backed by the Knowledge Navigator Agent.  
- Users can receive grounded answers with citations and open relevant documents.  
- Power Automate actions (send summary, post to Teams, etc.) work as expected.  
- Conversation context is preserved across follow-up questions.

---

## Success Criteria

**You will have successfully completed this challenge when you deliver:**

A **Knowledge Navigator Agent (Internal Copilot)** that can:

- Search across multiple enterprise content sources using Azure AI Search.  
- Use RAG patterns to generate grounded, cited responses.  
- Provide conversational access via Copilot Studio.  
- Execute contextual actions through Power Automate (e.g., share summaries, open documents).

### Technical Deliverables

- **Foundation:** Azure AI Foundry/OpenAI and Azure AI Search configured with a unified index.  
- **Connectors:** Data sources and indexers ingesting representative enterprise content.  
- **Reasoning:** RAG pipeline that retrieves, reasons, and responds with citations.  
- **Experience:** Copilot Studio bot wired to the agent for conversational UX.  
- **Actions:** Power Automate flows to perform contextual actions initiated from the copilot.

### Business Outcomes

- **Faster Discovery:** Reduced time spent searching for documents and answers.  
- **Consistent Responses:** More standardized and accurate internal answers.  
- **Higher Productivity:** Less duplication of effort and fewer “where is that doc?” questions.  
- **Better Collaboration:** Teams can quickly share summarized, contextual information.

## Additional Resources

- [Azure AI Search Documentation](https://learn.microsoft.com/azure/search/)  
- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/)  
- [Azure OpenAI Service Documentation](https://learn.microsoft.com/azure/ai-services/openai/)  
- [Microsoft Copilot Studio Documentation](https://learn.microsoft.com/copilot-studio/)  
- [Power Automate Documentation](https://learn.microsoft.com/power-automate/)  

## Conclusion

By completing this challenge, you have built an **end-to-end Knowledge Navigator Agent (Internal Copilot)** on the Microsoft cloud.

You learned how to:

- Index and unify enterprise content with Azure AI Search.  
- Apply retrieval-augmented generation with Azure AI Foundry and Azure OpenAI.  
- Deliver a conversational internal copilot using Copilot Studio.  
- Enable contextual actions and sharing workflows with Power Automate.

This lab demonstrates how agentic AI and RAG patterns can greatly improve **enterprise knowledge discovery, collaboration, and productivity**.