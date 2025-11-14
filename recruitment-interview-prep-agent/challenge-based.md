# Challenge: Recruitment Interview Prep Agent - Hack in a Day

**Estimated Time:** 4 Hours  

**Industry Focus:** Human Resources

## Problem Statement
HR teams and candidates often lack efficient tools to prepare for interviews or evaluate applicant fit. Manual question generation and feedback loops consume time and lack personalization. Traditional recruitment processes involve repetitive tasks such as reviewing resumes, generating interview questions, and providing consistent feedback—all of which can be time-consuming and prone to inconsistency.

In this challenge, you will develop an **HR Interview Copilot Agent** that autonomously generates role-specific interview questions, evaluates candidate resumes, and provides scoring or feedback using Azure OpenAI models. The agent will reason about job descriptions, identify skill mismatches automatically, and streamline the interview preparation process for both HR teams and candidates.

## Goals
By the end of this challenge, you will deliver a **fully functional HR Interview Copilot** with intelligent automation capabilities including:

- Automated generation of role-specific interview questions based on job descriptions
- AI-powered resume parsing and candidate evaluation
- Intelligent scoring and feedback mechanisms for skill alignment
- Reasoning-based candidate shortlisting with explainable decision-making
- Interactive interface for HR teams via Copilot Studio
- Integration with document repositories for seamless resume processing
- Ready-to-demo HR Copilot in Microsoft Teams

## Prerequisites
- **Skill Level:** Beginner to Intermediate
- **Audience:** HR Analysts, Recruiters, Developers
- **Required Knowledge:** Basic understanding of HR workflows, familiarity with Copilot Studio
- **Technology Stack:** Azure AI Foundry, Azure OpenAI, Copilot Studio, Power Automate, SharePoint

## Datasets
Use the following sample datasets provided in lab files:  

- **Sample Resumes:** Collection of candidate resumes in PDF/DOCX format for testing resume parsing and evaluation
- **Job Descriptions:** Sample job descriptions across various roles (Software Engineer, Data Analyst, HR Manager, etc.)
- **Evaluation Criteria Templates:** Predefined scoring rubrics for different job categories  

Ensure all datasets are stored in your designated SharePoint library or local directory: `C:\LabFiles\RecruitmentAgent`

## Challenge Objectives

### **Challenge 1: Foundation - Set Up Azure AI Environment and Resources**
**Estimated Duration:** 45 Minutes  

#### Objective
Establish the foundational Azure AI infrastructure required for building the intelligent recruitment agent.

#### Tasks
1. Create an Azure AI Foundry project named `RecruitmentCopilot_<uniqueID>` for centralized AI resource management
2. Deploy Azure OpenAI Service with the following models:
   - **GPT-4** for advanced reasoning and candidate evaluation
   - **GPT-3.5-turbo** for question generation and quick responses
3. Set up Azure Document Intelligence for resume parsing capabilities
4. Create a SharePoint document library `CandidateResumes` for centralized resume storage
5. Configure proper access controls and permissions for the Azure resources
6. Test API connectivity and verify model deployments

#### Validation Check
- Azure AI Foundry project is successfully created with proper resource group allocation
- Azure OpenAI models are deployed and accessible via API endpoints
- Document Intelligence service is operational and can process sample documents
- SharePoint library is configured with appropriate permissions
- API keys and endpoints are securely stored and accessible

### **Challenge 2: Document Processing - Build Resume Parsing and Analysis Pipeline**
**Estimated Duration:** 60 Minutes  

#### Objective
Implement intelligent document processing to extract, structure, and analyze candidate information from resumes.

#### Tasks
1. **Configure Document Intelligence:**
   - Set up custom document models for resume parsing
   - Define extraction schema for key resume sections (Education, Experience, Skills, Certifications)
   - Train the model on sample resume formats (PDF, DOCX, TXT)

2. **Build Resume Analysis Logic:**
   - Create Azure OpenAI prompts for structured data extraction
   - Implement skill categorization and tagging (Technical, Soft Skills, Domain Expertise)
   - Extract years of experience, education qualifications, and certifications
   - Identify relevant keywords matching job requirements

3. **Create Data Storage Schema:**
   - Design JSON structure for parsed resume data
   - Set up temporary storage in SharePoint or Azure Blob Storage
   - Implement metadata tagging for searchability

4. **Test Resume Processing:**
   - Upload sample resumes to SharePoint library
   - Execute parsing pipeline and validate extracted data accuracy
   - Review structured output for completeness and correctness

#### Validation Check
- Document Intelligence successfully extracts text and structure from various resume formats
- Azure OpenAI accurately categorizes skills and experience levels
- Parsed data is properly structured and stored with relevant metadata
- Processing pipeline handles errors gracefully (corrupted files, unsupported formats)
- Extraction accuracy meets minimum threshold (>85% for key fields)

