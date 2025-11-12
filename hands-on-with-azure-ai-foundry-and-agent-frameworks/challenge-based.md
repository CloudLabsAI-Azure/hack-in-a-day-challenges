# Challenge: Hands-on with Azure AI Foundry & Agent Frameworks

**Estimated Time:** 4 Hours  
**Difficulty Level:** Intermediate  
**Industry Focus:** Healthcare & Wellness (Cross-Industry use)

## Problem Statement
Enterprises struggle to move beyond basic LLM demos to production-ready, goal-driven agents that combine reasoning, retrieval, observability, and automation. Lack of integrated tools for RAG, telemetry, and multi-agent orchestration slows experimentation and governance.

In this challenge, you will build **intelligent, task-oriented agents using Azure AI Foundry**. You will configure projects, connect models and vector stores, apply RAG, integrate Azure AI Search and Bing grounding, add observability via OpenTelemetry/Azure Monitor, and implement multi-agent reasoning with Semantic Kernel and Autogen for health and fitness scenarios.

## Goals
By the end of this challenge, you will deliver a **functional multi-agent AI system grounded with Azure AI Search and RAG pipelines, capable of contextual reasoning, observability, and safe automation. You will finish with deployable AI agents and an understanding of evaluation and governance patterns in Azure AI Foundry** including:

- Set up Azure AI Foundry workspace, authentication, and SDK
- Run chat completions and embeddings  
- Build RAG pipelines for context grounding
- Develop agents using tools (code interpreter, web/Bing grounding, Azure AI Search)
- Add observability and evaluation via OpenTelemetry/Azure Monitor
- Integrate event-driven triggers
- Extend to multi-agent orchestration with Semantic Kernel + Autogen

## Prerequisites
- **Skill Level:** Familiarity with Azure AI Services, Azure AI Search, and OpenAI models
- **Audience:** AI developers, data scientists, solution architects, research engineers
- **Technology Stack:** Azure AI Foundry, Azure OpenAI Service, Azure AI Search, Semantic Kernel, Autogen Framework, Azure Monitor + OpenTelemetry, Azure Functions/Event Grid, Bing Grounding, GitHub Integration

## Datasets
Use the following sample datasets provided in lab files:

- **Health & Fitness Knowledge Base:** Wellness tips, nutrition data, and exercise routines for contextual AI responses
- **Multi-Agent Scenarios:** Complex health consultation workflows requiring agent collaboration
- **Evaluation Data:** Pre-labeled conversations for agent performance assessment

Ensure all datasets are stored in your development environment with proper notebook configurations.

| Resource Type | Description |
|---------------|-------------|
| `health_tips.csv` | Wellness and nutrition guidance for RAG implementation |
| `fitness_routines.json` | Exercise programs and training data for agent responses |
| Jupyter Notebooks | Pre-configured lab exercises with health and fitness scenarios |
| Vector Store Data | Embedded health resources for semantic search and retrieval |

## Challenge Objectives

### **Challenge 1: Foundation - Azure AI Foundry Setup and Authentication**
**Estimated Duration:** 60 Minutes

#### Objective
Establish Azure AI Foundry environment with proper authentication, project configuration, and validate connections to AI models and search services.

#### Tasks
1. **Configure Azure AI Foundry Environment:**
   - Navigate and explore Azure AI Foundry workspace interface and available resources
   - Understand models, endpoints, projects, and data management capabilities
   - Configure development environment with proper Python kernel and dependencies
   - Validate workspace permissions and access controls for development team

2. **Implement Authentication and Project Setup:**
   - Authenticate Azure credentials using Azure CLI integration in VS Code Jupyter environment
   - Configure AI Project Client with proper connection strings and security settings
   - Initialize AI Foundry project with health and fitness focus area
   - Validate connections to Azure OpenAI Service and Azure AI Search

3. **Test Basic AI Operations:**
   - Execute initial chat completion requests to verify model connectivity
   - Create basic AI agent and establish conversation thread for testing
   - Generate sample outputs to confirm environment functionality
   - Document authentication tokens and connection settings for development workflow

4. **Validate Service Integration:**
   - Test Azure OpenAI model endpoints and response quality
   - Verify Azure AI Search service connectivity and indexing capabilities
   - Confirm OpenTelemetry and Azure Monitor integration for observability
   - Establish baseline performance metrics for subsequent optimization

