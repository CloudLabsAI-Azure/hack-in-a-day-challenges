# Challenge: Developing a Custom Retrieval-Augmented Generation (RAG) Application Using Azure AI Foundry

**Estimated Time:** 4 Hours  
 
**Industry Focus:** Cross-Industry (Technology, Analytics, Enterprise AI)

## Problem Statement
Organizations often rely on static knowledge bases, leading to outdated or incomplete responses from AI systems. Without retrieval mechanisms, generative models hallucinate or give irrelevant answers. Lack of unified observability and evaluation makes it hard to assess accuracy and reliability.

In this challenge, you will build a **custom RAG application using Azure AI Foundry SDK**. It includes setting up AI Foundry projects, deploying GPT and embedding models, configuring Azure AI Search for vector indexing, and integrating telemetry with Azure Monitor. You will implement ingestion, retrieval, and generation pipelines, evaluate quality with Azure AI Evaluators, and optimize for accuracy and performance.

## Goals
By the end of this challenge, you will deliver a **fully functional RAG app that retrieves indexed data and generates grounded, contextually accurate responses. Telemetry will be captured in Azure Monitor, and evaluation metrics will improve after fine-tuning. The resulting workspace can be reused for future enterprise AI projects** including:

- Configure Azure AI Foundry SDK, projects, and connected resources
- Build a full RAG pipeline (ingestion → embedding → retrieval → generation)
- Integrate OpenTelemetry and Azure Monitor for observability
- Use Azure AI Evaluators for relevance, coherence, and groundedness
- Optimize prompts and parameters for improved output quality

## Prerequisites
- **Skill Level:** Familiarity with Azure AI Services, AI Search, and OpenAI models
- **Audience:** AI Developers, Data Scientists, Cloud Engineers, Solution Architects  
- **Technology Stack:** Azure AI Foundry, Azure OpenAI Service, Azure AI Search, Azure Monitor + OpenTelemetry, Azure Storage Account, Azure Functions

## Datasets
Use the following sample datasets provided in lab files:

- **Product Knowledge Base:** ContosoTrek outdoor equipment catalog for retrieval scenarios
- **Evaluation Dataset:** Pre-labeled chat conversations for RAG quality assessment
- **Prompt Templates:** Optimized prompts for intent mapping and grounded chat responses

Ensure all datasets are stored in your local directory: `C:\Users\demouser\Downloads\ContosoTrek`

| File Path | Description |
|-----------|-------------|
| `assets/products.csv` | Product dataset for knowledge indexing and retrieval |
| `assets/chat_eval_data.jsonl` | Evaluation dataset for RAG performance testing |
| `intent_mapping.prompty` | Template for customer intent classification |
| `grounded_chat.prompty` | Template for contextually grounded responses |

## Challenge Objectives

### **Challenge 1: Foundation - Azure AI Foundry Setup and Model Deployment**
**Estimated Duration:** 90 Minutes

#### Objective
Establish Azure AI Foundry environment with proper resource provisioning, model deployments, and SDK configuration for RAG application development.

#### Tasks
1. **Provision Azure AI Foundry Infrastructure:**
   - Create Azure AI Hub (`ContosoHub`) in designated resource group (`ragsdk-<uniqueID>`)
   - Launch Azure AI Foundry portal and create new project (`ContosoTrek`)
   - Configure project settings and access controls for development team
   - Verify resource group contains all necessary Azure services

2. **Deploy Required AI Models:**
   - **Chat Model:** Deploy GPT-4.1-mini with Global Standard pricing tier for response generation
   - **Embedding Model:** Deploy text-embedding-ada-002 with Standard tier for vector embeddings
   - Configure model endpoints and validate deployment status in Models + Endpoints section
   - Test model connectivity and API response times for optimal performance