### **Challenge 3: Intelligent Question Generation - Create Role-Specific Interview Questions**
**Estimated Duration:** 60 Minutes  

#### Objective
Develop an AI-powered system that generates contextual, role-specific interview questions based on job descriptions and candidate profiles.

#### Tasks
1. **Design Prompt Engineering Framework:**
   - Create system prompts for different interview types (Technical, Behavioral, Situational)
   - Build role-specific question templates (Engineering, Marketing, Finance, HR)
   - Implement difficulty level variation (Entry-level, Mid-level, Senior)

2. **Build Question Generation Logic:**
   - Analyze job description to extract key requirements and responsibilities
   - Cross-reference candidate resume to identify experience gaps and strengths
   - Generate 10-15 targeted questions per interview round
   - Include follow-up questions for deeper evaluation

3. **Implement Question Categories:**
   - **Technical Questions:** Role-specific skills and domain knowledge
   - **Behavioral Questions:** Past experience and problem-solving approach
   - **Situational Questions:** Hypothetical scenarios relevant to the role
   - **Culture Fit Questions:** Values alignment and team dynamics

4. **Create Reasoning Pipeline:**
   - Use Azure OpenAI reasoning capabilities to explain why each question is relevant
   - Map questions to specific job requirements and candidate gaps
   - Provide interviewer guidance notes for each question

5. **Build Question Customization Interface:**
   - Allow HR teams to adjust difficulty levels
   - Enable filtering by question category
   - Provide options to regenerate or refine specific questions

#### Validation Check
- Generated questions are relevant to job descriptions and role requirements
- Questions appropriately target candidate experience levels
- Question diversity covers technical, behavioral, and situational aspects
- AI provides clear reasoning for question selection
- Interviewer guidance notes are actionable and insightful
- Question quality meets HR team standards (validated through sample reviews)

### **Challenge 4: Candidate Evaluation & Scoring - Build AI-Powered Assessment System**
**Estimated Duration:** 75 Minutes  

#### Objective
Create an intelligent evaluation system that scores candidates, identifies skill mismatches, and provides explainable recommendations for hiring decisions.

#### Tasks
1. **Design Evaluation Framework:**
   - Create scoring rubrics for different job categories (0-100 scale)
   - Define weighted criteria (Technical Skills: 40%, Experience: 30%, Education: 15%, Cultural Fit: 15%)
   - Build mismatch detection logic for critical vs. nice-to-have requirements

2. **Implement Candidate Scoring Logic:**
   - Use Azure OpenAI to analyze resume against job description
   - Calculate skill match percentage for each requirement category
   - Identify experience gaps and overlaps with role responsibilities
   - Assess education and certification alignment
   - Generate overall candidate fit score with confidence intervals

3. **Build Reasoning and Explanation Engine:**
   - Provide detailed justification for each score component
   - Highlight strengths and areas of concern for each candidate
   - Generate comparative analysis when evaluating multiple candidates
   - Create visual scorecards for easy interpretation

4. **Implement Feedback Generation:**
   - **For HR Teams:** Actionable insights on candidate fit and interview focus areas
   - **For Candidates (Optional):** Constructive feedback on profile strengths and improvement areas
   - Include specific examples from resume supporting each evaluation point

5. **Create Shortlisting Automation:**
   - Automatically rank candidates based on evaluation scores
   - Flag high-potential candidates for priority review
   - Identify candidates requiring additional screening
   - Generate shortlist recommendations with explanations

6. **Test Evaluation Accuracy:**
   - Run evaluation on sample candidate pool (10-15 resumes)
   - Compare AI scoring with manual HR assessments
   - Refine prompts and criteria based on feedback
   - Validate reasoning quality and explainability

#### Validation Check
- Scoring system produces consistent and fair evaluations across candidates
- Skill mismatch detection accurately identifies critical gaps
- Explanations are clear, specific, and reference concrete resume details
- Candidate rankings align with HR team expectations (>80% agreement on top candidates)
- Feedback is constructive and actionable for both HR teams and candidates
- System handles edge cases (overqualified candidates, career changers) appropriately

### **Challenge 5: Copilot Studio Integration - Build Interactive HR Copilot Interface**
**Estimated Duration:** 60 Minutes  

#### Objective
Create an intuitive conversational interface using Copilot Studio that enables HR teams to interact with the recruitment agent seamlessly.

#### Tasks
1. **Set Up Copilot Studio Project:**
   - Create a new Copilot named `HR Interview Prep Copilot`
   - Configure authentication and user access controls
   - Connect to Azure OpenAI and Azure AI Foundry resources

2. **Design Conversational Flows:**
   - **Resume Upload Flow:** Accept resume files and trigger parsing pipeline
   - **Job Description Input Flow:** Capture role requirements and generate questions
   - **Candidate Evaluation Flow:** Analyze resume against job description and provide scoring
   - **Question Generation Flow:** Create interview questions on-demand
   - **Shortlist Review Flow:** Display ranked candidates with evaluation summaries