#### Validation Check
- Azure AI Foundry workspace is properly configured with authenticated access
- AI Project Client successfully connects to all required Azure services
- Basic chat completion and agent creation operations function correctly
- Development environment has all necessary dependencies and kernel configurations

### **Challenge 2: AI Development - RAG Implementation and Agent Creation**
**Estimated Duration:** 120 Minutes

#### Objective
Build comprehensive RAG pipelines and develop specialized AI agents with advanced tool integration for health and fitness scenarios.

#### Tasks
1. **Implement Chat Completions and Embeddings:**
   - Configure chat completion client with Azure OpenAI models for health and fitness conversations
   - Generate text and image embeddings for wellness content and visual health resources
   - Apply prompt engineering techniques for health-specific use cases and safety considerations
   - Test multiple AI models including GPT-4, Phi-4, and DeepSeek-R1 for comparative analysis

2. **Build RAG Pipelines for Health Intelligence:**
   - **Knowledge Indexing:** Embed health tips, nutrition data, and fitness routines into vector stores
   - **Semantic Retrieval:** Implement vector search capabilities for contextually relevant health information
   - **Context-Aware Generation:** Combine retrieved knowledge with LLM generation for grounded responses
   - **Multi-Modal RAG:** Integrate text and image embeddings for comprehensive health guidance

3. **Develop Specialized Health & Fitness Agents:**
   - **Wellness Assistant Agent:** Create conversational agent for general health and fitness guidance
   - **Health Calculator Agent:** Develop agent with code interpreter for BMI, nutrition, and fitness calculations
   - **Resource Search Agent:** Build file search agent with vector store integration for health documentation
   - **Real-Time Information Agent:** Implement Bing grounding for current health news and research updates

4. **Integrate Advanced Agent Tools:**
   - **Code Interpreter Integration:** Enable agents to perform calculations, data analysis, and visualization
   - **Vector Search Capabilities:** Connect agents to indexed health knowledge bases for informed responses
   - **Web Grounding:** Integrate Bing search for real-time health information and latest research
   - **Azure AI Search Integration:** Build comprehensive search and retrieval capabilities for fitness content

5. **Test Agent Functionality and Performance:**
   - Execute comprehensive testing scenarios across different health and fitness use cases
   - Validate agent responses for accuracy, safety, and contextual relevance
   - Test multi-turn conversations and agent memory capabilities
   - Performance benchmark different models and configurations for optimal user experience

#### Validation Check
- Chat completions and embeddings work effectively across multiple AI models
- RAG pipelines retrieve relevant health information and generate contextually appropriate responses
- Specialized agents perform their designated functions with proper tool integration
- All agent types handle multi-turn conversations and maintain context effectively

### **Challenge 3: Advanced Integration - Observability and Multi-Agent Orchestration**
**Estimated Duration:** 120 Minutes

#### Objective
Implement comprehensive observability with OpenTelemetry and Azure Monitor, and build sophisticated multi-agent systems using Semantic Kernel and Autogen for complex health and fitness scenarios.

#### Tasks
1. **Integrate Observability and Monitoring:**
   - **OpenTelemetry Configuration:** Set up distributed tracing for end-to-end agent interaction monitoring
   - **Azure Monitor Integration:** Connect telemetry data to Azure Monitor and Application Insights
   - **Performance Metrics:** Capture latency, success rates, and error patterns across agent operations
   - **Custom Instrumentation:** Add health-specific metrics for agent effectiveness and user satisfaction

2. **Implement Advanced Agent Evaluation:**
   - **Quality Assurance:** Monitor LLM interactions for reliability, accuracy, and compliance with health guidelines
   - **Safety Monitoring:** Implement guardrails for health-related advice and medical disclaimers
   - **Performance Tracking:** Create dashboards for agent response times and user engagement metrics
   - **Evaluation Frameworks:** Set up automated testing for agent quality and consistency

