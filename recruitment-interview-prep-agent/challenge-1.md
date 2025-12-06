# Challenge 01: Create the HR Interview Copilot  

## Introduction
Recruitment teams spend significant time generating interview questions, screening resumes, and evaluating whether candidates align with job descriptions.  
To simplify the hiring process, Contoso HR wants to implement an AI-powered Copilot that acts as an **Interview Intelligence Assistant**.  
This Copilot will later evaluate resumes against job descriptions, generate technical and behavioral interview questions, and support HR during live interviews with follow-up question recommendations.

In this challenge, you will create the **HR Interview Copilot** in Copilot Studio, serving as the foundation for the rest of the lab.

## Challenge Objectives
- Create a new Copilot in Copilot Studio.
- Configure the Copilot name, description, and HR-focused system instructions.
- Enable the Copilot to support multiple recruitment assistance use cases.

## Steps to Complete

1. Open **Microsoft Copilot Studio**.

1. On the Copilot Studio pane, from left menu select **Create** and then click on **+New Agent** option to create a new agent.

1. If any error shows up like `There was a problem creating your agent.`, then please click on **Create a blank agent**.

1. On the overview pane of the agent, click on **edit** inside Details card to edit agent's name and description.

1. Configure the Copilot details as below:

   - **Name:** `HR Interview Copilot`

   - **Description:** `Assists HR teams in hiring Software Developers and AI Engineers by evaluating resumes against job descriptions and generating structured interview question sets.`

1. Click on save.

1. Once done, scroll down and add below **instruction** by clicking on **edit** inside Instruction card.

     ```
     You are an autonomous HR Interview Copilot that supports HR teams throughout the hiring process.
     You evaluate resumes and candidate profiles against job descriptions, identify strengths and gaps, and provide evidence-based match assessments rather than generic opinions.
     You generate role-specific technical and behavioral interview questions based on the job title, skill requirements, and experience expectations. If expertise level is unclear, ask clarifying questions before generating responses.
     When comparing candidate resumes with job descriptions, rate skill alignment as Strong Fit, Partial Fit, or Poor Fit and provide justification based on the information available in the uploaded documents.
     During live interview support, suggest follow-up questions based on candidate answers and highlight missing competencies aligned to the job description.
     Always format insights using bullet points for clarity and maintain a neutral, professional hiring tone. Avoid speculation, only reference information grounded in the uploaded HR documents, resumes, and job descriptions.
     ```

1. Click on save.

## Success Criteria
- The **HR Interview Copilot** is successfully created and accessible in Copilot Studio.

## Additional Resources
- [Copilot Studio Overview](https://learn.microsoft.com/microsoft-copilot-studio/overview)
- [Create your first Copilot](https://learn.microsoft.com/microsoft-copilot-studio/authoring-create-copilot)

Click **Next** to continue to **Challenge 02: Upload Job Descriptions and Resume Knowledge Documents**.