3. **Build Copilot Topics:**
   - **Topic 1: Upload and Analyze Resume**
     - Prompt user to upload resume or provide SharePoint link
     - Extract candidate information and display parsed summary
     - Store parsed data for future reference
   
   - **Topic 2: Generate Interview Questions**
     - Request job description or role title
     - Optionally accept candidate resume for personalized questions
     - Generate and display 10-15 role-specific questions with reasoning
     - Allow regeneration or refinement of specific questions
   
   - **Topic 3: Evaluate Candidate Fit**
     - Accept both job description and candidate resume
     - Perform comprehensive evaluation and scoring
     - Display detailed scorecard with explanations
     - Provide hiring recommendation with confidence level
   
   - **Topic 4: Compare Multiple Candidates**
     - Accept multiple resumes for batch evaluation
     - Generate comparative analysis and rankings
     - Highlight differentiating factors between candidates

4. **Implement Power Automate Flows:**
   - **Flow 1: Resume Processing Automation**
     - Trigger on new file upload to SharePoint
     - Call Document Intelligence API for parsing
     - Store structured data and notify Copilot
   
   - **Flow 2: Evaluation Report Generation**
     - Generate PDF reports of candidate evaluations
     - Email summaries to HR team members
     - Log evaluation history for compliance

5. **Configure Teams Integration:**
   - Deploy Copilot to Microsoft Teams as a bot
   - Set up channel notifications for new candidate submissions
   - Enable team collaboration features for candidate reviews

6. **Test End-to-End Workflows:**
   - Execute complete scenarios from resume upload to evaluation
   - Validate conversation flow logic and error handling
   - Test multi-turn conversations and context retention

#### Validation Check
- Copilot successfully authenticates and connects to Azure services
- All conversational topics function correctly with appropriate responses
- Resume upload and parsing workflow completes without errors
- Question generation produces relevant, high-quality outputs
- Evaluation scoring and explanations are clearly presented
- Power Automate flows execute reliably and handle failures gracefully
- Teams integration allows seamless interaction within HR workflows
- User experience is intuitive and requires minimal training

## Success Criteria
**You will have successfully completed this challenge when you deliver:**

A **fully operational HR Interview Copilot Agent** that automates question generation, resume evaluation, and candidate scoring with explainable AI reasoning—deployed in Microsoft Teams and ready for HR team collaboration.

### **Technical Deliverables:**
- **Azure AI Infrastructure:** Azure AI Foundry project with deployed OpenAI models and Document Intelligence service
- **Document Processing Pipeline:** Automated resume parsing with structured data extraction (>85% accuracy)
- **Question Generation System:** AI-powered interview question generator producing role-specific, contextual questions
- **Evaluation Engine:** Intelligent candidate scoring system with explainable reasoning and mismatch detection
- **Copilot Interface:** Conversational HR Copilot in Microsoft Teams with intuitive topic flows
- **Automation Workflows:** Power Automate flows for resume processing and report generation
- **Integration:** Seamless connection between SharePoint, Azure services, and Copilot Studio

### **Business Outcomes:**
- **Time Savings:** 70% reduction in manual question generation and resume review time
- **Improved Accuracy:** Consistent, bias-reduced candidate evaluations with explainable criteria
- **Enhanced Candidate Experience:** Faster feedback loops and personalized interview preparation
- **Scalability:** Ability to process high volumes of applications during peak hiring periods
- **Data-Driven Decisions:** Evidence-based shortlisting with documented reasoning for hiring choices
- **Team Collaboration:** Centralized platform for HR teams to collaborate on candidate evaluations

## Additional Resources
- [Azure AI Foundry Documentation](https://learn.microsoft.com/azure/ai-studio/)  
- [Azure OpenAI Service Guide](https://learn.microsoft.com/azure/ai-services/openai/)  
- [Copilot Studio Overview](https://learn.microsoft.com/microsoft-copilot-studio/)  
- [Azure Document Intelligence](https://learn.microsoft.com/azure/ai-services/document-intelligence/)  
- [Power Automate for HR Workflows](https://learn.microsoft.com/power-automate/)  
- [Responsible AI Guidelines](https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview)

## Conclusion
By completing this challenge, you will have built an **end-to-end AI-powered recruitment assistant** that transforms HR workflows.  

You learned how to:  
- Set up Azure AI services for intelligent document processing and reasoning.  
- Build automated resume parsing and candidate evaluation pipelines.  
- Create role-specific interview questions using advanced prompt engineering.  
- Develop explainable AI systems for fair and transparent hiring decisions.  
- Integrate conversational AI into Microsoft Teams for seamless HR collaboration.  

This lab demonstrates how **Azure AI and Copilot Studio** enable HR teams to make faster, more informed hiring decisions while maintaining consistency, fairness, and transparency throughout the recruitment process.