3. **Configure Azure AI Search Service:**
   - Create Azure AI Search service (`aisearch-<uniqueID>`) with Standard pricing tier
   - Configure search service in same resource group for optimal network performance
   - Set up proper authentication and access keys for integration
   - Verify search service is operational and ready for vector indexing

4. **Establish Service Connections:**
   - Connect Azure AI Search to AI Foundry project through Management Center
   - Configure API key authentication for secure service communication
   - Test connection validity and permissions between all services
   - Document connection strings and endpoints for development environment

#### Validation Check
- Azure AI Foundry hub and project are successfully created and operational
- Both chat and embedding models are deployed and responding correctly
- Azure AI Search service is configured and connected to the project
- All service connections are established with proper authentication

### **Challenge 2: Development - Build RAG Pipeline with Knowledge Indexing**
**Estimated Duration:** 120 Minutes

#### Objective
Implement complete RAG pipeline including knowledge ingestion, vector indexing, retrieval mechanisms, and response generation with proper SDK integration.

#### Tasks
1. **Setup Development Environment:**
   - Clone Azure AI samples repository to local development environment
   - Configure VS Code workspace with proper Python environment and extensions
   - Install required dependencies including Azure AI Foundry SDK and related packages
   - Set up environment variables with project connection strings and API keys

2. **Build Knowledge Ingestion Pipeline:**
   - **Data Preparation:** Load and preprocess ContosoTrek product catalog (`assets/products.csv`)
   - **Vector Embedding:** Generate embeddings using deployed text-embedding-ada-002 model
   - **Index Creation:** Create Azure AI Search index with vector search capabilities
   - **Document Upload:** Populate search index with embedded product knowledge base
   - **Validation:** Test search index functionality and vector similarity queries

3. **Implement Retrieval Mechanism:**
   - **Query Processing:** Convert user queries into vector embeddings for semantic search
   - **Similarity Search:** Retrieve relevant documents using vector similarity and hybrid search
   - **Context Assembly:** Combine retrieved documents into coherent context for generation
   - **Relevance Filtering:** Apply relevance thresholds to ensure high-quality context

4. **Develop Response Generation:**
   - **Prompt Engineering:** Utilize optimized prompt templates (`grounded_chat.prompty`)
   - **Context Integration:** Merge retrieved knowledge with user query for grounded responses
   - **Model Inference:** Generate responses using deployed GPT-4.1-mini model
   - **Response Validation:** Ensure generated responses are factually grounded in retrieved context

5. **Test End-to-End Pipeline:**
   - Execute complete RAG workflow with sample queries (e.g., "I need a new tent for 4 people")
   - Validate retrieval accuracy and response quality across different query types
   - Test error handling and fallback mechanisms for edge cases
   - Document pipeline performance metrics and response times

#### Validation Check
- Knowledge base is successfully indexed in Azure AI Search with vector capabilities
- Retrieval mechanism returns relevant documents for various query types
- Response generation produces contextually accurate and grounded answers
- End-to-end pipeline processes queries efficiently with acceptable latency

### **Challenge 3: Observability & Optimization - Telemetry Integration and Performance Evaluation**
**Estimated Duration:** 90 Minutes

#### Objective
Integrate comprehensive observability with OpenTelemetry and Azure Monitor, implement AI evaluation frameworks, and optimize RAG performance through systematic evaluation and prompt engineering.

#### Tasks
1. **Implement Observability and Telemetry:**
   - **OpenTelemetry Integration:** Configure distributed tracing for end-to-end RAG pipeline monitoring
   - **Azure Monitor Setup:** Connect telemetry data to Azure Monitor and Application Insights
   - **Performance Metrics:** Capture latency, throughput, and error rates across pipeline components
   - **Custom Instrumentation:** Add business-specific metrics for retrieval quality and user satisfaction

