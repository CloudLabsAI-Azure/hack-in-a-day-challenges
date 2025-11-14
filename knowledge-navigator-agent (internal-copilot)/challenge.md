# Challenge: Knowledge Navigator Agent (Internal Copilot)

**Estimated Time:** 4 Hours  

**Industry Focus:** Cross-Enterprise Knowledge Management, Internal Productivity  

## Problem Statement

Employees waste time searching for information spread across Teams, SharePoint, emails, and project tools. The lack of unified search and contextual reasoning leads to duplication of effort, inconsistent answers, and decreased productivity.

In this challenge, you will build a **Knowledge Navigator Agent (Internal Copilot)** that uses Azure AI Foundry, Azure AI Search, and Copilot Studio to unify knowledge access. The agent will autonomously decide which data source to query, retrieve relevant information, summarize it, and return grounded responses with citations. It will also be able to launch contextual actions, such as opening documents or sending summaries.

## Goals

By the end of this challenge, you will deliver a **conversational knowledge assistant** capable of:

- Performing natural-language Q&A across multiple enterprise data sources.  
- Using Azure AI Search for relevant and grounded retrieval.  
- Summarizing and reasoning over retrieved content with context awareness.  
- Citing sources and enabling users to navigate directly to underlying documents.  
- Triggering contextual actions (open links, send summaries via Teams/Email).

## Expected Outcomes

You will have:

- A conversational knowledge assistant with autonomous retrieval.  
- Natural-language Q&A across enterprise data sources.  
- Context-aware summarization and reasoning with proper citations.  
- Improved internal productivity and collaboration patterns (simulated in the lab).

## Prerequisites

- **Skill Level:** Familiarity with Microsoft 365 and Azure AI Search.  
- **Audience:** IT pros, solution architects, productivity engineers, and power users.  
- **Technology Stack:**  
  - Azure AI Foundry / Azure OpenAI  
  - Azure AI Search  
  - Microsoft Copilot Studio  
  - Power Automate  
  - Microsoft 365 services (Teams, SharePoint, Outlook)

## Learning Objectives

By completing this challenge, you will:

- Learn to use retrieval-augmented generation (RAG) patterns.  
- Implement data connectors and indexing via Azure AI Search.  
- Build reasoning and orchestration layers in Azure AI Foundry.  
- Integrate Copilot Studio for a user-friendly internal copilot interface.  
- Wire in contextual actions through Power Automate.

## Datasets / Content Sources

Use the following representative content sources provided in the lab (or configured as part of the exercise):

- **SharePoint Documents:** Policies, project documents, and internal guides.  
- **Teams / Wiki Content:** Channel messages, FAQs, and how-to notes (sample exports or seeded content).  
- **Knowledge Articles:** A small set of curated internal FAQs or KB articles stored as markdown, text, or pages.  
- **Metadata:** Optional labels such as department, project, or topic tags to improve filtering and relevance.

Ensure any local sample files are stored under a path such as:  
`C:\LabFiles\KnowledgeNavigator`  

(Actual enterprise connectors may be simulated via sample data in this lab.)

## Challenge Objectives

### **Challenge 1: Foundation – Set Up AI Foundry and AI Search**

**Estimated Duration:** 45 Minutes  

#### Objective

Establish the foundational components for the Knowledge Navigator Agent, including AI resources and an Azure AI Search index.

#### Tasks

1. Create or validate access to:
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