3. **Build Multi-Agent Orchestration with Semantic Kernel:**
   - **Semantic Kernel Integration:** Connect Azure AI Search with Semantic Kernel for enhanced agent capabilities
   - **Agent Composition:** Create specialized agents that work together for comprehensive health consultations
   - **Skill Development:** Build reusable skills for nutrition analysis, exercise planning, and wellness tracking
   - **Context Sharing:** Implement agent-to-agent communication and shared context management

4. **Implement Autogen Multi-Agent Framework:**
   - **GitHub Authentication:** Configure secure GitHub integration with Personal Access Tokens
   - **Multi-Agent Conversations:** Set up collaborative agent workflows for complex health scenarios
   - **RAG-Enhanced Reasoning:** Combine retrieval capabilities with multi-agent decision making
   - **Asynchronous Processing:** Enable event-driven agent interactions and automated workflow triggers

5. **Advanced Features and Production Readiness:**
   - **Event-Driven Architecture:** Integrate Azure Functions and Event Grid for automated agent triggers
   - **Security and Compliance:** Implement proper authentication, authorization, and health data protection
   - **Scalability Testing:** Validate multi-agent performance under concurrent user loads
   - **Governance Patterns:** Establish agent lifecycle management and deployment best practices

6. **End-to-End Integration Testing:**
   - Test complex multi-agent scenarios involving health consultations, fitness planning, and nutrition guidance
   - Validate observability data collection and monitoring effectiveness
   - Confirm event-driven triggers and automated agent orchestration
   - Verify security controls and compliance with health data regulations

#### Validation Check
- OpenTelemetry and Azure Monitor successfully capture comprehensive agent telemetry and performance metrics
- Multi-agent systems using Semantic Kernel and Autogen work collaboratively on complex health scenarios
- Event-driven architecture triggers agents appropriately and maintains proper security controls
- Production-ready multi-agent system demonstrates governance patterns and scalable architecture

## Success Criteria
**You will have successfully completed this challenge when you deliver:**

A **functional multi-agent AI system grounded with Azure AI Search and RAG pipelines, capable of contextual reasoning, observability, and safe automation. You will finish with deployable AI agents and an understanding of evaluation and governance patterns in Azure AI Foundry**.

### **Technical Deliverables:**
- **Foundation Infrastructure:** Azure AI Foundry workspace with authenticated access and proper SDK configuration
- **RAG Pipelines:** Production-ready retrieval-augmented generation for health and fitness knowledge bases
- **Specialized Agents:** Multiple AI agents with tool integration (code interpreter, web grounding, vector search)
- **Observability Framework:** OpenTelemetry and Azure Monitor integration capturing comprehensive agent telemetry
- **Multi-Agent Orchestration:** Semantic Kernel and Autogen frameworks enabling collaborative agent workflows
- **Event-Driven Architecture:** Azure Functions and Event Grid integration for automated agent triggers
- **Production Readiness:** Security controls, governance patterns, and scalable deployment architecture

### **Business Outcomes:**
- **Intelligent Automation:** Goal-driven agents that move beyond basic demos to production-ready task automation
- **Contextual Reasoning:** RAG-enabled agents providing accurate, grounded responses for health and fitness scenarios
- **Operational Visibility:** Comprehensive monitoring enabling proactive agent performance management and compliance
- **Scalable AI Platform:** Reusable framework for building and deploying enterprise-grade multi-agent systems

## Additional Resources
- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Semantic Kernel Documentation](https://learn.microsoft.com/semantic-kernel/)
- [Autogen Framework Documentation](https://microsoft.github.io/autogen/)
- [Azure OpenAI Service Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [Azure AI Search Documentation](https://learn.microsoft.com/azure/search/)
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)

## Conclusion
By completing this challenge, you will have built **production-ready, multi-agent AI systems** using Azure AI Foundry with comprehensive observability and governance.

You learned how to:
- Set up Azure AI Foundry projects with proper authentication and service integration
- Build RAG pipelines combining retrieval, reasoning, and generation for contextual AI responses
- Develop specialized agents with advanced tool integration and multi-turn conversation capabilities
- Implement observability and evaluation frameworks for reliable AI operations and compliance
- Orchestrate multi-agent systems using Semantic Kernel and Autogen for complex task automation

This solution demonstrates how Azure AI Foundry enables **enterprise-grade AI agent development** through integrated tooling, comprehensive observability, and scalable multi-agent orchestration frameworks.