2. **Configure AI Evaluation Framework:**
   - **Azure AI Evaluators:** Implement CoherenceEvaluator, RelevanceEvaluator, and GroundednessEvaluator
   - **Evaluation Dataset:** Use `chat_eval_data.jsonl` for systematic quality assessment
   - **Automated Testing:** Set up automated evaluation pipeline for continuous quality monitoring
   - **Baseline Metrics:** Establish performance baselines for relevance, coherence, and groundedness scores

3. **Optimize RAG Performance:**
   - **Prompt Engineering:** Fine-tune prompt templates (`grounded_chat.prompty`, `intent_mapping.prompty`)
   - **Retrieval Optimization:** Adjust search parameters, relevance thresholds, and context window sizes
   - **Model Configuration:** Optimize temperature, top-p, and other generation parameters
   - **A/B Testing:** Compare different prompt strategies and configuration settings

4. **Advanced Features and Production Readiness:**
   - **Intent Classification:** Implement customer intent mapping for better query routing
   - **Safety and Guardrails:** Add content filtering and safety checks for production deployment
   - **Caching Strategies:** Implement intelligent caching for frequently asked questions
   - **Scalability Testing:** Validate performance under concurrent user loads

5. **Evaluation and Continuous Improvement:**
   - Execute comprehensive evaluation using Azure AI Evaluators across multiple metrics
   - Analyze evaluation results and identify areas for improvement
   - Iterate on prompt templates and configuration based on evaluation feedback
   - Document optimization strategies and performance improvements achieved

#### Validation Check
- OpenTelemetry and Azure Monitor successfully capture comprehensive RAG pipeline telemetry
- Azure AI Evaluators generate meaningful metrics for relevance, coherence, and groundedness
- Prompt optimization results in measurable improvements in evaluation scores
- Production-ready RAG application with proper observability and quality assurance

## Success Criteria
**You will have successfully completed this challenge when you deliver:**

A **fully functional RAG app that retrieves indexed data and generates grounded, contextually accurate responses. Telemetry will be captured in Azure Monitor, and evaluation metrics will improve after fine-tuning. The resulting workspace can be reused for future enterprise AI projects**.

### **Technical Deliverables:**
- **Infrastructure:** Azure AI Foundry hub and project with deployed chat and embedding models
- **Knowledge Pipeline:** Vector-indexed knowledge base with efficient retrieval mechanisms
- **RAG Application:** End-to-end pipeline processing queries and generating grounded responses
- **Observability:** OpenTelemetry integration with Azure Monitor capturing comprehensive telemetry
- **Quality Assurance:** AI evaluation framework measuring relevance, coherence, and groundedness
- **Optimization:** Fine-tuned prompts and parameters demonstrating measurable performance improvements
- **Production Readiness:** Scalable architecture with proper error handling and safety guardrails

### **Business Outcomes:**
- **Accurate AI Responses:** Elimination of hallucinations through grounded, context-aware generation
- **Enterprise Scalability:** Reusable workspace architecture for future AI application development
- **Quality Assurance:** Systematic evaluation framework ensuring consistent response quality
- **Operational Visibility:** Comprehensive monitoring enabling proactive performance management

## Additional Resources
- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Azure OpenAI Service Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [Azure AI Search Documentation](https://learn.microsoft.com/azure/search/)
- [Azure AI Evaluation Documentation](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app)
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
- [RAG Sample Repository](https://github.com/CloudLabsAI-Azure/azureai-samples)

## Conclusion  
By completing this challenge, you will have built a **production-ready RAG application** using Azure AI Foundry with comprehensive observability and quality assurance.

You learned how to:
- Set up Azure AI Foundry projects with proper resource provisioning and model deployments
- Build complete RAG pipelines with vector indexing, semantic retrieval, and grounded generation
- Integrate OpenTelemetry and Azure Monitor for comprehensive application observability
- Implement AI evaluation frameworks for systematic quality assessment and continuous improvement

This solution demonstrates how Azure AI Foundry enables **enterprise-grade AI applications** through integrated development environments, robust evaluation frameworks, and production-ready observability.
