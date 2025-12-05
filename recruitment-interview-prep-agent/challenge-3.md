# Challenge 03: Build Interview Topics for HR Support

## Introduction
The HR Interview Copilot now has access to Job Descriptions and Resumes through the Knowledge section.  
In this challenge, you will create two interactive interview topics that:
1) Ask the user for input  
2) Use uploaded documents as the grounding source  
3) Produce structured hiring insights based only on the provided documents

This ensures the Copilot behaves like a real HR assistant rather than a generic AI.

##  Challenge Objectives
- Create two interactive hiring topics using the new Copilot Studio UI
- Ask clarifying questions before generating responses
- Configure Generative answers to only use the uploaded knowledge documents


## Steps to Complete

### Topic 1 — Interview Question Generator

1. Open the HR Interview Copilot → click Topics → New topic.

2. In the topic setup panel, under “Describe what this topic does”, enter:

   ```
   Generates interview question sets based on the job role and experience level. It asks the user which role and seniority to focus on, then produces 6–10 technical and behavioral interview questions grounded in the Job Description documents.
   ```

3. In the topic flow editor, add a new **Ask a question** node and type:

   ```
   Which role do you want interview questions for — Software Developer or AI Engineer?
   ```

4. Under Identify, select **User’s entire response**.

5. Add one more Ask a question node and type:

   What is the experience level for this role? (Junior / Mid-Level / Senior)

6. Under Identify, again select User’s entire response.

7. Add a new node → Advanced → Generative answers.

8. In the Generative answers node:

   - Click the three dots (…) and select the variable created earlier  
   - Click Edit under Data sources  
   - Enable Search only selected resources  
   - Select all Job Description documents  
   - Disable Allow AI to use its own general knowledge

9. Click Save from the top-right corner and provide the name for the topic:
   Interview Question Generator

### Topic 2 — Resume Fit & Evaluation

1. From the Topics page, click New topic again.
2. In the topic setup panel, under “Describe what this topic does”, enter:
   Evaluates a resume against a job role to identify strengths, gaps and role alignment. It asks the user for the role and the candidate resume, then classifies suitability as Strong Fit, Partial Fit, or Poor Fit with justification grounded in the uploaded documents.
3. Add a new Ask a question node and type:
   Which job role should I evaluate the resume for — Software Developer or AI Engineer?
4. Under Identify, select User’s entire response.
5. Add one more Ask a question node and type:
   Please specify which candidate resume I should evaluate.
6. Under Identify, select User’s entire response.
7. Add a new node → Advanced → Generative answers.
8. In the Generative answers node:
   • Click the three dots (…) and select the variable created earlier  
   • Click Edit under Data sources  
   • Enable Search only selected resources  
   • Select all Resume documents and both Job Descriptions  
   • Disable Allow AI to use its own general knowledge
9. Click Save from the top-right corner and provide the name for the topic:
   Resume Fit & Evaluation

---

## Test Both Topics

1. Ensure all files in the Knowledge tab show status “Ready”.
2. Click Test (top-right of Copilot Studio).
3. Try the following prompts:
   Generate interview questions for a Senior AI Engineer
   Evaluate this resume for the Software Developer role
4. The Copilot should:
   • Ask the clarification questions configured in each topic  
   • Use only the uploaded documents as reference  
   • Provide structured, hiring-relevant output rather than generic responses

---

## Success Criteria
- Both topics are visible in the Topics list and saved without errors.
- Each topic asks clarifying questions before generating answers.
- Responses reference only the uploaded knowledge sources.
- Generative answers DO NOT rely on open-world/general AI knowledge.

---

Click Next to continue to Challenge 04: Build the Live Interview Support Mode.
