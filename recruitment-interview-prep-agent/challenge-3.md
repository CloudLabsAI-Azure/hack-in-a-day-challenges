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

### Topic 1: Interview Question Generator

1. Open the HR Interview Copilot, from the top navigation bar, select **Topics** and click on **+ Add a topic** and select **From Blank** to create a new topic.

   >If you don't see Topics option from top menu, expand the menu using **+** option and select **Topics** from the list.

1. In the topic setup panel, under **Describe what this topic does**, enter:

   ```
   Generates interview question sets based on the job role and experience level. It asks the user which role and seniority to focus on, then produces 6–10 technical and behavioral interview questions grounded in the Job Description documents.
   ```

1. In the topic flow editor, add a new **Ask a question** node and add the below question in the input area:

   ```
   Which role do you want interview questions for, Software Developer or AI Engineer?
   ```

1. Under Identify, select **User’s entire response**.

1. Add one more Ask a question node and type:
   
   ```
   What is the experience level for this role? (Junior / Mid-Level / Senior)
   ```

1. Under Identify, again select **User’s entire response**.

1. Add a new node, select Advanced and choose **Generative answers**.

1. In the **Generative answers** node:

   - Click the three dots (…) and select the variable created earlier, which will be the only variable available (var1).

   - Under data sources, click on **edit**.

   - In the configuration pane, under **Knowledge Sources** enable **Search only selected sources** toggle.

   - From the list select only **Job Description** PDF's which ends with the name `jd`.

1. Click Save from the top-right corner and provide the name for the topic:
   
   ```
   Interview Question Generator
   ```

### Topic 2: Resume Fit & Evaluation

1. Navigate back to **Topics** page, using top menu.

1. From the Topics page, click **+Add New topic** again.

1. In the topic setup panel, under **Describe what this topic does**, enter:

   ```
   Evaluates a resume against a job role to identify strengths, gaps and role alignment. It asks the user for the role and the candidate resume, then classifies suitability as Strong Fit, Partial Fit, or Poor Fit with justification grounded in the uploaded documents.
   ```

1. In the topic flow editor, add a new **Ask a question** node and add the below question in the input area:

   ```
   Which job role should I evaluate the resume for, Software Developer or AI Engineer?
   ```

1. Under Identify, select **User’s entire response**.

1. Add one more Ask a question node and type:

   ```
   Please specify which candidate resume I should evaluate.
   ```

1. Under Identify, again select **User’s entire response**.

1. Add a new node, select Advanced and choose **Generative answers**.

1. In the **Generative answers** node:

   - Click the three dots (…) and select the variable created earlier, which will be the only variable available (var1).

   - In the edit pane, under **Knowledge Sources** enable **Search only selected sources** toggle.

   - From the list, select all the resume files, ones with the prefix `resume`.

1. Click Save from the top-right corner and provide the name for the topic:

   ```
   Resume Fit & Evaluation
   ```

## Test Both Topics

1. Ensure all files in the Knowledge tab show status **Ready**.

   >If your files are still in **in-progress** state, it will take up to 30 minutes to index all these files, please skip the test and continue with further configurations as you will be testing the complete agent further in this hackathon.

1. Click Test (top-right of Copilot Studio).

1. Trigger Interview Questions Generator by giving the below prompt and answer the questions asked by agent:

   ```
   Generate some interview questions
   ```
1. Trigger the Resume Fit & Evaluation workflow:

   ```
   Evaluate The candidate resumes
   ```
1. Once it asks for the role, enter any of the given role:

   - `Software Developer`
   - `AI Engineer`

1. On the next prompt to specify, enter the following prompt:

   ```
   Evaluate all resumes and generate a report on shortlisted candidate.
   ```
1. The Copilot should:

   - Ask the clarification questions configured in each topic  
   - Use only the uploaded documents as reference  
   - Provide structured, hiring-relevant output rather than generic responses

<validation step="b4aecad3-7029-4b33-8fd3-6ec2e8e53a3c" />
 
> **Congratulations** on completing the Challenge! Now, it's time to validate it. Here are the steps:
> - Hit the Validate button for the corresponding Challenge. If you receive a success message, you can proceed to the next Challenge. 
> - If not, carefully read the error message and retry the step, following the instructions in the lab guide.
> - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help.

## Success Criteria
- Both topics are visible in the Topics list and saved without errors.
- Each topic asks clarifying questions before generating answers.
- Responses reference only the uploaded knowledge sources.
- Generative answers DO NOT rely on open-world/general AI knowledge.

Click Next to continue to Challenge 04: Build the Live Interview Support Mode.
